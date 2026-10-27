
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Spotify Trends Analytics",
    page_icon="🎵",
    layout="wide"
)

ROXO = "#7651A8"
VERDE = "#45B69C"

st.markdown("""
<style>
.stApp { background-color: #FAF8FC; }
h1, h2, h3 { color: #7651A8; }
[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E9E1F2;
    padding: 16px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

pasta = Path(__file__).parent
opcoes_csv = [
    pasta / "spotify_dashboard.csv",
    pasta / "data" / "spotify_dashboard.csv"
]
arquivo_csv = next((p for p in opcoes_csv if p.exists()), None)

st.title("🎵 Spotify Trends Analytics")
st.caption("Evolução das características musicais por década")

if arquivo_csv is None:
    st.error("Não encontrei spotify_dashboard.csv. Coloque o arquivo na raiz do repositório ou na pasta data.")
    st.stop()

@st.cache_data
def carregar_dados(caminho):
    df = pd.read_csv(caminho)
    df["ano_lancamento"] = pd.to_numeric(df["ano_lancamento"], errors="coerce")
    df["decada"] = pd.to_numeric(df["decada"], errors="coerce")
    df["duracao_min"] = df["duration_ms"] / 60000
    df["explicit"] = (
        df["explicit"].astype(str).str.lower()
        .map({"true": True, "false": False, "1": True, "0": False})
    )
    return df

df = carregar_dados(str(arquivo_csv))

st.sidebar.header("Filtros")

generos = sorted(df["track_genre"].dropna().unique().tolist())
generos_escolhidos = st.sidebar.multiselect(
    "Gêneros musicais", generos, default=generos
)

decadas = sorted(df["decada"].dropna().astype(int).unique().tolist())
decadas_escolhidas = st.sidebar.multiselect(
    "Décadas de lançamento", decadas, default=decadas
)

df_generos = df[df["track_genre"].isin(generos_escolhidos)].copy()
df_analise = df_generos[
    df_generos["decada"].isin(decadas_escolhidas)
].copy()

if df_analise.empty:
    st.warning("Nenhum registro encontrado. Ajuste os filtros.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Registros", f"{len(df_generos):,}".replace(",", "."))
c2.metric(
    "Músicas com ano",
    f"{df_generos.loc[df_generos['ano_lancamento'].notna(), 'track_id'].nunique():,}".replace(",", ".")
)
c3.metric("Gêneros", df_generos["track_genre"].nunique())
c4.metric("Popularidade média", f"{df_analise['popularity'].mean():.1f}")

resumo = df_analise.groupby("decada", as_index=False).agg(
    popularidade_media=("popularity", "mean"),
    energia_media=("energy", "mean"),
    dancabilidade_media=("danceability", "mean"),
    duracao_media=("duracao_min", "mean"),
    percentual_explicitas=("explicit", "mean"),
    quantidade=("track_id", "size")
).sort_values("decada")

resumo["decada_label"] = resumo["decada"].astype(int).astype(str) + "s"
resumo["percentual_explicitas"] *= 100

st.subheader("Popularidade média por década")
fig1 = px.bar(
    resumo, x="decada_label", y="popularidade_media",
    labels={"decada_label": "Década", "popularidade_media": "Popularidade média"},
    color_discrete_sequence=[ROXO]
)
st.plotly_chart(fig1, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Energia média")
    fig2 = px.line(
        resumo, x="decada_label", y="energia_media", markers=True,
        labels={"decada_label": "Década", "energia_media": "Energia média"},
        color_discrete_sequence=[VERDE]
    )
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.subheader("Dançabilidade média")
    fig3 = px.bar(
        resumo, x="decada_label", y="dancabilidade_media",
        labels={"decada_label": "Década", "dancabilidade_media": "Dançabilidade média"},
        color_discrete_sequence=[ROXO]
    )
    st.plotly_chart(fig3, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Duração média das músicas")
    fig4 = px.line(
        resumo, x="decada_label", y="duracao_media", markers=True,
        labels={"decada_label": "Década", "duracao_media": "Duração média (minutos)"},
        color_discrete_sequence=[VERDE]
    )
    st.plotly_chart(fig4, use_container_width=True)

with col4:
    st.subheader("Músicas explícitas por década")
    fig5 = px.bar(
        resumo, x="decada_label", y="percentual_explicitas",
        labels={"decada_label": "Década", "percentual_explicitas": "Músicas explícitas (%)"},
        color_discrete_sequence=[ROXO]
    )
    st.plotly_chart(fig5, use_container_width=True)

st.subheader("Resumo por década")
st.dataframe(resumo.drop(columns=["decada_label"]), use_container_width=True, hide_index=True)

with st.expander("Metodologia e limitações"):
    st.markdown("""
    - A base principal contém características musicais e gêneros de faixas do Spotify.
    - Os dados foram tratados para remover registros repetidos e lidar com valores ausentes.
    - As datas de lançamento foram complementadas com uma segunda base.
    - Nem todas as faixas possuem ano identificado; as análises por década consideram apenas as datas disponíveis.
    - A popularidade representa uma medida atual do Spotify, não a popularidade histórica na época do lançamento.
    - As décadas antigas têm menos registros e os anos 2020 estão representados parcialmente.
    """)

st.caption("Projeto acadêmico de Big Data — Spotify Trends Analytics")
