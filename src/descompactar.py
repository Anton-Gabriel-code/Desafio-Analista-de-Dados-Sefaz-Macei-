import pandas as pd
import zipfile
from pathlib import Path

pasta_dados = Path('dados_compactos')
lista_de_tabelas = []


print('Iniciando analise de dados...')

for arquivo_zip in pasta_dados.glob('**/*.zip'):
    print(f'Analisando arquivo: {arquivo_zip}')
    
    with zipfile.ZipFile(arquivo_zip, 'r') as z:
        for nome_arquivo in z.namelist():
            if nome_arquivo.endswith('.csv'):
                try:
                    df = pd.read_csv(z.open(nome_arquivo), sep= ';', encoding='latin-1', on_bad_lines='skip', skiprows=3)
                    df['ano_referencia'] = arquivo_zip.parent.name
                    lista_de_tabelas.append(df)
                
                except Exception as e:
                    print(f'Erro ao processar {nome_arquivo}: {e}')
                    
if lista_de_tabelas:
    tabela_final = pd.concat(lista_de_tabelas, ignore_index= True)
    
    tabela_final.dropna(how = 'all', inplace = True)
    
    tabela_final.to_csv('base_consolidada_sefaz.csv', index = False)
    
    print('\nProcessamento de dados concluído com sucesso!!!')
    print(f'Base consolidada contém {tabela_final.shape[0]} linhas e {tabela_final.shape[1]} colunas.')
else:
    print('Nenhum dado foi encontrado para consolidar.')