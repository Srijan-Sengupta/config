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



bl_info = {
    "name": "Instant Clean",
    "description": "Clean Mesh in one Click",
    "blender": (2, 93, 0),
    'version': (2, 0, 0),
    "category": "Mesh",
    "author": "Ruben Messerschmidt",
    "location": "View3D > Sidebar > Instant Clean",
    'doc_url': 'https://instant-clean.readthedocs.io/en/latest/',
}

import bpy
import addon_utils
import sys
import os
import shutil
import importlib
import pkgutil
from pathlib import Path
from bpy.types import AddonPreferences



##### Load Modules #####


def get_all_submodules(directory):
    return list(iter_submodules(directory, directory.name))


def iter_submodules(path, package_name):
    for name in sorted(iter_submodule_names(path)):
        mod = importlib.import_module("." + name, package_name)
        yield mod


def iter_submodule_names(path, root=""):
    for _, module_name, is_package in pkgutil.iter_modules([str(path)]):
        if is_package:
            if module_name == 'standard_presets':
                continue
            sub_path = path / module_name
            sub_root = root + module_name + "."
            yield from iter_submodule_names(sub_path, sub_root)
        else:
            yield root + module_name


def reload_modules():
    for name in reload_list:
        importlib.reload(sys.modules[name])


def get_loaded_modules():
    prefix = __name__ + "."
    return [name for name in sys.modules if name.startswith(prefix)]


if "reload_list" in locals():
    reload_modules()
else:
    modules = get_all_submodules(Path(__file__).parent)
    reload_list = get_loaded_modules()

    from .addon import *



##### Addon Prefs #####


class INSTANTCLEAN_Addon_Preferences(AddonPreferences):
    bl_idname=__package__

    merge_panels: bpy.props.BoolProperty(
        name='Merge Panels',
        default=False,
        description='Merge the Instant Clean panel into the "Ruben\'s Addons" tab',
        update=lambda s, c: addon.ui.update_merge(s.merge_panels)
    )

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.enabled = False
        row.label(text='Presets')
        layout.operator('bc.reinstall_presets')

        layout.separator()
        row = layout.row()
        row.enabled = False
        row.label(text='Ruben\'s Addons')

        split = layout.split()
        col = split.column()
        col.label(text='Merge Panels')
        col = split.column()
        col.prop(self, 'merge_panels', text='')



##### Registration #####


def register():
    if bpy.app.version < (2, 93, 0):
        print('Instant Clean is not compatible with your current Blender version!')
        print('Upgrade to Blender 2.93.0 or later.')
        return

    bpy.utils.register_class(INSTANTCLEAN_Addon_Preferences)
    addon.ui.super_panel.set_merge(bpy.context.preferences.addons['Instant Clean'].preferences.merge_panels)
    addon.register()

    filepath: str
    for mod in addon_utils.modules():
        if mod.bl_info['name'] == "Instant Clean":
            filepath = mod.__file__

    presets_path = os.path.join(bpy.utils.user_resource('SCRIPTS', path='presets', create=True), 'Instant Clean')
    if not os.path.isdir(presets_path):
        standard_presets = filepath.replace('__init__.py', 'standard_presets')
        files = os.listdir(standard_presets)

        os.makedirs(presets_path)
        [shutil.copy2(os.path.join(standard_presets, f), presets_path) for f in files]

    for preset in Path(presets_path).glob('*.py'):

        with open(preset, 'r') as file:
            filedata = file.read()

        if filedata.find('bc_states') == -1:
            continue

        filedata = filedata.replace('bc_states', 'instantclean_categories')
        filedata = filedata.replace('bc_repair', 'instantclean_repair')
        filedata = filedata.replace('bc_normals', 'instantclean_normals')
        filedata = filedata.replace('bc_limdiss', 'instantclean_dissolve')
        filedata = filedata.replace('bc_topology', 'instantclean_topology')
        filedata = filedata.replace('bc_objectdata', 'instantclean_objectdata')

        filedata = filedata.replace('instantclean_categories.limdiss', 'instantclean_categories.dissolve')
        filedata = filedata.replace('instantclean_objectdata.unused_material_slots', 'instantclean_objectdata.material_slots')

        if preset.name == 'Ultimate.py':
            features = '''
instantclean_manifold = bpy.context.scene.instantclean_manifold
instantclean_categories.manifold = True
instantclean_manifold.non_manifold_faces = True
instantclean_manifold.non_manifold_verts = True
instantclean_manifold.wire_geo = True
instantclean_manifold.fill_holes = True
instantclean_manifold.fill_holes_max_sides = 4
instantclean_manifold.flatten = True
instantclean_manifold.flatten_iterations = 3
instantclean_manifold.flatten_factor = 1.0
instantclean_manifold.undistort = True
instantclean_manifold.undistort_ang = 0.0872659981250763
instantclean_topology.quad_max_face_ang = 0.6981229782104492
instantclean_topology.quad_max_shape_ang = 0.6981229782104492
instantclean_objectdata.double_materials = True
instantclean_objectdata.double_materials_remove_data = False
instantclean_objectdata.material_slots_clear = 'UNUSED'
'''
        
        elif preset.name == 'Basic.py':
            features = '''
instantclean_manifold = bpy.context.scene.instantclean_manifold
instantclean_categories.manifold = True
instantclean_manifold.non_manifold_faces = True
instantclean_manifold.non_manifold_verts = False
instantclean_manifold.wire_geo = True
instantclean_manifold.fill_holes = False
instantclean_manifold.fill_holes_max_sides = 4
instantclean_manifold.flatten = False
instantclean_manifold.flatten_iterations = 3
instantclean_manifold.flatten_factor = 1.0
instantclean_manifold.undistort = False
instantclean_manifold.undistort_ang = 0.0872659981250763
instantclean_topology.quad_max_face_ang = 0.6981229782104492
instantclean_topology.quad_max_shape_ang = 0.6981229782104492
instantclean_objectdata.double_materials = True
instantclean_objectdata.double_materials_remove_data = False
instantclean_objectdata.material_slots_clear = 'UNUSED'
'''
        
        elif preset.name == 'Light.py':
            features = '''
instantclean_manifold = bpy.context.scene.instantclean_manifold
instantclean_categories.manifold = False
instantclean_manifold.non_manifold_faces = False
instantclean_manifold.non_manifold_verts = False
instantclean_manifold.wire_geo = False
instantclean_manifold.fill_holes = False
instantclean_manifold.fill_holes_max_sides = 4
instantclean_manifold.flatten = False
instantclean_manifold.flatten_iterations = 3
instantclean_manifold.flatten_factor = 1.0
instantclean_manifold.undistort = False
instantclean_manifold.undistort_ang = 0.0872659981250763
instantclean_topology.quad_max_face_ang = 0.6981229782104492
instantclean_topology.quad_max_shape_ang = 0.6981229782104492
instantclean_objectdata.double_materials = False
instantclean_objectdata.double_materials_remove_data = False
instantclean_objectdata.material_slots_clear = 'UNUSED'
'''

        filedata = f'{filedata}{features}'

        with open(preset, 'w') as file:
            file.write(filedata)
            file.close()
            

def unregister():
    bpy.utils.unregister_class(INSTANTCLEAN_Addon_Preferences)
    addon.unregister()


if __name__ == "__main__":
    register()