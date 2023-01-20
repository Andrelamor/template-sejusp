import sys
import pandas as pd

def convert_csv():
  # referências: https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03
  # referências: https://colab.research.google.com/drive/1R6SHFugbCEuy5ppjDFymquj3jjbgY7Sx?authuser=1
  xlsx_file_path = "upload/Sistema Gerencial.xlsx"
  abas = ["aditivos", "relatorios", "repasses", "termo-parceria-contrato-gestao"]
  for aba in abas:
    read_file = pd.read_excel (xlsx_file_path, aba)
    read_file.to_csv (f'data/{aba}.csv', index = None, header=True, sep = ';', decimal = ',', encoding = 'utf-8-sig', na_rep = "")

if __name__ == '__main__':
  convert_csv()

# AttributeError: module 'sys' has no attribute 'arg'
