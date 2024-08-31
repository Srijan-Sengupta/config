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


class INSTANTCLEAN_PT_ManifoldPanel(Super_Panel):
    bl_idname='instantclean.manifold_panel'
    bl_label=''

    @classmethod
    def poll(cls, context):
        return not context.scene.instantclean_misc.results or (context.scene.instantclean_categories.manifold and bpy.context.scene['Manifold'] is not None and [v for k, v in bpy.context.scene['Manifold'].items() if type(v) != type(False)])

    def draw_header(self, context):
        sub_panel_header(self.layout, 'manifold', context.scene.instantclean_misc.results)

    def draw(self, context):
        layout = self.layout
        layout.enabled = context.scene.instantclean_categories.manifold
        pg = context.scene.instantclean_manifold

        sub = sub_layout(layout, 3)

        if not context.scene.instantclean_misc.results:
            sub.prop(pg, 'fill_holes')
            row = sub.row()
            row.enabled = pg.fill_holes
            row.prop(pg, 'fill_holes_max_sides')
            
            sub.separator()
            sub.label(text='Remove')
            box = sub.box()
            col = box.column()
            col.prop(pg, 'non_manifold_faces')
            col.prop(pg, 'non_manifold_verts')
            col.prop(pg, 'wire_geo')

            sub.separator()
            sub.label(text='Make Planar')
            box = sub.box()
            boxsub = box.column()
            split = boxsub.split()
            col = split.column()
            col.prop(pg, 'undistort')
            col.prop(pg, 'flatten')
            col = split.column()
            row = col.row()
            row.enabled = pg.undistort
            row.prop(pg, 'undistort_ang', text='')
            row = col.row()
            row.enabled = pg.flatten
            row.prop(pg, 'flatten_factor', text='')
            row = boxsub.row()
            row.enabled = pg.flatten
            row.prop(pg, 'flatten_iterations', text='Flatten Iterations')

        else:
            results_layout(sub, bpy.context.scene['Manifold'])

            

