# 3:01 3:17


def main():

	# english = int(input("English grade: "))
	# math = int(input("Math grade: "))
	# global_studies = int(input("Global Studies grade: "))
	# art = int(input("Art grade: "))
	# music = int(input("Music grade: "))
	# grades = {'English':english, 'Math':math, 'Global Studies':global_studies, 'Art':art, 'Music':music}

	grades = {}

	grades['English'] = int(input("English grade: "))
	grades['Math'] = int(input("Math grade: "))
	grades['Global Studies']= int(input("Global Studies grade: "))
	grades['Art'] = int(input("Art grade: "))
	grades['Music'] = int(input("Music grade: "))


	# Determines the average grade and prints it out. Note, to do this you will need to convert the user input to integers.
	average = (sum(grades.values()))/len(grades)
	print("Your average is", average)

	#After printing the average, ask the user to change the grade in one subject and then get the new average and print it out. Hint: you will have to prompt the user twice, once for the subject and once for the grade.
	change_subject = input("What subject do you want to change? ")
	change_grade = int(input("New grade: "))
	grades[change_subject] = change_grade
	average = (sum(grades.values()))/len(grades)
	print("Your average is", average)


main()