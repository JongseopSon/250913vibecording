import streamlit as st
import random

# BTS 멤버 데이터 (인터넷 이미지 URL 사용 예시)
bts_members = [
    {"name": "RM", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3e/RM_for_Dispatch_%28cropped%29.jpg"},
    {"name": "Jin", "img": "https://upload.wikimedia.org/wikipedia/commons/5/57/Jin_for_Dispatch_%28cropped%29.jpg"},
    {"name": "Suga", "img": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Suga_for_Dispatch_%28cropped%29.jpg"},
    {"name": "J-Hope", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3d/J-Hope_for_Dispatch_%28cropped%29.jpg"},
    {"name": "Jimin", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Jimin_for_Dispatch_%28cropped%29.jpg"},
    {"name": "V", "img": "https://upload.wikimedia.org/wikipedia/commons/6/6b/V_for_Dispatch_%28cropped%29.jpg"},
    {"name": "Jungkook", "img": "https://upload.wikimedia.org/wikipedia/commons/8/87/Jungkook_for_Dispatch_%28cropped%29.jpg"}
]

# 세션 상태 초기화
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.players = random.sample(bts_members, len(bts_members))  # 랜덤 섞기
    st.session_state.winners = []

st.title("🔥 BTS 이상형 월드컵 🔥")

st.write(f"현재 라운드 {st.session_state.round}")

if len(st.session_state.players) >= 2:
    # 두 명씩 비교
    p1, p2 = st.session_state.players[0], st.session_state.players[1]

    col1, col2 = st.columns(2)

    with col1:
        st.image(p1["img"], caption=p1["name"], use_container_width=True)
        if st.button(f"{p1['name']} 선택"):
            st.session_state.winners.append(p1)
            st.session_state.players = st.session_state.players[2:]

    with col2:
        st.image(p2["img"], caption=p2["name"], use_container_width=True)
        if st.button(f"{p2['name']} 선택"):
            st.session_state.winners.append(p2)
            st.session_state.players = st.session_state.players[2:]

else:
    # 라운드 종료 → 다음 라운드 세팅
    if len(st.session_state.winners) == 1:
        # 최종 우승자
        winner = st.session_state.winners[0]
        st.success(f"🏆 최종 우승자는 {winner['name']} !!!")
        st.image(winner["img"], caption=winner["name"], use_container_width=True)
        if st.button("다시하기"):
            st.session_state.round = 1
            st.session_state.players = random.sample(bts_members, len(bts_members))
            st.session_state.winners = []
    else:
        st.session_state.players = st.session_state.winners
        st.session_state.winners = []
        st.session_state.round += 1
        st.experimental_rerun()
