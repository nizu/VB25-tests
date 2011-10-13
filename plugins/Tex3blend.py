'''
  V-Ray/Blender 2.5

  http://vray.cgdo.ru

  Author: Andrey M. Izrantsev (aka bdancer)
  E-Mail: izrantsev@cgdo.ru

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

  All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Software.
  
'''

'''
This is an experimental additional texture plugin for VB25.
Uses multiple standard Vray 2.0 plugins to create a composite texture. 

Written by Ni.Zu . 
Version 0.1  9 jul 2011.
Alpha . Work in progress. Use at your own risk .



'''

''' Blender modules '''
import bpy
from bpy.props import *

''' vb modules '''
from vb25.utils   import *
from vb25.ui.ui   import *
from vb25.plugins import *
from vb25.texture import *
from vb25.uvwgen  import *


TYPE= 'TEXTURE'
ID=   'Tex3Blend'
PLUG= 'Tex3Blend'

NAME= '3Blend'
DESC= "3 steps blendmask texture"

PID=  99

PARAMS= (
        'blendmap'
        'blackmult'
        'whitemult'
        'colormap1'
        'colormap2'
        'colormap3'
		'whiteint'
		'blackint'
		'greyint'
        )

def add_properties(VRayTexture):
	class Tex3Blend(bpy.types.PropertyGroup):
		pass
	bpy.utils.register_class(Tex3Blend)
	
	VRayTexture.Tex3Blend= PointerProperty(
		name= "Tex3Blend",
		type=  Tex3Blend,
		description= "V-Ray Tex3Blend settings"
	)

	Tex3Blend.blendmap_tex= StringProperty(
		name= "blendmap",
		description= "blendmap",
		default= ""
	)

	Tex3Blend.colormap1= FloatVectorProperty(
		name= "Black color",
		description= "TODO",
		subtype= 'COLOR',
		min= 0.0,
		max= 1.0,
		soft_min= 0.0,
		soft_max= 1.0,
		default= (0.0,0.0,0.0)
	)

	Tex3Blend.blackmult= FloatProperty(
		name= "BlackMult.",
		description= "blendmap Black amount multiplier",
		min= 0.0,
		max= 2.0,
		soft_min= 0.0,
		soft_max= 1.5,
		precision= 3,
		default= 1
	)

	Tex3Blend.blackint= FloatProperty(
		name= "BlackInt.",
		description= "Black texture intensity multiplier",
		min= 0.0,
		max= 2.0,
		soft_min= 0.0,
		soft_max= 1.5,
		precision= 3,
		default= 1
	)


	Tex3Blend.colormap1_tex= StringProperty(
		name= "black color texture",
		description= "black color texture.",
		default= ""
	)

	Tex3Blend.colormap2= FloatVectorProperty(
		name= "Grey color",
		description= "TODO",
		subtype= 'COLOR',
		min= 0.0,
		max= 1.0,
		soft_min= 0.0,
		soft_max= 1.0,
		default= (0.5,0.5,0.5)
	)

	Tex3Blend.colormap2_tex= StringProperty(
		name= "grey color texture",
		description= "grey color texture.",
		default= ""
	)
	
	Tex3Blend.greyint= FloatProperty(
		name= "GreyInt.",
		description= "grey texture intensity multiplier",
		min= 0.0,
		max= 2.0,
		soft_min= 0.0,
		soft_max= 1.5,
		precision= 3,
		default= 1
	)

	
	

	Tex3Blend.colormap3= FloatVectorProperty(
		name= "White color",
		description= "TODO",
		subtype= 'COLOR',
		min= 0.0,
		max= 1.0,
		soft_min= 0.0,
		soft_max= 1.0,
		default= (1.0,1.0,1.0)
	)

	Tex3Blend.whitemult= FloatProperty(
		name= "WhiteMult.",
		description= "blendmap white amount multiplier",
		min= 0.0,
		max= 2.0,
		soft_min= 0.0,
		soft_max= 1.5,
		precision= 3,
		default= 1
	)

	Tex3Blend.whiteint= FloatProperty(
		name= "whiteInt.",
		description= "white texture intensity multiplier",
		min= 0.0,
		max= 2.0,
		soft_min= 0.0,
		soft_max= 1.5,
		precision= 3,
		default= 1
	)


	Tex3Blend.colormap3_tex= StringProperty(
		name= "White color texture",
		description= "white color texture.",
		default= ""
	)

'''
  OUTPUT
'''
def write(bus):
	scene= bus['scene']
	ofile= bus['files']['textures']

	slot=     bus['mtex']['slot']
	texture=  bus['mtex']['texture']
	tex_name= bus['mtex']['name']

	Tex3Blend= getattr(texture.vray, PLUG)

	mapped_params= write_sub_textures(bus,
									  Tex3Blend,
									  ('blendmap_tex','colormap1_tex','colormap2_tex','colormap3_tex'))

	for param in ('blendmap_tex','colormap1_tex','colormap2_tex','colormap3_tex'):
		value= getattr(Tex3Blend, param)
		tex_key= param+'_tex'
		if tex_key in mapped_params:
				value= mapped_params[tex_key]		

	
# remap blendmap range : black to grey > full range (texture Y)

	ofile.write("\nTexAColorOp y_%s {\n"%(tex_name))
	ofile.write("\tcolor_a= %s;\n"%(a(scene,mapped_params['blendmap_tex'])))	
	ofile.write("\tmult_a= 2/%s;\n"%(getattr(Tex3Blend,'blackmult')))
	ofile.write("\tcolor_b= AColor(1,1,1,1);\n")
	ofile.write("\tmult_b= 1;\n")
	ofile.write("\tmode= 7;\n")
	ofile.write("\tresult_alpha= 1.0;\n")
	ofile.write("\n}\n")

