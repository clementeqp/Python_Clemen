# Set: Conjuntos. No ordenado, no repeticion,

sistema_solar="Mercurio Tierra Venus Tierra Marte Jupiter Saturno Urano Neptuno Pluton"

planetas = set()

for p in sistema_solar.split(" "):
    planetas.add(p)
    
print(planetas)
print(len(planetas))


# otra forma
planetas2 = set(sistema_solar.split(" "))
print(planetas2)

print("-------------------------------------------------")
# queue, Colas

import queue
print("FIFO")
# Tipo FIFO first in first out
micola=queue.Queue(3) # 3 limitamos num elementos

micola.put("Lunes")
micola.put("Martes")
micola.put("Miercoles")

print(micola.get())
print(micola.get())

for e in micola.queue:
    print(e)
print("-----------------------------")
# Tipo LIFO
print("LIFO")
micola2=queue.LifoQueue()

micola2.put("Lunes")
micola2.put("Martes")
micola2.put("Miercoles")




for e in micola2.queue:
    print(e)
print("-----------------------------")

    # Tipo Priority
    
print("Priority")
miCola3=queue.PriorityQueue()

miCola3.put((3,"Lunes"))
miCola3.put((2,"Martes"))
miCola3.put((1,"Miercoles"))

#print(micola.get())
#print(micola.get())
#print("-----------------------------")
for e in miCola3.queue:
    print(e)