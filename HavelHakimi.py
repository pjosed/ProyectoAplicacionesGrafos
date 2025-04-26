def HavelHakimi(secuencia: list) -> bool:

    while secuencia:
        primero = secuencia[0]

        if(primero > len(secuencia)):
            print("No existe un  gráfico para esta secuencia de grados :(")
            return False
        
        else:
            print("Ordenado: ",secuencia)
            primero = secuencia.pop(0)
            for i in range (primero):
                secuencia[i]  -= 1
                if (secuencia[i] < 0):
                    print("Resultado falso: ",secuencia)
                    print("No existe un  gráfico para esta secuencia de grados :( ")
                    return False
                print ("Restar -1 y eliminar: ",secuencia)
            secuencia.sort(reverse = True)
            if (secuencia[0] == 0):
                print("Resultado final: ",secuencia)
                print("Si! existe un gráfico para esta secuencia de grados :D")
                return True
            
secuencia = [4, 4, 4, 4, 3, 3]
print(HavelHakimi(secuencia))
                

                
                  
            

            






