bruto = float(input("Salario bruto: "))
porc = float(input("% impuestos: "))
ded = float(input("Deducciones: "))
neto = bruto - (bruto * (porc/100)) - ded
print(f"Salario neto: {neto}")
