from datetime import datetime

def convertir_hora(hora24):
    horaobj = datetime.strptime(hora24, "%H:%M")
    hora12 = horaobj.strftime("%I:%M %p")
    return hora12.lstrip("0")

hora24 = input("Introduce la hora en formato de 24 horas (HH:MM): ")
hora12 = convertir_hora(hora24)

print("La hora en formato de 12 horas es:", hora12)
