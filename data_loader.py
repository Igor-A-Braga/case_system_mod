import pandas as pd 
import os

class DataLoader:
    SUPORTED_EXTENSIONS = {'.csv', '.xls', '.xlsx', '.parquet'}

    def __init__(self,caminho_arquivo):

        if not isinstance(caminho_arquivo, str):
            raise TypeError('O Caminho do arquivo deve ser uma string')
        
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(f"O Arquivo '{caminho_arquivo}' não foi encontrado  ")
        

        self.caminho_arquivo = caminho_arquivo
        self.extensao = os.path.splitext(caminho_arquivo)[1].lower()

        if self.extensao not in self.SUPORTED_EXTENSIONS:
            raise ValueError(f"Extensão {self.extensao} não suportada ")


    
    def read_data(self):
        """Lê o arquivo e retorna um DataFrame do Pandas."""
        try:
            if self.extensao == '.csv':
                return pd.read_csv(self.caminho_arquivo)
            elif self.extensao in ['.xls', '.xlsx']:
                return pd.read_excel(self.caminho_arquivo,engine='openpyxl')
            elif self.extensao == '.parquet':
                return pd.read_parquet(self.caminho_arquivo)
        
        except Exception as e:
            raise IOError(f" Não foi possivel ler o arquivo deste caminho '{self.caminho_arquivo}'. Erro:{str(e)} ")
        