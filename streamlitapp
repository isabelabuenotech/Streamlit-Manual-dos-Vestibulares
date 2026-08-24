import streamlit as st
 
st.set_page_config(
    page_title="Vestibulares 2026 | Informações e Dicas",
    page_icon="📚",
    layout="wide"
)
 
if "pagina" not in st.session_state:
    st.session_state.pagina = "home"
if "seguir_sub" not in st.session_state:
    st.session_state.seguir_sub = None
 
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Lato:wght@400;700&display=swap');
 
    html, body, .stApp { background-color: #f5fbff; font-family: 'Lato', sans-serif; }
 
    .main-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.1rem;
        font-weight: 800;
        color: #002561;
        text-align: center;
        padding: 1rem 0 0.2rem 0;
    }
    .main-subtitle {
        font-family: 'Lato', sans-serif;
        text-align: center;
        color: #008ED4;
        font-size: 1rem;
        margin-bottom: 1.2rem;
    }
    h2, h3 { font-family: 'Montserrat', sans-serif !important; color: #002561 !important; }
    h4 { font-family: 'Montserrat', sans-serif !important; color: #008ED4 !important; }
    hr { border: 1.5px solid #9DDCF9; margin: 1rem 0; }
 
    .badge {
        display: inline-block;
        background: #D4EFFC;
        color: #002561;
        border-radius: 20px;
        padding: 3px 14px;
        font-size: 0.82rem;
        font-weight: 700;
        font-family: 'Montserrat', sans-serif;
        margin: 2px 3px 2px 0;
    }
    .badge-gray { background: #f0f0f0; color: #888; }
 
    .dica-box {
        background: #fffde7;
        border-left: 4px solid #EBEA70;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin: 0.7rem 0;
        font-family: 'Lato', sans-serif;
        color: #002561;
    }
    .alert-box {
        background: #fff0f3;
        border-left: 4px solid #EE2D67;
        border-radius: 8px;
        padding: 0.9rem 1.2rem;
        margin: 0.5rem 0;
        font-size: 0.93rem;
        font-family: 'Lato', sans-serif;
        color: #002561;
    }
    .nav-btn button {
        background-color: #00BDF2 !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        border: none !important;
        border-radius: 10px !important;
        width: 100% !important;
    }
    .nav-btn button:hover { background-color: #008ED4 !important; }
    .back-btn button {
        background-color: transparent !important;
        color: #008ED4 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
        border: 2px solid #00BDF2 !important;
        border-radius: 8px !important;
    }
    div[data-testid="stInfo"] {
        background-color: #D4EFFC;
        color: #002561;
        border-left-color: #00BDF2;
        font-family: 'Lato', sans-serif;
    }
    div[data-testid="stSuccess"] {
        background-color: #8EC6B2;
        color: #002561;
        border-left-color: #002561;
        font-family: 'Lato', sans-serif;
    }
    [data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)
 
# ── Helpers ──────────────────────────────────────────────────────────────────
def render_datas(dados):
    for item, data, gray in dados:
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(f"**{item}**")
        with c2:
            cls = "badge badge-gray" if gray else "badge"
            st.markdown(f'<span class="{cls}">{data}</span>', unsafe_allow_html=True)
        st.markdown("")
 
def render_cronograma(dados, site=None):
    if site:
        st.markdown(f"🔗 **Site:** [{site}](https://{site})")
        st.markdown("")
    render_datas(dados)
 
def btn_voltar(destino="home"):
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("← Voltar"):
        st.session_state.pagina = destino
        st.session_state.seguir_sub = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("---")
 
def nav_btn(label, destino, col):
    with col:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        if st.button(label, use_container_width=True):
            st.session_state.pagina = destino
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
 
# ════════════════════════════════════════════════════════════════════════════
# HOME
# ════════════════════════════════════════════════════════════════════════════
if st.session_state.pagina == "home":
    st.markdown("<br>", unsafe_allow_html=True)
    try:
        c1, c2, c3 = st.columns([2, 1, 2])
        with c2:
            st.image("logo_ismart.png", use_container_width=True)
    except Exception:
        pass
    st.markdown('<div class="main-title">Vestibulares 2026 | Informações e Dicas</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Selecione uma seção para começar</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
 
    _, c1, c2, c3, c4, _ = st.columns([0.5, 2, 2, 2, 2, 0.5])
    nav_btn("🎓 Vestibulares 2026", "vest2026", c1)
    nav_btn("📅 Vestibulares Meio de Ano", "meioano", c2)
    nav_btn("💡 Você sabia?", "sabia", c3)
    nav_btn("🏛️ Políticas de Permanência e Auxílios", "permanencia", c4)
    st.stop()
 
# ════════════════════════════════════════════════════════════════════════════
# POLÍTICAS DE PERMANÊNCIA
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "permanencia":
    btn_voltar("home")
    st.markdown('<div class="main-title">🏛️ Políticas de Permanência e Auxílios</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Selecione o tipo de instituição</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
 
    _, c1, c2, _ = st.columns([1, 2, 2, 1])
    nav_btn("🎓 Universidades Públicas", "publicas", c1)
    nav_btn("🏫 Universidades Privadas", "privadas", c2)
    st.stop()
 
# ════════════════════════════════════════════════════════════════════════════
# UNIVERSIDADES PÚBLICAS
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "publicas":
    btn_voltar("permanencia")
    st.markdown('<div class="main-title">🎓 Universidades Públicas</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Clique em uma universidade para ver os detalhes</div>', unsafe_allow_html=True)
    st.markdown("")
 
    universidades_publicas = [
        {
            "nome": "USP - Universidade de São Paulo",
            "programa": "PAPFE",
            "beneficios": [
                "💰 Bolsa mensal: valor mensal para manutenção",
                "🏠 Moradia estudantil (CRUSP): residência gratuita para alunos de outras cidades",
                "🍽️ Alimentação: isenção total ou parcial no restaurante",
                "💻 Inclusão digital (equipamentos/internet)",
                "🧠 Apoio psicológico e social",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade",
                "Prioridade para estudantes de escola pública",
            ],
            "site": "https://www.usp.br",
        },
        {
            "nome": "UNICAMP - Universidade Estadual de Campinas",
            "programa": "SAE / DEAPE",
            "beneficios": [
                "💰 Bolsa Auxílio Social: valor mensal para manutenção",
                "🏠 Moradia (Moradia Estudantil): vaga ou auxílio aluguel",
                "🍽️ Alimentação: isenção total ou parcial no restaurante",
                "🚌 Transporte: auxílio financeiro",
                "🧠 Apoio psicológico e pedagógico",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade e de permanência na cidade",
                "Prioridade para ingressantes por cotas",
            ],
            "site": "https://www.unicamp.br",
        },
        {
            "nome": "UNESP - Universidade Estadual Paulista",
            "programa": "PAE",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Moradia (Moradia Estudantil): vaga ou auxílio aluguel",
                "🍽️ Alimentação: isenção total ou parcial no restaurante",
                "🚌 Transporte: auxílio financeiro",
                "📚 Apoio pedagógico",
            ],
            "criterios": [
                "Análise socioeconômica",
                "Renda familiar",
                "Distância da cidade de origem",
                "Situação de vulnerabilidade social",
            ],
            "site": "https://www.unesp.br",
        },
        {
            "nome": "UNIFESP - Universidade Federal de São Paulo",
            "programa": "Assistência Estudantil",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação: Restaurante universitário",
                "🚌 Transporte",
                "💻 Inclusão digital (equipamentos/internet)",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade",
            ],
            "site": "https://www.unifesp.br",
        },
        {
            "nome": "UFABC - Universidade Federal do ABC",
            "programa": "PAE",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação: Restaurante universitário",
                "💻 Inclusão digital (equipamentos/internet)",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade e de permanência na cidade",
            ],
            "site": "https://www.ufabc.edu.br",
        },
        {
            "nome": "UFSCAR - Universidade Federal de São Carlos",
            "programa": "Assistência Estudantil",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação: Restaurante universitário",
                "💻 Inclusão digital (equipamentos/internet)",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade",
            ],
            "site": "https://www.ufscar.br",
        },
        {
            "nome": "UFLA - Universidade Federal de Lavras",
            "programa": "PRAEC",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação: Restaurante universitário",
                "🧠 Apoio psicológico",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade e de permanência na cidade",
            ],
            "site": "https://ufla.br",
        },
        {
            "nome": "UFU - Universidade Federal de Uberlândia",
            "programa": "PROAE",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação: Restaurante universitário",
                "🚌 Transporte",
                "🧠 Saúde e apoio acadêmico",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade",
            ],
            "site": "https://www.ufu.br",
        },
        {
            "nome": "UNIFEI - Universidade Federal de Itajubá",
            "programa": "",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação: Restaurante universitário",
                "💻 Inclusão digital (equipamentos/internet)",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade e de permanência na cidade",
            ],
            "site": "https://www.unifei.edu.br",
        },
        {
            "nome": "UFF - Universidade Federal Fluminense",
            "programa": "PROAES",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação: Restaurante universitário",
                "🧠 Apoio psicológico",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade",
            ],
            "site": "https://www.uff.br",
        },
        {
            "nome": "UFSC - Universidade Federal de Santa Catarina",
            "programa": "PRAE",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação: Restaurante universitário",
                "🧠 Apoio psicológico",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade e de permanência na cidade",
            ],
            "site": "https://ufsc.br",
        },
        {
            "nome": "UFPR - Universidade Federal do Paraná",
            "programa": "PRAE",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação: Restaurante universitário",
                "🚌 Transporte",
                "🧠 Saúde",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade",
            ],
            "site": "https://www.ufpr.br",
        },
        {
            "nome": "UFV - Universidade Federal de Viçosa",
            "programa": "",
            "beneficios": [
                "💰 Auxílio permanência",
                "🏠 Auxílio moradia",
                "🍽️ Alimentação",
                "🧠 Saúde",
            ],
            "criterios": [
                "Renda familiar",
                "Avaliação socioeconômica",
                "Situação de vulnerabilidade",
            ],
            "site": "https://www.ufv.br",
        },
    ]
 
    for u in universidades_publicas:
        with st.expander(f"🏛️ {u['nome']}"):
            if u["programa"]:
                st.markdown(f"**Programa:** {u['programa']}")
            st.markdown("**Benefícios:**")
            for b in u["beneficios"]:
                st.markdown(f"- {b}")
            st.markdown("**Critérios:**")
            for c in u["criterios"]:
                st.markdown(f"- {c}")
            st.markdown(f"🔗 [Site oficial]({u['site']})")
    st.stop()
 
