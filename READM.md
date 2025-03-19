# Analisador de Filas de Espera - PMAE e OCIs

Este projeto é uma ferramenta para análise de filas de espera no contexto do **Programa de Melhoria do Acesso e da Qualidade da Atenção Especializada (PMAE)** e das **Ofertas de Cuidados Integrados (OCIs)**. O aplicativo permite identificar agrupamentos de pacientes que podem ser atendidos de forma integrada, facilitando a gestão das filas de espera e a organização dos procedimentos no Sistema Único de Saúde (SUS).

---

## Sobre o PMAE e as OCIs

### O que é o PMAE?
O **Programa de Melhoria do Acesso e da Qualidade da Atenção Especializada (PMAE)** é uma iniciativa do Ministério da Saúde que visa melhorar o acesso e a qualidade dos serviços de saúde no SUS. O programa promove a organização das filas de espera, a integração entre os níveis de atenção (primária, secundária e terciária) e a otimização dos recursos disponíveis.

### O que são as OCIs?
As **Ofertas de Cuidados Integrados (OCIs)** são conjuntos de procedimentos (consultas, exames, terapias, etc.) organizados em etapas de cuidado, como diagnóstico ou tratamento de curta duração. Cada OCI possui itens obrigatórios e facultativos, que devem ser realizados de forma integrada para garantir um atendimento oportuno e de qualidade.

O objetivo das OCIs é oferecer um cuidado mais eficiente, reduzindo o tempo de espera e melhorando a experiência do paciente no SUS.

---

## Sobre o Aplicativo

O **Analisador de Filas de Espera** é uma ferramenta desenvolvida para auxiliar gestores de saúde na análise das filas de espera e na identificação de pacientes que podem ser agrupados em OCIs. O aplicativo processa arquivos CSV contendo solicitações de atendimento e verifica quais pacientes possuem os procedimentos necessários para serem incluídos em uma OCI.

### Funcionalidades Principais:
1. **Análise de Agrupamentos**:
   - Identifica pacientes que podem ser agrupados em OCIs com base nos procedimentos solicitados.
   - Verifica os itens obrigatórios e facultativos de cada OCI.

2. **Geração de Relatórios**:
   - Gera relatórios em formato CSV e PDF, detalhando os agrupamentos encontrados e os pacientes que não se encaixam em nenhum agrupamento.
   - Os relatórios incluem informações como o código da OCI, o nome da OCI, os pacientes agrupados e os procedimentos realizados.

3. **Interface Gráfica Simples**:
   - Interface intuitiva para seleção do arquivo CSV e geração dos relatórios.
   - Facilita o uso por gestores e equipes de saúde, sem necessidade de conhecimentos técnicos avançados.

4. **Filtragem de Dados**:
   - Filtra os registros com STATUS igual a 1 (PENDENTE), garantindo que apenas os procedimentos pendentes sejam considerados na análise.

---

## Estrutura do Projeto

O projeto está organizado seguindo as melhores práticas da PEP (Python Enhancement Proposals) e a estrutura de diretórios recomendada para projetos Python. Abaixo está a estrutura de pastas:

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

## Como Executar o Projeto

### Pré-requisitos:
- Python 3.8 ou superior.
- Dependências listadas no arquivo `requirements.txt`.

### Passos para Execução:

1. Clone o repositório:
```bash
   git clone https://github.com/seu-usuario/analisador-oci.git
   cd analisador-oci
```


2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o projeto:
```bash
python main.py
```

4. Utilize a interface gráfica para selecionar o arquivo CSV e gerar os relatórios.

.

## Exemplo de Uso
Passo 1: Selecionar o Arquivo CSV
* Na interface gráfica, clique em "Selecionar Arquivo CSV" e escolha o arquivo contendo as solicitações de atendimento.

Passo 2: Gerar Relatórios
* Após a análise, o aplicativo solicitará os caminhos para salvar os relatórios em CSV e PDF.

Passo 3: Visualizar os Resultados
* O relatório gerado inclui:
    * Agrupamentos de pacientes por OCI.
    * Pacientes que não se encaixam em nenhum agrupamento.
    * Data e hora da geração do relatório.

## Exemplo de Saída
Aqui está um exemplo de como o relatório pode ser gerado:

```bash
*********************    FORAM ENCONTRADOS 4 CONJUNTOS DE OCI'S    ***********************

_________________________________________________________________________________________
09.01.01.0014 - OCI AVALIAÇÃO DIAGNÓSTICA INICIAL DE CÂNCER DE MAMA

--- 708706*****5792
-------- OBG    2759306    2025-01-27    0204030030 - MAMOGRAFIA
-------- OBG    2759306    2024-12-12    0301010307 - TELECONSULTA MÉDICA NA ATENÇÃO ESPECIALIZADA
-------- OBG    2759306    2025-01-30    0301010072 - CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA

********************    PACIENTES QUE NÃO ESTÃO EM NENHUM CONJUNTO  ***********************
--- 2759306    12345678901    2024-10-31    0204030030 - MAMOGRAFIA
--- 2759306    12345678901    2024-10-31    0301010072 - CONSULTA MEDICA EM ATENÇÃO ESPECIALIZADA

19/10/2023 14:30:45
```
# Imagens do Projeto
[imgem]

# Contribuição
Contribuições são bem-vindas! Se você deseja contribuir para o projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -m 'Adicionando nova feature').
4. Push para a branch (git push origin feature/nova-feature).
5. Abra um Pull Request.

# Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

# Contato
Para dúvidas ou sugestões, entre em contato:
* Nome do Desenvolvedor: **Otavio Augusto**
* E-mail: **otavio.august@hotmail.com**
* GitHub: **https://github.com/otavioaugut1**