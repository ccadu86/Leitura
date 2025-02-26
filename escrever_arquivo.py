import csv

#### Escrever em um arquivo CSV ####

# Dados a serem escritos
data = [
    ['Nome', 'Idade', 'Cidade'],
    ['Carlos', '100', 'São Paulo'],
    ['Ana', '35', 'Rio de Janeiro'],
    ['Ana Fernanda', '10', 'Rio de Janeiro']
]

# Caminho para o arquivo CSV
file_path = 'arquivo.csv'

# Abrir e escrever no arquivo CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)