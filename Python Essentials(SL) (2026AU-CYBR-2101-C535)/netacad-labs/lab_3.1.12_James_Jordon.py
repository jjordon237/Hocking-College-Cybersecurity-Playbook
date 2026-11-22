year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    #  Write the if-elif-elif-else block here.
    if year % 4 == 0:
        if year % 100 != 0:
            print("Leap year")
        else:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Common year")
    else:
        print("Common year")