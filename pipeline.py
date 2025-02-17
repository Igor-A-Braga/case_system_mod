import pandas as pd
from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from data_transformer import DataTransformer

class DataPipeline():
    def __init__(self,caminho_arquivo):
        self.loader = DataLoader(caminho_arquivo)
        self.df = None
    

    def executar(self):
        """Executa todas as etapas do pipeline."""
        print("📥 Carregando dados...")
        self.df = self.loader.read_data()


        print("🛠 Aplicando transformações...")
        transformer = DataTransformer(self.df)
        transformer.remover_duplicatas()
        transformer.remover_nulos()
        self.df = transformer.get_dataframe()

        print("📊 Analisando dados...")
        analyzer = DataAnalyzer(self.df)
        print(analyzer.estatisticas_basicas())
        print(analyzer.visualizar_distribuicao('idade'))


        return self.df
    

if __name__ == "__main__":
    caminho = "/Users/igorantunesbraga/Documents/Estudo_p_pd/teste1.xlsx"
    pipeline = DataPipeline(caminho)
    df_processado = pipeline.executar()
