# 10:31  10:36

def say_hello(name):
    print('Hello, ', name, '!', sep='')

def insert_separator(s="=", num=30):
    print(s * num)

def recite_poem():
    print("How about a Monty Python poem?")
    insert_separator("-", 5)
    print("Much to his Mum and Dad's dismay")
    print("Horace ate himself one day.")
    print("He didn't stop to say his grace,")
    print("He just sat down and ate his face.")

def say_goodbye(name):
    print('Goodbye, ', name, '!', sep='')

def main():
    your_name = input('What is your name? ')
    insert_separator("-", 15)
    say_hello(your_name)
    # Uses default value and num
    insert_separator()
    recite_poem()
    insert_separator()
    say_goodbye(your_name)

main()
