# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import time
import keyboard


# letter 1 1305,300
# letter 2 1371, 300
# letter 3 1438, 300
# letter 4 1507, 300
# letter 5 1574, 300
# vertical offset - 70

# screenshot 1275 274 1604, 674

colours = [0,0,0,0,0]
green = 141
grey = 58
yellow = 159
black = 18

def main():
    index = 0
    offset = 30
    while offset < 400:
        # print(pyautogui.position())
        pic = pyautogui.screenshot(region = (1275,275,330,400))
        for x in range(0, 5):
            r,g,b = pic.getpixel((10+(x * 70), offset))
            # print("Green = " + str(g))
            colours[x] = g
        print(colours)
        offset += 70
        index += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
