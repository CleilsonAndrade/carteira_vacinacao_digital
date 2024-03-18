<div align="center">
    <h1 align="center">Carteira de Vacinação Digital</h1>
    <p>Aplicação tem objetivo de transformar os dados da carteira de vacinação convencional de papel, em um sistema digital para guardar informações do usuário e suas vacinas já tomadas.</p>
    <img src="./design/logo.png" alt="Logo" width="500">
</div>

# 📒 Índice

- [Descrição](#descrição)
- [Requisitos Funcionais](#requisitos-funcionais)
- [Features](#features)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Licença](#licença)

# 📃 <span id="descrição">Descrição</span>
Aplicação com temática sobre saúde, tendo objetivo de transformar os dados da carteira de vacinação convencional de papel, em um sistema digital para guardar informações do usuário e suas vacinas já tomadas, sendo seu desenvolvimento realizado durante o Projeto Integrador Ministrado pelo <a href="https://www.linkedin.com/in/carlos-henrique-duarte-felisbino-9b493526/">_Professor Carlos Henrique Duarte Felisbino_</a>

## Requisitos Funcionais
- [x] Salva os dados do paciente<br>
- [x] Mostra vacinas obrigatórias<br>
- [x] Salva vacinas tomadas<br>
- [x] Válida vacinas obrigatórias<br>
- [x] Mostra vacinas já tomadas<br>
- [x] Especifica quais vacinas faltam, se houver<br>

## Features
- [x] Impressão do documento<br>
- [x] Responsividade<br>
- [x] Exibição de notícias<br>

# 💻 <span id="tecnologias">Tecnologias</span>
## Front-End:
- **HTML**
- **CSS**
- **JavaScript**
- **Jinja2 (Template Engine)**
- **Bootstrap 4**
- **Axios (Cliente HTTP)**

### Back-End:
- **Python**
- **Flask (Micro-Framework de Servidor)**
- **SQL**
- **SQLite3 (Banco de Dados)**

# 🎨 <span id="design">Design</span>
- O modelo final para versão desktop e mobile está disponível na pasta `./design`

- <span id="cores">Cores<br></span>
  * #90caf9<br>
  * #f4f4f4<br>

- <span id="fontes">Fontes<br></span>
  * Roboto sans-serif

# 🚀 <span id="instalação">Instalação</span>
```bash
  # Instalar o pacote:
  $ pip install pipreqs

  # Clone este repositório:
  $ git clone https://github.com/CleilsonAndrade/carteira_vacinacao_digital.git

  $ cd ./carteira_vacinacao_digital

  # Windows
  $ python3 -m venv virtual
  $ virtual\Scripts\activate
  $ pip install flask && flask --version
  $ python init_db.py
  $ set FLASK_ENV=app && set FLASK_ENV=development
  $ flask run

  # Linux
  $ python3 -m venv virtual
  $ source virtual/bin/activate
  $ pip install -r requirements.txt
  $ python init_db.py
  $ export FLASK_ENV=app && export FLASK_ENV=development && flask run
```

# 📝 <span id="licença">Licença</span>

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  Feito com 💜 by CleilsonAndrade
</p>