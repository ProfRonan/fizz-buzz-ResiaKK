numero = int(input("Digite um numero inteiro:  "))

divisivel_por_3 = False
if ((numero % 3) == 0):
    divisivel_por_3 = True

divisivel_por_5 = False
if ((numero % 5) == 0):
    divisivel_por_5 = True

if (divisivel_por_3 & divisivel_por_5):
    print("FizzBuzz")

elif (divisivel_por_5):
    print("Buzz") 

elif (divisivel_por_3):
    print("Fizz")

else:
    print("%d"% numero)

