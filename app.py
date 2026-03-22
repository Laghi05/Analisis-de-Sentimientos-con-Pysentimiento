import pandas as pd
from cleaning import limpiar_datos
from model import ejecutar_modelo

def main():
    print("--- INICIANDO PIPELINE DE DATOS BANRESERVAS ---")
    
    # Carga de datos
    ruta_archivo = 'Data/Data_Banreservas_Original.csv'

    try:
        df = pd.read_csv(ruta_archivo, sep=',', encoding='utf-8')
    except:
        df = pd.read_csv(ruta_archivo, sep=';', encoding='utf-8')
    
    # Limpieza
    df_cleaned = limpiar_datos(df)
    
    # Implementación del modelo
    df_etiquetado = ejecutar_modelo(df_cleaned)
    
    # Exportación de datos procesados
    df_cleaned.to_csv("Data/Data_Banreservas_Cleaned.csv", index=False)
    df_etiquetado.to_csv("Data/Data_Banreservas_Labeled.csv", index=False)
    
    print("--- PROCESO FINALIZADO ---")

if __name__ == "__main__":
    main()