# function that takes in a word and tests for letter e

def letter_box(word):
    for letters in word:
        if letters == "e" or letters == "E":
            print("word has letter e")
            break
        print(f"the word {word} has no letter 'e' in it")


letter_box("janury")


# corrected the printing problem - not else is under for
def letter_box(words):
    for letter in words:
        if letter == "e" or letter == "E":
            print(f"the word '{words}' has letter 'e'")
            break
    else:
        print(f"the word '{words}' has no letter 'e' in it")


letter_box("janury")  # the word 'janury' has no letter 'e' in it
letter_box("letter")  # the word 'letter' has letter 'e'


# better / simpler / cleaner way of witting
def letter_box(word):
    if "e" in word.lower():
        print(f"the word '{word}' has letter 'e'")
    else:
        print(f"the word '{word}' has no letter 'e' in it")


letter_box("mary")  # the word 'janury' has no letter 'e' in it
letter_box("joseph")  # the word 'letter' has letter 'e'
