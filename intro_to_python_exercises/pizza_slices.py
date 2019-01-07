import math

def total_slices(people, slices_per_person):
    return people * slices_per_person

def num_whole_pizza(slices, slices_per_pie):
    return math.ceil(slices / slices_per_pie)

def rem_slices(whole_pizza, slices_per_pie, slices):
    return math.floor(whole_pizza * slices_per_pie - slices)

def main():
    people = int(input("How many people are eating? "))
    slices_per_person = float(input("How many slices per person? "))
    slices_per_pie =  int(input("How many slices per pie? "))

    slices= total_slices(people, slices_per_person)
    whole_pizza = num_whole_pizza(slices, slices_per_pie)
    remainder = rem_slices(whole_pizza, slices_per_pie, slices)


    print("You need ", whole_pizza, " pizzas to feed ", people, " people. ")
    print("There will be ", remainder, " leftover slices.")

main()
