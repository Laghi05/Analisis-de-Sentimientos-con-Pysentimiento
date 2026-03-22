import pandas as pd
import Utils

def limpiar_datos(df):
  
    # Filtro de variables
    columnas_clave = [
    'Document ID', 'Date', 'Time', 'URL', 'Author Name', 'Author Handle',
    'Hit Sentence', 'Hashtags', 'Keyphrases',
    'Reach', 'Engagement', 'Likes', 'Replies', 'Reposts', 'Views'
    ]

    df_filtered = df[columnas_clave].copy()

    # Eliminación de duplicados
    columnas_para_comparar = [col for col in df_filtered.columns if col != 'Document ID']
    df_filtered = df_filtered.drop_duplicates(subset=columnas_para_comparar, keep='first')

    # Tratamiento de valores faltantes

    # Imputación
    metricas_sociales = ['Reach', 'Engagement', 'Likes', 'Replies', 'Reposts', 'Views']

    for col in metricas_sociales:
        df_filtered[col] = pd.to_numeric(df_filtered[col], errors='coerce').fillna(0)
    
    df_filtered['Hashtags'] = df_filtered['Hashtags'].fillna('Sin_Hashtag')
    df_filtered['Keyphrases'] = df_filtered['Keyphrases'].fillna('Ninguna')
    df_filtered['Hit Sentence'] = df_filtered['Hit Sentence'].fillna('')
    
    # Eliminación
    df_filtered = df_filtered.dropna(subset=['Author Handle'])

    # Corrección formato de fecha
    df_filtered['Date'] = pd.to_datetime(df_filtered['Date'], errors='coerce')

    # Limpieza de texto
    df_filtered['Cleaned_Text'] = df_filtered['Hit Sentence'].apply(Utils.procesar_texto_nlp)

    # Eliminación de comentarios de ciertos usuarios específicos
    invalid_users = ['@Banreservas', '@banreservasrd', '@BanreservasRD', '@segurosreservas']

    df_filtered = df_filtered[
        (~df['Author Handle'].isin(invalid_users))
    ]

    # Eliminación de comentarios en blanco
    df_cleaned = df_filtered[df_filtered['Cleaned_Text'] != '']
    
    return df_cleaned