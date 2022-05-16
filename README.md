# Wordle-Unlimited-Bot

This is a bot to play the game at https://wordle-unlimited.io/ - it requires a specific layout of the screen in order to find the correct part of the screen. 

Resolution set to 1920x1080
Wordle Unlimited on the right hand side of split screen, program on left hand side of screen

Basic description:

Starts by using the word "slate"
Scans the colours of the letters and compares the matches to a list of words in "changed_words.txt"
Will type in what it deems to be the best match - a valid word with the lowest scrabble score and therefore the most likely. It will also prefer words without double letters as it has the best chance of dismissing other letters.
Then it will scan the letters again and so on until it finds the answer, at which point it'll restart the game automatically and continue and can therefore be left to run indefinitely.
If a word is not valid, it will delete it and try the next best word.

Hold the letter 'Q' down to quit the bot.

Be warned - the bot will assume you have your screen set up like this and clicks positions on the screen, so make sure you have it all set up before you go!

I'm sure there are a ton of ways to optimise this, I wanted to just do it as a fun little project using pyautogui.

Please install these before you start by using 'pip' -
pyautogui
opencv-python
keyboard
