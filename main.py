import streamlit as st
import pandas as pd
import altair as alt

st.title("🌍 국가별 MBTI 유형 분포 분석")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 데이터 구조 변환 (Country, MBTI, Proportion)
df_melted = df.melt(id_vars="Country", var_name="MBTI", value_name="Proportion")

# -------------------------------
# 1. 특정 국가 MBTI 비율 시각화
# -------------------------------
st.subheader("국가별 MBTI 비율 확인")

country = st.selectbox("국가를 선택하세요", df["Country"].unique())
country_data = df_melted[df_melted["Country"] == country]

chart_country = (
    alt.Chart(country_data)
    .mark_bar()
    .encode(
        x=alt.X("MBTI:N", title="MBTI 유형"),
        y=alt.Y("Proportion:Q", title="비율"),
        color="MBTI:N",
        tooltip=["Country", "MBTI", "Proportion"]
    )
    .properties(width=700, height=400, title=f"{country} MBTI 유형별 분포")
    .interactive()
)

st.altair_chart(chart_country, use_container_width=True)

# -------------------------------
# 2. 한국 vs 일본 비교
# -------------------------------
st.subheader("한국 vs 일본 MBTI 분포 비교")

compare_countries = df_melted[df_melted["Country"].isin(["South Korea", "Japan"])]

chart_compare = (
    alt.Chart(compare_countries)
    .mark_bar()
    .encode(
        x=alt.X("MBTI:N", title="MBTI 유형"),
        y=alt.Y("Proportion:Q", title="비율"),
        color="Country:N",
        column=alt.Column("MBTI:N", title="MBTI 유형"),
        tooltip=["Country", "MBTI", "Proportion"]
    )
    .properties(width=50, height=300, title="한국 vs 일본 MBTI 유형 비교")
)

st.altair_chart(chart_compare, use_container_width=True)
