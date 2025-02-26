import os

#### Criar arquivo CSV ####
# Caminho para o arquivo CSV
file_path = 'arquivo.csv'

# Verificar se o arquivo CSV existe, se não existir cria o mesmo
if not os.path.exists(file_path):
    # Criar um arquivo vazio
    open(file_path, mode='w').close()
else:
    print('O arquivo já existe!')