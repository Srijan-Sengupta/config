import bpy
instantclean_categories = bpy.context.scene.instantclean_categories
instantclean_repair = bpy.context.scene.instantclean_repair
instantclean_manifold = bpy.context.scene.instantclean_manifold
instantclean_dissolve = bpy.context.scene.instantclean_dissolve
instantclean_topology = bpy.context.scene.instantclean_topology
instantclean_normals = bpy.context.scene.instantclean_normals
instantclean_objectdata = bpy.context.scene.instantclean_objectdata

instantclean_categories.repair = True
instantclean_repair.loose = True
instantclean_repair.loose_verts = True
instantclean_repair.loose_edges = True
instantclean_repair.loose_faces = True
instantclean_repair.doubles = True
instantclean_repair.doubles_dst = 9.999999747378752e-05
instantclean_repair.zero_faces = True
instantclean_repair.zero_faces_area = 9.999999747378752e-05
instantclean_repair.dispensables = True
instantclean_repair.dispensables_ang = 0.08749999850988388
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
instantclean_categories.dissolve = False
instantclean_dissolve.max_angle = 0.08749999850988388
instantclean_dissolve.boundaries = False
instantclean_dissolve.protect_sharp = True
instantclean_dissolve.protect_seam = True
instantclean_dissolve.protect_uv = True
instantclean_dissolve.protect_materials = True
instantclean_categories.topology = False
instantclean_topology.type = 'TRIS'
instantclean_topology.quad_method = 'BEAUTY'
instantclean_topology.quad_max_face_ang = 0.6981229782104492
instantclean_topology.quad_max_shape_ang = 0.6981229782104492
instantclean_topology.ngon_method = 'BEAUTY'
instantclean_topology.compare_sharp = True
instantclean_topology.compare_seam = True
instantclean_topology.compare_vcol = True
instantclean_topology.compare_uv = True
instantclean_topology.compare_material = True
instantclean_categories.normals = True
instantclean_normals.recalculate = True
instantclean_normals.recalculate_orientation = 'OUTSIDE'
instantclean_normals.auto_smooth = False
instantclean_normals.auto_smooth_ang = 0.785398006439209
instantclean_normals.weighted_normals = False
instantclean_categories.objectdata = True
instantclean_objectdata.double_materials = True
instantclean_objectdata.double_materials_remove_data = False
instantclean_objectdata.material_slots = True
instantclean_objectdata.material_slots_clear = 'UNUSED'
instantclean_objectdata.empty_vertex_groups = True
