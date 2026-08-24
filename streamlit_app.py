import streamlit as st

# ════════════════════════════════════════════════════════════════════════════
# CONFIGURAÇÃO DA PÁGINA
# ════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Vestibulares 2026 | Informações e Dicas",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inicialização de variáveis no Session State
if "pagina" not in st.session_state:
    st.session_state.pagina = "home"
if "seguir_sub" not in st.session_state:
    st.session_state.seguir_sub = None

# ════════════════════════════════════════════════════════════════════════════
# ESTILIZAÇÃO CUSTOMIZADA (CSS) — CORREÇÃO DE ACESSIBILIDADE E CORES
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Lato:wght@400;700&display=swap');

    /* Força a cor do fundo global e texto padrão escuro para alto contraste */
    html, body, .stApp {
        background-color: #f5fbff !important;
        color: #002561 !important;
        font-family: 'Lato', sans-serif;
    }

    /* Garantia de cor para todos os textos parágrafo e listas */
    p, span, label, li, div {
        color: #002561 !important;
    }

    /* Cabeçalhos principais */
    .main-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        color: #002561 !important;
        text-align: center;
        padding: 0.8rem 0 0.2rem 0;
    }
    .main-subtitle {
        font-family: 'Lato', sans-serif;
        text-align: center;
        color: #008ED4 !important;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }

    h1, h2, h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #002561 !important;
    }
    h4 {
        font-family: 'Montserrat', sans-serif !important;
        color: #008ED4 !important;
    }
    hr {
        border: 1px solid #9DDCF9 !important;
        margin: 1.2rem 0;
    }

    /* Correção dos Menus de Seleção (st.selectbox) e Input Labels */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #002561 !important;
        border: 1.5px solid #00BDF2 !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] span {
        color: #002561 !important;
    }
    ul[role="listbox"] {
        background-color: #ffffff !important;
    }
    li[role="option"] span {
        color: #002561 !important;
    }

    /* Badges e Tags */
    .badge {
        display: inline-block;
        background: #D4EFFC !important;
        color: #002561 !important;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.85rem;
        font-weight: 700;
        font-family: 'Montserrat', sans-serif;
        margin: 2px 3px 2px 0;
    }
    .badge-gray {
        background: #e2e8f0 !important;
        color: #475569 !important;
    }

    /* Caixas de Dicas e Alertas com contraste garantido */
    .dica-box {
        background: #fffde7 !important;
        border-left: 5px solid #EBEA70 !important;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin: 0.8rem 0;
        font-family: 'Lato', sans-serif;
        color: #002561 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }
    .alert-box {
        background: #fff0f3 !important;
        border-left: 5px solid #EE2D67 !important;
        border-radius: 8px;
        padding: 0.9rem 1.2rem;
        margin: 0.6rem 0;
        font-size: 0.95rem;
        font-family: 'Lato', sans-serif;
        color: #002561 !important;
    }

    /* Botões de Navegação Principal */
    .nav-btn button {
        background-color: #00BDF2 !important;
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1rem !important;
        min-height: 3.2rem !important;
        box-shadow: 0 4px 6px rgba(0, 189, 242, 0.2);
        transition: all 0.2s ease-in-out !important;
    }
    .nav-btn button * {
        color: #ffffff !important;
    }
    .nav-btn button:hover {
        background-color: #008ED4 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 142, 212, 0.3);
    }

    /* Botão Voltar */
    .back-btn button {
        background-color: #ffffff !important;
        color: #008ED4 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        border: 2px solid #00BDF2 !important;
        border-radius: 8px !important;
        padding: 0.3rem 1.2rem !important;
    }
    .back-btn button * {
        color: #008ED4 !important;
    }
    .back-btn button:hover {
        background-color: #D4EFFC !important;
    }

    /* Estilização de Expander e Containers */
    div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #bae6fd !important;
        border-radius: 8px !important;
    }
    div[data-testid="stExpander"] summary span {
        color: #002561 !important;
        font-weight: 700 !important;
    }

    /* Estilização de Alertas nativos */
    div[data-testid="stInfo"] {
        background-color: #e0f2fe !important;
        color: #0369a1 !important;
        border-left-color: #00BDF2 !important;
        border-radius: 8px;
    }
    div[data-testid="stSuccess"] {
        background-color: #d1fae5 !important;
        color: #065f46 !important;
        border-left-color: #10b981 !important;
        border-radius: 8px;
    }

    /* Ocultar barra lateral */
    [data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# HELPERS (FUNÇÕES AUXILIARES)
# ════════════════════════════════════════════════════════════════════════════
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
        st.markdown(f"🔗 **Site Oficial:** [{site}](https://{site})")
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
        if st.button(label, use_container_width=True, key=f"btn_{destino}_{label}"):
            st.session_state.pagina = destino
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: HOME
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
    st.markdown('<div class="main-subtitle">Selecione uma seção para começar a navegar</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    _, c1, c2, c3, c4, _ = st.columns([0.2, 2, 2, 2, 2, 0.2])
    nav_btn("🎓 Vestibulares 2026", "vest2026", c1)
    nav_btn("📅 Vestibulares Meio de Ano", "meioano", c2)
    nav_btn("💡 Você sabia?", "sabia", c3)
    nav_btn("🏛️ Políticas de Permanência", "permanencia", c4)
    st.stop()

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: POLÍTICAS DE PERMANÊNCIA
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "permanencia":
    btn_voltar("home")
    st.markdown('<div class="main-title">🏛️ Políticas de Permanência e Auxílios</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Selecione a categoria de universidade</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    _, c1, c2, _ = st.columns([1, 2, 2, 1])
    nav_btn("🎓 Universidades Públicas", "publicas", c1)
    nav_btn("🏫 Universidades Privadas", "privadas", c2)
    st.stop()

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: UNIVERSIDADES PÚBLICAS
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "publicas":
    btn_voltar("permanencia")
    st.markdown('<div class="main-title">🎓 Universidades Públicas</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Clique em uma universidade para expandir os detalhes</div>', unsafe_allow_html=True)
    st.markdown("")

    universidades_publicas = [
        {
            "nome": "USP - Universidade de São Paulo",
            "programa": "PAPFE",
            "beneficios": [
                "💰 Bolsa mensal: valor financeiro para manutenção geral",
                "🏠 Moradia estudantil (CRUSP): residência gratuita para alunos de outras cidades",
                "🍽️ Alimentação: isenção total ou parcial no restaurante universitário",
                "💻 Inclusão digital (auxílio para equipamentos/internet)",
                "🧠 Apoio psicológico e social contínuo",
            ],
            "criterios": [
                "Renda familiar per capita",
                "Avaliação socioeconômica detalhada",
                "Situação de vulnerabilidade social",
                "Prioridade para estudantes de escola pública",
            ],
            "site": "https://www.usp.br",
        },
        {
            "nome": "UNICAMP - Universidade Estadual de Campinas",
            "programa": "SAE / DEAPE",
            "beneficios": [
                "💰 Bolsa Auxílio Social: valor mensal para manutenção",
                "🏠 Moradia Estudantil: vaga residencial ou auxílio aluguel",
                "🍽️ Alimentação: isenção nos restaurantes universitários",
                "🚌 Transporte: auxílio financeiro para locomoção",
                "🧠 Apoio psicológico e pedagógico especial",
            ],
            "criterios": [
                "Renda familiar comprovada",
                "Avaliação socioeconômica pelo SAE",
                "Necessidade de permanência na cidade do campus",
            ],
            "site": "https://www.unicamp.br",
        },
        {
            "nome": "UNESP - Universidade Estadual Paulista",
            "programa": "PAE",
            "beneficios": [
                "💰 Auxílio permanência estudantil",
                "🏠 Moradia Estudantil: vaga ou auxílio financeiro moradia",
                "🍽️ Alimentação: isenção total/parcial no R.U.",
                "🚌 Auxílio transporte",
            ],
            "criterios": ["Análise socioeconômica documental", "Renda familiar per capita"],
            "site": "https://www.unesp.br",
        },
        {
            "nome": "UNIFESP - Universidade Federal de São Paulo",
            "programa": "Assistência Estudantil",
            "beneficios": ["💰 Auxílio permanência", "🏠 Auxílio moradia", "🍽️ Alimentação", "💻 Inclusão digital"],
            "criterios": ["Renda familiar de até 1,5 salário mínimo per capita"],
            "site": "https://www.unifesp.br",
        },
        {
            "nome": "UFABC - Universidade Federal do ABC",
            "programa": "PAE",
            "beneficios": ["💰 Auxílio permanência", "🏠 Auxílio moradia", "🍽️ Alimentação", "💻 Inclusão digital"],
            "criterios": ["Análise socioeconômica"],
            "site": "https://www.ufabc.edu.br",
        },
        {
            "nome": "UFSCAR - Universidade Federal de São Carlos",
            "programa": "Assistência Estudantil",
            "beneficios": ["💰 Auxílio permanência", "🏠 Moradia/Auxílio Moradia", "🍽️ Alimentação"],
            "criterios": ["Critérios socioeconômicos do PNAES"],
            "site": "https://www.ufscar.br",
        },
        {
            "nome": "UFLA - Universidade Federal de Lavras",
            "programa": "PRAEC",
            "beneficios": ["💰 Auxílio permanência", "🏠 Moradia", "🍽️ R.U.", "🧠 Apoio psicológico"],
            "criterios": ["Renda familiar e vulnerabilidade social"],
            "site": "https://ufla.br",
        },
        {
            "nome": "UFU - Universidade Federal de Uberlândia",
            "programa": "PROAE",
            "beneficios": ["💰 Auxílio permanência", "🏠 Auxílio moradia", "🍽️ R.U.", "🚌 Transporte"],
            "criterios": ["Análise socioeconômica"],
            "site": "https://www.ufu.br",
        },
        {
            "nome": "UNIFEI - Universidade Federal de Itajubá",
            "programa": "Assistência Estudantil",
            "beneficios": ["💰 Auxílio permanência", "🏠 Moradia", "🍽️ Alimentação"],
            "criterios": ["Avaliação socioeconômica"],
            "site": "https://www.unifei.edu.br",
        },
        {
            "nome": "UFF - Universidade Federal Fluminense",
            "programa": "PROAES",
            "beneficios": ["💰 Auxílio permanência", "🏠 Auxílio moradia", "🍽️ R.U."],
            "criterios": ["Renda familiar e vulnerabilidade"],
            "site": "https://www.uff.br",
        },
        {
            "nome": "UFSC - Universidade Federal de Santa Catarina",
            "programa": "PRAE",
            "beneficios": ["💰 Auxílio permanência", "🏠 Moradia", "🍽️ R.U. gratuito"],
            "criterios": ["Análise socioeconômica"],
            "site": "https://ufsc.br",
        },
        {
            "nome": "UFPR - Universidade Federal do Paraná",
            "programa": "PRAE",
            "beneficios": ["💰 Auxílio permanência", "🏠 Moradia", "🍽️ R.U.", "🚌 Transporte"],
            "criterios": ["Renda familiar per capita"],
            "site": "https://www.ufpr.br",
        },
        {
            "nome": "UFV - Universidade Federal de Viçosa",
            "programa": "Assistência Estudantil",
            "beneficios": ["💰 Auxílio permanência", "🏠 Moradia", "🍽️ Alimentação"],
            "criterios": ["Análise socioeconômica"],
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
# PÁGINA: UNIVERSIDADES PRIVADAS
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "privadas":
    btn_voltar("permanencia")
    st.markdown('<div class="main-title">🏫 Universidades Privadas</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Clique em uma universidade para ver os detalhes de bolsas</div>', unsafe_allow_html=True)
    st.markdown("")

    universidades_privadas = [
        {
            "nome": "Insper",
            "beneficios": ["💰 Bolsa integral 100%", "💵 Ajuda de custo mensal", "🏠 Moradia", "💻 Notebook"],
            "criterios": ["Desempenho acadêmico", "Avaliação socioeconômica", "Entrevistas"],
            "obs": [],
            "site": "https://www.insper.edu.br",
        },
        {
            "nome": "FGV - Fundação Getulio Vargas",
            "beneficios": ["💰 Bolsas integrais/parciais", "🏠 Auxílios de manutenção", "💳 Financiamento próprio"],
            "criterios": ["Mérito no vestibular", "Avaliação socioeconômica"],
            "obs": [],
            "site": "https://www.fgv.br",
        },
        {
            "nome": "INTELI - Instituto de Tecnologia e Liderança",
            "beneficios": ["💰 Bolsa integral 100%", "💵 Ajuda de custo", "🏠 Moradia", "💻 Notebook"],
            "criterios": ["Desafio de lógica + perfil", "Avaliação socioeconômica"],
            "obs": [],
            "site": "https://www.inteli.edu.br",
        },
        {
            "nome": "Instituto Mauá de Tecnologia",
            "beneficios": ["💰 Bolsas de até 100%"],
            "criterios": ["Classificação no vestibular", "Análise de renda"],
            "obs": [],
            "site": "https://maua.br",
        },
        {
            "nome": "PUC SP - Pontifícia Universidade Católica de São Paulo",
            "beneficios": ["💰 Bolsas filantrópicas até 100%"],
            "criterios": ["Desempenho no vestibular", "Avaliação socioeconômica"],
            "obs": ["**Bolsa SER PUC:** Edital para necessidades específicas.", "**Pod PuG:** Parcelamento sem juros."],
            "site": "https://www.pucsp.br",
        },
        {
            "nome": "Universidade Presbiteriana Mackenzie",
            "beneficios": ["💰 Bolsas integrais e parciais"],
            "criterios": ["Bolsa Filantrópica e Programa Mackenzie Pra Você"],
            "obs": [],
            "site": "https://www.mackenzie.br",
        },
        {
            "nome": "Centro Universitário FEI",
            "beneficios": ["💰 Bolsas de até 100%"],
            "criterios": ["Desempenho no vestibular"],
            "obs": [],
            "site": "https://www.fei.edu.br",
        },
        {
            "nome": "Faculdade Israelita de Ciências da Saúde Albert Einstein",
            "beneficios": ["💰 Bolsas integrais e parciais"],
            "criterios": ["Alto desempenho e perfil socioeconômico"],
            "obs": [],
            "site": "https://www.einstein.br",
        },
        {
            "nome": "Faculdade de Ciências Médicas da Santa Casa de SP",
            "beneficios": ["💰 Bolsas de 50% e 100%"],
            "criterios": ["Desempenho no vestibular e renda"],
            "obs": [],
            "site": "https://fcmsantacasasp.edu.br",
        },
        {
            "nome": "Hospital Sírio-Libanês Ensino e Pesquisa",
            "beneficios": ["💰 Bolsas integrais na área da saúde"],
            "criterios": ["Processo seletivo e entrevista socioeconômica"],
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
# PÁGINA: VESTIBULARES 2026
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "vest2026":
    btn_voltar("home")
    st.markdown('<div class="main-title">🎓 Vestibulares 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Selecione um exame para consultar os detalhes completos</div>', unsafe_allow_html=True)
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
            ])

        with tab2:
            st.markdown("### ℹ️ Informações")
            st.markdown("#### 📌 Modelo TESTLETS")
            st.info("O ENEM adotou o modelo de **TESTLETS** — formato com texto base para blocos de 2 a 5 perguntas.")
            st.markdown("#### 📝 Redação")
            st.markdown("""
- **Maior rigor na competência 5** (proposta de intervenção).
- **Penalização para repertórios considerados 'de bolso'**.
""")

        with tab3:
            st.markdown("### 🌟 Dicas de Ouro")
            st.markdown('<div class="dica-box">✅ Treine questões de exames interdisciplinares.</div>', unsafe_allow_html=True)

    elif vestibular == "FUVEST":
        st.markdown("## 🏛️ FUVEST")
        st.markdown("---")
        tab1, tab2, tab3, tab4 = st.tabs(["📅 Cronograma", "ℹ️ Informações", "📚 Leituras Obrigatórias", "🌟 Dicas de Ouro"])

        with tab1:
            st.markdown("### 📅 Cronograma")
            render_cronograma([
                ("Inscrições", "17/08 a 09/10", False),
                ("1ª Fase", "15/11", False),
                ("2ª Fase — Dia 1", "13/12", False),
                ("2ª Fase — Dia 2", "14/12", False),
            ], site="fuvest.br")

        with tab2:
            st.markdown("### ℹ️ Informações")
            st.info("A 1ª Fase conta com **80 questões de múltipla escolha**.")

        with tab3:
            st.markdown("### 📚 Leituras Obrigatórias")
            st.success("🎉 Lista composta exclusivamente por autoras mulheres!")
            obras = [
                ("Opúsculo Humanitário (1853)", "Nísia Floresta"),
                ("Nebulosas (1872)", "Narcisa Amália"),
                ("Memórias de Martha (1899)", "Julia Lopes de Almeida"),
                ("Caminho de pedras (1937)", "Rachel de Queiroz"),
                ("A paixão segundo G.H. (1964)", "Clarice Lispector"),
                ("Geografia (1967)", "Sophia de Mello Breyner Andresen"),
                ("Balada de amor ao vento (1990)", "Paulina Chiziane"),
                ("Canção para ninar menino grande (2018)", "Conceição Evaristo"),
                ("A visão das plantas (2019)", "Djaimilia Pereira de Almeida"),
            ]
            for titulo, autora in obras:
                st.markdown(f"- **{titulo}** — *{autora}*")

        with tab4:
            st.markdown("### 🌟 Dicas de Ouro")
            st.markdown('<div class="dica-box">✅ Treine a resolução de questões discursivas para a 2ª Fase.</div>', unsafe_allow_html=True)

    elif vestibular == "UNICAMP":
        st.markdown("## 🔬 UNICAMP")
        st.markdown("---")
        tab1, tab2, tab3 = st.tabs(["📅 Cronograma", "ℹ️ Informações", "📚 Leituras Obrigatórias"])

        with tab1:
            st.markdown("### 📅 Cronograma")
            render_cronograma([
                ("Isenção", "11/05 a 05/06", False),
                ("Inscrições", "03 a 31/08", False),
                ("1ª Fase", "18/10", False),
            ], site="comvest.unicamp.br")

        with tab2:
            st.markdown("### ℹ️ Informações")
            st.info("Prova crítica e focada em análise de contexto.")

        with tab3:
            st.markdown("### 📚 Leituras Obrigatórias")
            obras_unicamp = [
                ("Prosas seguidas de odes mínimas", "José Paulo Paes"),
                ("Olhos d'água", "Conceição Evaristo"),
                ("A vida não é útil", "Ailton Krenak"),
                ("Vida e morte de M.J. Gonzaga de Sá", "Lima Barreto"),
                ("No seu pescoço", "Chimamanda Ngozi Adichie"),
            ]
            for titulo, autora in obras_unicamp:
                st.markdown(f"- **{titulo}** — *{autora}*")

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: VESTIBULARES MEIO DE ANO
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "meioano":
    btn_voltar("home")
    st.markdown('<div class="main-title">📅 Vestibulares Meio de Ano 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Consulte prazos e inscrições do meio do ano</div>', unsafe_allow_html=True)
    st.markdown("---")

    vestibular_meio = st.selectbox("Escolha o vestibular:", ["Selecione...", "UNESP 2026/2", "INSPER 2026/2", "MAUÁ 2026/2", "FGV 2026/2"], label_visibility="collapsed")

    if vestibular_meio == "UNESP 2026/2":
        st.markdown("## 🏫 UNESP 2026/2")
        st.markdown("---")
        render_cronograma([
            ("Inscrições", "13/04 a 05/05", False),
            ("1ª Fase", "24/05", False),
        ], site="vunesp.com.br")

    elif vestibular_meio == "INSPER 2026/2":
        st.markdown("## 🏦 INSPER 2026/2")
        st.markdown("---")
        render_cronograma([
            ("Inscrições", "Até 13/05", False),
            ("Prova", "07/06", False),
        ], site="insper.edu.br")

    elif vestibular_meio == "MAUÁ 2026/2":
        st.markdown("## ⚙️ MAUÁ 2026/2")
        st.markdown("---")
        st.markdown("🔗 **Site:** [maua.br](https://www.maua.br)")

    elif vestibular_meio == "FGV 2026/2":
        st.markdown("## 📊 FGV 2026/2")
        st.markdown("---")
        render_cronograma([
            ("Inscrições", "Até 27/04", False),
            ("Prova", "24/05", False),
        ], site="fgv.br")

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA: VOCÊ SABIA?
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "sabia":
    btn_voltar("home")
    st.markdown('<div class="main-title">💡 Você sabia?</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Recursos gratuitos e recomendações para turbinar seus estudos</div>', unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("**Estratégia Vestibulares**")
            st.link_button("Acessar simulados", "https://vestibulares.estrategia.com/instituicao/cursos/simulados-gratuitos", use_container_width=True)

        with st.container(border=True):
            st.markdown("**Objetivo**")
            st.link_button("Acessar simulados", "https://www.curso-objetivo.br/vestibular/simulados.aspx", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("**Etapa**")
            st.link_button("Acessar simulados", "https://etapa.com.br/home/apoio-ao-vestibulando/simulados", use_container_width=True)

        with st.container(border=True):
            st.markdown("**Poliedro / Poliedro Resolve**")
            st.link_button("Acessar Poliedro Resolve", "https://poliedroresolve.sistemapoliedro.com.br/", use_container_width=True)

    st.markdown("---")
    st.markdown("### 📱 O que seguir para se atualizar?")
    st.markdown("")

    _, b1, b2, b3, _ = st.columns([0.2, 2, 2, 2, 0.2])
    with b1:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        if st.button("📚 Organização", use_container_width=True):
            st.session_state.seguir_sub = "organizacao"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with b2:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        if st.button("📰 Atualidades", use_container_width=True):
            st.session_state.seguir_sub = "noticias"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with b3:
        st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
        if st.button("🧑‍🏫 Professores", use_container_width=True):
            st.session_state.seguir_sub = "professores"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    sub = st.session_state.get("seguir_sub", None)

    if sub == "organizacao":
        st.markdown("---")
        with st.expander("🎯 Estrategistas e Mentores", expanded=True):
            st.markdown("""
- **@sabrinaoliveira.vemed:** Mentoria para Medicina e estratégia de prova.
- **@viniciusdeoliiveira:** Técnicas de memorização.
""")

    elif sub == "noticias":
        st.markdown("---")
        with st.expander("📡 Curadoria de Notícias", expanded=True):
            st.markdown("""
- **@g1 (Educação):** Notícias do ENEM e vestibulares.
- **@jocacorreia:** Geopolítica e atualidades.
""")

    elif sub == "professores":
        st.markdown("---")
        with st.expander("✍️ Professores Referência", expanded=True):
            st.markdown("""
- **@professorapablina & @viniciusoliveirapro:** Redação.
- **@professorfredao:** TRI no ENEM.
""")
