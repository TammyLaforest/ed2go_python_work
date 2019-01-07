

def main():
    get_phrase = input("Choose a phrase? ")
    print('Your phrase is "', get_phrase, '"', sep="")
    which_character = int(input("Which character would you like to see? [Enter number] "))
    # Challenge to correct numbering
    the_character = get_phrase[which_character - 1]
    print("Character number ", which_character, " is ", the_character)

main()
