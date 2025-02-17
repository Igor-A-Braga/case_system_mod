import pandas as pd
class DataTransformer:
    def __init__(self,df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError('O objeto deve ser um Dataframe do pandas')
        self._df = df

    

    def remover_duplicatas(self):
        """Remove linhas duplicadas do DataFrame."""
        self._df.drop_duplicates(inplace=True)

    
    def remover_nulos(self):
        """Remove linhas com valores nulos."""
        self._df.dropna(axis=0,inplace=True)
    
    def transformar_coluna_maiuscula(self,coluna):
        """Transforma os valores de uma coluna para maiúsculas."""
        if coluna in self._df.columns:
            self._df[coluna] = self._df[coluna].str.upper()
        else:
            raise ValueError(f"A coluna {coluna} não existe no DataFrame.")

    def get_dataframe(self):
        """Retorna o DataFrame transformado."""
        return self._df