# ════════════════════════════════════════════════════════════════════════════
# UNIVERSIDADES PRIVADAS
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "privadas":
    btn_voltar("permanencia")
    st.markdown('<div class="main-title">🏫 Universidades Privadas</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Clique em uma universidade para ver os detalhes</div>', unsafe_allow_html=True)
    st.markdown("")
 
    universidades_privadas = [
        {
            "nome": "Insper",
            "beneficios": [
                "💰 Bolsa integral cobre 100% da mensalidade",
                "💵 Ajuda de custo mensal",
                "🏠 Moradia",
                "💻 Notebook",
                "🌍 Inglês",
            ],
            "criterios": [
                "Processo seletivo acadêmico (prova + desempenho)",
                "Avaliação socioeconômica e de Renda familiar",
                "Entrevistas + análise de perfil",
            ],
            "obs": [],
            "site": "https://www.insper.edu.br",
        },
        {
            "nome": "FGV - Fundação Getulio Vargas",
            "beneficios": [
                "💰 Bolsas integrais ou parciais",
                "🏠 Alguns auxílios adicionais (limitados)",
                "💳 Bolsas reembolsáveis (tipo financiamento)",
            ],
            "criterios": [
                "Mérito (desempenho no vestibular)",
                "Avaliação socioeconômica e de Renda familiar",
                "Em alguns casos, compromisso de devolução futura",
            ],
            "obs": [],
            "site": "https://www.fgv.br",
        },
        {
            "nome": "INTELI - Instituto de Tecnologia e Liderança",
            "beneficios": [
                "💰 Bolsa integral cobre 100% da mensalidade",
                "💵 Ajuda de custo mensal",
                "🏠 Moradia",
                "🍽️ Alimentação",
                "🚌 Transporte",
                "💻 Notebook",
                "🌍 Inglês",
            ],
            "criterios": [
                "Processo seletivo próprio (prova + desempenho + perfil)",
                "Avaliação socioeconômica e de Renda familiar",
                "Entrevistas + análise de perfil",
            ],
            "obs": [],
            "site": "https://www.inteli.edu.br",
        },
        {
            "nome": "Instituto Mauá de Tecnologia",
            "beneficios": ["💰 Bolsas integrais/parciais até 100%"],
            "criterios": [
                "Desempenho no vestibular",
                "Avaliação socioeconômica e de Renda familiar",
                "Desempenho acadêmico",
                "Análise de perfil",
            ],
            "obs": [],
            "site": "https://maua.br",
        },
        {
            "nome": "PUC SP - Pontifícia Universidade Católica de São Paulo",
            "beneficios": ["💰 Bolsas integrais/parciais até 100%"],
            "criterios": [
                "Desempenho no vestibular",
                "Desempenho acadêmico",
                "Entrevista",
                "Avaliação socioeconômica e de Renda familiar",
            ],
            "obs": [
                "**Bolsa SER PUC:** Edital específico para alunos que não se enquadram totalmente no perfil filantrópico, mas precisam de auxílio, mantido por doações.",
                "**Pod PuG:** Programa de parcelamento da própria PUC, sem juros, onde se paga metade durante o curso e o restante após a formatura.",
            ],
            "site": "https://www.pucsp.br",
        },
        {
            "nome": "Universidade Presbiteriana Mackenzie",
            "beneficios": ["💰 Bolsas integrais/parciais até 100%"],
            "criterios": [
                "**Bolsa Filantrópica Mackenzie:** Avaliação socioeconômica e de Renda familiar.",
                "**Programa Mackenzie Pra Você:** Destinado a alunos que cursaram o ensino médio em escola pública. A seleção é a partir do desempenho no vestibular.",
            ],
            "obs": [],
            "site": "https://www.mackenzie.br",
        },
        {
            "nome": "Centro Universitário FEI",
            "beneficios": [
                "💰 Bolsas integrais/parciais até 100%",
                "A bolsa é reavaliada semestralmente a partir de uma análise de critérios socioeconômicos e do desempenho acadêmico",
            ],
            "criterios": [
                "Desempenho no vestibular",
                "Avaliação socioeconômica e de Renda familiar",
            ],
            "obs": [],
            "site": "https://www.fei.edu.br",
        },
        {
            "nome": "Faculdade Israelita de Ciências da Saúde Albert Einstein",
            "beneficios": [
                "💰 Bolsas integrais/parciais até 100%",
                "A bolsa é reavaliada anualmente a partir de uma análise de critérios socioeconômicos e do desempenho acadêmico",
            ],
            "criterios": [
                "Alto desempenho acadêmico",
                "Avaliação socioeconômica e de Renda familiar",
                "Entrevistas + análise de perfil",
            ],
            "obs": [],
            "site": "https://www.einstein.br",
        },
        {
            "nome": "Faculdade de Ciências Médicas da Santa Casa de São Paulo",
            "beneficios": [
                "💰 Bolsas integrais (100%) e parciais (50%)",
                "A bolsa é reavaliada anualmente a partir de uma análise de critérios socioeconômicos",
            ],
            "criterios": [
                "Desempenho no vestibular",
                "Avaliação socioeconômica e de Renda familiar",
            ],
            "obs": [],
            "site": "https://fcmsantacasasp.edu.br",
        },
        {
            "nome": "Hospital Sírio-Libanês Ensino e Pesquisa",
            "beneficios": [
                "💰 Bolsas integrais que cobrem matrícula e mensalidades do curso",
                "A bolsa é reavaliada semestralmente a partir de uma análise de critérios socioeconômicos e do desempenho acadêmico",
            ],
            "criterios": [
                "Entrevistas + análise de perfil",
                "Desempenho no vestibular",
                "Avaliação socioeconômica e de Renda familiar",
            ],
            "obs": [],
            "site": "https://www.hospitalsiriolibanes.org.br",
        },
    ]
 
    for u in universidades_privadas:
        with st.expander(f"🏫 {u['nome']}"):
            st.markdown("**Benefícios:**")
            for b in u["beneficios"]:
                st.markdown(f"- {b}")
            st.markdown("**Critérios:**")
            for c in u["criterios"]:
                st.markdown(f"- {c}")
            if u["obs"]:
                st.markdown("**Observações:**")
                for o in u["obs"]:
                    st.markdown(f"- {o}")
            st.markdown(f"🔗 [Site oficial]({u['site']})")
    st.stop()
 
