# 🧩 Desafio Técnico — Estágio em Análise de Dados | Sefaz Maceió

Este projeto tem como objetivo realizar a extração, tratamento e análise de despesas públicas, automatizando o processamento de arquivos compactados fornecidos pela Sefaz.
Como rodar o projeto

O fluxo foi dividido em dois scripts para garantir eficiência e organização:

Organização dos Dados:
    Execute o script de processamento para descompactar os arquivos, limpar inconsistências e gerar uma base consolidada:
    
    Bash
    python src/organizar_dados.py

Isso gerará o arquivo base_consolidada_sefaz.csv.

Análise e Visualização:

Após consolidar a base, execute o script de análise para gerar os relatórios e o gráfico principal:
    
    Bash

    python src/analise.py

Principais características

> Pipeline de ETL: Automação total desde a extração dos .zip até a unificação dos dados.
>
> Tratamento de Dados: Limpeza de metadados, ajuste de codificação (latin-1) e conversão de valores monetários para formato numérico.
>
>Resiliência: Tratamento de exceções para garantir que arquivos mal formatados não interrompam o processamento.

Projeto desenvolvido para o desafio técnico de Análise de Dados.
