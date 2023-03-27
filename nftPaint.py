from PIL import Image, ImageDraw, ImageFont
import os

# 获取文件夹中所有图片路径
image_folder = 'E:\\NFT\\MARKET\\huiyuan\\fameimage'
image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.endswith('.png') or filename.endswith('.jpg')]


# 读取txt文件，保存昵称和id到字典中
members = {}
with open('E:\\NFT\\MARKET\\huiyuan\\member_name.txt', 'r') as f:
    for i, line in enumerate(f):
        # 计数器变量
        count = 1       
        nickname, member_id = line.strip().split(',')
        members[member_id] = nickname

        # 遍历所有图片
        for j, image_path in enumerate(image_paths):
            # 打开要添加昵称的图片
            img = Image.open(image_path)

            # 调整图片大小
            img = img.resize((768, 430))

            # 创建可编辑的ImageDraw对象
            draw = ImageDraw.Draw(img)

            # 设置文本属性
            font = ImageFont.truetype('arial.ttf', 36)
            color = (0, 0, 0)

            # 在图片上添加昵称
            draw.text((490, 170), nickname, font=font, fill=color)
            font = ImageFont.truetype('arial.ttf', 18)
            draw.text((450, 240), 'https://myfame.io/' + nickname, font=font, fill=color)

            # 保存修改后的图片
            img.save(os.path.join(image_folder, f'image{member_id}.png'))

            # 计数器加1
            count += 1
