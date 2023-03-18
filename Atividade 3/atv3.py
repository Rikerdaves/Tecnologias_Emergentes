import numpy as np
import pandas as pd

# Ler o arquivo csv
df = pd.read_csv('video_games_sales.csv')

# Criar um array NumPy a partir da coluna 'Global_Sales'
global_sales = np.array(df['Global_Sales'])

# Média de Vendas Globais
mean = np.mean(global_sales)
print(f'Média: U${mean}')

# Mediana das Vendas Globais
median = np.median(global_sales)
print(f'Mediana: U${median}')

# Valor mínimo das Vendas Globais
min_value = np.min(global_sales)
print(f'Valor mínimo: U${min_value}')

# Valor máximo das Vendas Globais
max_value = np.max(global_sales)
print(f'Valor máximo: U${max_value}')