# ════════════════════════════════════════════════════════════════════════════
# VESTIBULARES 2026
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "vest2026":
    btn_voltar("home")
    st.markdown('<div class="main-title">🎓 Vestibulares 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Selecione um vestibular para ver as informações completas</div>', unsafe_allow_html=True)
    st.markdown("---")
 
    vestibular = st.selectbox("Escolha o vestibular:", ["Selecione...", "ENEM", "FUVEST", "UNICAMP"], label_visibility="collapsed")
 
    if vestibular == "ENEM":
        st.markdown("## 📝 ENEM")
        st.markdown("---")
        tab1, tab2, tab3 = st.tabs(["📅 Cronograma", "ℹ️ Informações", "🌟 Dicas de Ouro"])
 
        with tab1:
            st.markdown("### 📅 Cronograma")
            render_datas([
                ("Período para solicitar isenção", "13 a 24/04", False),
                ("Resultado da isenção", "08/05", False),
                ("Inscrições", "A ser divulgado", True),
                ("1º dia de prova", "A ser divulgado", True),
                ("2º dia de prova", "A ser divulgado", True),
                ("Datas SISU", "A ser divulgado", True),
            ])
 
        with tab2:
            st.markdown("### ℹ️ Informações")
            st.markdown("#### 📌 Modelo TESTLETS")
            st.info("O ENEM adotou o modelo de **TESTLETS** — formato que utiliza um único texto, gráfico ou mapa base para um bloco de 2 a 5 perguntas em sequência.")
            st.markdown("#### Como isso me afeta?")
            st.markdown("""
- **Tenha calma!** Não se apresse e leia as questões isoladamente. Busque entender profundamente o texto base para responder às questões. Muitas vezes, a resposta da questão 2 pode depender da lógica aplicada na questão 1.
- **Mais interpretação, menos Decoreba!** O foco deixa de ser decoreba e virá capacidade de interpretar contextos, inferir sentidos e analisar informações de forma integrada. Este ano, até questões de Exatas contarão com enunciados elaborados pensando em situações-problema complexas.
""")
            st.markdown("#### 📝 Redação")
            st.markdown("""
Na redação, os corretores esperam **menos redações prontas**, que seguem a "fôrma" que cabe qualquer tema; e **mais redações autorais**, que utilizam repertório sociocultural autêntico.
 
**Como tudo isso me afeta:**
- Evite ser genérico! O elemento **Ação** virou o mais influente da competência 5.
- Haverá **maior rigor na competência 5** (proposta de intervenção), **menor exigência na competência 4** (conectivos interparágrafos) e **penalização para repertórios considerados "de bolso"**.
""")
 
        with tab3:
            st.markdown("### 🌟 Dicas de Ouro")
            st.markdown('<div class="dica-box">✅ Treine questões/simulados de instituições que já utilizam o TESTLET em seus processos (como UNESP e FUVEST).</div>', unsafe_allow_html=True)
            st.markdown('<div class="dica-box">✅ Estude relacionando as disciplinas: Quando estudar Biologia, relacione com Química e Física; Quando estudar História, relacione com Geografia e Física. É essa visão interdisciplinar que será cobrada.</div>', unsafe_allow_html=True)
            st.markdown('<div class="dica-box">✅ Procure se atentar ao contexto, conecte pontos e eixos temáticos de cada questão!</div>', unsafe_allow_html=True)
 
    elif vestibular == "FUVEST":
        st.markdown("## 🏛️ FUVEST")
        st.markdown("---")
        tab1, tab2, tab3, tab4 = st.tabs(["📅 Cronograma", "ℹ️ Informações", "📚 Leituras Obrigatórias", "🌟 Dicas de Ouro"])
 
        with tab1:
            st.markdown("### 📅 Cronograma")
            st.markdown("🔗 **Site:** [fuvest.br](https://www.fuvest.br)")
            st.markdown("")
            render_datas([
                ("Período para solicitar isenção", "A ser divulgado", True),
                ("Inscrições", "17/08 a 09/10", False),
                ("1ª Fase", "15/11", False),
                ("2ª Fase — Dia 1", "13/12", False),
                ("2ª Fase — Dia 2", "14/12", False),
            ])
 
        with tab2:
            st.markdown("### ℹ️ Informações")
            st.info("Desde o ano passado a FUVEST vem adequando sua prova para um estilo **interdisciplinar**, onde as questões são menos diretas e passam a cobrar a conexão de conhecimentos.")
            st.info("Os candidatos ao Vestibular 2027 terão pela frente uma **1ª Fase com menos questões de múltipla escolha** — em vez das tradicionais 90, serão **80 questões**, mantido o tempo de prova (5h).")
            st.markdown("#### 📋 Formato")
            st.markdown("""
**1ª Fase (5h):** 80 questões de Artes, Biologia, Educação Física, Filosofia, Física, Geografia, História, Inglês, Matemática, Português, Química e Sociologia.
 
**2ª Fase:**
- **Dia 1 (4h):** 10 questões discursivas de Português e uma redação.
- **Dia 2 (4h):** 12 questões discursivas de disciplinas específicas de acordo com a carreira escolhida.
""")
            st.markdown("#### Como tudo isso me afeta?")
            st.markdown("""
- **Mais interpretação e raciocínio, menos Decoreba!** O foco deixa de ser decoreba e virá capacidade de conectar e analisar conhecimentos de diferentes áreas em uma mesma questão, interpretar e relacionar contextos.
- **Sociologia, Filosofia, Educação Física e Artes** ganham mais espaço e seus conhecimentos passam a ser cobrados com maior especificidade.
- A **redação** poderá cobrar diferentes gêneros textuais para além da dissertação. Poderão ser cobradas redações no estilo artigo de opinião, posts, carta, crônica, discurso, etc.
""")
 
        with tab3:
            st.markdown("### 📚 Lista de Leituras Obrigatórias")
            st.success("🎉 **Novidade histórica:** Lista de leituras obrigatórias **só com autoras mulheres** pela primeira vez na história da FUVEST!")
            for titulo, autora in [
                ("Opúsculo Humanitário (1853)", "Nísia Floresta"),
                ("Nebulosas (1872)", "Narcisa Amália"),
                ("Memórias de Martha (1899)", "Julia Lopes de Almeida"),
                ("Caminho de pedras (1937)", "Rachel de Queiroz"),
                ("A paixão segundo G.H. (1964)", "Clarice Lispector"),
                ("Geografia (1967)", "Sophia de Mello Breyner Andresen"),
                ("Balada de amor ao vento (1990)", "Paulina Chiziane"),
                ("Canção para ninar menino grande (2018)", "Conceição Evaristo"),
                ("A visão das plantas (2019)", "Djaimilia Pereira de Almeida"),
            ]:
                st.markdown(f"- **{titulo}** — *{autora}*")
            st.markdown("---")
            st.markdown("#### 🏛️ Aulas Gratuitas — Biblioteca Brasiliana Guita e José Mindlin")
            st.markdown("A Biblioteca Brasiliana Guita e José Mindlin promoverá aulas dedicadas às obras literárias exigidas no Vestibular FUVEST 2027. Os encontros exploram enredo, personagens e contexto histórico, sendo conduzidos por professores e pesquisadores universitários.")
            st.markdown('<div class="alert-box">⚠️ As aulas são gratuitas; no entanto, para participação presencial, é necessário realizar inscrição prévia.</div>', unsafe_allow_html=True)
            st.markdown('<div class="alert-box">⚠️ As transmissões ocorrem ao vivo pelo canal do <strong>@bbmusp</strong> no YouTube, onde as gravações permanecem disponíveis posteriormente. Para mais informações, acesse a bio do <strong>@bbmusp</strong>.</div>', unsafe_allow_html=True)
 
        with tab4:
            st.markdown("### 🌟 Dicas de Ouro")
            st.markdown('<div class="dica-box">✅ Treine questões/simulados de instituições que já utilizam o TESTLET em seus processos (como UNESP e UNICAMP).</div>', unsafe_allow_html=True)
            st.markdown('<div class="dica-box">✅ Estude relacionando as disciplinas: Quando estudar Biologia, relacione com Química e Física; Quando estudar História, relacione com Geografia e Física. É essa visão interdisciplinar que será cobrada.</div>', unsafe_allow_html=True)
            st.markdown('<div class="dica-box">✅ Procure se atentar ao contexto, conecte pontos e eixos temáticos de cada questão!</div>', unsafe_allow_html=True)
 
    elif vestibular == "UNICAMP":
        st.markdown("## 🔬 UNICAMP")
        st.markdown("---")
        tab1, tab2, tab3 = st.tabs(["📅 Cronograma", "ℹ️ Informações", "📚 Leituras Obrigatórias"])
 
        with tab1:
            st.markdown("### 📅 Cronograma")
            st.markdown("🔗 **Site:** [comvest.unicamp.br](http://comvest.unicamp.br)")
            st.markdown("")
            render_datas([
                ("Período para solicitar isenção", "11/05 a 05/06", False),
                ("Inscrições", "03 a 31/08", False),
                ("1ª Fase", "18/10", False),
                ("2ª Fase — Dia 1", "29/11", False),
                ("2ª Fase — Dia 2", "30/11", False),
            ])
 
        with tab2:
            st.markdown("### ℹ️ Informações")
            st.info("O vestibular da UNICAMP é famoso por ser bastante **crítico** e focar na **interdisciplinaridade** das áreas do conhecimento em detrimento da memorização e decoreba.")
            st.markdown("#### 📋 Formato")
            st.markdown("""
**1ª Fase (5h):** 72 questões de Português, Literatura, Matemática, Inglês, História, Geografia, Física, Química, Biologia, Filosofia e Sociologia.
 
**2ª Fase:** Redação e questões dissertativas divididas entre núcleo comum e específicas por área do curso escolhido (Exatas, Humanas ou Biológicas).
""")
 
        with tab3:
            st.markdown("### 📚 Lista de Leituras Obrigatórias")
            for titulo, autora in [
                ("Prosas seguidas de odes mínimas", "José Paulo Paes"),
                ("Olhos d'água", "Conceição Evaristo"),
                ("A vida não é útil", "Ailton Krenak"),
                ("Vida e morte de M.J. Gonzaga de Sá", "Lima Barreto"),
                ("No seu pescoço", "Chimamanda Ngozi Adichie"),
                ("Morangos mofados (Contos escolhidos*)", "Caio Fernando Abreu"),
                ("Memórias Póstumas de Brás Cubas", "Machado de Assis"),
                ("Canções escolhidas**", "Paulo César Pinheiro"),
                ("Os funerais da Mamãe Grande", "Gabriel García Márquez"),
            ]:
                st.markdown(f"- **{titulo}** — *{autora}*")
 
