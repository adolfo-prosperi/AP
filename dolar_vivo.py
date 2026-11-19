import requests

url = "https://dolarapi.com/v1/dolares"
respuesta = requests.get(url)
datos = respuesta.json()

# 1. Creamos dos variables vacías en 0 antes de empezar a recorrer la lista
venta_oficial = 0
venta_blue = 0

for dolar in datos:
    print(
        dolar["nombre"], "-> Compra:", dolar["compra"], "| Venta:", dolar["venta"]
    )

    # 2. Dos 'if' separados porque en cada vuelta 'dolar' es una sola cotización
    if dolar["nombre"] == "Oficial":
        venta_oficial = dolar["venta"]

    if dolar["nombre"] == "Blue":
        venta_blue = dolar["venta"]

# 3. Afuera del ciclo 'for' (sin sangría), ya tenemos ambos precios guardados y restamos
brecha = venta_blue - venta_oficial
print("-----------------------------------------")
print("Brecha Blue vs Oficial: $", brecha)