# Pipeline de Extração: Clones de Código e Discussões (AIDev)

Este repositório contém a automação necessária para extrair pares de códigos clonados em Pull Requests e reconstruir a linha do tempo cronológica das discussões ocorridas nessas mesmas PRs.

## 📁 Pré-requisitos (Estrutura de Diretórios)

Antes de executar qualquer script, garanta que a raiz do projeto possua as seguintes pastas preenchidas:

* `clones_classified/`: Arquivos `.csv` com as classificações prévias dos clones (categorias, commits, duração).
* `metadata/`: Arquivos `.csv` com os metadados dos repositórios (SHAs, URLs, histórico).
* `search_results/`: Arquivos `.xml` (saída do NiCad) contendo os blocos, impressões digitais (fingerprints) e linhas exatas dos clones.
* `git_repos/`: Diretório base onde os repositórios estão armazenados. (Se algum projeto faltar, os scripts de extração farão o clone automático no modo `blobless` para poupar rede).

---

## 🚀 Fluxo de Execução (Passo a Passo)

### Passo 1: Extração dos Códigos Fonte dos Clones
**Script:** `extract_clone_codes.py`
* **Objetivo:** Faz o `git checkout` no commit exato de cada Pull Request, mapeia o arquivo via XML e extrai as linhas de código afetadas.
* **Comportamento:** Cria arquivos Markdown individuais dividindo os fragmentos de código e gera uma planilha inicial de classificação.
* **Saídas:** 
  * Pasta `extracted_clones_md/` (com os arquivos `.md` contendo o código).
  * Arquivo `Clone_Code_Classification.xlsx`.

### Passo 2: Padronização e Separação do Excel de Clones
**Script:** `fix_excel_tabs.py`
* **Objetivo:** Lê a planilha gerada no Passo 1, conserta o parseamento de links e categoriza os projetos.
* **Comportamento:** Monta a URL limpa apontando para o seu padrão no GitHub e separa os dados em abas independentes (Python, Java, C#, Ruby).
* **Saída:** 
  * Arquivo `Clone_Code_Classification_Fixed.xlsx`.

### Passo 3: Mineração e Construção das Discussões (Code Review)
**Script:** `construcao_arquivos_discussao.py` (ou `extract_discussions.py`)
* **Objetivo:** Extrair o contexto humano por trás da Pull Request.
* **Comportamento:** Conecta ao banco de dados do Hugging Face (`hao-li/AIDev`), cruza os dados com as PRs mapeadas e gera uma linha do tempo cronológica mesclando *Body*, *PR Comments*, *Reviews* e *Line Comments*. Também gera a planilha de mapeamento final.
* **Saídas:** 
  * Pasta `discussion/` (com arquivos `.md` contendo a conversa completa, divididos por linguagem e projeto).
  * Arquivo `Discussions_Summary.xlsx` (com as URLs customizadas para visualização no GitHub).

---

## 📊 Estrutura das URLs no GitHub
Os scripts estão configurados para gerar links dinâmicos no padrão de visualização deste repositório:
* **Códigos:** `https://github.com/ItaloVicente/Extract_discussion_AiDev/blob/main/extracted_clones_md/{nome_do_arquivo}.md`
* **Discussões:** `https://github.com/ItaloVicente/Extract_discussion_AiDev/blob/main/discussion/{linguagem}/{projeto}/{pr}.md`