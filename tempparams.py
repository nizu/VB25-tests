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


''' Blender modules '''
import bpy

''' vb modules '''
from vb25.utils import *
from vb25.plugins import *
from vb25.uvw import *
from vb25.texture import *


OBJECT_PARAMS= {
	'LightOmni': (
		'enabled',
		#'color_tex',
		'shadows',
		'shadowColor',
		#'shadowColor_tex',
		'shadowBias',
		#'photonSubdivs',
		'causticSubdivs',
		#'diffuseMult',
		'causticMult',
		'cutoffThreshold',
		'affectDiffuse',
		'affectSpecular',
		'bumped_below_surface_check',
		'nsamples',
		'diffuse_contribution',
		'specular_contribution',
		#'units',
		'intensity',
		#'intensity_tex',
		#'shadowRadius',
		'areaSpeculars',
		'shadowSubdivs',
		'decay'
	),

	'LightSphere': (
		'enabled',
		#'color_tex',
		'shadows',
		'shadowColor',
		#'shadowColor_tex',
		'shadowBias',
		#'photonSubdivs',
		'causticSubdivs',
		#'diffuseMult',
		'causticMult',
		'cutoffThreshold',
		'affectDiffuse',
		'affectSpecular',
		'bumped_below_surface_check',
		'nsamples',
		'diffuse_contribution',
		'specular_contribution',
		#'units',
		'intensity',
		#'intensity_tex',
		'subdivs',
		'storeWithIrradianceMap',
		'invisible',
		'affectReflections',
		'noDecay',
		'radius',
		'sphere_segments'
	),

	'LightRectangle': (
		'enabled',
		#'color_tex',
		'shadows',
		'shadowColor',
		#'shadowColor_tex',
		'shadowBias',
		#'photonSubdivs',
		'causticSubdivs',
		#'diffuseMult',
		'causticMult',
		'cutoffThreshold',
		'affectDiffuse',
		'affectSpecular',
		'bumped_below_surface_check',
		'nsamples',
		'diffuse_contribution',
		'specular_contribution',
		#'units',
		'intensity',
		#'intensity_tex',
		'subdivs',
		#'storeWithIrradianceMap',
		'invisible',
		'affectReflections',
		'noDecay'
	),

	'LightDirectMax': (
		'enabled',
		#'color_tex',
		'shadows',
		'shadowColor',
		#'shadowColor_tex',
		'shadowBias',
		#'photonSubdivs',
		'causticSubdivs',
		#'diffuseMult',
		'causticMult',
		'cutoffThreshold',
		'affectDiffuse',
		'affectSpecular',
		'bumped_below_surface_check',
		'nsamples',
		'diffuse_contribution',
		'specular_contribution',
		'intensity',
		#'intensity_tex',
		'shadowRadius',
		'areaSpeculars',
		'shadowSubdivs',
		'fallsize',
	),

	'SunLight': (
		'turbidity',
		'ozone',
		'water_vapour',
		'intensity_multiplier',
		'size_multiplier',
		#'up_vector',
		'invisible',
		'horiz_illum',
		#'sky_model',
		'shadows',
		#'atmos_shadows',
		'shadowBias',
		'shadow_subdivs',
		'shadow_color',
		#'shadow_color_tex',
		#'photon_radius',
		#'photonSubdivs',
		'causticSubdivs',
		#'diffuseMult',
		'causticMult',
		'enabled'
	),	

	'LightIES': (
		'enabled',
		'intensity',
		#'color_tex',
		'shadows',
		'shadowColor',
		#'shadowColor_tex',
		'shadowBias',
		#'photonSubdivs',
		'causticSubdivs',
		#'diffuseMult',
		'causticMult',
		'cutoffThreshold',
		'affectDiffuse',
		'affectSpecular',
		'bumped_below_surface_check',
		'nsamples',
		'diffuse_contribution',
		'specular_contribution',
		'shadowSubdivs',
		'ies_file',
		#'filter_color',
		'soft_shadows',
		#'area_speculars'
	),

	'LightDome': (
		'enabled',
		#'color_tex',
		'shadows',
		'shadowColor',
		#'shadowColor_tex',
		'shadowBias',
		#'photonSubdivs',
		'causticSubdivs',
		#'diffuseMult',
		'causticMult',
		'cutoffThreshold',
		'affectDiffuse',
		'affectSpecular',
		#'bumped_below_surface_check',
		'nsamples',
		'diffuse_contribution',
		'specular_contribution',
		#'channels',
		#'channels_raw',
		#'channels_diffuse',
		#'channels_specular',
		#'units',
		'intensity',
		#'intensity_tex',
		'subdivs',
		#'storeWithIrradianceMap',
		'invisible',
		'affectReflections',
		#'dome_tex',
		#'use_dome_tex',
		#'tex_resolution',
		#'dome_targetRadius',
		#'dome_emitRadius',
		#'dome_spherical',
		#'tex_adaptive',
		#'dome_rayDistance',
		#'dome_rayDistanceMode',
	),

	'LightSpot': (
		'enabled',
		#'color_tex',
		'shadows',
		'shadowColor',
		#'shadowColor_tex',
		'shadowBias',
		#'photonSubdivs',
		'causticSubdivs',
		#'diffuseMult',
		'causticMult',
		'cutoffThreshold',
		'affectDiffuse',
		'affectSpecular',
		'bumped_below_surface_check',
		'nsamples',
		'diffuse_contribution',
		'specular_contribution',
		#'units',
		'intensity',
		#'intensity_tex',
		'shadowRadius',
		'areaSpeculars',
		'shadowSubdivs',
		#'coneAngle',
		#'penumbraAngle',
		#'dropOff',
		#'falloffType',
		'decay',
		#'barnDoor',
		#'barnDoorLeft',
		#'barnDoorRight',
		#'barnDoorTop',
		#'barnDoorBottom',
		#'useDecayRegions',
		#'startDistance1',
		#'endDistance1',
		#'startDistance2',
		#'endDistance2',
		#'startDistance3',
		#'endDistance3'
	),

	'LightMesh': (
		'enabled',
		# 'transform',
		'color',
		# 'color_tex',
		# 'shadows',
		# 'shadowColor',
		# 'shadowColor_tex',
		# 'shadowBias',
		# 'photonSubdivs',
		'causticSubdivs',
		# 'diffuseMult',
		# 'causticMult',
		# 'cutoffThreshold',
		'affectDiffuse',
		'affectSpecular',
		# 'bumped_below_surface_check',
		# 'nsamples',
		# 'diffuse_contribution',
		# 'specular_contribution',
		# 'channels',
		# 'channels_raw',
		# 'channels_diffuse',
		# 'channels_specular',
		'units',
		'intensity',
		# 'intensity_tex',
		'subdivs',
		'storeWithIrradianceMap',
		'invisible',
		'affectReflections',
		'noDecay',
		'doubleSided',
		'lightPortal',
		'geometry',
		# 'ignoreLightNormals',
		# 'tex',
		# 'use_tex',
		# 'tex_resolution',
		# 'cache_tex'
	),

	'TexSky': (
		#'transform',
		#'target_transform',
		'turbidity',
		'ozone',
		'water_vapour',
		'intensity_multiplier',
		'size_multiplier',
		#'up_vector',
		'invisible',
		'horiz_illum',
		'sky_model',
		'sun'
	),

	'MtlWrapper': (
		#'base_material',
		'generate_gi',
		'receive_gi',
		'generate_caustics',
		'receive_caustics',
		'alpha_contribution',
		'matte_surface',
		'shadows',
		'affect_alpha',
		'shadow_tint_color',
		'shadow_brightness',
		'reflection_amount',
		'refraction_amount',
		'gi_amount',
		'no_gi_on_other_mattes',
		'matte_for_secondary_rays',
		'gi_surface_id',
		'gi_quality_multiplier',
		#'alpha_contribution_tex',
		#'shadow_brightness_tex',
		#'reflection_filter_tex',
		'trace_depth',
		#'channels'
	),

	'MtlRenderStats': (
		'camera_visibility',
		'reflections_visibility',
		'refractions_visibility',
		'gi_visibility',
		'shadows_visibility',
		'visibility'
	)
}

