import bpy
scene = bpy.context.scene

scene.render.fps = 24
scene.render.fps_base = 1.0
scene.render.pixel_aspect_x = 1.0
scene.render.pixel_aspect_y = 1.0
scene.render.resolution_percentage = 100
scene.render.resolution_x = 640
scene.render.resolution_y = 360