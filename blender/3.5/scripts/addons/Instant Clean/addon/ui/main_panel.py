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
import addon_utils
from .super_panel import Super_Panel
from .layout_temps import sub_layout, results_layout
from ..ops.presets_op import INSTANTCLEAN_MT_Preset_Menu


class INSTANTCLEAN_PT_Main_Panel(Super_Panel):
    bl_idname='bc.main_panel'
    bl_label='Instant Clean'

    version = [addon.bl_info.get('version', (-1,-1,-1)) for addon in addon_utils.modules() if addon.bl_info['name'] == 'Instant Clean'][0]

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        pg = scene.instantclean_misc

        col = layout.column()
        split = layout.split()
        col = split.column()
        col.enabled = False
        col.label(text=f'Instant Clean v{self.version[0]}.{self.version[1]}.{self.version[2]}')
        col = split.column()
        row = col.row(align=True)
        row.alignment = 'RIGHT'
        row.operator('preferences.addon_show', text='', icon='PREFERENCES').module = 'Instant Clean'
        row.operator('wm.url_open', text='', icon='HELP').url = 'https://instant-clean.readthedocs.io/en/latest/'
        row.separator(factor=3)

        sub = sub_layout(layout, 3)

        
        col.separator()
        
        row = sub.row()
        row.scale_y = 2
        if bpy.context.mode not in ('OBJECT', 'EDIT_MESH'):
            row.enabled = False

        if pg.results: row.operator('instantclean.clean', text='Close Results').action = 'close'
        else: row.operator('instantclean.clean', text='Clean').action = 'all'

        row.separator(factor=1.8)

        if not pg.results:
            row = sub.row(align=True)
            row.menu(INSTANTCLEAN_MT_Preset_Menu.__name__, text=INSTANTCLEAN_MT_Preset_Menu.bl_label)
            row.operator('instantclean.override_preset', text='', icon='DUPLICATE')
            row.operator('instantclean.add_preset', text='', icon='ADD')
            row.operator('instantclean.add_preset', text='', icon='REMOVE').remove_active = True
            row.separator(factor=3)

        else:
            sub.separator()
            sub.label(text='Overall')
            row = sub.row()
            results_layout(row, bpy.context.scene['Stats'])
            row.separator()


