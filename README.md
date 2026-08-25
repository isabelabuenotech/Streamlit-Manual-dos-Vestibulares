# 📚 Vestibulares 2026 | Informações e Dicas

> **Aplicação Web interativa desenvolvida em Python e Streamlit para centralizar calendários, modelos de prova, dicas de estudos e políticas de permanência universitária.**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---
## 📌 O que é o projeto?

O **Portal Vestibulares 2026** é uma plataforma *data-driven* desenvolvida para orientar estudantes de Ensino Médio e pré-vestibulandos em sua jornada rumo ao Ensino Superior. 

Criado com foco em **Acessibilidade, Usabilidade (UX) e Eficiência Operacional**, o sistema consolida dados complexos de múltiplos vestibulares e instituições de ensino em um painel simples, intuitivo e com visualização dinâmica.

### 🎯 Principais Funcionalidades
- **🎓 Guias dos Vestibulares:** Cronogramas de isenção, inscrição, datas de prova, listas de leituras obrigatórias e análise do formato das provas (ex: modelo *TESTLET* do ENEM).
  
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
## 🧪 Validação e Qualidade da Aplicação (QA)
Para garantir a estabilidade e fluidez da aplicação, foram aplicadas boas práticas de Garantia de Qualidade (QA) durante o desenvolvimento:

- **Teste de Fluxo de Navegação (Session State):** Validação da alternância entre telas e botões de retorno (btn_voltar) sem perda do histórico do usuário.

- **Validação de Exceções:** Tratamento de erros assíncronos no carregamento de ativos gráficos (logo_ismart.png) garantindo que o app continue funcional caso a imagem esteja indisponível.

- **Tratamento de Layout e Acessibilidade:** Testes de responsividade em layouts dinâmicos via st.columns e validação visual de contraste em componentes CSS customizados.

---
# 👩‍💻 Autora e Contato
> **Isabela Bueno**
> Psicóloga Escolar | Analista Educacional Sênior | Data & Tech Enabler (QA & Python)

📧 **E-mail:** isabelabueno.tech@gmail.com

💼 **LinkedIn:** isabela-bueno-silva

🐱 **GitHub:** @isabelabuenotech
