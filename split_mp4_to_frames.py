import cv2
import argparse
import os

def extract_frames(video_path, frames_dir):
    # 如果输出的文件夹不存在，创建输出文件夹
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
        print("create dir success!")

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    # 获取视频的总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 获取视频的帧率
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # 遍历每一帧，将其保存为图片
    for i in range(total_frames):
        # 读取一帧
        ret, frame = cap.read()
        # 如果成功读取了一帧，将其保存为图片
        if ret:
            cv2.imwrite(f"{frames_dir}/{i+1}.jpg", frame)
            print(i)
            i = i + 1
        # 否则跳过这一帧
        else:
            continue
    # 释放视频文件
    cap.release()

if __name__ == '__main__':
    # 创建解析器
    parser = argparse.ArgumentParser(description="Extract frames from a mp4 video file")
    # 添加文件路径参数
    parser.add_argument('video_path', type=str, help="Path of the mp4 video file")
    # 添加保存目录参数
    parser.add_argument('frames_dir', type=str, help="Directory to save the frames")
    # 解析参数
    args = parser.parse_args()
    # 提取帧
    extract_frames(args.video_path, args.frames_dir)
