import pyautogui
import time
import cv2
import keyboard

def clickLetters(word):
    for letter in word:
        x = keyLocs.get(letter)[0]
        y = keyLocs.get(letter)[1]
        pyautogui.click(x, y)
        time.sleep(0.3)
    time.sleep(0.5)
    pyautogui.click(1500, 850)
    time.sleep(1.5)
    return

def checkWord(word):
    for i in range(5):
        if word[i] not in potential_word[i]:
            return False
    for letter in letters_in_word:
        if letter not in word:
            return False
    return True


def checkDoubles(word):
    curLetters = []
    for letter in word:
        if letter in curLetters:
            return True
        else:
            curLetters.append(letter)
    return False


def calcScore(word):
    score = 0
    for letter in word:
        for string in values:
            if letter in string:
                score += values[string]
    return score

def takeScreenshot():
    pic = pyautogui.screenshot(region=(1139, 287, 350, 420))
    for x in range(0, 5):
        r, g, b = pic.getpixel((10 + (x * 70), offset + 10))
        colours[x] = g
    return colours

alphabet = "abcdefghijklmnopqrstuvwxyz"
keyLocs = {
    'q':(1106,763),
    'w':(1152,765),
    'e':(1198,763),
    'r':(1248,763),
    't':(1288,763),
    'y':(1334,763),
    'u':(1378,763),
    'i':(1420,763),
    'o':(1470,763),
    'p':(1514,763),
    'a':(1108,810),
    's':(1159,810),
    'd':(1201,810),
    'f':(1259,810),
    'g':(1314,810),
    'h':(1360,810),
    'j':(1413,810),
    'k':(1461,810),
    'l':(1512,810),
    'z':(1177,853),
    'x':(1223,853),
    'c':(1269,853),
    'v':(1311,853),
    'b':(1354,853),
    'n':(1398,853),
    'm':(1443,853)
}
potential_word = []
for i in range(5):
    potential_word.append(alphabet)

letters_in_word = []
blacklistedWords = []
offset = 30
index = 0

green = 184
grey = 174
yellow = 194
black = 18
white = 252

valid_col = [green,grey,yellow,black]

# 1139, 287
# 1482, 698
# offset 70

while True:
    retry = False
    if keyboard.is_pressed('q'):
        exit()

    f = open("changed_words.txt", 'r')
    values = {
        "aeioulnstr": 1,
        "dg": 2,
        "bcmp": 3,
        "fhvwy": 4,
        "k": 5,
        "jx": 8,
        "qz": 10
    }
    letters = 0
    list_lowest = []
    lowest_score = 1000
    valid_letters = []
    invalid_letters = []
    colours = [0, 0, 0, 0, 0]

    valid = False  # Insert word to be checked

    if index == 0:
        current_word = "slate"

        clickLetters(current_word)

    pic = pyautogui.screenshot(region=(1139, 287, 350, 420))
    for x in range(0, 5):
        r, g, b = pic.getpixel((10 + (x * 70), offset + 10))
        colours[x] = g

    finished = True
    for k in range(5):
        if colours[k] != green:
            finished = False
        if colours[0] == white:
            while True:
                if keyboard.is_pressed('q'):
                    exit()
                for x in range(5):
                    pyautogui.click(1128,859)
                    time.sleep(0.3)
                blacklistedWords.append(current_word)
                answers.pop(0)
                current_word = answers[0]
                for letter in current_word:
                    x = keyLocs.get(letter)[0]
                    y = keyLocs.get(letter)[1]
                    pyautogui.click(x, y)
                    time.sleep(0.3)

                pyautogui.click(1500, 850)
                time.sleep(1.5)
                pic = pyautogui.screenshot(region=(1139, 287, 350, 420))
                for x in range(0, 5):
                    r, g, b = pic.getpixel((10 + (x * 70), offset + 10))
                    colours[x] = g
                finished = True
                for k in range(5):
                    if colours[k] != green:
                        finished = False
                if colours[0] != white:
                    break

    if not finished:
        for i in range(5):
            if colours[i] == green:
                potential_word[i] = current_word[i]
                if current_word[i] not in valid_letters:
                    valid_letters.append(current_word[i])
            if colours[i] == yellow:
                s = potential_word[i]
                s1 = s.replace(current_word[i], '')
                potential_word[i] = s1
                if current_word[i] not in valid_letters:
                    valid_letters.append(current_word[i])
            if colours[i] == grey:
                if current_word[i] not in valid_letters:
                    for j in range(5):
                        s = potential_word[j]
                        s1 = s.replace(current_word[i], '')
                        potential_word[j] = s1

        valid_word = True

        answers = []
        doubles = []
        for line in f:
            if not checkWord(line[:5]):
                pass
            else:
                if (line[:5] not in blacklistedWords):
                    if checkDoubles(line[:5]):
                        doubles.append(line[:5])
                    else:
                        answers.append(line[:5])
        for word in doubles:
            answers.append(word)

        if len(answers) > 1:
            nonDoublesNum = 0
            for word in answers:
                if not checkDoubles(word):
                    nonDoublesNum += 1

            lowestScore = 1000
            topWord = ""

            if nonDoublesNum > 0:
                for word in answers:
                    if not checkDoubles(word):
                        a = calcScore(word)
                        if a <= lowestScore:
                            lowestScore = a
                            topWord = word
            else:
                for word in answers:
                    a = calcScore(word)
                    if a <= lowestScore:
                        lowestScore = a
                        topWord = word
        else:

            topWord = answers[0]

        offset += 70
        index += 1
        current_word = topWord
        for letter in current_word:
            x = keyLocs.get(letter)[0]
            y = keyLocs.get(letter)[1]
            pyautogui.click(x, y)
            time.sleep(0.3)
        time.sleep(0.5)
        pyautogui.click(1500, 850)
        time.sleep(1.5)
        blacklistedWords.append(current_word)
        f.close()
    else:
        while True:
            time.sleep(0.2)
            restartImage = cv2.imread('restart.png')
            if pyautogui.locateOnScreen(restartImage, confidence=0.9):
                pyautogui.click(1312, 482)
                offset = 30
                index = 0
                potential_word = []
                for i in range(5):
                    potential_word.append(alphabet)

                letters_in_word = []
                blacklistedWords = []

                time.sleep(1)
                break

# print(list_lowest)
# print(len(list_lowest))
# print(letters)
