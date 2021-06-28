def calculoIRPF(renta):
    irpf=0
    if renta<=0:
        irpf=0
    elif renta<12000:
        irpf=7
    elif renta<18000:
        irpf=15
    elif renta<35000:
        irpf=21
    elif renta<70000:
        irpf=35
    else:
        irpf=45
        
    print("A la renta %.2f € le corresponde un %d" %(renta, irpf) + " % " +  "de tipo impositivo" )
    
    print(f"A la renta {renta} € le corresponde un {irpf} % de tipo impositivo")
    
    print("A la renta ", renta, "Le corresponde un ", irpf, "% de tipo impositivo")


renta=float(input("Introduzca su renta: "))
calculoIRPF(renta)