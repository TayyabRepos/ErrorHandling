#Error handling
while True:
    try:
        age = int(input("How old are you? "))
        print(age)
    except:
        print("Please enter a number")
    else:
        print("Thank you")
        break
