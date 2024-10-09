import pygame
import sys
from PIL import Image
from convert import conver_to_map, get_map_with_walls, get_txt

screen_width = 1280
screen_height = 1280

picture_width = 64
picture_height = 64
filename = "file.png"

cell_size = screen_width // picture_width

def save_image(surface):
    img = pygame.image.tostring(surface, 'RGB')
    image = Image.frombytes('RGB', (screen_width, screen_height), img)
    image = image.resize((picture_width, picture_height))
    image.save(filename)
    return image


def draw():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pixel Art Program")

    color = (0, 0, 0)
    screen.fill(color)
    
    drawing = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False      
                  
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

        if drawing:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = mouse_x // cell_size
            grid_y = mouse_y // cell_size

            pygame.draw.rect(screen, (255, 255, 255), (grid_x * cell_size, grid_y * cell_size, cell_size, cell_size))

        pygame.display.flip()

    return screen

if __name__ == "__main__":
    pygame.init()
    screen = draw()
    resized = save_image(screen)
    map = conver_to_map(resized)
    map_for_cub3d = get_map_with_walls(map)
    get_txt(map_for_cub3d)
    pygame.quit()
    