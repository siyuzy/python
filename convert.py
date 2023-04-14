import bpy

# 获取当前场景
scene = bpy.context.scene
camera = scene.camera

# 如果不存在摄像机，则创建一个
if camera is None:
    camera_data = bpy.data.cameras.new(name="Camera")
    camera = bpy.data.objects.new(name="Camera", object_data=camera_data)
    scene.collection.objects.link(camera)
    scene.camera = camera
    # 设置摄像机位置camera_object.location = [10, 0, 0]

# 设置输出参数
scene.render.image_settings.file_format = "FFMPEG"
scene.render.ffmpeg.format = "MPEG4"
scene.render.ffmpeg.codec = "H264"

# 设置输出路径和文件名
scene.render.filepath = "/Users/siyu/Documents/AIGC/运动模型/Hip Hop Dancing.mp4"

# 渲染动画
bpy.ops.render.render(animation=True)
