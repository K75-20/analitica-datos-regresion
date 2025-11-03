import os
import pandas as pd

# Mostrar la carpeta actual (opcional)
print("Carpeta actual:", os.getcwd())

# 1. Leer el archivo Excel
ruta = r"C:\Users\julia\OneDrive - Fundacion Universitaria del Area Andina\1. Documentos Universidad\7. Septimo Semestre\ANALITICA DE DATOS\datos.xlsx"

# Cargar el archivo Excel
df = pd.read_excel(ruta)
df["Fecha"] = pd.to_datetime(df["Fecha"])


#2. Convertir la fecha a formato numérico
# (si tienes una columna llamada 'Fecha (dd/mm/aaaa)')
df['Fecha_num'] = pd.to_datetime(df['Fecha'])
df['Fecha_num'] = (df['Fecha_num'] - df['Fecha_num'].min()).dt.days

#3. Seleccionar las columnas de interés
# Cambia los nombres de columnas según tu Excel si es necesario
datos_utilizado = df['Fecha_num'].values
factura_mensual = df['Tasa de cambio representativa del mercado (TRM)'].values

#4. Calcular medias
media_X = datos_utilizado.mean()
media_Y = factura_mensual.mean()

#5. Calcular pendiente (m)
num = sum((x - media_X) * (y - media_Y) for x, y in zip(datos_utilizado, factura_mensual))
denom = sum((x - media_X) ** 2 for x in datos_utilizado)
pendiente = num / denom

#6. Calcular intercepto (b)
intercepto = media_Y - pendiente * media_X

#7. Calcular coeficiente de correlación (r)
num_corr = sum((x - media_X) * (y - media_Y) for x, y in zip(datos_utilizado, factura_mensual))
denom_X = sum((x - media_X) ** 2 for x in datos_utilizado)
denom_Y = sum((y - media_Y) ** 2 for y in factura_mensual)
coef_corr = num_corr / ((denom_X ** 0.5) * (denom_Y ** 0.5))

#8. Mostrar resultados
print(f"Pendiente (m): {pendiente}")
print(f"Intercepto (b): {intercepto}")
print(f"Coeficiente de correlación (r): {coef_corr}")
