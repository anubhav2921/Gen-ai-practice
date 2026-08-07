#her we lear about condition and all


a = int(input("Enter your age"))
if a>=18:
 print("can vote")
else:
 print("not ellegible for voting") 

 #nested if else coditions

year = int(input("Enter year value = "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "--> is a leap year")
        else:
            print(year, "--> is not a leap year")
    else:
        print(year, "--> is a leap year")
else:
    print(year, "--> is not a leap year")