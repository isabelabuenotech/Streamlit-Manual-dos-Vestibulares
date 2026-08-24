# Streamlit-Manual-dos-Vestibulares

# 📚 Vestibulares 2026 | Informações e Dicas

> **Aplicação Web interativa desenvolvida em Python e Streamlit para centralizar calendários, modelos de prova, dicas de estudos e políticas de permanência universitária.**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📌 O que é o projeto?

O **Portal Vestibulares 2026** é uma plataforma *data-driven* desenvolvida para orientar estudantes de Ensino Médio e pré-vestibulandos em sua jornada rumo ao Ensino Superior. 

Criado com foco em **Acessibilidade, Usabilidade (UX) e Eficiência Operacional**, o sistema consolida dados complexos de múltiplos vestibulares e instituições de ensino em um painel simples, intuitivo e com visualização dinâmica.

### 🎯 Principais Funcionalidades
- **🎓 Guias do Vestibular (ENEM, FUVEST, UNICAMP):** Cronogramas de isenção, inscrição, datas de prova, listas de leituras obrigatórias e análise do formato das provas (ex: modelo *TESTLET* do ENEM).
  
- **📅 Vestibulares de Meio de Ano:** Mapeamento de datas e links oficiais das principais faculdades públicas e privadas (UNESP, INSPER, FGV, MAUÁ).

- **🏛️ Políticas de Permanência e Auxílios:** Painel comparativo de auxílios (moradia, alimentação, bolsa permanência e inclusão digital) de mais de 20 universidades públicas e privadas.

- **💡 Curadoria de Recursos Educacionais:** Diretório de simulados abertos, ferramentas de estudos e indicação de mentores/professores referência nas redes sociais.

---

## 🛠️ Tecnologias Utilizadas

O projeto utiliza **Python** puro, tanto no *back-end* quanto no *front-end*, aproveitando o ecossistema do Streamlit combinado com estilização customizada:

* **[Python](https://www.python.org/):** Linguagem base para manipulação do estado da aplicação e estruturas de dados.
  
* **[Streamlit](https://streamlit.io/):** Framework para construção da interface Web, gerenciamento de estado (`session_state`), navegação modular em abas e colunas.

* **HTML5 & CSS3 Customizado:** Injeção de estilos para *design system* próprio (fontes *Google Fonts*, botões interativos, badges de status, alertas e componentes acessíveis).

---

## 💻 Como Instalar e Executar

### Pré-requisitos
Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/isabelabuenotech/nome-do-repositorio.git](https://github.com/isabelabuenotech/nome-do-repositorio.git)

2. **Acesse a pasta do projeto:**
cd nome-do-seu-repositorio

3. **Crie e ative um ambiente virtual**
   
***Linux / macOS***

  > _python3 -m venv venv_  
  > _source venv/bin/activate_

***Windows***

  > _python -m venv venv_  
  > _venv\Scripts\activate_

4. **Instale as dependências necessárias:**
_pip install streamlit_

5. **Execute a aplicação:**
_streamlit run streamlitapp.py_

## 🧪 Validação e Qualidade da Aplicação (QA)
Para garantir a estabilidade e fluidez da aplicação, foram aplicadas boas práticas de Garantia de Qualidade (QA) durante o desenvolvimento:

- **Teste de Fluxo de Navegação (Session State):** Validação da alternância entre telas e botões de retorno (btn_voltar) sem perda do histórico do usuário.

- **Validação de Exceções:** Tratamento de erros assíncronos no carregamento de ativos gráficos (logo_ismart.png) garantindo que o app continue funcional caso a imagem esteja indisponível.

- **Tratamento de Layout e Acessibilidade:** Testes de responsividade em layouts dinâmicos via st.columns e validação visual de contraste em componentes CSS customizados.

## 🤝 Como Contribuir
Contribuições são muito bem-vindas! Para contribuir com atualizações de datas, inserção de novas universidades ou refatoração de código:

1. **Faça um Fork deste repositório**

2. **Crie uma branch para sua funcionalidade:**
git checkout -b feature/NovaFuncionalidade.

4. **Suba suas alterações:**
git commit -m 'feat: Adiciona informações do Vestibular X'.

6. **Envie para a branch principal:**
git push origin feature/NovaFuncionalidade.

8. **Abra um Pull Request.**

# 👩‍💻 Autora e Contato
> **Isabela Bueno**
> Psicóloga Escolar | Analista Educacional Sênior | Data & Tech Enabler (QA & Python)

📧 **E-mail:** isabelabueno.tech@gmail.com

💼 **LinkedIn:** isabela-bueno-silva

🐱 **GitHub:** @isabelabuenotech