BLEND_MODES= {
	'NONE':         '0',
	'STENCIL':      '1',
	'OVER':         '1',
	'IN':           '2',
	'OUT':          '3',
	'ADD':          '4',
	'SUBTRACT':     '5',
	'MULTIPLY':     '6',
	'DIFFERENCE':   '7',
	'LIGHTEN':      '8',
	'DARKEN':       '9',
	'SATURATE':    '10',
	'DESATUREATE': '11',
	'ILLUMINATE':  '12',
}

def write_BRDFGlossy(ofile, sce, ma, ma_name, textures):
	BRDFVRayMtl= ma.vray.BRDFVRayMtl

	brdf_name= get_random_string()

	if BRDFVRayMtl.brdf_type == 'PHONG':
		ofile.write("\nBRDFPhong %s {"%(brdf_name))
	elif BRDFVRayMtl.brdf_type == 'WARD':
		ofile.write("\nBRDFWard %s {"%(brdf_name))
	else:
		ofile.write("\nBRDFBlinn %s {"%(brdf_name))

	ofile.write("\n\tcolor= %s;"%(a(sce,"Color(%.6f,%.6f,%.6f)"%(tuple(BRDFVRayMtl.reflect_color)))))
	ofile.write("\n\tsubdivs= %i;"%(BRDFVRayMtl.reflect_subdivs))

	if 'reflect' in textures:
		ofile.write("\n\ttransparency= Color(1.0,1.0,1.0);")
		ofile.write("\n\ttransparency_tex= %s;"%(textures['reflect']))
	else:
		ofile.write("\n\ttransparency= %s;"%(a(sce,"Color(%.6f,%.6f,%.6f)"%(tuple([1.0 - c for c in BRDFVRayMtl.reflect_color])))))

	ofile.write("\n\treflectionGlossiness= %s;"%(a(sce,BRDFVRayMtl.reflect_glossiness)))
	if BRDFVRayMtl.hilight_glossiness_lock:
		ofile.write("\n\thilightGlossiness= %s;"%(a(sce,BRDFVRayMtl.reflect_glossiness)))
	else:
		ofile.write("\n\thilightGlossiness= %s;"%(a(sce,BRDFVRayMtl.hilight_glossiness)))
	if 'reflect_glossiness' in textures:
		ofile.write("\n\treflectionGlossiness_tex= %s;"%("%s::out_intensity"%(textures['reflect_glossiness'])))
	if 'hilight_glossiness' in textures:
		ofile.write("\n\thilightGlossiness_tex= %s;"%("%s::out_intensity"%(textures['hilight_glossiness'])))
	ofile.write("\n\tback_side= %d;"%(BRDFVRayMtl.option_reflect_on_back))
	ofile.write("\n\ttrace_reflections= %s;"%(p(BRDFVRayMtl.reflect_trace)))
	ofile.write("\n\ttrace_depth= %i;"%(BRDFVRayMtl.reflect_depth))
	if BRDFVRayMtl.brdf_type != 'PHONG':
		ofile.write("\n\tanisotropy= %s;"%(a(sce,BRDFVRayMtl.anisotropy)))
		ofile.write("\n\tanisotropy_rotation= %s;"%(a(sce,BRDFVRayMtl.anisotropy_rotation)))
	ofile.write("\n\tcutoff= %.6f;"%(BRDFVRayMtl.option_cutoff))
	ofile.write("\n}\n")

	return brdf_name


