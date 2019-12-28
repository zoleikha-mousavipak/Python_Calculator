import re

print("My Magic Calculator")
print("For Exit type 'quit'")

run = True
previous = 0


def zcalculator():
    global previous
    global run
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("Goodbye")
        run = False
    else:
        equation = re.sub('[a-aZ-Z,.:()" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)


while run:
    zcalculator()


