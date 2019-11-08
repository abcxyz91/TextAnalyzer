# This program reads a text file to find what percentage of each letter in that file:


def count_char(file, char):
    counter = 0
    for c in file:
        if c == char:
            counter = counter + 1
    return counter


def count_blank(file):
    counter_blank = 0
    for c in file:
        if c == " ":
            counter_blank = counter_blank + 1
    return counter_blank


while True:
    filename = input("\nWelcome to my text analyzer. \nPlease enter the file name or type quit to exit. Note: the file should be in same folder. \n")

    if filename == "quit":
        break
    else:
        try:
            with open(filename) as f:
                text = f.read().lower()

            print("\nAnalyze finished! \n")
            print("There are: " + str(len(text) - count_blank(text)) + " characters \n")

            for character in "abcdefghijklmnopqrstuvwxyz":
                percent = 100 * count_char(text, character) / (len(text) - count_blank(text))
                print("{0} - {1} - {2}%".format(character, str(count_char(text, character)) + " words", round(percent, 2)))
        except FileNotFoundError:
            print("No such file or directory. Please try again")
