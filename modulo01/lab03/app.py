payRate = float(input('Pago por Hora: '))
hours = float(input('Horas trabajadas '))

overtimeHours = 0

if (hours > 40):
    overtimeHours = hours - 40
    totalPay = (40 * payRate) + (overtimeHours * (payRate * 2))
else:
    totalPay = hours * payRate

print(f'El sueldo a pagar es: ${totalPay}')