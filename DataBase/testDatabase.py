from backend import BackEnd

back = BackEnd()
m = int(input("digite 1 "))
if m == 1:
    date = input("informe a data: ")
    number = int(input("informe o numero: "))
    CPF = input("informe o cpf: ")
    back.verifica(date,number,CPF)