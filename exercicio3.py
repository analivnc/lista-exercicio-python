#. Faça um Programa que pergunte em que turno você estuda. Peça para digitar
#M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
#"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


turno = input("Que turno você estuda? Digite N para Noturno, M para Matutino e V para vespertino ")

manha = 'M'
vespertino = "V"
noturno = 'N'

if turno == 'M':
    print("Bom diiiaaaa!!!")
elif turno == 'V':
    print("Boa Tardeeee!!!")
elif turno == 'N':
    print("Boa Noiteeee!!!")
else: 
    print("Inválido")
