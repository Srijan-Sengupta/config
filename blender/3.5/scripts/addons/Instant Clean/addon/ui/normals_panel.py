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


class INSTANTCLEAN_PT_Normals_Panel(Super_Panel):
    bl_idname='bc.normals_panel'
    bl_label=''

    @classmethod
    def poll(cls, context):
        return not context.scene.instantclean_misc.results or (context.scene.instantclean_categories.normals and bpy.context.scene['Normals'] is not None and [v for k, v in bpy.context.scene['Normals'].items() if type(v) != type(False)])

    def draw_header(self, context):
        sub_panel_header(self.layout, 'normals', context.scene.instantclean_misc.results)

    def draw(self, context):
        layout = self.layout
        layout.enabled = context.scene.instantclean_categories.normals
        pg = context.scene.instantclean_normals

        sub = sub_layout(layout, 3)

        if not context.scene.instantclean_misc.results:
            sub.prop(pg, 'recalculate')
            col = sub.column()
            col.prop(pg, 'recalculate_orientation', text='')
            col.enabled = pg.recalculate

            sub.separator()

            sub.prop(pg, 'auto_smooth')
            col = sub.column()
            col.prop(pg, 'auto_smooth_ang')
            col.enabled = pg.auto_smooth

            sub.separator()
            sub.prop(pg, 'weighted_normals')

            sub.separator()
            sub.label(text='Clear Data')
            box = sub.box()
            col = box.column()
            col.prop(pg, 'clear_custom_split_normals')
            col.prop(pg, 'clear_sharp_edges')
        
        else:
            results_layout(sub, bpy.context.scene['Normals'])
        