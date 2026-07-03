import pandas as pd
import zipfile
from pathlib import Path

pasta_dados = Path('dados_compactos')

for arquivo_zip in pasta_dados.glob('**/*.zip'):
    print(f'Analisando arquivo: {arquivo_zip}')
    
    with zipfile.ZipFile(arquivo_zip, 'r') as z:
        for nome_arquivo in z.namelist():
            if nome_arquivo.endswith('.csv'):
                tabela = pd.read_csv(z.open(nome_arquivo), sep = ';', encoding= 'latin-1', skiprows= 3, on_bad_lines= 'skip')
                print(tabela.head())