def write_BRDFMirror(ofile, sce, ma, ma_name, textures):
	BRDFVRayMtl= ma.vray.BRDFVRayMtl

	brdf_name= get_random_string()

	ofile.write("\nBRDFMirror %s {"%(brdf_name))
	if 'color' in textures:
		ofile.write("\n\tcolor= %s;"%(textures['color']))
	else:
		ofile.write("\n\tcolor= %s;"%(a(sce,"Color(%.6f,%.6f,%.6f)"%(tuple(BRDFVRayMtl.reflect_color)))))
	if 'reflect' in textures:
		ofile.write("\n\ttransparency= Color(1.0, 1.0, 1.0);")
		ofile.write("\n\ttransparency_tex= %s;"%(textures['reflect']))
	else:
		ofile.write("\n\ttransparency= %s;"%(a(sce,"Color(%.6f,%.6f,%.6f)"%(tuple([1.0 - c for c in BRDFVRayMtl.reflect_color])))))
	ofile.write("\n\tback_side= %d;"%(BRDFVRayMtl.option_reflect_on_back))
	ofile.write("\n\ttrace_reflections= %s;"%(p(BRDFVRayMtl.reflect_trace)))
	ofile.write("\n\ttrace_depth= %i;"%(BRDFVRayMtl.reflect_depth))
	ofile.write("\n\tcutoff= %.6f;"%(BRDFVRayMtl.option_cutoff))
	ofile.write("\n}\n")

	return brdf_name


