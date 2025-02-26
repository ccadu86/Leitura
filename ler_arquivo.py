import csv

#### Ler arquivo CSV ####

# Caminho para o arquivo CSV
file_path = 'arquivo.csv'

# Abrir e ler o arquivo CSV
with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)




