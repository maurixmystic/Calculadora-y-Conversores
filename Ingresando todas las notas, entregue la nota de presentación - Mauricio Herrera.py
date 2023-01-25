print ('Introduce la nota de laboratorio 1')
lab1=input()
print ('Introduce la nota de laboratorio 2')
lab2=input()
print ('Introduce la nota de laboratorio 3')
lab3=input()

lab1= float(lab1)
lab2= float(lab2)
lab3= float(lab3)

suma=lab1+lab2+lab3
promedio=suma/3

print('El promedio de las notas de laboratorio es : %.2f'%promedio)


print ('Introduce la nota de tareas 1')
tar1=input()
print ('Introduce la nota de tareas 2')
tar2=input()
print ('Introduce la nota de tareas 3')
tar3=input()

tar1= float(tar1)
tar2= float(tar2)
tar3= float(tar3)

suma=tar1+tar2+tar3
promedio=suma/3

print('El promedio de notas de las tareas es : %.2f'%promedio)


print ('Introduce la nota de solemne 1')
sol1=input()
print ('Introduce la nota de solemne 2')
sol2=input()


sol1= float(sol1)
sol2= float(sol2)


print('Calcular nota de presentacion');

suma=(lab1+lab2+lab3)/3*0.15+(tar1+tar2+tar3)/3*0.15+sol1*0.35+sol2*0.35
promedio=suma

print('La nota de presentacion es : %.2f'%promedio)