def write_BRDFGlass(ofile, sce, ma, ma_name, textures):
	BRDFVRayMtl= ma.vray.BRDFVRayMtl

	brdf_name= get_random_string()

	ofile.write("\nBRDFGlass %s {"%(brdf_name))
	ofile.write("\n\tcolor= %s;"%(a(sce,"Color(%.6f,%.6f,%.6f)"%(tuple(BRDFVRayMtl.refract_color)))))
	if 'refract' in textures:
		ofile.write("\n\tcolor_tex= %s;"%(textures['refract']))
	ofile.write("\n\tior= %s;"%(a(sce,BRDFVRayMtl.refract_ior)))
	ofile.write("\n\taffect_shadows= %d;"%(BRDFVRayMtl.refract_affect_shadows))
	ofile.write("\n\taffect_alpha= %d;"%(BRDFVRayMtl.refract_affect_alpha))
	ofile.write("\n\ttrace_refractions= %d;"%(BRDFVRayMtl.refract_trace))
	ofile.write("\n\ttrace_depth= %s;"%(BRDFVRayMtl.refract_depth))
	ofile.write("\n\tcutoff= %.6f;"%(BRDFVRayMtl.option_cutoff))
	ofile.write("\n}\n")

	return brdf_name


def write_BRDFGlassGlossy(ofile, sce, ma, ma_name, textures):
	BRDFVRayMtl= ma.vray.BRDFVRayMtl

	brdf_name= get_random_string()

	ofile.write("\nBRDFGlassGlossy %s {"%(brdf_name))
	ofile.write("\n\tcolor= %s;"%(a(sce,"Color(%.6f,%.6f,%.6f)"%(tuple(BRDFVRayMtl.refract_color)))))
	if 'refract' in textures:
		ofile.write("\n\tcolor_tex= %s;"%(textures['refract']))
	ofile.write("\n\tglossiness= %s;"%(a(sce,BRDFVRayMtl.refract_glossiness)))
	ofile.write("\n\tsubdivs= %i;"%(BRDFVRayMtl.refract_subdivs))
	ofile.write("\n\tior= %s;"%(a(sce,BRDFVRayMtl.refract_ior)))
	ofile.write("\n\taffect_shadows= %d;"%(BRDFVRayMtl.refract_affect_shadows))
	ofile.write("\n\taffect_alpha= %d;"%(BRDFVRayMtl.refract_affect_alpha))
	ofile.write("\n\ttrace_refractions= %d;"%(BRDFVRayMtl.refract_trace))
	ofile.write("\n\ttrace_depth= %s;"%(BRDFVRayMtl.refract_depth))
	ofile.write("\n\tcutoff= %.6f;"%(BRDFVRayMtl.option_cutoff))
	ofile.write("\n}\n")

	return brdf_name


