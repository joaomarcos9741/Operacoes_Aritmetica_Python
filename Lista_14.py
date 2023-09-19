
print("Opições\n")
print("[+] Soma\n")
print("[-] Subtração\n")
print("[*] Multiplicão\n")
print("[/] Divisão\n")


flag = False
Num1 = int(input("Informe um valor\n"))
Num2 = int(input("Informe outro valor\n"))
while(not flag):
    operando = input("Informe uma operação\n")
    flag = True
    if operando == "+":
        print(f"Resultado da soma {Num1 + Num2}")
    elif operando == "-":
        print(f"Resultado da subtração {Num1 - Num2}")
    elif operando == "*":
        print(f"Resultado da multiplicão {Num1 * Num2}")
    elif operando == "/":
        print(f"Resultado da divisao{Num1 / Num2}")
    else:
        flag = False
