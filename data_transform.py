import pandas as pd

# Ruta del archivo CSV intermedio
archivo_csv = 'clientes.csv'

try:
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv)
    
    # Regla 1: Ordenar los datos por nombre
    data_ordenada = data.sort_values(by='CLIENTE')

    # Regla 2: Ordenar los datos por IDCLIENTE
    data_ordenada = data.sort_values(by='IDCLIENTE')
    
    # Regla 3: Ordenar los datos por departamento
    data_ordenada = data.sort_values(by='DEPARTAMENTO')
    
    # Exportar a Excel
    archivo_excel = 'clientes_ordenados.xlsx'
    data_ordenada.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")
