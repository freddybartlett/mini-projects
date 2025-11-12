#iterative approach for counting
def countingi(targetNum):
    for count in range(1,targetNum+1):
        print(count)

#recursive approach for counting
def countingr(targetNum):
    count = targetNum
    if count == 0:
        return
    countingr(count-1)
    print(count)


#iterative approach to finding a factorial of a given number
def factoriali(n):
    result = 1
    for count in range(1, n+1):
        result = result * count
    return result

#recursive approach to finding a factorial of a given number
def factorialr(n):
    if n == 1:
        return 1
    else:
        return n * factorialr(n-1)


#iterative approach to finding digits in a number
def finddigitsi(n):
    count = 0
    for digit in str(n):
        count += 1
    return count

#recursive approach to finding digits in a number
def finddigitsr(n):
    if n < 10:
        return 1
    else:
        return 1 + finddigitsr(n // 10)


#iterative approach to finding a sum of a list of numbers
def sumlisti(inputList):
    sum = 0
    for item in inputList:
        sum += item
    return sum

#recursive approach to finding a sum of list of numbers
def sumlistr(inputList):
    if len(inputList) == 0:
        return 0
    else:
        return inputList[0] + sumlistr(inputList[1:])


#iterative approach to reversing a string
def reversestringi(inputString):
    reversedString = ''
    count = len(inputString)
    while count != 0:
        count += -1
        reversedString += inputString[count]
    return reversedString

#recursive approach to reversing a string
def reversestringr(inputString):
    if len(inputString) <= 1:
        return inputString
    else:
        return reversestringr(inputString[1:]) + inputString[0]


#recursive approach to a binary search algorithm
def binarysearchr(inputList,targetChar):
    if len(inputList) == 0:
        return False
    mid = len(inputList) // 2
    if inputList[mid] == targetChar:
        return True
    else:
        left = inputList[:mid]
        right = inputList[mid+1:]
        if targetChar > inputList[mid]:
            return binarysearchr(right,targetChar)
        else:
            return binarysearchr(left,targetChar)


#recursive approach to quicksort
def getPivot(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        num1 = arr[len(arr)-1]
        num2 = arr[len(arr)//2]
        num3 = arr[0]
        if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
            return num2
        elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
            return num1
        else:
            return num3

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot  = getPivot(arr)
        left = []
        right = []
        for item in arr:
            if item < pivot:
                left.append(item)
            elif item > pivot:
                right.append(item)
        return qsort(left) + [pivot] + qsort(right)

