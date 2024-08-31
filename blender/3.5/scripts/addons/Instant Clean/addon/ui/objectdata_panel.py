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
from .super_panel import Super_Panel
from .layout_temps import sub_layout, sub_panel_header, results_layout


class INSTANTCLEAN_PT_Objectdata_Panel(Super_Panel):
    bl_idname='bc.objectdata_panel'
    bl_label=''

    @classmethod
    def poll(cls, context):
        return not context.scene.instantclean_misc.results or (context.scene.instantclean_categories.objectdata and bpy.context.scene['Objectdata'] is not None and [v for k, v in bpy.context.scene['Objectdata'].items() if type(v) != type(False)])

    def draw_header(self, context):
        sub_panel_header(self.layout, 'objectdata', context.scene.instantclean_misc.results)

    def draw(self, context):
        layout = self.layout
        layout.enabled = context.scene.instantclean_categories.objectdata
        pg = context.scene.instantclean_objectdata

        sub = sub_layout(layout, 3)

        if not context.scene.instantclean_misc.results:
            sub.label(text='Materials')
            box = sub.box()
            split = box.split()
            col = split.column()
            col.prop(pg, 'double_materials')
            col.prop(pg, 'material_slots')
            col = split.column()
            col.prop(pg, 'double_materials_remove_data', text='', icon='TRASH', toggle=True)
            col.prop(pg, 'material_slots_clear', text='')

            sub.separator()
            sub.label(text='Vertex Groups')
            box = sub.box()
            col = box.column()
            col.prop(pg, 'empty_vertex_groups')
        
        else:
            results_layout(sub, bpy.context.scene['Objectdata'])
