import random

def menu():
    checkMenu = 1
    while checkMenu == 1:
        print("----MENU----\n(1) Bogosort\n(2) Merge sort\n(3) Bubble sort\n(4) Quit program")
        choice = int(input())
        if choice < 1 or choice > 4:
            print("Invalid choice, please enter a number from 1 to 4.\n")
            return menu()
        elif choice == 4:
            print("Stopping program")
            checkMenu = 0
        else:
            userList = getList()
            if choice == 1:
                sortedList = bogosort(userList)
            elif choice == 2:
                sortedList = mergeSort(userList)
            elif choice == 3:
                sortedList = bubblesort(userList)
            print(f"Sorted list: {sortedList}")


def getList():
    userList = []
    check = 0
    while check == 0:
        print("How many items are in the list?")
        itemCount = int(input())
        if itemCount > 0:
            check = 1
        else:
            print("Please enter a valid number for the items in the list (i.e greater than 0)")
    for count in range(itemCount):
        print(f"Please enter item number {count+1} of the list")
        item = float(input())
        userList.append(item)
    return userList

def checkSorted(userList):
    if len(userList) == 1:
        return True
    else:
        checkOrder = 1
        for count in range(len(userList)-1):
            if userList[count+1] < userList[count]:
                checkOrder = 0
    if checkOrder == 0:
        return False
    else:
        return True


def bogosort(userList):
    sortedList = userList
    while checkSorted(sortedList) == False:
        random.shuffle(sortedList)
    return sortedList


def merge(left,right):
    result = []
    countLeft = 0
    countRight = 0
    while countLeft < len(left) and countRight < len(right):
        if left[countLeft] <= right[countRight]:
            result.append(left[countLeft])
            countLeft += 1
        else:
            result.append(right[countRight])
            countRight += 1
    result.extend(left[countLeft:])
    result.extend(right[countRight:])
    return result

def mergeSort(userList):
    if len(userList) <= 1:
        return userList
    mid = len(userList)//2
    left = mergeSort(userList[:mid])
    right = mergeSort(userList[mid:])
    userList = merge(left, right)
    return userList


def bubblesort(userList):
    while checkSorted(userList) == False:
        for count in range(len(userList)-1):
            if userList[count] > userList[count+1]:
                movingItem = userList[count]
                userList[count] = userList[count+1]
                userList[count+1] = movingItem
    return userList


menu()