# ════════════════════════════════════════════════════════════════════════════
# VESTIBULARES MEIO DE ANO
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "meioano":
    btn_voltar("home")
    st.markdown('<div class="main-title">📅 Vestibulares Meio de Ano 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Selecione um vestibular para ver as informações completas</div>', unsafe_allow_html=True)
    st.markdown("---")
 
    vestibular_meio = st.selectbox("Escolha o vestibular:", ["Selecione...", "UNESP 2026/2", "INSPER 2026/2", "MAUÁ 2026/2", "FGV 2026/2"], label_visibility="collapsed")
 
    if vestibular_meio == "UNESP 2026/2":
        st.markdown("## 🏫 UNESP 2026/2")
        st.markdown("---")
        render_cronograma([
            ("Período para solicitar isenção e redução de 50% da taxa", "06 a 12/04", False),
            ("Inscrições (vestibular)", "13/04 a 05/05", False),
            ("1ª Fase", "24/05", False),
            ("2ª Fase — Dia 1", "20/06", False),
            ("2ª Fase — Dia 2", "21/06", False),
        ], site="vunesp.com.br")
 
    elif vestibular_meio == "INSPER 2026/2":
        st.markdown("## 🏦 INSPER 2026/2")
        st.markdown("---")
        render_cronograma([
            ("Período para solicitar isenção (via Ismart)", "Em análise", True),
            ("Inscrições", "Até 13/05", False),
            ("Prova", "07/06", False),
        ], site="insper.edu.br")
 
    elif vestibular_meio == "MAUÁ 2026/2":
        st.markdown("## ⚙️ MAUÁ 2026/2")
        st.markdown("---")
        st.markdown("🔗 **Site:** [maua.br](https://www.maua.br)")
        st.markdown("")
        st.markdown("**Isenção:** Solicitada no processo de inscrição")
        st.markdown("")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🏢 Modalidade Presencial")
            st.markdown('<span class="badge">Até 17/06</span> Inscrições para prova presencial', unsafe_allow_html=True)
            st.markdown("")
            st.markdown('<span class="badge">21/06</span> Prova presencial', unsafe_allow_html=True)
        with col2:
            st.markdown("#### 💻 Modalidade Online")
            st.markdown('<span class="badge">Até 22/06</span> Inscrições para prova online', unsafe_allow_html=True)
            st.markdown("")
            st.markdown('<span class="badge">24/06</span> Prova online', unsafe_allow_html=True)
 
    elif vestibular_meio == "FGV 2026/2":
        st.markdown("## 📊 FGV 2026/2")
        st.markdown("---")
        render_cronograma([
            ("Período para solicitar isenção", "Até 20/04", False),
            ("Inscrições", "Até 27/04", False),
            ("Prova", "24/05", False),
        ], site="fgv.br")
 
