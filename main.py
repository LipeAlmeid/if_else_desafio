'''

Criar um programa que dependendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em portugues. O usuário deverá 
fornecer a temperatura. 

Temperaturas - Cozimento
48C - Selada
54C - Ao ponto para mal 
60C - Ao ponto 
65C - Ao ponto para bem 
71C - Bem passada 

'''


carne1 = input('Digite a carne escolhida: ')
temperatura = int(input('Digite a temperatura em celsius: '))
cozimento = 'Crua'

if temperatura < 48 : 
    print('Precisa cozinhar mais')
if temperatura >= 48 and temperatura < 54:
    cozimento = 'Selada'
if temperatura >= 54 and temperatura < 60:
    cozimento = 'Ao ponto para mal'
if temperatura >= 60 and temperatura < 65:
    cozimento = 'Ao ponto'
if temperatura >= 65 and temperatura < 71: 
    cozimento = 'Ao ponto para bem'
if temperatura >= 71:
    cozimento = 'Bem passada'
else:
    print(f'O ponto da {carne1} é {cozimento}')


# Resolução 2 

tem_cel = int(input('Qual é a temperatura da carne? '))

if tem_cel < 48:
    print('Cozinhar por mais alguns minutos')
elif tem_cel in range(48, 53):
    print('Selada')
elif tem_cel in range(54, 59):
    print('Ao ponto para mal')
elif tem_cel in range(60, 64):
    print('Ao ponto')
elif tem_cel in range(65, 70):
    print('Ao ponto para bem')
else:
    print('Bem passada')