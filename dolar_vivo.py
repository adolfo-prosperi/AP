import requests

url = "https://dolarapi.com/v1/dolares"
respuesta = requests.get(url)
datos = respuesta.json()

for dolar in datos:
    print(
        dolar["nombre"],
        "-> Compra:",
        dolar["compra"],
        "| Venta:",
        dolar["venta"],
    )