# ════════════════════════════════════════════════════════════════════════════
# VOCÊ SABIA?
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "sabia":
    btn_voltar("home")
    st.markdown('<div class="main-title">💡 Você sabia?</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Dicas e recursos gratuitos para turbinar seus estudos</div>', unsafe_allow_html=True)
    st.markdown("---")
 
    st.markdown("### Provas Antigas e/ou simulados")
    st.markdown("Grande parte das universidades oferecem provas antigas e/ou simulados gratuitos e online em seus sites. Acesse os sites das instituições e aproveite!")
    st.markdown("Ao longo do ano, diversos cursinhos abrem inscrições para simulados abertos gratuitos nas modalidades presencial/online. Confira as oportunidades:")
    st.markdown("")
 
    col1, col2 = st.columns(2)
 
    with col1:
        with st.container(border=True):
            st.markdown("**Estratégia Vestibulares**")
            st.link_button("Acessar simulados", "https://vestibulares.estrategia.com/instituicao/cursos/simulados-gratuitos", use_container_width=True)
 
    with col2:
        with st.container(border=True):
            st.markdown("**Etapa**")
            st.link_button("Acessar simulados", "https://etapa.com.br/home/apoio-ao-vestibulando/simulados", use_container_width=True)
 
    with col1:
        with st.container(border=True):
            st.markdown("**Objetivo**")
            st.link_button("Acessar simulados", "https://www.curso-objetivo.br/vestibular/simulados.aspx", use_container_width=True)
 
    with col2:
        with st.container(border=True):
            st.markdown("**Poliedro**")
            st.markdown("O cursinho oferece simulados abertos ao longo do ano. Fique atento ao site.")
            st.markdown("Acesse também o **Poliedro Resolve**, ferramenta de correção e resolução de questões de vestibular através de vídeos explicativos e comentários de questões de provas feito por professores do Poliedro.")
            st.link_button("Acessar simulados", "https://cursopoliedro.com.br/", use_container_width=True)
            st.link_button("Acessar Poliedro Resolve", "https://poliedroresolve.sistemapoliedro.com.br/", use_container_width=True)
 
    with col1:
        with st.container(border=True):
            st.markdown("**Anglo**")
            st.markdown("O cursinho oferece simulados abertos ao longo do ano. Fique atento ao site.")
            st.link_button("Acessar simulados", "https://cursoanglo.com.br/", use_container_width=True)
 
    with col2:
        with st.container(border=True):
            st.markdown("**CPV**")
            st.link_button("Acessar simulados", "https://cursinho.cpv.com.br/simulados-abertos-cpv", use_container_width=True)
 
    st.markdown("---")
    st.markdown("### 🏫 Outros cursinhos com simulados abertos")
    st.markdown("""
Outros cursinhos que oferecem simulados abertos presenciais/online:
- **Cursinho da Poli**
- **CUJA (UNIFESP)**
""")
 
    st.markdown("---")
    st.markdown("### 📱 O que seguir para me atualizar?")
    st.markdown("")
 
    _, b1, b2, b3, _ = st.columns([0.2, 2, 2, 2, 0.2])
    with b1:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        if st.button("📚 Organização de Estudos", use_container_width=True):
            st.session_state.seguir_sub = "organizacao"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with b2:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        if st.button("📰 Notícias e Atualidades", use_container_width=True):
            st.session_state.seguir_sub = "noticias"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with b3:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        if st.button("🧑‍🏫 Professores Referência", use_container_width=True):
            st.session_state.seguir_sub = "professores"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
 
    sub = st.session_state.get("seguir_sub", None)
 
    if sub == "organizacao":
        st.markdown("---")
        with st.expander("🎯 Estrategistas e Mentores", expanded=True):
            st.markdown("""
- **@sabrinaoliveira.vemed:** Uma das maiores referências em mentoria, especialmente para Medicina. Ela foca muito em estratégia de prova, controle emocional e como otimizar o tempo para matérias de peso maior.
- **@viniciusdeoliiveira:** Focado em ensinar o "caminho das pedras" para a aprovação. Suas dicas costumam envolver técnicas de memorização, como lidar com simulados e como não travar em questões difíceis.
- **@olastro** (Theo Affini e Matheus Custódio): Especialistas em ajudar vestibulandos a construir uma base sólida, focando em métodos de estudo baseados em evidência (revisão espaçada, prática deliberada, etc.).
""")
        with st.expander("📒 Studygrams de Organização", expanded=True):
            st.markdown("""
- **@biazmed** (Beatriz Zamarco): Referência em organização para ENEM e Fuvest. Ela compartilha como usa ferramentas de gestão, como aumentou sua nota em pontos específicos e como mantém a disciplina no dia a dia.
- **@luisaoliveirx:** Excelente para quem quer dicas de hábitos e aprendizado eficiente. Ela foca muito em como tornar a rotina menos pesada e mais produtiva.
- **@matt.studies** (Mateus Negri): Traz um conteúdo muito visual e prático sobre vlogs de estudo e técnicas de organização que funcionam tanto para o colégio quanto para o cursinho.
""")
        with st.expander("🗓️ Ferramentas e Cronogramas", expanded=True):
            st.markdown("""
- **@vestibulandoapp:** Ótimo perfil para acompanhar calendários de provas e dicas de como usar aplicativos para cronometrar o estudo (técnica Pomodoro, etc.).
- **@querosercaloura:** Focado em mapas mentais e organização de agenda. É ideal para quem se perde com o volume de conteúdos e precisa de uma guia visual para os tópicos.
- **@planeje_estudos:** Focado especificamente em planners e cronogramas detalhados de quanto tempo dedicar a cada matéria.
""")
 
    elif sub == "noticias":
        st.markdown("---")
        with st.expander("📡 Curadoria de Notícias", expanded=True):
            st.markdown("""
- **@g1** (Editoria de Educação): O G1 tem um braço muito forte focado no ENEM. Eles postam diariamente notícias sobre o que está acontecendo no Brasil e no mundo com uma linguagem direta, além de quadros como o "Fato ou Fake", excelente para desenvolver senso crítico.
- **@jocacorreia:** O professor Joca é uma das maiores referências em Geopolítica. Ele consegue conectar conflitos atuais (como as tensões no Oriente Médio ou crises climáticas) com o contexto histórico que o vestibular exige.
- **@atualidadescomorlando:** O professor Orlando traz análises semanais sobre os principais fatos do mundo, sempre com foco em como aquele tema pode virar uma proposta de redação ou uma questão de Geografia/História.
""")
        with st.expander("🗺️ Infográficos e Dados (Visuais)", expanded=True):
            st.markdown("""
- **@brasilemmapas:** Essencial. Eles transformam dados complexos de demografia, economia e sociedade em mapas fáceis de entender. Ajuda muito a visualizar as desigualdades regionais do Brasil.
- **@nexojornal:** Um perfil focado em jornalismo explicativo. Os gráficos e "nós explicamos" deles são perfeitos para entender temas complexos (como inflação, IA ou sistema eleitoral) de forma profunda mas rápida.
""")
        with st.expander("🌍 Geopolítica e História do Presente", expanded=True):
            st.markdown("""
- **@geografiageral:** Posta conteúdos diários sobre o mundo, misturando curiosidades com fatos políticos e ambientais. É excelente para manter a mente "fresca" sobre os nomes de líderes mundiais e fronteiras em disputa.
- **@geopoliticahoje:** Focado 100% em relações internacionais. É um perfil mais denso, ideal para quem vai prestar cursos como Relações Internacionais, Direito ou quer uma nota muito alta em Humanas.
""")
        with st.expander("🎭 Repertório Cultural e Sociedade", expanded=True):
            st.markdown("""
- **@quebrandootabu:** Embora seja um perfil de opinião, ele levanta muitos debates sociais (racismo, feminismo, saúde mental, sustentabilidade) que são temas clássicos de redação. É bom para ver diferentes argumentos sobre o mesmo assunto.
- **@tededucation:** As animações e pílulas de conhecimento deles (muitas vezes traduzidas/legendadas) trazem conceitos científicos e sociológicos que dão um "up" imediato na qualidade do seu texto.
""")
 
    elif sub == "professores":
        st.markdown("---")
        with st.expander("✍️ Redação e Linguagens", expanded=True):
            st.markdown("""
- **@professorapablina:** Especialista em Redação ENEM. Ela foca muito em estrutura, conectivos e como garantir a nota 1000 com estratégias replicáveis.
- **@viniciusoliveirapro:** Criador do "Manual da Redação". É excelente para quem precisa de repertório sociocultural e quer entender como as bancas (não só ENEM, mas também as de São Paulo) avaliam o texto.
- **@professor_noslen:** O maior canal de Língua Portuguesa do Brasil. No Instagram, ele traz pílulas rápidas de gramática e literatura que ajudam muito nas questões objetivas.
""")
        with st.expander("📐 Matemática e Física", expanded=True):
            st.markdown("""
- **@professorfredao:** Se você vai prestar ENEM, ele é indispensável. Fredão é o "guru" da TRI (Teoria de Resposta ao Item) e analisa cada questão com foco em estatística e eficiência.
- **@fisicacomdouglas:** Focado em simplificar a Física. Ele utiliza muitas demonstrações visuais e resolve questões de vestibulares paulistas e nacionais de forma bem didática.
- **@professorguiandrade:** Excelente para quem precisa de Matemática Básica e dicas rápidas de raciocínio lógico.
""")
        with st.expander("🔬 Química e Biologia", expanded=True):
            st.markdown("""
- **@professorgabrielcabral:** Química de um jeito leve. Ele usa músicas e mnemônicos que realmente grudam na cabeça, ótimo para decorar aquelas fórmulas chatas de orgânica.
- **@biologiacomsamuelcunha:** Referência em Biologia. O perfil dele traz muitos esquemas visuais e atualizações sobre temas que as bancas amam, como ecologia e genética.
- **@quimicacomgabs:** Focado em aprofundamento para quem busca cursos concorridos (como Medicina).
""")
        with st.expander("🌎 Humanas (História, Geografia e Atualidades)", expanded=True):
            st.markdown("""
- **@prof.sergiogrunier:** Especialista em Geografia e Atualidades. Essencial para entender os conflitos mundiais que acabam virando tema de prova meses depois.
- **@historiaonline** (Professores Rodolfo e Dalton): Uma das maiores autoridades em História. Eles fazem análises profundas de contextos históricos e sociais, essenciais para as questões dissertativas de 2ª fase.
- **@guiandradehistoria:** Focado em História do Brasil e Geral, com resumos bem estruturados.
""")
