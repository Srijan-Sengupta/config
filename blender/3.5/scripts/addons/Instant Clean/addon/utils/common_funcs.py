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
import bmesh


def select_geo(geometry):
    for geo in geometry:
        geo.select = True


def deselect_geo(geometry):
    for geo in geometry:
        geo.select = False


def deselect_all_geo(bm):
    for type in ('verts', 'edges', 'faces'):
        for geo in getattr(bm, type):
            geo.select = False


def in_mode(mode: str):
    return bpy.context.mode == mode


def update_mesh(obj):
    bmesh.update_edit_mesh(obj.data)


def get_objects():
    if not bpy.context.selected_objects and not bpy.context.objects_in_mode:
        return []
    if bpy.context.mode == 'OBJECT':
        return bpy.context.selected_objects
    else:
        return bpy.context.objects_in_mode


def get_bmeshs(objects):
    bmeshs = []
    for obj in objects:
        bmeshs.append(bmesh.from_edit_mesh(obj.data))

    return bmeshs


def update_bmeshs(objects):
    for obj in objects:
        bmesh.update_edit_mesh(obj.data)


def visible_verts(bm):
    return [v for v in bm.verts if not v.hide]


def visible_edges(bm):
    return [e for e in bm.edges if not e.hide]

    
def visible_faces(bm):
    return [f for f in bm.faces if not f.hide]


def visible_loops(bm):
    loops = []
    for f in bm.faces:
        for loop in f.loops:
            if not loop.vert.hide:
                loops.append(loop)
    
    return loops


def get_triangle_count(faces):
    count = 0
    for f in faces:
        count += len(f.loops) - 2

    return count