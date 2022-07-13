#!/venv/bin python3

"""
driver.py: does stuff
"""

__author__ = "Max Hariri-Turner"
__email__ = "maxkht8@gmail.com"

from PIL import ImageGrab
from PIL import Image

def main():
    img = ImageGrab.grab((100, 100, 200, 200))
    img.show()


if __name__ == "__main__":
    main()