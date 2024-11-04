class Carro:
    nome= 'gol'
    ano = 10997
    qt = 10
    banco=Banco()
carro = Carro()
print(carro.nome,carro.ano,carro.qt)
carro.banco.couro+=10
class Banco:
    couro=5
    pano=0
    