import pyfiglet

logo = pyfiglet.figlet_format("ZX-0B111", font="standard")
print(logo)

print("0. Soma")
print("1. Subtração")
print("2. Multiplicação")
print("3. Divisão")
opcoes = int(input("Opção: "))

def soma():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    adicao = x + y
    print("A soma é:",adicao)

def subtracao():
     x = int(input("Digite o primeiro número: "))
     y = int(input("Digite o segundo número: "))
     subtrair = x - y
     print("A subtração é:", subtrair)

def multiplicao():
      x = int(input("Digite o primeiro número: "))
      y = int(input("Digite o segundo número: "))
      multiplicar = x * y
      print("A multiplicação é:",multiplicar)

def divisao():
      x = int(input("Digite o primeiro número: "))
      y = int(input("Digite o segundo número: "))
     
      if x == 0 or y == 0:
           print("Não pode dividir por 0.")
      else:
            dividir = x / y
            print("A divisão é:",dividir)


if opcoes == 0:
     soma()

elif opcoes == 1:
     subtracao()

elif opcoes == 2:
     multiplicao()

elif opcoes == 3:
     divisao()