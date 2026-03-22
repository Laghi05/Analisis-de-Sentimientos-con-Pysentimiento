import pandas as pd
import re

def procesar_texto_nlp(texto: str) -> str:
  if pd.isna(texto):
    return ""
  texto = str(texto).lower()
  texto = re.sub(r'http\S+|www\.\S+', '', texto)
  texto = re.sub(r'@\w+', '', texto)
  texto = re.sub(r'[^\w\s]', ' ', texto)
  texto = re.sub(r'\s+', ' ', texto).strip()
  return texto
