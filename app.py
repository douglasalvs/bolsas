import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="BolsaStore PRO",
    page_icon="👜",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "bolsas.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1584917865442-de89df76afd3"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_FROTA = (
    "https://images.unsplash.com/"
    "photo-1594223274512-ad4803739b7c"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        linear-gradient(
            135deg,
            #F5EFE8 0%,
            #E8D8C8 50%,
            #D8C2AD 100%
        );
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #38251F,
            #56382E
        );
    border-right: 2px solid #C49A6C;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #E7C9A9 !important;
    letter-spacing: 1px;
}

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #38251F !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #654B3D !important;
    margin-bottom: 30px;
}

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;
    background-size: cover;
    background-position: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.22);
}

.hero-overlay {
    position: absolute;
    inset: 0;
    background:
        linear-gradient(
            90deg,
            rgba(45,28,23,0.97) 0%,
            rgba(45,28,23,0.86) 45%,
            rgba(45,28,23,0.15) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;
    transform: translateY(-50%);
    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #E3B887 !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #F5EDE5 !important;
    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;
    margin-top: 24px;
    padding: 10px 22px;
    border-radius: 30px;
    background: #A66A3F;
    color: #FFFFFF !important;
    font-size: 14px;
    font-weight: 700;
}

.info-card {
    background: #FFFFFF;
    border-radius: 22px;
    padding: 28px;
    min-height: 170px;
    border: 1px solid rgba(166,106,63,0.30);
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;
    color: #38251F !important;
    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;
    color: #705648 !important;
    margin-top: 5px;
}

.dark-card {
    background:
        linear-gradient(
            135deg,
            #38251F,
            #624236
        );
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #F0E2D7 !important;
    line-height: 1.7;
}

[data-testid="stForm"] {
    background: rgba(255,255,255,0.88);
    padding: 30px;
    border-radius: 25px;
    border: 1px solid #CBAF91;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #38251F !important;
    opacity: 1 !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #30231E !important;
    -webkit-text-fill-color: #30231E !important;
    border: 2px solid #A98265 !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border: 2px solid #8B5738 !important;
    box-shadow: 0 0 0 3px rgba(139,87,56,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #74675F !important;
    opacity: 1 !important;
}

[data-baseweb="select"] > div {
    background-color: #3D302B !important;
    border: 2px solid #A98265 !important;
    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"] {
    background-color: #3D302B !important;
}

[role="option"] {
    background-color: #3D302B !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #76513D !important;
    color: #FFFFFF !important;
}

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #8B5738,
            #B27A52
        ) !important;

    color: #FFFFFF !important;
    border: none !important;
    border-radius: 14px !important;
    min-height: 54px;
    font-family: 'Poppins', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    box-shadow: 0 8px 18px rgba(139,87,56,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #704329,
            #96623F
        ) !important;
    color: #FFFFFF !important;
    transform: translateY(-1px);
}

[data-testid="stDataFrame"] {
    background: #FFFFFF;
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid #CBAF91;
}

.footer {
    margin-top: 50px;
    text-align: center;
    color: #705648 !important;
    font-size: 14px;
    font-weight: 600;
}

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Marca",
        "Modelo",
        "Categoria",
        "Ano",
        "Cor",
        "Material",
        "Código",
        "Quantidade",
        "Valor",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:
            return pd.read_csv(ARQUIVO)

        except Exception:
            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()

