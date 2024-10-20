import math
import pygame

spritesFolderPath = "sprites\\"

originalDisplayWidth = 640
originalDisplayHeight = 640
# Calculate the smallest for height and width
# CalculateHeightANDwidthIntoSmallesT = CHADIST


# Draw Rectangle(resizes with screen)
def DrawRect(surface, R, G, B, X, Y, W, H):
    chad = min(surface.get_width(),surface.get_height())
    pygame.draw.rect(
        (surface),
        (R, G, B),
        (
            ((chad / originalDisplayWidth) * X)
            + (surface.get_width() - chad) / 2,
            ((chad / originalDisplayHeight) * Y)
            + (surface.get_height() - chad) / 2,
            (chad / originalDisplayWidth) * W,
            (chad / originalDisplayHeight) * H,
        ),
    )

# Draw Text at X,Y with specific size,font and RGB (resizes with screen)
def DrawText(surface, text, X, Y, Size, font, R, G, B, Boolean):
    chad = min(surface.get_width(),surface.get_height())
    font = pygame.font.SysFont(
        font, math.floor((chad / originalDisplayHeight) * Size)
    )
    textSurface = font.render(text, Boolean, (R, G, B))
    textrect = textSurface.get_rect(
        center=(
            math.floor(
                (chad / originalDisplayWidth) * X
                + (surface.get_width() - chad) / 2
            ),
            math.floor(
                (chad / originalDisplayHeight) * Y
                + (surface.get_height() - chad) / 2
            ),
        )
    )
    surface.blit(textSurface, textrect)

# Draws an Image
def DrawImage(surface, X, Y, imgname, rotation):
    chad = min(surface.get_width(),surface.get_height())
    image = pygame.image.load(spritesFolderPath+imgname)
    Size = image.get_size()

    ratio = chad / originalDisplayWidth
    if ratio != 1:
        image = pygame.transform.scale(
            image, (math.floor(ratio * Size[0]), math.floor(ratio * Size[1]))
        )
    image2 = pygame.transform.rotate(image, rotation)
    imgRect = image2.get_rect(
        center=(
            math.floor(
                (chad / originalDisplayWidth) * X
                + (surface.get_width() - chad) / 2
            ),
            math.floor(
                (chad / originalDisplayHeight) * Y
                + (surface.get_height() - chad) / 2
            ),
        )
    )
    surface.blit(image2, imgRect)


# get the position of the mouse
def mousePos(surface):
    chad = min(surface.get_width(),surface.get_height())
    MousePosition = pygame.mouse.get_pos()
    MousePositionX = MousePosition[0] - (((surface.get_width()) - chad )/ 2)
    MousePositionY = MousePosition[1] - (((surface.get_height()) - chad )/ 2)
    MousePositionX = (MousePositionX) / (chad * (originalDisplayWidth))
    MousePositionY = (MousePositionY) / (chad * (originalDisplayHeight))
    return (MousePositionX, MousePositionY)

