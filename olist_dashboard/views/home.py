"""Olist 대시보드 시작 화면."""
import streamlit as st
from utils.data import load_data

st.html("""<section class="olist-hero">
<div class="eyebrow">OLIST / DATA & AI</div>
<h2>주문 데이터에서<br>다음 의사결정까지</h2>
<p>브라질 이커머스 주문 흐름을 살펴보고,<br>리뷰 · 상품 · 판매자 데이터를 AI 모델로 탐색하세요.</p>
</section>""")
orders, _ = load_data()
c1, c2, c3 = st.columns(3)
c1.metric("분석 대상 주문", f"{len(orders):,}건")
c2.metric("실습 AI 모델", "4개")
c3.metric("탐색 화면", "7개")
st.html('<div class="olist-note">처음이라면 <strong>데이터 분석 → AI 모델 → 분석 Q&A</strong> 순서로 살펴보세요.</div>')
st.subheader("무엇을 살펴볼까요?")
pages = [
    ("views/analysis.py", "데이터 분석", "📊", "지역과 기간을 골라 매출, 배송, 리뷰를 비교합니다."),
    ("views/sentiment.py", "리뷰 감성 분석", "💬", "포르투갈어 리뷰의 긍정·부정 확률을 확인합니다."),
    ("views/recommend.py", "상품 추천", "🛍️", "같은 카테고리에서 특징이 비슷한 상품을 찾습니다."),
    ("views/segment.py", "판매자 유형", "🏪", "주문·판매액·활동 기간으로 판매자 유형을 살펴봅니다."),
    ("views/churn.py", "판매자 이탈 위험", "🚨", "이탈 확률과 예상 손실로 관리 우선순위를 비교합니다."),
    ("views/qa.py", "분석 Q&A", "🤖", "분석 자료에 질문하고 답변의 근거를 확인합니다."),
]
for start in range(0, len(pages), 2):
    for col, (path, label, icon, description) in zip(st.columns(2), pages[start:start+2]):
        with col.container(border=True):
            st.page_link(path, label=label, icon=icon)
            st.write(description)
st.caption("학습용 과거 데이터와 모델입니다. 예측 결과는 실제 사실과 구분하고 근거를 확인하세요.")
