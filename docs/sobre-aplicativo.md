# Sobre o Aplicativo

O **Analisador de Filas de Espera** é uma ferramenta desenvolvida para auxiliar gestores de saúde na análise das filas de espera e na identificação de pacientes que podem ser agrupados em OCIs. O aplicativo processa arquivos CSV contendo solicitações de atendimento e verifica quais pacientes possuem os procedimentos necessários para serem incluídos em uma OCI.

## Funcionalidades Principais

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

**Próximo**: [Instalação](instalacao.md)