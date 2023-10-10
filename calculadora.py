num1=int(input("Ingresa tu primer número:"))
num2=int(input("Ingresa tu segundo número:"))
operator=input("Operación que deseas realizar en formato de texto:")

if operator.lower() == "suma":
    a=num1 + num2
    print(a)
elif operator.lower() ==  "resta":
    b=num1 - num2
    print(b)
elif operator.lower() == "division":
    if num2!=0:
        c= num1/num2
        print(c)
    else:
        print("tu divisor no puede ser cero")
elif operator.lower() == "multiplicacion":
    d = num1*num2
    print(d)
elif operator.lower()== "potenciacion":
    print(num1**num2)
elif operator.lower() == "raiz":
    if num1>=0:
        raiz = num1**(1/num2)
    else:
        print("Parametros incorrectos")
else:
    print("Datos incorrectos o incompletos")