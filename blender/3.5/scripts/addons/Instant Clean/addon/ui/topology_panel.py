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


class INSTANTCLEAN_PT_Topology_Panel(Super_Panel):
    bl_idname='bc.topology_panel'
    bl_label=''

    @classmethod
    def poll(cls, context):
        return not context.scene.instantclean_misc.results or (context.scene.instantclean_categories.topology and bpy.context.scene['Topology'] is not None and [v for k, v in bpy.context.scene['Topology'].items() if type(v) != type(False)])

    def draw_header(self, context):
        sub_panel_header(self.layout, 'topology', context.scene.instantclean_misc.results)

    def draw(self, context):
        layout = self.layout
        layout.enabled = context.scene.instantclean_categories.topology
        pg = context.scene.instantclean_topology

        sub = sub_layout(layout, 3)

        if not context.scene.instantclean_misc.results:
            sub.label(text='Convert to')

            col = sub.column()
            col.prop(pg, 'type', text='')

            if pg.type == 'TRIS':
                sub.separator()
                sub.label(text='Methods')
                box = sub.box()

                split = box.split(factor=0.3)

                col = split.column()
                col.label(text='Quads')
                col.label(text='NGons')

                col = split.column()
                col.prop(pg, 'quad_method', text='')
                col.prop(pg, 'ngon_method', text='')
            else:
                sub.prop(pg, 'quad_max_face_ang')
                sub.prop(pg, 'quad_max_shape_ang')
                sub.separator()
                sub.label(text='Compare')
                box = sub.box()

                split = box.split()

                col = split.column()
                col.prop(pg, 'compare_sharp')
                col.prop(pg, 'compare_uv')
                col.prop(pg, 'compare_vcol')

                col = split.column()
                col.prop(pg, 'compare_seam')
                col.prop(pg, 'compare_material')
        else:
            results_layout(sub, bpy.context.scene['Topology'])