colunas_necessarias = [
    "Marca",
    "Modelo",
    "Categoria",
    "Ano",
    "Cor",
    "Material",
    "Código",
    "Quantidade",
    "Valor",
    "Observações"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:
        df[coluna] = ""


df["Valor"] = pd.to_numeric(
    df["Valor"],
    errors="coerce"
).fillna(0)

df["Quantidade"] = pd.to_numeric(
    df["Quantidade"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
👜 BolsaStore
</div>

<div class="logo-subtitle">
GESTÃO INTELIGENTE DE BOLSAS
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Bolsa",
        "👜 Bolsas Cadastradas"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "BolsaStore PRO • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Sua coleção.<br>
Seu estilo.
</div>

<div class="hero-text">
Tenha todas as suas bolsas organizadas em um único lugar.
Cadastre, consulte e acompanhe seu estoque de forma simples,
rápida e profissional.
</div>

<div class="hero-badge">
👜 GESTÃO INTELIGENTE
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
"""
<div class="page-title">
📊 Visão geral da sua coleção
</div>

<div class="page-subtitle">
Acompanhe suas bolsas e mantenha seu estoque organizado.
</div>
""",
        unsafe_allow_html=True
    )

    total_bolsas = int(df["Quantidade"].sum())

    valor_total = (
        df["Valor"] * df["Quantidade"]
    ).sum()

    modelos = len(df)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
👜
</div>

<div class="card-number">
{total_bolsas}
</div>

<div class="card-label">
BOLSAS EM ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💰
</div>

<div class="card-number">
R$ {valor_total:,.2f}
</div>

<div class="card-label">
VALOR TOTAL DO ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
✨
</div>

<div class="card-number">
{modelos}
</div>

<div class="card-label">
MODELOS CADASTRADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    coluna1, coluna2 = st.columns([1.1, 1])

    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
✨ Controle profissional
</h2>

<p>
A BolsaStore PRO permite manter todas as suas bolsas
organizadas em um único lugar.
</p>

<p>
Cadastre modelos, consulte o estoque, pesquise produtos
e acompanhe o valor da sua coleção de maneira moderna
e profissional.
</p>

</div>
""",
            unsafe_allow_html=True
        )

    with coluna2:

        st.image(
            IMAGEM_FROTA,
            use_container_width=True
        )


# =========================================================
# CADASTRAR BOLSA
# =========================================================

elif menu == "➕ Cadastrar Bolsa":

    st.markdown(
"""
<div class="page-title">
➕ Nova bolsa
</div>

<div class="page-subtitle">
Adicione uma nova bolsa ao seu estoque.
</div>
""",
        unsafe_allow_html=True
    )

    with st.form(
        "cadastro_bolsa",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)

        with col1:

            marca = st.text_input(
                "🏷️ Marca"
            )

            modelo = st.text_input(
                "👜 Modelo"
            )

            categoria = st.selectbox(
                "🛍️ Categoria",
                [
                    "Bolsa de Ombro",
                    "Bolsa Transversal",
                    "Bolsa de Mão",
                    "Mochila",
                    "Clutch",
                    "Bolsa Tote",
                    "Bolsa Pequena",
                    "Carteira",
                    "Outro"
                ]
            )

            ano = st.number_input(
                "📅 Ano",
                min_value=1900,
                max_value=2035,
                value=2026,
                step=1
            )

            cor = st.selectbox(
                "🎨 Cor",
                [
                    "Preto",
                    "Branco",
                    "Bege",
                    "Marrom",
                    "Caramelo",
                    "Vermelho",
                    "Rosa",
                    "Azul",
                    "Verde",
                    "Dourado",
                    "Prata",
                    "Outro"
                ]
            )

        with col2:

            material = st.selectbox(
                "🧵 Material",
                [
                    "Couro",
                    "Couro Sintético",
                    "Tecido",
                    "Nylon",
                    "Camurça",
                    "Palha",
                    "Lona",
                    "Outro"
                ]
            )

            codigo = st.text_input(
                "🔢 Código do Produto"
            )

            quantidade = st.number_input(
                "📦 Quantidade em Estoque",
                min_value=0,
                value=1,
                step=1
            )

            valor = st.number_input(
                "💰 Valor da Bolsa",
                min_value=0.0,
                value=0.0,
                step=50.0
            )

            observacoes = st.text_area(
                "📝 Observações"
            )

        cadastrar = st.form_submit_button(
            "💾 CADASTRAR BOLSA"
        )

    if cadastrar:

        if (
            marca.strip()
            and modelo.strip()
            and codigo.strip()
        ):

            nova_bolsa = pd.DataFrame(
                [{
                    "Marca": marca.strip(),
                    "Modelo": modelo.strip(),
                    "Categoria": categoria,
                    "Ano": int(ano),
                    "Cor": cor,
                    "Material": material,
                    "Código": codigo.strip().upper(),
                    "Quantidade": int(quantidade),
                    "Valor": float(valor),
                    "Observações": observacoes.strip()
                }]
            )

            df = pd.concat(
                [
                    df,
                    nova_bolsa
                ],
                ignore_index=True
            )

            salvar_dados(df)

            st.success(
                "👜 Bolsa cadastrada com sucesso!"
            )

            st.rerun()

        else:

            st.warning(
                "⚠️ Preencha Marca, Modelo e Código."
            )


# =========================================================
# BOLSAS CADASTRADAS
# =========================================================

elif menu == "👜 Bolsas Cadastradas":

    st.markdown(
"""
<div class="page-title">
👜 Minha coleção
</div>

<div class="page-subtitle">
Consulte e pesquise todas as bolsas cadastradas.
</div>
""",
        unsafe_allow_html=True
    )

    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
👜 Nenhuma bolsa cadastrada
</h2>

<p>
Seu estoque ainda está vazio.
Cadastre sua primeira bolsa para começar.
</p>

</div>
""",
            unsafe_allow_html=True
        )

    else:

        busca = st.text_input(
            "🔎 Pesquisar bolsa",
            placeholder="Digite marca, modelo, código, categoria ou cor..."
        )

        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df

        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        opcoes_bolsas = df.index.tolist()

        bolsa_excluir = st.selectbox(
            "🗑️ Selecione uma bolsa para excluir",
            options=opcoes_bolsas,
            format_func=lambda indice:
                f"{df.loc[indice, 'Marca']} "
                f"{df.loc[indice, 'Modelo']} - "
                f"{df.loc[indice, 'Código']}"
        )

        if st.button(
            "🗑️ EXCLUIR BOLSA"
        ):

            df = df.drop(
                bolsa_excluir
            )

            df = df.reset_index(
                drop=True
            )

            salvar_dados(df)

            st.success(
                "👜 Bolsa excluída com sucesso!"
            )

            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

👜 BolsaStore PRO<br>
Gestão inteligente de bolsas

</div>
""",
    unsafe_allow_html=True
)
