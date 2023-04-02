#Error handling
def sum(num1, num2):
    try:
        return num1/num2
    except(BaseException) as err:
        print(err)

sum(2, 0)

