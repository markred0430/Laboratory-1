import random
Question = 'yes'
while Question == 'yes':
    print()
    List1 = list(range(1, 10000))
    random.shuffle(List1)
    list_2 = List1[:10]
    New_List = []
    for i in list_2:
        New_List.append(i)
    print('Array : ', New_List)
    print("Menu:")
    print(' 1 -> Add an element')
    print(' 2 -> Insert an element')
    print(' 3 -> Show the largest and smallest number in the array')
    print(' 4 -> Delete an element')
    print(' 5 -> Arrange in ascending order')
    print(' 6 -> Arrange in descending order')
    choice = str(input("What do you want to do? (1-6): \n"))
    while (choice != '1') and (choice != '2') and (choice != '3') and (choice != '4') and (choice != '5') and (
            choice != '6'):
        choice = str(input("What do you want to do? (1-6): \n"))
    if choice == '1':
        choice1 = int(input("Enter the number you want to add to list. : "))
        New_List.append(choice1)
        print("This is the new Array: ", New_List)
    elif choice == '2':
        choice1 = int(input("Enter the number you want to insert to list. : "))
        index = int(input("Enter the index of a number: "))
        New_List.insert(index, choice1)
        print("This is the new Array: ", New_List)
    elif choice == '3':
        print("The largest is", max(New_List), "and the smallest is", min(New_List))
    elif choice == '4':
        index = int(input("Enter the index of the element: "))
        New_List.remove(New_List[index])
        print("This is the new Array: ", New_List)
    elif choice == '5':
        New_List.sort()
        print("This is the new Array: ", New_List)
    elif choice == '6':
        New_List.sort()
        New_List.reverse()
        print("This is the new Array: ", New_List)
    Question = str(input("Do you want to do it again? (Yes or No)")).lower()
    if Question == 'no':
        break
