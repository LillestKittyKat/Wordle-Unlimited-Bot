import pyautogui
import time


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


# set up word

alphabet = "abcdefghijklmnopqrstuvwxyz"
potential_word = []
for i in range(5):
    potential_word.append(alphabet)
# print(potential_word)

letters_in_word = []
blacklistedWords = []
offset = 30
index = 0

green = 141
grey = 58
yellow = 159
black = 18

while True:

    f = open("changed_words.txt", 'r')
    # print(f)
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
        current_word = input("What word did you use first?")
    else:
        input("Type in word and push Enter when complete")
    pic = pyautogui.screenshot(region=(1275, 275, 330, 400))
    for x in range(0, 5):
        r, g, b = pic.getpixel((10 + (x * 70), offset))
        # print("Green = " + str(g))
        colours[x] = g

    print(colours)
    finished = True
    for k in range(5):
        if colours[k] != green:
            finished = False

    if finished:
        exit()
    # work out what letters we have

    for i in range(5):
        if colours[i] == green:
            print("Letter " + current_word[i].upper() + " is here and in the right position")
            potential_word[i] = current_word[i]
            if current_word[i] not in valid_letters:
                valid_letters.append(current_word[i])
            print(potential_word)
        if colours[i] == yellow:
            print("Letter " + current_word[i].upper() + " is in the word somewhere but not in this position")
            s = potential_word[i]
            s1 = s.replace(current_word[i], '')
            potential_word[i] = s1
            # potential_word[i].replace(current_word[i],"")
            if current_word[i] not in valid_letters:
                valid_letters.append(current_word[i])
            print(potential_word)
        if colours[i] == grey:
            if current_word[i] not in valid_letters:
                print("Letter " + current_word[i].upper() + " is not here")
                for j in range(5):
                    s = potential_word[j]
                    s1 = s.replace(current_word[i], '')
                    potential_word[j] = s1
                    # a.replace(current_word[i],"")
            print(potential_word)


    # print(current_word)

    # yellows = input("enter any yellow letters in their positions, enter ? for dark or green letters (push enter if
    # no yellows yet): ")



    valid_word = True
    # print(letters_in_word)
    # print(potential_word)
    print("Potential  Words:")
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

        # count amount of non doubles
        nonDoublesNum = 0
        for word in answers:
            if not checkDoubles(word):
                nonDoublesNum += 1

        lowestScore = 1000
        topWord = ""

        # if more than one non double, only use words with non doubles
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

    print("Please type in " + topWord)
    offset += 70
    index += 1
    current_word = topWord
    blacklistedWords.append(current_word)
    f.close()

''' for line in f:
    score = 0
    for letter in line:
        for key in values:
            if letter in key:
                score += values[key]
    if score < lowest_score:
        # print(score)
        lowest_score = score
        list_lowest = [line[:5]]
    elif score == lowest_score:
        # print(score)
        list_lowest.append(line[:5]) '''
# print(list_lowest)
# print(len(list_lowest))
# print(letters)
