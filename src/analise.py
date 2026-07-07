import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('base_consolidada_sefaz.csv')

df['Valor'] = df['Valor'].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)

agrupado = df.groupby('Conta')['Valor'].sum().sort_values(ascending=False).head(10)

print("\n--- Top 10 Contas com maiores despesas ---")
print(agrupado)

plt.figure(figsize=(12, 6))
sns.barplot(x=agrupado.values, y=agrupado.index, palette='viridis')
plt.title('Top 10 Contas com Maiores Despesas')
plt.xlabel('Valor Total')
plt.ylabel('Conta')
plt.tight_layout()

plt.savefig('grafico_despesas.png')
print("\nGráfico 'grafico_despesas.png' salvo com sucesso!")
plt.show()