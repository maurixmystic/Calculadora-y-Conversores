print('Programa para calcular digito verificador de rut');

print ('Introduce el octavo numero de un rut en especifico')
oct=input()
print ('Introduce el septimo numero de un rut en especifico')
sep=input()
print ('Introduce el sexto numero de un rut en especifico')
sex=input()
print ('Introduce el quinto numero de un rut en especifico')
qui=input()
print ('Introduce el cuarto numero de un rut en especifico')
cua=input()
print ('Introduce el tercer numero de un rut en especifico')
ter=input()
print ('Introduce el segundo numero de un rut en especifico')
seg=input()
print ('Introduce el primer numero de un rut en especifico')
pri=input()

oct= int(oct)
sep= int(sep)
sex= int(sex)
qui= int(qui)
cua= int(cua)
ter= int(ter)
seg= int(seg)
pri= int(pri)

(a)=(oct*2)+(sep*3)+(sex*4)+(qui*5)+(cua*6)+(ter*7)+(seg*2)+(pri*3)/11*11
(b)= (a)%11
(c)= 11-(b)

print('la suma de los números ingresados segun la formula es '+str(a)+' y el resto es '+str(b)+'  , Digito verificador es '+str(c))









