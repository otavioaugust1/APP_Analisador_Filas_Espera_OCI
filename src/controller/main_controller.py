from src.models.oci_model import OCIModel
from src.views.main_view import MainView


class MainController:
    def __init__(self):
        self.model = OCIModel()
        self.view = MainView(self)

    def run(self):
        self.view.run()

    def analisar_csv(self, caminho_arquivo):
        return self.model.analisar_csv(caminho_arquivo)

    def salvar_relatorio(
        self, relatorio, caminho_saida_csv, caminho_saida_pdf
    ):
        self.model.salvar_relatorio(
            relatorio, caminho_saida_csv, caminho_saida_pdf
        )
