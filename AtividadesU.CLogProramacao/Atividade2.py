velocidade = float(input("Velocidade (km/h): "))

if velocidade > 80:
    Multa = (velocidade - 80) * 5
    print("Você foi multado! ")
    print(f"Multa: R$ {Multa:.2f} ")
    
else:
    print("Você não foi multado!")