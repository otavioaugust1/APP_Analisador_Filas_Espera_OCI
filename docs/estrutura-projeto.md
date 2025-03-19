# Estrutura do Projeto

O projeto está organizado seguindo as melhores práticas da PEP (Python Enhancement Proposals). Abaixo está a estrutura de pastas:
```bash
/
├── docs/ # Documentação do projeto
├── src/ # Código-fonte do projeto
│ ├── controller/ # Lógica de controle (interação com o usuário)
│ ├── models/ # Lógica de processamento de dados
│ ├── views/ # Interface gráfica (PySimpleGUI ou Tkinter)
│ ├── utils/ # Utilitários (funções auxiliares)
│ ├── img/ # Imagens internas
│ └── app/ # Configuração da aplicação
├── img/ # Imagens gerais (ex: screenshots)
├── tests/ # Testes unitários e de integração
├── README.md # Documentação principal
├── requirements.txt # Dependências do projeto
├── .gitignore # Arquivos ignorados pelo Git
├── setup.py # Configuração para empacotamento
└── main.py # Ponto de entrada do projeto

```

---

**Próximo**: [Contribuição](contribuicao.md)