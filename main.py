def welcome():
    print("""
    Hello there!
    This program will pluralise words for you. 
    All you need to do is enter a word and I will give you the plural form.""")

def print_result(result):
    print(f"The plural form of that word is: {result}")

#------#

def pluralise():
    word = str(input("Enter the word here:  "))
    if (word=="fish") or (word=="sheep") or (word=="bison"):
        result = f"{word}"
    elif word.endswith("s") or word.endswith("ss") or word.endswith("sh") or word.endswith("ch") or word.endswith("x") or word.endswith("z"):
        result = f"{word}es"
    else:
        result = f"{word}s"
    
    print_result(result)

welcome()
pluralise()