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

from .presets_op import INSTANTCLEAN_MT_Preset_Menu, INSTANTCLEAN_OT_Add_Preset, INSTANTCLEAN_OT_Override_Preset
from .prefs_op import INSTANTCLEAN_OT_Reinstall_Presets
from .clean import INSTANTCLEAN_OT_Clean


classes = [
    INSTANTCLEAN_MT_Preset_Menu,
    INSTANTCLEAN_OT_Add_Preset,
    INSTANTCLEAN_OT_Override_Preset,
    INSTANTCLEAN_OT_Reinstall_Presets,
    INSTANTCLEAN_OT_Clean,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)