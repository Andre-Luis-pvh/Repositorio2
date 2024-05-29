nota_joao = float(input('qual nota: '))
media = 7
if nota_joao >= media:
    print('aprovado')
else:
    print('reprovado')

s1 = 'programação em python'
print(s1[0:2])

senha = ""
while senha != "senha123":
    senha = input("Digite a senha: ")
print("Senha correta!")

a = 0
while a < 5:
    b = 1
    while b <= 10:
        resultado = a * 10 + b
        print(resultado)
        b += 1
    a += 1

for a in range(5):
    for b in range(1, 11):
        resultado = a * 10 + b
        print(resultado)

x = 1
while x <= 5:
    print(x)
    x += 1
    
print('git/hub e linux')

    
x = 1
while 