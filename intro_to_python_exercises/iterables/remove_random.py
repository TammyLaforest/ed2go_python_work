# 12:51 1:02
import random

def remove_random(l):
    removed = random.choice(l)
    l.remove(removed)
    return removed

def main():
    colors = ['red','blue','green','orange']
    removed = remove_random(colors)

    print("The removed color was",  removed)
    print("The remaining colors are",  colors)

main()
