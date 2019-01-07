# 11:14 12:00

_output = ''

def addheaders():
    #  The four headers should each take up 10 spaces, be aligned to the center, and be separated by tabs, like this:
    #'  Company  \t Revenue  \t Expenses \t  Profit  \n'
    global _output
    _output += ('{:^10} \t {:^10} \t {:^10} \t {:^10} \n'.format("Company", "Revenue", "Expenses", "Profit"))


def addrow():
    global _output
    company = str.title(input("Company: "))
    revenue = float(input("Revenue: "))
    expenses = float(input("Expenses: "))
    profit = revenue - expenses
    _output += ('{:10} \t ${:10,.2f} \t ${:10,.2f} \t ${:10,.2f} \n'.format(company, revenue, expenses, profit))

    #The rest of the function prompts the user to add another row
    # or quit. On quitting, it prints _output. Leave it as is.

    again = input("Again? Press ENTER to add a row or Q to quit. ")
    if again.lower() != 'q':
        addrow()
    else:
        print(_output)

def main():
    #call addheaders() and addrow()
    addheaders()
    addrow()

main()
