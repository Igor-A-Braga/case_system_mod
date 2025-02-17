import pandas as pd
import matplotlib.pyplot as plt
class DataAnalyzer:
    def __init__(self,df):
        if not isinstance(df,pd.DataFrame):
            raise TypeError(" objeto deve ser um DataFrame do Pandas.")


        self._df = df


    

    def estatisticas_basicas(self):
        """Retorna estatísticas descritivas básicas."""
        return self._df.describe()
    

    def contar_valores_unicos(self, coluna):
        """Conta valores únicos em uma coluna específica."""
        if coluna in self._df.columns:
            return self._df[coluna].nunique()
        else:
            raise ValueError(f"A coluna {coluna} não existe no DataFrame.")
        
    
    def visualizar_distribuicao(self, coluna):
        """Gera um gráfico de distribuição da variável escolhida."""
        if coluna in self._df.columns:
            self._df[coluna].hist()
            plt.title(f"Distribuição de {coluna}")
            plt.savefig("grafico.png")
            plt.show(block=True)  # <-- Força a janela a abrir e esperar
        else:
            raise ValueError(f"A coluna {coluna} não existe no DataFrame.")
