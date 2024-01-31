def generar_informacion(df_filtrado):
    # Lógica para generar la información del objeto con etiqueta y posición
    resultJSON = df_filtrado.to_json(orient="records")
    return resultJSON
