from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - ano
    if idade >= 18:
        totalmaior +=1
    else:
        totalmenor +=1
print("Tiivemos {} pessoas maiores de idade e {} menores de idade".format(totalmaior, totalmenor))
