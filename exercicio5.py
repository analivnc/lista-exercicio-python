"""Faça um Programa que leia um número e exiba o dia correspondente da
semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer
valor inválido.
"""

print("1-Domingo")
print("2-Segunda")
print("3-Terça")
print("4-Quarta")
print("5-Quinta")
print("6-Sexta")
print("7-Sábado")

diaDaSemana = int(input("Escolha um dos números para um dia da semana: "))

if diaDaSemana == 1:
    print("Domingo")
elif diaDaSemana == 2:
    print("Segunda")
elif diaDaSemana == 3:
    print("Terça")
elif diaDaSemana == 4:
    print("Quarta")
elif diaDaSemana == 5:
    print("Quinta")
elif diaDaSemana == 6:
    print("Sexta")
elif diaDaSemana == 7:
    print("Sábado")
else:
    print("Valor inválido")