#match case
i=int(input("Enter a number between 1 and 5: "))
match i:
    case 1:
        print("You entered One")
    case 2:
        print("You entered Two")
    case 3:
        print("You entered Three")
    case 4:
        print("You entered Four")
    case 5:
        print("You entered Five")
    case _ if i<10:
        print("Number out of range and less than 10")
    case _ if i<20:
        print("Number out of range and less than 20")