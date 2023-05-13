import pandas as pd

def planilha_generator():
    
    # Ler o arquivo CSV exportado
    dataframe = pd.read_csv('data.csv')

    # Vejo se o exitem os ocorrências de "," para subtsituir "." nas colunas do DataFrame
    try:
            # Substitui-se todas as ocorrências de "," por "." nas colunas do DataFrame
            dataframe['VALOR_GASTO'] = dataframe['VALOR_GASTO'].str.replace(",", ".").astype(float)
            dataframe['UNIDADES'] =  dataframe['UNIDADES'].str.replace(",", ".").astype(float)

            # Substitui-se todas as ocorrências de "," por "." nas colunas do DataFrame
            dataframe['GASTOS_FIXOS'] = dataframe['GASTOS_FIXOS'].str.replace(",", ".").astype(float)
            dataframe['GASTOS_EXTRAS'] =  dataframe['GASTOS_EXTRAS'].str.replace(",", ".").astype(float)
            
            # Substitui-se todas as ocorrências de "," por "." nas colunas do DataFrame
            dataframe['JUROS'] =  dataframe['JUROS'].str.replace(",", ".").astype(float)
    except:
        False

    # Selecione, por uma expressão regular, as colunas que não começam com "Unnamed".
    # Crio uma nova coluna 'TOTAL' para receber a multiplicação do VALOR * UNIDADE
    dataframe = dataframe.filter(regex='^(?!Unnamed)').copy()
    dataframe['TOTAL'] = (dataframe['VALOR_GASTO'] *  dataframe['UNIDADES'])

    return dataframe