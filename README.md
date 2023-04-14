# python
放一些好用的python工具脚本

convert.py是执行在blender里面的代码。在blender控制台执行以下命令，将blender当前画布的3d模型保存成mp4文件。
```
exec(compile(open("/Users/siyu/Documents/AIGC/运动模型/convert.py").read(), "/Users/siyu/Documents/AIGC/运动模型/convert.py", 'exec'))
```

crop.py是将某个文件夹下面所有的图片，就图像的中心，裁剪成n*n的大小，n可以输入，然后保存到输出文件夹里面。执行脚本，然后按照脚本提示输入参数
```
python crop.py
```

split_mp4_to_frames是将mp4视频转换成一帧一帧的图片，保存到输出文件夹中
```
python split_mp4_to_frames.py "/Users/siyu/Documents/AIGC/运动模型/Hip Hop Dancing.mp4" "/Users/siyu/Documents/AIGC/运动模型/Hip-Hop-Dancing"
```
