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

from ..ui.layout_temps import popup_results

from ..utils.repair import repair
from ..utils.normals import normals
from ..utils.manifold import manifold
from ..utils.dissolve import dissolve
from ..utils.topology import topology
from ..utils.objectdata import objectdata


class INSTANTCLEAN_OT_Clean(bpy.types.Operator):
    bl_idname='instantclean.clean'
    bl_label='Clean'
    bl_description='Clean the selected objects based on your settings.\nShift: Selection only'
    bl_options={'UNDO', 'REGISTER'}

    action: bpy.props.StringProperty() #all|repair|manifold|dissolve|topology|normals|objectdata|close
    stats = {}


    def invoke(self, context, event):
        self.bl_label = 'Clean'
        if self.action == 'close':
            context.scene.instantclean_misc.results = False
            return {'CANCELLED'}

        self.selection_only = event.shift
        prev_mode = context.mode
        prev_mesh_select_mode = context.scene.tool_settings.mesh_select_mode[:]
        prev_active = context.view_layer.objects.active
        self.objects = [o for o in context.view_layer.objects.selected if o.type == 'MESH']
        if not self.objects: return {'CANCELLED'}

        if context.mode != 'EDIT_MESH': bpy.ops.object.mode_set(mode='EDIT')
        self.bmeshes = [bmesh.from_edit_mesh(o.data) for o in self.objects]
        if self.selection_only:
            prev_hidden = set()
            for bm in self.bmeshes: [prev_hidden.add(v) for v in bm.verts if v.hide]
            bpy.ops.mesh.hide(unselected=True)

        else: bpy.ops.mesh.select_all(action='SELECT')

        # actions
        if self.action == 'all':
            self.execute_all(context)
        
        elif self.action == 'repair':
            self.stats = repair(context, self.objects, self.bmeshes)
            for obj in self.objects: bmesh.update_edit_mesh(obj.data)
        
        elif self.action == 'normals':
            self.stats = normals(context, self.objects, self.bmeshes)
            for obj in self.objects: bmesh.update_edit_mesh(obj.data)

        elif self.action == 'manifold':
            self.stats = manifold(context, self.objects, self.bmeshes)
            for obj in self.objects: bmesh.update_edit_mesh(obj.data)
        
        elif self.action == 'dissolve':
            self.stats = dissolve(context, self.objects, self.bmeshes)
            for obj in self.objects: bmesh.update_edit_mesh(obj.data)
        
        elif self.action == 'topology':
            self.stats = topology(context, self.objects, self.bmeshes)
            for obj in self.objects: bmesh.update_edit_mesh(obj.data)
        
        elif self.action == 'objectdata':
            self.stats = objectdata(context, self.objects, self.bmeshes)
          
        if self.selection_only:
            bpy.ops.mesh.reveal(select=False)
            for v in prev_hidden: v.hide_set(True)

        else: bpy.ops.mesh.select_all(action='DESELECT')
        if prev_mode == 'OBJECT': bpy.ops.object.mode_set(mode='OBJECT')
        context.scene.tool_settings.mesh_select_mode = prev_mesh_select_mode
        context.view_layer.objects.active = prev_active
        if self.action == 'all':
            bpy.ops.ed.undo_push(message=self.action)
            return {'CANCELLED'}
        
        return {'FINISHED'}
    

    def execute(self, context):
        return {'FINISHED'}
    

    def draw(self, context):
        if self.action != 'all': popup_results(self.layout, self.stats)
    

    def execute_all(self, context):
        pg = context.scene.instantclean_categories
        context.scene['Stats'] = {
                        'Triangles': 0,
                        'Vertices': 0,
                        'Edges': 0,
                        'Faces': 0
                    }

        for o in self.objects:
            count = o.data.count_selected_items()
            tris = 0
            for f in o.data.polygons: tris += len(f.vertices) - 2
            context.scene['Stats']['Triangles'] += tris
            context.scene['Stats']['Vertices'] += count[0]
            context.scene['Stats']['Edges'] += count[1]
            context.scene['Stats']['Faces'] += count[2]

        context.scene['Repair'] = False
        context.scene['Manifold'] = False
        context.scene['Normals'] = False
        context.scene['Dissolve'] = False
        context.scene['Topology'] = False
        context.scene['Objectdata'] = False

        if pg.repair: 
            context.scene['Repair'] = repair(context, self.objects, self.bmeshes)

        if pg.manifold:
            context.scene['Manifold'] = manifold(context, self.objects, self.bmeshes)
        
        if pg.normals:
            context.scene['Normals'] = normals(context, self.objects, self.bmeshes)

        if pg.dissolve:
            context.scene['Dissolve'] = dissolve(context, self.objects, self.bmeshes)

        if pg.topology:
            context.scene['Topology'] = topology(context, self.objects, self.bmeshes)

        for obj in self.objects: bmesh.update_edit_mesh(obj.data)

        if pg.objectdata:
            context.scene['Objectdata'] = objectdata(context, self.objects, self.bmeshes)

        bpy.ops.mesh.select_all(action='SELECT')
        for o in self.objects:
            count = o.data.count_selected_items()
            tris = 0
            for f in o.data.polygons: tris += len(f.vertices) - 2
            context.scene['Stats']['Triangles'] -= tris
            context.scene['Stats']['Vertices'] -= count[0]
            context.scene['Stats']['Edges'] -= count[1]
            context.scene['Stats']['Faces'] -= count[2]

        context.scene.instantclean_misc.results = True
        for k in context.scene['Stats'].keys():
            if context.scene['Stats'][k] >= 0:
                context.scene['Stats'][k] = -context.scene['Stats'][k]
            else:
                context.scene['Stats'][k] = '+' + str(-context.scene['Stats'][k])
