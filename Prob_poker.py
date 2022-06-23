import random
lista1 = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
lista2 = ("Corazones","Diamantes","Trebol","Picas")
#Probabilidad de sacar 3 ASES
baraja = list()
repeticiones = 4000000
mano = list()
cont = 0
AS3 = 0
for k in range(repeticiones):
  for i in lista1:
    for j in lista2:
      baraja.append(i+'-'+j)
  for _ in range(5):
    rango = len(baraja)-1
    num = random.randint(0,rango)
    valor = baraja[num]
    baraja.pop(num)

    mano.append(valor)
  for i in mano:
    if(i.split('-')[0]=='A'):
      cont = cont + 1
    if(cont==3):
      AS3 = AS3 + 1
      cont=0
  baraja.clear()
  mano.clear()
  cont=0 
AS3/repeticiones 
print("Hola usuario")
