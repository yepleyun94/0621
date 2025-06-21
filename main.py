import streamlit as st
import random

# 🎨 웹앱 기본 설정
st.set_page_config(
    page_title="MBTI 직업 추천기 🎭💼",
    page_icon="🌟",
    layout="centered",
)

# 🌟 타이틀
st.markdown(
    """
    <h1 style='text-align: center; color: #ff69b4; font-size: 50px;'>🌈✨ MBTI로 알아보는 직업 추천 💼🔮</h1>
    <p style='text-align: center; font-size: 20px;'>당신의 MBTI를 선택하면 어울리는 직업을 알려드릴게요! 😍</p>
    """,
    unsafe_allow_html=True
)

# 🎭 MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 💼 MBTI별 직업 추천 딕셔너리
mbti_jobs = {
    "INTJ": ["🧠 데이터 과학자", "📊 전략 컨설턴트", "💼 CEO", "👨‍💻 인공지능 전문가"],
    "INTP": ["🔬 연구원", "👨‍💻 개발자", "📚 철학자", "📈 시스템 설계자"],
    "ENTJ": ["💼 경영 컨설턴트", "🧑‍💼 관리자", "📊 투자 분석가", "🧑‍⚖️ 변호사"],
    "ENTP": ["📣 마케팅 전문가", "🧪 발명가", "💻 UX 디자이너", "🎤 크리에이터"],
    "INFJ": ["💖 상담사", "📚 작가", "🌱 사회운동가", "🎨 아티스트"],
    "INFP": ["🎨 일러스트레이터", "🎼 음악가", "📖 시인", "🌈 콘텐츠 제작자"],
    "ENFJ": ["🧑‍🏫 교사", "💞 심리상담사", "🌟 연예기획자", "📢 캠페이너"],
    "ENFP": ["🎬 영화감독", "🌍 여행가", "🎤 유튜버", "🎭 배우"],
    "ISTJ": ["🧾 회계사", "📚 사서", "⚖️ 법률 전문가", "🧑‍💻 관리자"],
    "ISFJ": ["🧑‍⚕️ 간호사", "🏥 의료보조", "🍽️ 셰프", "📦 창고 관리자"],
    "ESTJ": ["📈 관리자", "🚔 경찰", "🧾 세무사", "🏛️ 공무원"],
    "ESFJ": ["🏫 교사", "🎁 이벤트 코디네이터", "🍰 베이커", "🛍️ 쇼핑몰 운영자"],
    "ISTP": ["🛠️ 기술자", "🚗 자동차 정비사", "🔧 기계공", "🎮 게임 개발자"],
    "ISFP": ["🎨 디자이너", "📸 사진작가", "🧵 패션디자이너", "🎶 작곡가"],
    "ESTP": ["🚀 스타트업 창업자", "📣 세일즈", "🏋️‍♂️ 트레이너", "🎮 게임 스트리머"],
    "ESFP": ["🎤 가수", "🎉 MC", "💃 댄서", "📺 방송인"]
}

# 🌟 MBTI 선택 위젯
selected_mbti = st.selectbox("📌 나의 MBTI를 선택해주세요!", mbti_types, index=0)

# 🎁 추천 버튼
if st.button("✨ 직업 추천 받기! 💼"):
    jobs = mbti_jobs.get(selected_mbti, [])
    random.shuffle(jobs)
    st.markdown(
        f"""
        <h2 style='text-align: center; color: #00bfff;'>🎉 {selected_mbti} 에게 어울리는 직업은?!</h2>
        <ul style='font-size: 22px; text-align: center; color: #444;'>{''.join(f'<li>{job}</li>' for job in jobs[:3])}</ul>
        """,
        unsafe_allow_html=True
    )
    st.balloons()

# 🔗 하단 안내
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 16px;'>이 웹앱은 진로 탐색을 돕기 위한 교육용 도구입니다 🎓<br>MBTI는 참고용이며, 직업 선택은 다양한 요소를 고려해 주세요 🌱</p>
    """,
    unsafe_allow_html=True
)
