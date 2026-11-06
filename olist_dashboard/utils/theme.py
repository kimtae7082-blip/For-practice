"""첨부 팔레트를 모든 페이지와 Plotly 차트에 적용합니다."""
import streamlit as st
import plotly.io as pio
import plotly.graph_objects as go

CREAM = "#FAF8F1"
YELLOW = "#FAEAB1"
TEAL = "#34656D"
INK = "#334443"

def apply_theme():
    pio.templates["olist"] = go.layout.Template(layout=go.Layout(
        paper_bgcolor=CREAM, plot_bgcolor=CREAM,
        font=dict(color=INK, family="Malgun Gothic, sans-serif", size=14),
        colorway=[TEAL, INK, YELLOW],
        colorscale=dict(sequential=[[0, CREAM], [0.4, YELLOW], [1, TEAL]]),
        xaxis=dict(gridcolor="#E4E5DC", zeroline=False),
        yaxis=dict(gridcolor="#E4E5DC", zeroline=False),
        margin=dict(t=64, b=48, l=48, r=32),
        title=dict(font=dict(size=21, color=INK)),
    ))
    pio.templates.default = "olist"
    st.html("""<style>
    .stApp { background: #FAF8F1; color: #334443; }
    .stMainBlockContainer { max-width: 1280px; padding-top: 2.5rem; padding-bottom: 4rem; }
    h1 { letter-spacing: -.04em; font-size: clamp(1.8rem, 3vw, 2.6rem) !important; }
    h2, h3 { letter-spacing: -.025em; }
    [data-testid="stSidebar"] { background: #334443; }
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] a,
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] span,
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] p,
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p { color: #FAF8F1; }
    [data-testid="stSidebarNav"] a:hover { background: #34656D; }
    [data-testid="stSidebarNav"] a[aria-current="page"] { background: #34656D; border-left: 4px solid #FAEAB1; }
    [data-testid="stSidebar"] [data-testid="stSlider"] { color: #FAEAB1; }
    [data-testid="stSidebar"] [data-testid="stSlider"] [data-testid*="TickBar"],
    [data-testid="stSidebar"] [data-testid="stSlider"] [data-testid*="ThumbValue"] { color: #FAEAB1 !important; }
    [data-testid="stMetric"] { background: white; border: 1px solid #E4E5DC;
        border-top: 4px solid #34656D; border-radius: 14px; padding: 20px; height: 100%; }
    [data-testid="stMetricValue"] { font-size: clamp(1.4rem, 2.4vw, 2.1rem); color: #34656D; }
    [data-testid="stMetricLabel"] { color: #334443; }
    [data-testid="stAlertContainer"]:has([data-testid="stAlertContentInfo"]),
    [data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]) { background: #FAEAB1; color: #334443; }
    [data-testid="stAlertContentInfo"] *, [data-testid="stAlertContentSuccess"] * { color: #334443 !important; }
    [data-testid="stCaptionContainer"] { color: #526462; }
    .stButton > button, .stDownloadButton > button { border-radius: 9px; min-height: 44px; }
    [data-testid="stTabs"] button[aria-selected="true"] { color: #34656D; font-weight: 700; }
    [data-testid="stDataFrame"], [data-testid="stExpander"] { border-radius: 12px; overflow: hidden; }
    .olist-hero { background: #34656D; color: #FAF8F1; border-radius: 20px;
        padding: 32px; margin-bottom: 26px; }
    .olist-hero .eyebrow { color: #FAEAB1; font-size: 13px; letter-spacing: .15em; font-weight: 700; }
    .olist-hero h2 { color: #FAF8F1 !important; margin: 12px 0; font-size: 30px; }
    .olist-hero p { color: #FAF8F1; line-height: 1.8; margin-bottom: 0; }
    .olist-note { background: #FAEAB1; color: #334443; border-radius: 12px; padding: 16px 20px; margin: 20px 0; }
    @media (max-width: 640px) { .olist-hero { padding: 22px; } .stMainBlockContainer { padding-top: 1.5rem; } }
    </style>""")
