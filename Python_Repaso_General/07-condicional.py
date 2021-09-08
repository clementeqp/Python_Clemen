
# IF
def evaluarAlumno(nota):
    
    if nota >=5:
        valoracion="aprobado"
    else:
        valoracion="Suspenso"
    
    return valoracion

print("El alumno esta: " + evaluarAlumno(6))

# IF Elif ELse

def notaAlumno(nota):
    valoracion="suspenso"
    if nota<0 or nota >10:
        valoracion="Nota no valida"
    elif nota > 8:
        valoracion="Sobresaliente"
    elif 6<nota<=8:
        valoracion="Notable"
    elif nota>5 and nota <=6:
        valoracion="Aprobado"
    else:
        valoracion="No Aprobado"
        
    return valoracion
        
notaAlm=int(input("Introduce la nota: "))
print(notaAlumno(notaAlm))
        