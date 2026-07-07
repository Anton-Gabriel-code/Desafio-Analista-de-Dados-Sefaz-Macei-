import pandas as pd
import zipfile
from pathlib import Path

pasta_dados = Path('dados_compactos')
lista_de_tabelas = []

print("--- Iniciando processamento ---")

for arquivo_zip in pasta_dados.glob('**/*.zip'):
    with zipfile.ZipFile(arquivo_zip, 'r') as z:
        for nome_arquivo in z.namelist():
            if nome_arquivo.endswith('.csv'):
                try:
                    df = pd.read_csv(
                        z.open(nome_arquivo), 
                        sep=';', 
                        encoding='latin-1', 
                        on_bad_lines='skip', 
                        skiprows=3 
                    )
                    
                    df['ano_referencia'] = arquivo_zip.parent.name
                    lista_de_tabelas.append(df)
                except Exception as e:
                    print(f"Erro ao ler {nome_arquivo}: {e}")

if lista_de_tabelas:
    tabela_final = pd.concat(lista_de_tabelas, ignore_index=True)
    tabela_final.dropna(how='all', inplace=True)
    
    tabela_final.to_csv('base_consolidada_sefaz.csv', index=False)
    
    print("\n--- SUCESSO! Base consolidada criada ---")
    print(f"Total de linhas: {tabela_final.shape[0]}")
    
    print("\n--- NOMES EXATOS DAS SUAS COLUNAS ---")
    print(tabela_final.columns.tolist())
    print("--------------------------------------")
else:
    print("Nenhum dado encontrado.")
    
