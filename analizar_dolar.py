import sqlite3

# 1. Apertura de la base de datos
conexion = sqlite3.connect("dolar.db")
cursor = conexion.cursor()

# 2. Métrica 1: Promedio histórico (lo que ya tenías escrito)
cursor.execute("SELECT AVG(brecha) FROM historial")
promedio = cursor.fetchone()[0]
print("Promedio de la brecha Blue vs Oficial:", promedio)

# 3. Métrica 2: Cantidad total de mediciones
cursor.execute("SELECT COUNT(*) FROM historial")
cantidad = cursor.fetchone()[0]
print("Cantidad total de mediciones guardadas:", cantidad)

# 4. Métrica 3: Valor máximo registrado
cursor.execute("SELECT MAX(brecha) FROM historial")
maximo = cursor.fetchone()[0]
print("Brecha máxima registrada:", maximo)

# 5. Cierre seguro de la base de datos
conexion.close()