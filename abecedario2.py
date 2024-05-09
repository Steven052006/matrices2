import os 
matriz1 =   [['🍆','🍆','🍆','🍆','🍆'],
            ['🍆','🍆','🍆','🍆','🍆'],
            ['🍆','🍆','🍆','🍆','🍆'],
            ['🍆','🍆','🍆','🍆','🍆'],
            ['🍆','🍆','🍆','🍆','🍆']]

correcto = '🌕'
incorrecto = '🌑'
ls_preguntas  = ['¿Que es python? \n\n1.juego  \n2.lenguaje de programacion \n3.marca de auto \n4. ninguna de las anteriores' ,
'¿Que es Html? \n\n1.Lenguaje de maquetacion  \n2.Marca de gaseosa \n3.Navegador \n4.Perro caliente']
ls_respuestas = ['2', '1']
def fnt_pintarmatriz():
    for i in  range (len(matriz1)):
        for j in range (len(matriz1[i])):
            print(matriz1[i][j], end='     ')
        print('\n \n')

sw= True 
contador = 0 

for i in  range (len(matriz1)):
        for j in range (len(matriz1[i])):
            import os       
            os.system('cls')
            fnt_pintarmatriz()
            print()
            print(ls_preguntas[contador])
            print()
            r= input ('- >')
            if r == ls_respuestas [contador]:
                matriz1[i][j] = correcto
            else:
                matriz1[i][j] = incorrecto
            contador += 1
            
            
    