# remap blendmap range : grey to white > full range  (texture X)

	ofile.write("\nTexAColorOp x1_%s {\n"%(tex_name))
	ofile.write("\tcolor_a= %s;\n"%(a(scene,mapped_params['blendmap_tex'])))	
	ofile.write("\tmult_a= %s;\n"%(getattr(Tex3Blend,'whitemult')))
	ofile.write("\tcolor_b= AColor(0.5,0.5,0.5,1);\n")
	ofile.write("\tmult_b= 1;\n")
	ofile.write("\tmode= 8;\n")
	ofile.write("\tresult_alpha= 1.0;\n")
	ofile.write("\n}\n")

	ofile.write("\nTexAColorOp x_%s {\n"%(tex_name))
	ofile.write("\tcolor_a= x1_%s;\n"%(tex_name))	
	ofile.write("\tmult_a= 2;\n")
	ofile.write("\tcolor_b= AColor(1,1,1,1);\n")
	ofile.write("\tmult_b= 1;\n")
	ofile.write("\tmode= 4;\n")
	ofile.write("\tresult_alpha= 1.0;\n")
	ofile.write("\n}\n")

#  intensity mults

	for param in ('colormap1','colormap2','colormap3'):
	
		if param == 'colormap1':
			intparam='blackint'
		if param == 'colormap2':
			intparam='greyint'
		if param == 'colormap3':
			intparam='whiteint'
		
		intmult = (getattr(Tex3Blend,intparam)) 		
		
		value= getattr(Tex3Blend,param)	
		key= param+'_tex'
		if key in mapped_params:
			value= mapped_params[key]
		else: pass
#		if intmult != 1.0 :   
		ofile.write("\nTexAColorOp %s_%s {\n"%(tex_name,param))
		ofile.write("\tcolor_a= %s;\n"%(a(scene,value)))	
		ofile.write("\tmult_a= %s;\n"%(intmult))
#		ofile.write("\tcolor_b= AColor(0,0,0,0);\n")
#		ofile.write("\tmult_b= 1;\n")
		ofile.write("\tmode= 0;\n")
#		ofile.write("\tresult_alpha= 1.0;\n")
		ofile.write("\n}\n")

# mix black with grey (texture A)
	ofile.write("\nTexMix a_%s {\n"%(tex_name))
	ofile.write("\tmix_map= y_%s;\n"%(tex_name))	
	ofile.write("\tcolor1= %s;\n"%(tex_name+'_colormap1'))	
	ofile.write("\tcolor2= %s;\n"%(tex_name+'_colormap2'))	
	ofile.write("\n}\n")

# mix black & grey with white  (final texture)
	ofile.write("\nTexMix %s {\n"%(tex_name))
	ofile.write("\tmix_map= x_%s;\n"%(tex_name))	
	ofile.write("\tcolor1= a_%s;\n"%(tex_name))	
	ofile.write("\tcolor2= %s;\n"%(tex_name+'_colormap3'))	
	ofile.write("\n}\n")

	return tex_name


'''
  GUI
'''
class VRAY_TP_Tex3Blend(VRayTexturePanel, bpy.types.Panel):
	bl_label = NAME

	COMPAT_ENGINES = {'VRAY_RENDER','VRAY_RENDER_PREVIEW'}

	@classmethod
	def poll(cls, context):
		tex= context.texture
		if not tex:
			return False
#		vtex= tex.vray
		engine= context.scene.render.engine
		return ((tex and tex.type == 'VRAY' and tex.vray.type == ID) and (engine_poll(__class__, context)))

	def draw(self, context):
		tex= context.texture
		tex3blend= getattr(tex.vray, PLUG)
		
		wide_ui= context.region.width > narrowui

		layout= self.layout
		
		split= layout.split()
		col= split.column()		
		row = layout.row()

		col.prop_search(tex3blend, 'blendmap_tex', bpy.data, 'textures', text= "Control Map")
		split= layout.split()
		row= split.row(align= True)
		row.label(text='control Mults.')		
		row.prop(tex3blend,'blackmult',text="black")		
		row.prop(tex3blend,'whitemult',text="white")

		layout= self.layout

		split= layout.split()
		row = layout.row()
		row.label(text='Black')		
		row.prop(tex3blend,'blackint',text="int.")

		split= layout.split()
		row= split.row(align= True)
		row.prop(tex3blend,'colormap1', text= "")
		row.prop_search(tex3blend, 'colormap1_tex', bpy.data, 'textures',text='')

		split= layout.split()
		row= split.row(align= True)
		row.label(text='Grey')
		row.prop(tex3blend,'greyint',text="int.")

		split= layout.split()
		row = layout.row()
		row= split.row(align= True)
		row.prop(tex3blend,'colormap2', text= "")
		row.prop_search(tex3blend, 'colormap2_tex', bpy.data, 'textures',text='')


		split= layout.split()
		row = layout.row()
		row.label(text='White')
		row.prop(tex3blend,'whiteint',text="int.")

		split= layout.split()
		row = layout.row()
		row= split.row(align= True)
		row.prop(tex3blend,'colormap3', text= "")
		row.prop_search(tex3blend, 'colormap3_tex', bpy.data, 'textures',text='')



bpy.utils.register_class(VRAY_TP_Tex3Blend)