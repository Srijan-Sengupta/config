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


class INSTANTCLEAN_PT_Dissolve_Panel(Super_Panel):
    bl_idname='instantclean.dissolve_panel'
    bl_label=''

    @classmethod
    def poll(cls, context):
        return not context.scene.instantclean_misc.results or (context.scene.instantclean_categories.dissolve and bpy.context.scene['Dissolve'] is not None and [v for k, v in bpy.context.scene['Dissolve'].items() if type(v) != type(False)])

    def draw_header(self, context):
        sub_panel_header(self.layout, 'dissolve', context.scene.instantclean_misc.results)

    def draw(self, context):
        layout = self.layout
        layout.enabled = context.scene.instantclean_categories.dissolve
        pg = context.scene.instantclean_dissolve

        sub = sub_layout(layout, 3)

        if not context.scene.instantclean_misc.results:
            sub.prop(pg, 'max_angle')
            sub.prop(pg, 'boundaries')

            sub.separator()
            sub.label(text='Protect')
            box = sub.box()
            split = box.split()

            col = split.column()
            col.prop(pg, 'protect_seam')
            col.prop(pg, 'protect_uv')

            col = split.column()
            col.prop(pg, 'protect_sharp')
            col.prop(pg, 'protect_materials')
        else:
            results_layout(sub, bpy.context.scene['Dissolve'])

