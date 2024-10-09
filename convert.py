from PIL import Image
import sys

block_size = 8

def resize_png(image_path):
    img = Image.open(image_path)
    
    original_size = img.size
    print(f"Original size: {original_size}")
    
    new_size = (original_size[0] // block_size, original_size[1] // block_size)
    print(f"New size: {new_size}")

    resized_img = img.resize(new_size, Image.ANTIALIAS)

    return resized_img


def conver_to_map(image):
    map = []
    for y in range(image.size[1]):
        row = []
        for x in range(image.size[0]):
            pixel = image.getpixel((x, y))
            if pixel <= (50, 50, 50):
                row.append(' ')
            else:
                row.append('1')
        map.append(row)
    return map


def get_map_with_walls(map):
    x = len(map[0])
    y = len(map)
    map_for_cub3d = []
    for i in range(y):
        if i == 0 or i == y - 1:
            map_for_cub3d.append(['1'] * (x + 2))
        else:
            map_for_cub3d.append(['1'] + map[i] + ['1'])
    return map_for_cub3d


def get_txt(map):
    with open("map.txt", "w") as f:
        for row in map:
            f.write("".join(row) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_png>")
    else:
        Img = resize_png(sys.argv[1])
        Img.save("resized.png")
        map = conver_to_map(Img)
        map_for_cub3d = get_map_with_walls(map)
        get_txt(map_for_cub3d)
