import streamlit as st
import pandas as pd
import altair as alt

st.title("🌍 MBTI 유형별 비율 비교")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 데이터 구조 변환 (Country, MBTI, Proportion)
df_melted = df.melt(id_vars="Country", var_name="MBTI", value_name="Proportion")

# 국가 선택
country = st.selectbox("국가를 선택하세요", df["Country"].unique())

# 선택된 국가 데이터
country_data = df_melted[df_melted["Country"] == country]

# Altair 그래프
chart = (
    alt.Chart(country_data)
    .mark_bar()
    .encode(
        x=alt.X("MBTI:N", title="MBTI 유형"),
        y=alt.Y("Proportion:Q", title="비율"),
        color="MBTI:N",
        tooltip=["Country", "MBTI", "Proportion"]
    )
    .properties(width=700, height=400, title=f"{country}의 MBTI 유형별 비율")
    .interactive()
)

st.altair_chart(chart, use_container_width=True)
