a=5
b=2

try:
    print("resource open")
    print(a/b)
    k=int(input("Enter a number"))
    print(k)

except Exception as e:

    print("You cannot div a number by zero",e)

finally:
    print("resource close")





