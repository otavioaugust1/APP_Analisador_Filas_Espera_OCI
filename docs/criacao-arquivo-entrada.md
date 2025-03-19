# Criação do Arquivo de Entrada

O arquivo de entrada é um arquivo CSV que contém as solicitações de atendimento a serem analisadas pelo aplicativo. Este arquivo deve seguir um formato específico para garantir que o aplicativo possa processá-lo corretamente. Abaixo estão as regras e os atributos necessários para a criação do arquivo.

---

## Formatação do Arquivo

- **Tamanho máximo do arquivo**: 50 MB. Arquivos maiores serão rejeitados pelo servidor.
- **Cabeçalho**: A primeira linha do arquivo é considerada o cabeçalho e não deve conter dados das solicitações de atendimento.
- **Delimitador**: O caractere delimitador é o **ponto e vírgula (`;`)**.
- **Extensão**: O arquivo deve ser salvo com a extensão **`.csv`**.
- **Número de colunas**: Cada linha do arquivo deve possuir **10 colunas**, mesmo que o valor de algumas colunas seja fornecido em branco.
- **Encoding**: Recomenda-se que o arquivo seja salvo com o encoding **UTF-8** para evitar problemas com acentuações.

---

## Atributos do Arquivo

Cada linha do arquivo deve conter os seguintes atributos, na ordem especificada:

### 1. **IDENTIFICADOR_LOCAL** (Obrigatório)
- **Descrição**: Identificador único do registro no sistema de origem.
- **Formato**: Texto com tamanho máximo de **150 caracteres**.

### 2. **DOCUMENTO_PACIENTE** (Obrigatório)
- **Descrição**: Documento do paciente (CPF ou CNS).
- **Formato**:
  - **CPF**: 11 dígitos.
  - **CNS**: 15 dígitos.

### 3. **DATA_SOLICITACAO** (Obrigatório)
- **Descrição**: Data da solicitação do atendimento.
- **Formato**: Data no formato **ISO (YYYY-MM-DD)**.
- **Exemplo**: `2023-09-19`.
- **Regra**: A data deve ser **inferior ou igual à data atual**.

### 4. **CNES_SOLICITANTE** (Obrigatório)
- **Descrição**: Código do estabelecimento de saúde que solicitou o atendimento.
- **Formato**: 7 dígitos (mesmo para códigos que começam com 0).
- **Exemplo**: `2759306`.

### 5. **CNES_REGULADOR** (Obrigatório)
- **Descrição**: Código do estabelecimento de saúde responsável pela regulação do atendimento.
- **Formato**: 7 dígitos (mesmo para códigos que começam com 0).
- **Exemplo**: `2759306`.

### 6. **CODIGO_SIGTAP** (Obrigatório)
- **Descrição**: Código do procedimento solicitado, conforme tabela SIGTAP.
- **Formato**: 10 dígitos.
- **Exemplo**: `0204030030` (Mamografia).

### 7. **CBO** (Opcional)
- **Descrição**: Código da Classificação Brasileira de Ocupações (CBO) do profissional que solicitou o atendimento.
- **Formato**: 6 dígitos.
- **Obrigatoriedade**: Obrigatório apenas para procedimentos de consulta, se o atributo **CODIGO_SIGTAP** começar com `030101`.

### 8. **CID10** (Opcional)
- **Descrição**: Código da Classificação Internacional de Doenças (CID-10) relacionado à solicitação.
- **Formato**: Máximo de 4 dígitos.
- **Exemplo**: `C50` (Câncer de mama).

### 9. **CODIGO_MODALIDADE_ASSISTENCIAL** (Obrigatório)
- **Descrição**: Código que indica a modalidade de assistência.
- **Valores**:
  - `04`: Atenção hospitalar.
  - `07`: Ambulatorial.

### 10. **CODIGO_CARTER_SOLICITACAO** (Obrigatório)
- **Descrição**: Código que indica o tipo de solicitação.
- **Valores**:
  - `1`: Atendimento eletivo.
  - `2`: Urgência.

### 11. **STATUS** (Obrigatório)
- **Descrição**: Status da solicitação.
- **Valores**:
  - `1`: Pendente.
  - `2`: Agendada.
  - `3`: Cancelada.
  - `4`: Negada.
  - `5`: Atendido/Internado.
  - `6`: Falta.
  - `7`: Devolvido.

### 12. **DATA_AUTORIZACAO** (Opcional)
- **Descrição**: Data de autorização do atendimento.
- **Formato**: Data no formato **ISO (YYYY-MM-DD)**.
- **Exemplo**: `2023-09-19`.
- **Obrigatoriedade**: Obrigatório apenas para o status **2 - Agendada**.
- **Regra**: A data deve ser **superior ou igual à data da solicitação**.

### 13. **DATA_EXECUCAO** (Opcional)
- **Descrição**: Data de execução do atendimento.
- **Formato**: Data no formato **ISO (YYYY-MM-DD)**.
- **Exemplo**: `2023-09-19`.
- **Obrigatoriedade**: Obrigatório apenas para o status **2 - Agendada**.
- **Regra**: A data deve ser **superior ou igual à data da solicitação**.

### 14. **CNES_EXECUTANTE** (Opcional)
- **Descrição**: Código do estabelecimento de saúde que executou o atendimento.
- **Formato**: 7 dígitos (mesmo para códigos que começam com 0).
- **Obrigatoriedade**: Obrigatório apenas para o status **2 - Agendada**.

---

## Exemplo de Arquivo CSV

Abaixo está um exemplo de como o arquivo CSV deve ser estruturado:

```csv
IDENTIFICADOR_LOCAL;DOCUMENTO_PACIENTE;DATA_SOLICITACAO;CNES_SOLICITANTE;CNES_REGULADOR;CODIGO_SIGTAP;CBO;CID10;CODIGO_MODALIDADE_ASSISTENCIAL;CODIGO_CARTER_SOLICITACAO;STATUS;DATA_AUTORIZACAO;DATA_EXECUCAO;CNES_EXECUTANTE
REG001;12345678901;2023-09-19;2759306;2759306;0204030030;223456;C50;07;1;1;;;;
REG002;98765432109;2023-09-20;2759306;2759306;0301010072;223456;C50;07;1;2;2023-09-21;2023-09-22;2759306
```