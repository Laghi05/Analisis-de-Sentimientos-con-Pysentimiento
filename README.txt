El proyecto se divide en las siguientes fases:

1. Limpieza
2. EDA
3. Implementación de modelo pysentimiento
4. Evaluación del modelo

La limpieza y el EDA se realizan automáticamente al ejecutar el script
app.py tomando el archivo Data_Banreservas_original.csv (en el directorio Data)
como punto de partida.
Al finalizar, se genera un archivo csv con los datos limpios y otro
con los datos limpios y etiquetados por el modelo. Ambos se guardan en el
directorio Data automáticamente.

Dentro del directorio Notebooks encontrará el EDA y la evaluación del
modelo, que se nutren de los archivos generados por el paso anterior.
La evaluación también usa un archivo llamado Sample que contiene una muestra
manualmente etiquetada de comentarios para su comparación con las etiquetas del modelo.