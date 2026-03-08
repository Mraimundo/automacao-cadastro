# 🤖 Python Automação — Cadastro Automático de Produtos

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Automação-red?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

---

## 📌 Sobre o Projeto

Este projeto automatiza o processo de **cadastro em massa de produtos** em um sistema web empresarial, eliminando a necessidade de inserção manual, registro por registro. Utilizando a biblioteca **PyAutoGUI**, o script simula ações humanas no computador — movimentos de mouse, cliques e digitação — para preencher formulários automaticamente com os dados extraídos de uma planilha `.csv`.

O que levaria horas de trabalho repetitivo é concluído em minutos, com zero intervenção humana após a execução.

---

## 🎯 Objetivos

- ✅ Automatizar o login no sistema web da empresa
- ✅ Ler a lista de produtos a partir de um arquivo `.csv`
- ✅ Cadastrar cada produto no sistema via automação de interface gráfica
- ✅ Tratar campos opcionais (como observações) sem quebrar o fluxo
- ✅ Eliminar erros humanos e retrabalho no processo de cadastro

---

## 🗂️ Estrutura do Projeto

```
📦 python-automacao-cadastro/
├── 📄 produtos.csv               # Planilha com os produtos a serem cadastrados
├── 📓 automacao_cadastro.py      # Script principal de automação
└── 📄 README.md                  # Documentação do projeto
```

---

## 📋 Estrutura Esperada do arquivo `produtos.csv`

O arquivo deve conter as seguintes colunas:

| Coluna           | Tipo             | Descrição                       |
| ---------------- | ---------------- | ------------------------------- |
| `codigo`         | int/str          | Código identificador do produto |
| `marca`          | str              | Marca do produto                |
| `tipo`           | str              | Tipo do produto                 |
| `categoria`      | str              | Categoria do produto            |
| `preco_unitario` | float            | Preço de venda unitário         |
| `custo`          | float            | Custo do produto                |
| `obs`            | str _(opcional)_ | Observações adicionais          |

> ⚠️ A coluna `obs` pode conter valores vazios — o script trata esse caso automaticamente.

---

## 🛠️ Tecnologias e Ferramentas

| Ferramenta       | Finalidade                                       |
| ---------------- | ------------------------------------------------ |
| **Python 3.10+** | Linguagem principal do projeto                   |
| **PyAutoGUI**    | Automação de mouse, teclado e interface gráfica  |
| **Pandas**       | Leitura e iteração sobre a planilha de produtos  |
| **Time**         | Controle de pausas e sincronização com o sistema |

---

## ⚙️ Instalação e Configuração

### Pré-requisitos

- Python 3.10 ou superior instalado
- Google Chrome instalado e acessível via barra de pesquisa do Windows

### Instalando as dependências

```bash
pip install pyautogui pandas openpyxl
```

### Clonando o repositório

```bash
git clone https://github.com/seu-usuario/python-automacao-cadastro.git
cd python-automacao-cadastro
```

---

## ▶️ Como Executar

1. Certifique-se de que o arquivo `produtos.csv` está na mesma pasta do script
2. **Não mova o mouse nem use o teclado** durante a execução — o PyAutoGUI controla o computador em tempo real
3. Execute o script:

```bash
python automacao_cadastro.py
```

4. Aguarde a mensagem de conclusão no terminal:

```
Todos os produtos cadastrados!
```

> 💡 **Dica:** Para interromper a automação emergencialmente, mova o mouse rapidamente para um dos cantos da tela — o PyAutoGUI possui um mecanismo de segurança (`FailSafe`) que encerra o script ao detectar isso.

---

## 🔍 Metodologia — Passo a Passo

### Configuração Inicial

Antes de qualquer ação, o script define uma pausa global entre cada comando para garantir que o sistema web tenha tempo de responder:

```python
import time
import pyautogui
import pandas

pyautogui.PAUSE = 0.3  # pausa de 0.3s entre cada ação
```

---

### Passo 1 — Abrir o Navegador e Acessar o Sistema

O script abre o Google Chrome via atalho do Windows e navega automaticamente até a URL do sistema:

```python
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)  # aguarda o carregamento da página
```

---

### Passo 2 — Realizar o Login

O script localiza os campos de e-mail e senha pelas coordenadas da tela e preenche as credenciais:

```python
pyautogui.click(x=723, y=436)
pyautogui.write("pythonimpressionador@gmail.com", interval=0.05)
pyautogui.press("tab")
pyautogui.write("sua senha", interval=0.05)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)  # aguarda o redirecionamento após login
```

> ⚠️ **Atenção:** As coordenadas `x` e `y` são específicas para a resolução de tela utilizada durante o desenvolvimento. Se necessário, ajuste-as usando `pyautogui.position()` para identificar as coordenadas corretas na sua tela.

---

### Passo 3 — Importar a Base de Produtos

Leitura da planilha `.csv` com todos os produtos a serem cadastrados:

```python
tabela = pandas.read_csv("produtos.csv")
print(tabela)
```

---

### Passo 4 e 5 — Cadastrar os Produtos em Loop

O script percorre cada linha da planilha e preenche o formulário do sistema automaticamente, campo a campo:

```python
for linha in tabela.index:
    pyautogui.click(x=653, y=294)  # clica no primeiro campo do formulário

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # tratamento do campo opcional "obs"
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")   # confirma o cadastro
    pyautogui.scroll(5000)     # rola a tela para o topo para o próximo registro
```

**Detalhes importantes do loop:**

| Detalhe                       | Explicação                                                      |
| ----------------------------- | --------------------------------------------------------------- |
| `tabela.index`                | Itera sobre cada linha da planilha                              |
| `tabela.loc[linha, "coluna"]` | Acessa o valor de uma célula específica                         |
| `str(valor)`                  | Converte qualquer tipo de dado para texto antes de digitar      |
| `pandas.isna(obs)`            | Verifica se o campo `obs` está vazio antes de tentar escrevê-lo |
| `pyautogui.scroll(5000)`      | Retorna ao topo do formulário após cada cadastro                |

---

## ⚠️ Pontos de Atenção

### Coordenadas de Tela

As posições `x` e `y` dos cliques foram mapeadas para uma resolução específica. Se o script não estiver clicando nos lugares corretos, identifique as novas coordenadas com:

```python
import pyautogui
import time

time.sleep(3)  # dá tempo de posicionar o mouse
print(pyautogui.position())
```

### Velocidade de Digitação

O parâmetro `interval` dentro do `pyautogui.write()` controla a velocidade de digitação (em segundos por caractere). Para sistemas mais lentos, aumente esse valor:

```python
pyautogui.write("texto", interval=0.1)  # mais lento e seguro
```

### Segurança das Credenciais

> 🔐 Nunca suba credenciais reais no repositório. Utilize variáveis de ambiente ou um arquivo `.env` para armazenar senhas com segurança, e adicione esse arquivo ao `.gitignore`.

---

## 💡 Conclusões

- A automação com **PyAutoGUI** elimina completamente o trabalho manual de cadastro repetitivo, reduzindo tempo e erros operacionais.
- O tratamento do campo opcional `obs` com `pandas.isna()` garante que o script **não quebre** mesmo em planilhas com dados incompletos.
- O uso de `pyautogui.PAUSE` e `time.sleep()` é essencial para sincronizar a automação com o tempo de resposta do sistema web.
- O projeto é **facilmente adaptável** a outros sistemas e formulários, bastando ajustar as coordenadas e os nomes das colunas da planilha.

---

## 👤 Autor

Desenvolvido como parte do programa **Python Impressionador** — automação de tarefas repetitivas com Python para ganho de produtividade no dia a dia.

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
