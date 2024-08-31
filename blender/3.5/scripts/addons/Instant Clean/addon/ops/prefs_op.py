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
import shutil
import os
from bpy.types import Operator


class INSTANTCLEAN_OT_Reinstall_Presets(Operator):
    bl_idname='bc.reinstall_presets'
    bl_label='Reinstall Standard Presets'

    def execute(self, context):
        filepath: str
        for mod in addon_utils.modules():
            if mod.bl_info['name'] == "Instant Clean":
                filepath = mod.__file__

        presets_path = os.path.join(bpy.utils.user_resource('SCRIPTS', path='presets', create=True), 'Instant Clean')
        standard_presets = filepath.replace('__init__.py', 'standard_presets')
        files = os.listdir(standard_presets)
        installed = os.listdir(presets_path)
        for f in [f for f in files if f not in installed]:
            shutil.copy2(os.path.join(standard_presets, f), presets_path)

        self.report({'INFO'}, message='Reinstalled standard presets successfully!')

        return {'FINISHED'}