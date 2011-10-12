'''

  V-Ray/Blender 2.5

  http://vray.cgdo.ru

  Time-stamp: "Monday, 11 July 2011 [00:39]"

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
from bpy.props import *

''' vb modules '''
from vb25.utils import *
from vb25.ui.ui import *


TYPE= 'SETTINGS'

ID=   'EXPORTER'
NAME= 'Exporter'
DESC= "Exporter options."

PARAMS= (
)


def add_properties(rna_pointer):
	class VRayExporter(bpy.types.PropertyGroup):
		pass
	bpy.utils.register_class(VRayExporter)

	rna_pointer.exporter= PointerProperty(
		name= "Exporter",
		type=  VRayExporter,
		description= "Exporter settings."
	)

	VRayExporter.draft= BoolProperty(
		name= "Draft render",
		description= "Render with low settings.",
		default= False
	)

	VRayExporter.mesh_active_layers= BoolProperty(
		name= "Export meshes from active layers",
		description= "Export meshes from active layers only.",
		default= False
	)

	VRayExporter.mesh_ascii= BoolProperty(
		name= "ASCII",
		description= "Export meshes in ASCII format. Only affects Python mesh export.",
		default= False
	)

	VRayExporter.use_displace= BoolProperty(
		name= "Displace / subdiv",
		description= "Use displace / subdivisions.",
		default= True
	)

	VRayExporter.image_to_blender= BoolProperty(
		name= "Image to Blender",
		description= "Pass image to Blender on render end (EXR file format is used).",
		default= False
	)

	VRayExporter.autoclose= BoolProperty(
		name= "Auto close",
		description= "Close VFB on Esc.",
		default= False
	)
	VRayExporter.srgb= BoolProperty(
		name= "sRGB button",
		description= "turn on sRGB button in VFB at each render",
		default= True
	)

	VRayExporter.log_window= BoolProperty(
		name= "Show log window",
		description= "Show log window (Linux).",
		default= False
	)

	VRayExporter.animation= BoolProperty(
		name= "Animation",
		description= "Render animation.",
		default= False
	)

	VRayExporter.check_animated= BoolProperty(
		name= "Check animated",
		description= "Detect animated meshes.",
		default= False
	)

	VRayExporter.use_hair= BoolProperty(
		name= "Hair",
		description= "Render hair.",
		default= True
	)

	VRayExporter.use_instances= BoolProperty(
		name= "Instances",
		description= "Use instances (Alt+D meshes will be the same; saves memory and faster export)",
		default= False
	)

	VRayExporter.camera_loop= BoolProperty(
		name= "Camera loop",
		description= "Render views from all cameras.",
		default= False
	)

	VRayExporter.active_layers= BoolProperty(
		name= "Active layers",
		description= "Render objects only from visible layers.",
		default= True
	)

	VRayExporter.auto_meshes= BoolProperty(
		name= "Auto export meshes",
		description= "Export meshes automatically before render.",
		default= 0
	)

	VRayExporter.autorun= BoolProperty(
		name= "Autorun",
		description= "Start V-Ray automatically after export.",
		default= 1
	)

	VRayExporter.debug= BoolProperty(
		name= "Debug",
		description= "Enable script\'s debug output.",
		default= False
	)

	VRayExporter.mesh_debug= BoolProperty(
		name= "Debug",
		description= "Enable build debug output.",
		default= False
	)

	VRayExporter.output= EnumProperty(
		name= "Exporting directory",
		description= "Exporting directory.",
		items= (
			('USER',"User-defined directory",""),
			('SCENE',"Scene file directory",""),
			('TMP',"Global TMP directory","")
		),
		default= 'TMP'
	)

	VRayExporter.detect_vray= BoolProperty(
		name= "Detect V-Ray",
		description= "Detect V-Ray binary location.",
		default= True
	)

	VRayExporter.vray_binary= StringProperty(
		name= "Path",
		subtype= 'FILE_PATH',
		description= "Path to V-Ray binary. Don\'t use relative path here - use absolute!"
	)

	VRayExporter.output_dir= StringProperty(
		name= "Directory",
		subtype= 'DIR_PATH',
		description= "User-defined output directory."
	)

	VRayExporter.output_unique= BoolProperty(
		name= "Use unique file name",
		description= "Use unique file name.",
		default= False
	)

	VRayExporter.auto_save_render= BoolProperty(
		name= "Save render",
		description= "Save render automatically.",
		default= False
	)

	VRayExporter.display= BoolProperty(
		name= "Display VFB",
		description= "Display VFB.",
		default= True
	)

	VRayExporter.verboseLevel= EnumProperty(
		name= "Log level",
		description= "Specifies the verbose level of information printed to the standard output.",
		items= (
			('0', "No information", "No information printed."),
			('1', "Only errors",    "Only errors."),
			('2', "Warnings",       "Errors and warnings."),
			('3', "Progress",       "Errors, warnings and informational messages."),
			('4', "All",            "All output."),
		),
		default= '3'
	)
