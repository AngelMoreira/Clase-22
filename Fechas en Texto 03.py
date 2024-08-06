meses = {
    "Enero": 1,
    "Febrero": 2,
    "Marzo": 3,
    "Abril": 4,
    "Mayo": 5,
    "Junio": 6,
    "Julio": 7,
    "Agosto": 8,
    "Septiembre": 9,
    "Octubre": 10,
    "Noviembre": 11,
    "Diciembre": 12
}

def convertir_fecha(fecha_str):
    partes = fecha_str.split()
    
    dia = partes[0].replace(",", "")
    mes_nombre = partes[1]
    año = partes[2]
    
    mes = meses[mes_nombre]
    
    return f"{dia} {mes} {año}"

fecha_str = input("Introduce la fecha en formato '15, Febrero 1989': ")
fecha_nueva = convertir_fecha(fecha_str)

print("La fecha en formato numérico es:", fecha_nueva)
