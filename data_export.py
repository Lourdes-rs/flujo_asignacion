import pandas as pd

# Ruta del archivo CSV ordenado
archivo_csv_ordenado = 'clientes_ordenados.csv'

try:
    # Leer el archivo CSV ordenado
    data_ordenada = pd.read_csv(archivo_csv_ordenado)
    
    # Exportar a Excel
    archivo_excel = 'clientes_ordenados.xlsx'
    data_ordenada.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al exportar los datos: {e}")