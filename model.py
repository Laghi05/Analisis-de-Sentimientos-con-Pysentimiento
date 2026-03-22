import pandas as pd
from pysentimiento import create_analyzer

def ejecutar_modelo(df_cleaned):
    # Creación del modelo
    analyzer = create_analyzer(task="sentiment", lang="es")

    batch_size = 500 # Tamaño de cada bloque de datos
    sentimientos = []

    # Aplicación del modelo por bloques
    for i in range(0, len(df_cleaned), batch_size):
        batch = df_cleaned["Cleaned_Text"].iloc[i:i+batch_size].tolist()
        
        resultados = analyzer.predict(batch)
        sentimientos.extend([r.output for r in resultados])
        
        print(f"Procesados: {i + batch_size}")

    # Anexión de etiquetas al conjunto de datos
    df_cleaned["sentimiento"] = sentimientos
    
    data_labeled = df_cleaned
    return data_labeled