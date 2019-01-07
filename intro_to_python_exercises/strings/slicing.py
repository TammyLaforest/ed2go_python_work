# 10:16 10:23

def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is '", phrase, "'", sep="")
    start = int(input("Which character would you like to start with? "))
    ending = int(input("Which character would you like to end with? "))
    
    your_substring = phrase[start-1:ending]
    print("Your substring is '", your_substring, "'", sep="")

main()
