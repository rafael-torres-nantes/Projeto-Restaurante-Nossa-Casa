import pandas as pd

def planilha_generator():
    
    # Ler o arquivo CSV exportado
    dataframe = pd.read_csv('data.csv')

    # Selecione, por uma expressão regular, as colunas que não começam com "Unnamed".
    # Crio uma nova coluna 'TOTAL' para receber a multiplicação do VALOR * UNIDADE
    dataframe = dataframe.filter(regex='^(?!Unnamed)').copy()
    dataframe['TOTAL'] = (dataframe['VALOR_GASTO'] *  dataframe['UNIDADES'])

    print(dataframe)
    return dataframe

def planilha_cleaner(dataframe):
    
    # Transformo as linhas da Planilha em NULOS, exceto os Index
    # Após isso, removo as linhas que contêm valores vazios
    dataframe[:] = None
    dataframe = dataframe.dropna()

    return 0

def replace_comman_to_dot(dataframe):
    # Selecionar apenas as colunas numéricas
    numeric_cols = dataframe.select_dtypes(include='number').columns

    # Substituir vírgulas por pontos em todas as colunas numéricas
    dataframe[numeric_cols] = dataframe[numeric_cols].replace(',', '.', regex=True)
    return dataframe

def planilha_save(dataframe, output_name):
    # Salvar a planilha com as alterações
    dataframe.to_csv(f'{output_name}.csv', index=False)

plan = planilha_generator()
planilha_cleaner(plan)
planilha_save(plan, "output")