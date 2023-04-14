from PIL import Image
import argparse
import os

def crop_images(folder_path, crop_size, output_folder):

    # 创建保存裁剪后图片的文件夹
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # 遍历文件夹下所有的图片文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
            # 打开图片文件
            image_path = os.path.join(folder_path, file_name)
            with Image.open(image_path) as image:
                # 计算裁剪区域的左上角和右下角坐标
                width, height = image.size
                left = (width - crop_size) // 2
                top = (height - crop_size) // 2
                right = left + crop_size
                bottom = top + crop_size

                # 裁剪图片
                cropped_image = image.crop((left, top, right, bottom))

                # 保存裁剪后的图片
                output_file_name = 'cropped_' + file_name
                output_file_path = os.path.join(output_folder, output_file_name)
                cropped_image.save(output_file_path)



if __name__ == '__main__':
    # 创建解析器
    parser = argparse.ArgumentParser(description="crop pic")
    # 添加文件路径参数
    parser.add_argument('folder_path', type=str, help="Path of the src dir")
    # 添加参数size
    parser.add_argument('crop_size', type=str, help="crop size")
    # 添加保存目录参数
    parser.add_argument('output_folder', type=str, help="Path of the output dir")
    # 裁剪图片
    crop_images(parser.folder_path, parser.crop_size, parser.output_folder)
