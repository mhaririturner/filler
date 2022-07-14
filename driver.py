#!/venv/bin python3

"""
driver.py: does stuff
"""

__author__ = "Max Hariri-Turner"
__email__ = "maxkht8@gmail.com"

from PIL import ImageGrab

# Constants
MAGIC_BOX = (905, 315, 1215, 585)
BOARD_HEIGHT = 7
BOARD_WIDTH = 8
BUMP = 20
COLOR_BLUE = (71, 159, 212)


def main():
    img = ImageGrab.grab(MAGIC_BOX)
    img.show()
    get_board_pixels(img)


def get_board_pixels(img):
    board = [[None for i in range(BOARD_HEIGHT)] for j in range(BOARD_WIDTH)]
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            x = BUMP + i * img.width // BOARD_WIDTH
            y = BUMP + j * img.height // BOARD_HEIGHT
            r, g, b, a = img.getpixel((x, y))
            r = r // 10 * 10
            g = g // 10 * 10
            b = b // 10 * 10
            board[i][j] = (r, g, b)
            img.putpixel((x, y), (255, 0, 0))
    print(board)
    print(len(board))
    print(len((board[0])))
    img.show()


#def color_correct(pixel):


if __name__ == "__main__":
    main()
