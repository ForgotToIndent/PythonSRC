print("-------------------------------")
print("Chinese Calendar")
print("-------------------------------")

userYear = int(input("Enter the year to be converted: "))

yearConversion = userYear % 12

match yearConversion:
    case 0:
        print("Year of the Monkey")
    case 1:
        print("Year of the Rooster")
    case 2:
        print("Year of the Dog")
    case 3:
        print("Year of the Pig")
    case 4:
        print("Year of the Rat")
    case 5:
        print("Year of the Ox")
    case 6:
        print("Year of the Tiger")
    case 7:
        print("Year of the Rabbit")
    case 8:
        print("Year of the Dragon")
    case 9:
        print("Year of the Snake")
    case 10:
        print("Year of the Horse")
    case 11:
        print("Year of the Sheep")
    case _:
        print("ERROR, Retry")
