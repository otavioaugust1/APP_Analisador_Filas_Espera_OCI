import tkinter as tk
from tkinter import filedialog, messagebox


class MainView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title('Analisador de CSV - OCI')
        self.root.geometry('320x100')

        self.btn_selecionar = tk.Button(
            self.root,
            text='Selecionar Arquivo CSV',
            command=self.selecionar_arquivo,
        )
        self.btn_selecionar.pack(pady=20)

    def run(self):
        self.root.mainloop()

    def selecionar_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(
            filetypes=[('CSV files', '*.csv')]
        )
        if caminho_arquivo:
            relatorio = self.controller.analisar_csv(caminho_arquivo)
            caminho_saida_csv = filedialog.asksaveasfilename(
                defaultextension='.csv', filetypes=[('CSV files', '*.csv')]
            )
            caminho_saida_pdf = filedialog.asksaveasfilename(
                defaultextension='.pdf', filetypes=[('PDF files', '*.pdf')]
            )
            if caminho_saida_csv and caminho_saida_pdf:
                self.controller.salvar_relatorio(
                    relatorio, caminho_saida_csv, caminho_saida_pdf
                )
                messagebox.showinfo('Sucesso', 'Relatório gerado com sucesso!')
