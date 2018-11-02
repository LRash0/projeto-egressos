import time
import csv
from dataBaseConnect import ConnecyMyDataBase
from openpyxl import load_workbook

inicio = time.time()
print('Conectando com o banco de dados')
database = ConnecyMyDataBase()
database.set_connection(user, password, host, database=schema
print("Lendo o arquivo")
linha = 0
with open('pathfile', 'r', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter = '|')
    data = next(reader)
    for data in reader:
        t = ",".join(str("'" + str(x) + "'") for x in data)
        database.insert_table_escola(t,linha)
        linha += 1



