import math
import pygame

cached_raw_images = {}
cached_transformed_images = {}
cached_fonts = {}

def _spec_load_image(file_path: str ):
    if (not file_path in cached_raw_images):

        loaded_image = pygame.image.load(file_path)
        cached_raw_images[file_path] = loaded_image
        return loaded_image

    else:
        print("cached") 
        loaded_image = cached_raw_images[file_path]
        return loaded_image

def _spec_transform_image(file_path: str, image, sx, sy):
    key = (file_path, image, sx, sy)
    if (not key in cached_transformed_images):

        resized_image = pygame.transform.scale(image, (sx, sy))
        cached_transformed_images[key] = resized_image
        return resized_image

    else:
        
        resized_image = cached_transformed_images[key]
        return resized_image

def _spec_font_get(text_font: str, size):
    key = (text_font, size)
    if (not key in cached_fonts):

        cached_font = pygame.font.SysFont(text_font, size)
        cached_fonts[key] = cached_font
        return cached_font

    else:
        
        cached_font = cached_fonts[key]
        return cached_font


def get_relative_mouse_pos(surface: pygame.Surface) -> tuple[float, float]:
    smallest_dimension = min(surface.width, surface.height)
    absolute_mouse_pos = pygame.mouse.get_pos()

    original_display_width, original_display_height = surface.size

    mouse_x = absolute_mouse_pos[0] - (((surface.width) - smallest_dimension) / 2)
    mouse_y = absolute_mouse_pos[1] - (((surface.height) - smallest_dimension) / 2)

    mouse_x = (mouse_x) / (smallest_dimension / (original_display_width))
    mouse_y = (mouse_y) / (smallest_dimension / (original_display_height))

    return (mouse_x, mouse_y)


def draw_rect(
    surface: pygame.Surface,
    color_rgb: tuple[int, int, int] = (0, 0, 0),
    x: int = 0,
    y: int = 0,
    w: int = 0,
    h: int = 0,
) -> None:
    original_display_width, original_display_height = surface.size

    smallest_dimension = min(surface.width, surface.height)

    pygame.draw.rect(
        surface,
        color_rgb,
        (
            ((smallest_dimension / original_display_width) * x)
            + ((surface.get_width() - smallest_dimension) / 2),
            ((smallest_dimension / original_display_height) * y)
            + ((surface.get_height() - smallest_dimension) / 2),
            (smallest_dimension / original_display_width) * w,
            (smallest_dimension / original_display_height) * h,
        ),
    )


def draw_text(
    surface: pygame.Surface,
    text: str = "",
    x: int = 0,
    y: int = 0,
    size: int = 0,
    font: str = "",
    color_rgb: tuple[int, int, int] = (0, 0, 0),
    boolean: bool = False,
) -> None:
    original_display_width, original_display_height = surface.size
    smallest_dimension = min(surface.width, surface.height)
    font_obj =  _spec_font_get(font, math.floor((smallest_dimension / original_display_height) * size))

    text_surface = font_obj.render(text, boolean, color_rgb)
    text_rect = text_surface.get_rect(
        center=(
            math.floor(
                ((smallest_dimension / original_display_width) * x)
                + ((surface.get_width() - smallest_dimension) / 2)
            ),
            math.floor(
                ((smallest_dimension / original_display_height) * y)
                + ((surface.get_height() - smallest_dimension) / 2)
            ),
        )
    )
    surface.blit(text_surface, text_rect)


# Draw Text at X,Y with specific size,font and RGB (resizes with screen)
def draw_text_to_right(
    surface: pygame.Surface,
    text: str = "",
    x: int = 0,
    y: int = 0,
    size: int = 0,
    font: str = "",
    color_rgb: tuple[int, int, int] = (0, 0, 0),
    boolean: bool = False,
) -> None:
    original_display_width, original_display_height = surface.size
    smallest_dimension = min(surface.width, surface.height)
    font_obj =  _spec_font_get(font, math.floor((smallest_dimension / original_display_height) * size))
    text_surface = font_obj.render(text, boolean, color_rgb)
    text_rect = text_surface.get_rect(
        center=(
            math.floor(
                ((smallest_dimension / original_display_width) * x)
                + (text_surface.get_width()/2)
            ),
            math.floor(
                ((smallest_dimension / original_display_height) * y)
                + ((surface.get_height() - smallest_dimension) / 2)
            ),
        )
    )
    surface.blit(text_surface, text_rect)

# Draw Text at X,Y with specific size,font and RGB (resizes with screen)
def draw_text_to_left(
    surface: pygame.Surface,
    text: str = "",
    x: int = 0,
    y: int = 0,
    size: int = 0,
    font: str = "",
    color_rgb: tuple[int, int, int] = (0, 0, 0),
    boolean: bool = False,
) -> None:
    original_display_width, original_display_height = surface.size
    smallest_dimension = min(surface.width, surface.height)
    font_obj =  _spec_font_get(font, math.floor((smallest_dimension / original_display_height) * size))
    text_surface = font_obj.render(text, boolean, color_rgb)
    text_rect = text_surface.get_rect(
        center=(
            math.floor(
                ((smallest_dimension / original_display_width) * x)
                - (text_surface.get_width() / 2)
            ),
            math.floor(
                ((smallest_dimension / original_display_height) * y)
                + ((surface.get_height() - smallest_dimension) / 2)
            ),
        )
    )
    surface.blit(text_surface, text_rect)

def draw_image(
    surface: pygame.Surface,
    x: int = 0,
    y: int = 0,
    path: str = "",
    rotation: int = 0,
) -> None:
    original_display_width, original_display_height = surface.size
    smallest_dimension = min(surface.width, surface.height)

    image = _spec_load_image(path)

    size = image.get_size()
    ratio = smallest_dimension / original_display_width

    resized_image = _spec_transform_image(path ,image, math.floor(ratio * size[0]), math.floor(ratio * size[1]) )
    rotated_image = pygame.transform.rotate(resized_image, rotation)

    rect = rotated_image.get_rect(
        center=(
            math.floor(
                ((smallest_dimension / original_display_width) * x)
                + ((surface.get_width() - smallest_dimension) / 2)
            ),
            math.floor(
                ((smallest_dimension / original_display_height) * y)
                + ((surface.get_height() - smallest_dimension) / 2)
            ),
        )
    )

    surface.blit(rotated_image, rect)
