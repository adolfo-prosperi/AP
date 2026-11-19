from datetime import datetime
import sqlite3
import requests

# 1. Traemos los datos de la API y calculamos la brecha (igual que en dolar_vivo.py)
url = "https://dolarapi.com/v1/dolares"
respuesta = requests.get(url)
datos = respuesta.json()

venta_oficial = 0
venta_blue = 0

for dolar in datos:
    if dolar["nombre"] == "Oficial":
        venta_oficial = dolar["venta"]
    if dolar["nombre"] == "Blue":
        venta_blue = dolar["venta"]

brecha = venta_blue - venta_oficial
fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2. Nos conectamos a la base de datos SQLite y creamos la tabla
conexion = sqlite3.connect("dolar.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS historial (
        fecha TEXT,
        oficial REAL,
        blue REAL,
        brecha REAL
    )
""")

# 3. Insertamos la fila nueva con los 4 datos y guardamos en disco
cursor.execute(
    "INSERT INTO historial VALUES (?, ?, ?, ?)",
    (fecha_hoy, venta_oficial, venta_blue, brecha),
)
conexion.commit()

# 4. Leemos todo el historial acumulado y cerramos la conexión
cursor.execute("SELECT * FROM historial")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.close()