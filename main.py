import streamlit as st
import random

# 🎨 웹앱 기본 설정
st.set_page_config(
    page_title="MBTI 직업 & 공부법 추천기 🎭💼📚",
    page_icon="🌟",
    layout="centered",
)

# 🌟 타이틀
st.markdown(
    """
    <h1 style='text-align: center; color: #ff69b4; font-size: 50px;'>🌈✨ MBTI로 알아보는 직업 & 공부법 💼📚</h1>
    <p style='text-align: center; font-size: 20px;'>당신의 MBTI를 선택하면 어울리는 직업과 공부 스타일을 알려드릴게요! 😍</p>
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

# 📚 MBTI별 공부법 설명
mbti_study_tips = {
    "INTJ": "📘 **계획적인 학습**을 좋아하며 목표 설정이 중요해요. 자기주도 학습이 강점이에요!",
    "INTP": "🔍 **호기심 중심의 학습**을 좋아해요. 깊이 파고드는 주제를 정해서 탐구하면 효과적이에요.",
    "ENTJ": "📈 **목표 달성형 학습**이 잘 맞아요. 성취감을 줄 수 있는 도전 과제를 활용해보세요.",
    "ENTP": "💡 **토론이나 아이디어 교환**을 통해 배우는 걸 좋아해요. 친구들과의 스터디 그룹이 효과적!",
    "INFJ": "🧘 **조용한 환경에서 몰입 학습**이 잘 맞아요. 정리된 필기와 마인드맵이 좋아요.",
    "INFP": "🎨 **감성적 연결**이 중요해요. 흥미로운 이야기나 사례로 학습을 연결해보세요.",
    "ENFJ": "💬 **사람과 함께 하는 학습**이 효과적이에요. 누군가에게 설명하면서 배우는 것도 좋아요.",
    "ENFP": "🌈 **재미있는 방식으로 배우는 것**이 중요해요. 영상, 게임, 이야기로 연결하세요!",
    "ISTJ": "📚 **정리된 학습자료**와 규칙적인 복습이 중요해요. 체크리스트를 만들어서 진행해보세요.",
    "ISFJ": "📝 **차분하고 꼼꼼한 학습**에 강해요. 요점 정리, 정리노트를 잘 활용하세요.",
    "ESTJ": "📊 **성과 중심의 학습**이 맞아요. 일정과 목표를 구체적으로 설정해보세요.",
    "ESFJ": "👩‍🏫 **협동 학습**이나 누군가를 도우며 배우는 게 잘 맞아요. 퀴즈나 팀플도 좋아요!",
    "ISTP": "🔧 **직접 실험하고 적용**하는 실용적인 학습이 효과적이에요. 프로젝트 기반 학습 추천!",
    "ISFP": "🎨 **감성적이고 시각적인 자극**이 도움이 돼요. 예쁜 노트나 색깔 정리도 좋아요.",
    "ESTP": "⚡ **동기부여가 강한 활동형 학습**에 잘 맞아요. 실습이나 퀴즈 방식도 좋아요!",
    "ESFP": "🎉 **즐겁고 활동적인 방식**이 좋아요. 다양한 형식의 콘텐츠로 배우면 좋아요!"
}

# 🌟 MBTI 선택 위젯
selected_mbti = st.selectbox("📌 나의 MBTI를 선택해주세요!", mbti_types, index=0)

# 🎁 추천 버튼
if st.button("✨ 직업 & 공부법 추천 받기!"):
    jobs = mbti_jobs.get(selected_mbti, [])
    study_tip = mbti_study_tips.get(selected_mbti, "학습 팁 정보를 찾을 수 없어요.")
    random.shuffle(jobs)
    
    st.markdown(
        f"""
        <h2 style='text-align: center; color: #00bfff;'>🎯 {selected_mbti} 에게 어울리는 직업은?</h2>
        <ul style='font-size: 22px; text-align: center; color: #444;'>{''.join(f'<li>{job}</li>' for job in jobs[:3])}</ul>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <h2 style='text-align: center; color: #ff7f50;'>📚 공부 스타일 & 팁</h2>
        <p style='text-align: center; font-size: 20px; color: #333;'>{study_tip}</p>
        """,
        unsafe_allow_html=True
    )

    st.balloons()

# 🔗 하단 안내
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 16px;'>이 웹앱은 진로 탐색을 돕기 위한 교육용 도구입니다 🎓<br>MBTI는 참고용이며, 직업과 공부 방식은 다양한 요소를 고려해 주세요 🌱</p>
    """,
    unsafe_allow_html=True
)
