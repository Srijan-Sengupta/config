# Instant Clean  Copyright (C) 2023  Ruben Messerschmidt

# Instant Clean is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Instant Clean is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



import bpy
from bl_operators.presets import AddPresetBase
from bpy.types import Menu, Operator


class INSTANTCLEAN_MT_Preset_Menu(Menu):
    bl_label='Presets'
    bl_description='Choose Preset'
    preset_subdir='Instant Clean'
    preset_operator='script.execute_preset'
    draw = Menu.draw_preset


class INSTANTCLEAN_OT_Override_Preset(Operator):
    bl_idname='instantclean.override_preset'
    bl_label=''
    bl_description='Save changes to Preset'

    def execute(self, context):
        bpy.ops.instantclean.add_preset(name=INSTANTCLEAN_MT_Preset_Menu.bl_label)
        return {'FINISHED'}


class INSTANTCLEAN_OT_Add_Preset(AddPresetBase, Operator):
    bl_idname='instantclean.add_preset'
    bl_label=''
    bl_description='Add/Remove Preset'
    preset_menu='INSTANTCLEAN_MT_Preset_Menu'
    preset_subdir='Instant Clean'

    preset_defines=[
        'instantclean_categories = bpy.context.scene.instantclean_categories',
        'instantclean_repair = bpy.context.scene.instantclean_repair',
        'instantclean_manifold = bpy.context.scene.instantclean_manifold',
        'instantclean_dissolve = bpy.context.scene.instantclean_dissolve',
        'instantclean_topology = bpy.context.scene.instantclean_topology',
        'instantclean_normals = bpy.context.scene.instantclean_normals',
        'instantclean_objectdata = bpy.context.scene.instantclean_objectdata'
    ]

    preset_values=[
        # Repair
        'instantclean_categories.repair',
        'instantclean_repair.loose',
        'instantclean_repair.loose_verts',
        'instantclean_repair.loose_edges',
        'instantclean_repair.loose_faces',
        'instantclean_repair.doubles',
        'instantclean_repair.doubles_dst',
        'instantclean_repair.zero_faces',
        'instantclean_repair.zero_faces_area',
        'instantclean_repair.dispensables',
        'instantclean_repair.dispensables_ang',

        # Manifold
        'instantclean_categories.manifold',
        'instantclean_manifold.non_manifold_faces',
        'instantclean_manifold.non_manifold_verts',
        'instantclean_manifold.wire_geo',
        'instantclean_manifold.fill_holes',
        'instantclean_manifold.fill_holes_max_sides',
        'instantclean_manifold.flatten',
        'instantclean_manifold.flatten_iterations',
        'instantclean_manifold.flatten_factor',
        'instantclean_manifold.undistort',
        'instantclean_manifold.undistort_ang',

        # Dissolve
        'instantclean_categories.dissolve',
        'instantclean_dissolve.max_angle',
        'instantclean_dissolve.boundaries',
        'instantclean_dissolve.protect_sharp',
        'instantclean_dissolve.protect_seam',
        'instantclean_dissolve.protect_uv',
        'instantclean_dissolve.protect_materials',

        # Topology
        'instantclean_categories.topology',
        'instantclean_topology.type',
        'instantclean_topology.quad_method',
        'instantclean_topology.quad_max_face_ang',
        'instantclean_topology.quad_max_shape_ang',
        'instantclean_topology.ngon_method',
        'instantclean_topology.compare_sharp',
        'instantclean_topology.compare_seam',
        'instantclean_topology.compare_vcol',
        'instantclean_topology.compare_uv',
        'instantclean_topology.compare_material',

        # Normals
        'instantclean_categories.normals',
        'instantclean_normals.recalculate',
        'instantclean_normals.recalculate_orientation',
        'instantclean_normals.auto_smooth',
        'instantclean_normals.auto_smooth_ang',
        'instantclean_normals.weighted_normals',

        # Objectdata
        'instantclean_categories.objectdata',
        'instantclean_objectdata.double_materials',
        'instantclean_objectdata.double_materials_remove_data',
        'instantclean_objectdata.material_slots',
        'instantclean_objectdata.material_slots_clear',
        'instantclean_objectdata.empty_vertex_groups'
    ]