def write_BRDFDiffuse(ofile, sce, ma, ma_name, textures):
	BRDFVRayMtl= ma.vray.BRDFVRayMtl
		
	brdf_name= get_random_string()

	ofile.write("\nBRDFDiffuse %s {"%(brdf_name))
	ofile.write("\n\tcolor= %s;"%(a(sce,"Color(%.6f, %.6f, %.6f)"%(tuple(ma.diffuse_color)))))
	ofile.write("\n\troughness= %s;"%(a(sce,"Color(1.0,1.0,1.0)*%.6f"%(BRDFVRayMtl.roughness))))
	if 'diffuse' in textures:
		ofile.write("\n\tcolor_tex= %s;" % textures['diffuse'])
	ofile.write("\n\ttransparency= %s;" % a(sce,"Color(1.0,1.0,1.0)*%.6f"%(1.0 - ma.alpha)))
	if 'opacity' in textures:
		ofile.write("\n\ttransparency_tex= %s;" % textures['opacity'])
	ofile.write("\n}\n")

	return brdf_name


def write_BRDF(ofile, sce, ma, ma_name, textures):
	def bool_color(color):
		for c in color:
			if c > 0.0:
				return True
		return False

	BRDFVRayMtl= ma.vray.BRDFVRayMtl

	brdfs= []

	reflect= None

	if 'reflect' in textures:
		reflect= write_TexInvert(textures['reflect'])

	if reflect or bool_color(BRDFVRayMtl.reflect_color):
		if BRDFVRayMtl.reflect_glossiness < 1.0 or 'reflect_glossiness' in textures:
			brdf_name= write_BRDFGlossy(ofile, sce, ma, ma_name, textures['mapto'])
		else:
			brdf_name= write_BRDFMirror(ofile, sce, ma, ma_name, textures['mapto'])
		brdfs.append(brdf_name)

	if 'refract' in textures or bool_color(BRDFVRayMtl.refract_color):
		if BRDFVRayMtl.refract_glossiness < 1.0 or 'refract_glossiness' in textures:
			brdf_name= write_BRDFGlassGlossy(ofile, sce, ma, ma_name, textures['mapto'])
		else:
			brdf_name= write_BRDFGlass(ofile, sce, ma, ma_name, textures['mapto'])
	else:
		brdf_name= write_BRDFDiffuse(ofile, sce, ma, ma_name, textures['mapto'])
	brdfs.append(brdf_name)

	if len(brdfs) == 1:
		brdf_name= brdfs[0]
	else:
		brdf_name= "BRDFLayered_%s"%(ma_name)
		ofile.write("\nBRDFLayered %s {"%(brdf_name))
		ofile.write("\n\tbrdfs= List(%s);"%(','.join(brdfs)))
		ofile.write("\n\ttransparency= %s;"%(a(sce,"Color(1.0,1.0,1.0)*%.6f"%(1.0 - ma.alpha))))
		if 'opacity' in textures:
			ofile.write("\n\ttransparency_tex= %s;" % textures['opacity'])
		ofile.write("\n}\n")

	return brdf_name


def write_BRDFLight(ofile, sce, ma, ma_name, mapped_params):
	textures= mapped_params['mapto']

	brdf_name= "BRDFLight_%s"%(ma_name)

	light= ma.vray.BRDFLight

	ofile.write("\nBRDFLight %s {"%(brdf_name))

	if 'diffuse' in textures:
		color= textures['diffuse']
		if 'opacity' in textures:
			alpha= write_TexInvert(ofile, sce, textures['opacity'])
			color= write_TexCompMax(ofile, sce, {'name': "%s_alpha" % brdf_name,
												 'sourceA': alpha,
												 'sourceB': color,
												 'opertor': 'Multiply'})
		ofile.write("\n\tcolor= %s;" % color)
	else:
		ofile.write("\n\tcolor= %s;" % a(sce, ma.diffuse_color))

	ofile.write("\n\tcolorMultiplier= %s;" % a(sce, ma.emit * 10))
	ofile.write("\n\tcompensateExposure= %s;" % p(light.compensateExposure))
	ofile.write("\n\temitOnBackSide= %s;" % p(light.emitOnBackSide))
	ofile.write("\n\tdoubleSided= %s;" % p(light.doubleSided))

	if 'opacity' in textures:
		ofile.write("\n\ttransparency= %s;" % textures['opacity'])
	else:
		ofile.write("\n\ttransparency= %s;" % a(sce,"Color(1.0,1.0,1.0)*%.6f" % (1.0 - ma.alpha)))

	ofile.write("\n}\n")

	return brdf_name