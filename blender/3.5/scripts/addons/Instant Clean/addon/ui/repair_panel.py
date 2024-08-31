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


class INSTANTCLEAN_PT_Repair_Panel(Super_Panel):
    bl_idname='bc.repair_panel'
    bl_label=''

    @classmethod
    def poll(cls, context):
        return not context.scene.instantclean_misc.results or (context.scene.instantclean_categories.repair and bpy.context.scene['Repair'] is not None and [v for k, v in bpy.context.scene['Repair'].items() if type(v) != type(False)])

    def draw_header(self, context):
        sub_panel_header(self.layout, 'repair', context.scene.instantclean_misc.results)

    def draw(self, context):
        layout = self.layout
        layout.enabled = context.scene.instantclean_categories.repair
        pg = context.scene.instantclean_repair

        sub = sub_layout(layout, 3)

        if not context.scene.instantclean_misc.results:
            sub.label(text='Remove')
            box = sub.box()
            col = box.column()
            split = col.split()
            
            col = split.column()
            col.prop(pg, 'loose')
            col.prop(pg, 'doubles')
            col.prop(pg, 'zero_faces')
            col.prop(pg, 'dispensables')

            col = split.column()
            row = col.row(align=True)
            row.prop(pg, 'loose_verts',icon='VERTEXSEL' ,icon_only=True)
            row.prop(pg, 'loose_edges',icon='EDGESEL' ,icon_only=True)
            row.prop(pg, 'loose_faces',icon='FACESEL' ,icon_only=True)
            row.enabled = pg.loose
            row = col.row()
            row.prop(pg, 'doubles_dst', icon_only=True)
            row.enabled = pg.doubles

            row = col.row()
            row.prop(pg, 'zero_faces_area', icon_only=True)
            row.enabled = pg.zero_faces
            row = col.row()
            row.prop(pg, 'dispensables_ang', icon_only=True)
            row.enabled = pg.dispensables

        else:
            results_layout(sub, bpy.context.scene['Repair'])

            

