import csv

#### Editar um arquivo CSV####

# Caminho para o arquivo CSV
file_path = 'arquivo.csv'

# Ler o arquivo CSV
rows = []
with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)

# Modificar os dados (exemplo: alterar a idade de Carlos)
for row in rows:
    if row[0] == 'Carlos':
        row[1] = '25'

# Escrever de volta no arquivo CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)