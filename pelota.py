print("///Caer///Pelota////")
# Input
h=int(input("Ingresa la haltura de donde vaz a lanzar la pelota: " ))
f=h /5
r=0

while (h>f):
    h=h-(h*0.1)
    r=r+1
print("La 5 parte la da en el rebote: ",r)   