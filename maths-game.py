import random
import time

def menu():
   print("---MENU---\n1. Start program\n2. Quit program")
   try:
       choice = int(input())
   except ValueError:
       print("Please enter a valid number (1 or 2)\n")
       return menu()
   if choice < 1 or choice > 2:
       print("Please enter a valid number (1 or 2)\n")
       return menu()
   elif choice == 1:
       main()


def getValue(string):
    try:
        value = int(input(string))
    except ValueError:
        return getValue("Please enter a valid integer greater than 0: ")
    if value < 0:
        return getValue("Please enter a valid integer greater than 0: ")
    return value


def getRanges():
    lbas = getValue("Enter lower bound for addition/subtraction problems: ") # lbas is shorthand for lower bound addition subtraction and so on
    ubas = getValue("Enter upper bound for addition/subtraction problems: ")
    lbmd = getValue("Enter lower bound for multiplication/division problems: ")
    ubmd = getValue("Enter upper bound for multiplication/division problems: ")
    userTime = getValue("How long do you want to do problems for? (in seconds): ")
    return lbas, ubas, lbmd, ubmd, userTime


def createProblem(lbas,ubas,lbmd,ubmd):
    # randNum = random.randint(0,3)
    randNum = 3
    if randNum == 0 or randNum == 1:
        num1 = random.randint(lbas,ubas)
        num2 = random.randint(lbas,ubas)
        if randNum == 0:
            problem = f"{num1} + {num2}: "
            ans = num1+ num2
        else:
            problem = f"{num1} - {num2}: "
            ans = num1 - num2
    elif randNum == 2:
        num1 = random.randint(lbmd, ubmd)
        num2 = random.randint(lbmd, ubmd)
        if randNum == 2:
            problem = f"{num1} * {num2}: "
            ans = num1 * num2
    elif randNum == 3:
        checkint = 0
        while checkint == 0:
            num1 = random.randint(lbmd, ubmd)
            num2 = random.randint(lbmd, ubmd)
            if num2 > num1:
                num3 = num2
                num2 = num1
                num1 = num3
            ans = num1 / num2
            if ans % 1 == 0:
                ans = int(ans)
                checkint = 1
        problem = f"{num1} / {num2}: "
    return problem, ans


def main():
    lbas,ubas,lbmd,ubmd,userTime = getRanges()
    initialTime = time.time()
    score = 0
    count = 0
    while initialTime + userTime > time.time():
        problem,ans = createProblem(lbas,ubas,lbmd,ubmd)
        checkCorrect = 0
        while checkCorrect == 0:
            userAns = getValue(problem)
            if userAns == ans:
                checkCorrect = 1
                print("Correct answer!")
                score += 1
                count += 1
            else:
                print("Incorrect answer, try again")
                score += -1
    print(f"Times up! You got {count} questions right.\nConsidering incorrect answers (a correct answer is equal to 1 point and an incorrect answer is equal to -1 point), your overall score is {score}!")
    time.sleep(3)
    menu()


menu()