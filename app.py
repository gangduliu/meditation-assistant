import time
import streamlit as st

# 页面基本配置
st.set_page_config(
    page_title="心灵之港 - 冥想与正念助手",
    page_icon="🧘",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 自定义 CSS 样式
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #0F766E;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #115E59;
        color: white;
    }
    .breathing-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 180px;
        font-size: 24px;
        font-weight: bold;
        color: #2F4F4F;
        background-color: #E8F0EC;
        border-radius: 15px;
        margin-bottom: 20px;
        transition: all 1s ease-in-out;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 侧边栏：工具选择
st.sidebar.title("🧘 冥想助手")
st.sidebar.markdown("---")
st.sidebar.info("💡 闭上眼睛，调整呼吸，给自己留出几分钟的平静时光。")

with st.sidebar:
    st.markdown("### 🌐 Source Code")
    st.markdown(
        """
        <div style="margin-bottom: 12px;">
            <a href="https://github.com/gangduliu/us-etf-dashboard" target="_blank" style="text-decoration: none;">
                <div style="background-color: var(--secondary-background-color); border: 1px solid var(--border-color); border-radius: 8px; padding: 10px 14px; text-align: center; color: var(--text-color); font-weight: 600; font-size: 0.9rem; transition: all 0.2s;">
                    ⭐ GitHub Repository
                </div>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🍋‍🟩 Support the Author")
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 10px;">
            <p style="font-size: 0.85rem; opacity: 0.8; margin-bottom: 10px;">If this dashboard has been helpful to you, feel free to buy me a lime! 🍋‍🟩</p>
            <a href="https://buymeacoffee.com/qingning618" target="_blank">
                <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a lime&emoji=🍋‍🟩&slug=qingning618&button_colour=0F766E&font_colour=ffffff&font_family=Inter&outline_colour=ffffff&coffee_colour=FFDD00" style="width: 100%;" alt="Buy Me A Lime">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==================== 核心模块：呼吸引导 ====================
st.title("✨ 呼吸与正念调息")
st.write(
    "4-7-8 呼吸法可以有效缓解焦虑、放松神经。跟随下方的文字提示调整呼吸节奏："
)
st.markdown("- **吸气** 4 秒\n- **屏气** 7 秒\n- **呼气** 8 秒")

col1, col2 = st.columns(2)
with col1:
    start_btn = st.button("开始呼吸训练")
with col2:
    stop_btn = st.button("停止")

placeholder = st.empty()

if "breathing_active" not in st.session_state:
    st.session_state.breathing_active = False

if start_btn:
    st.session_state.breathing_active = True

if stop_btn:
    st.session_state.breathing_active = False

if st.session_state.breathing_active:
    cycles = 3  # 演示 3 个循环
    for i in range(cycles):
        if not st.session_state.breathing_active:
            break
        # 吸气
        for t in range(4, 0, -1):
            placeholder.markdown(
                f"""
                <div class="breathing-box" style="background-color: #D1E7DD;">
                    🌱 请吸气... ({t}s)
                </div>
                """,
                unsafe_allow_html=True,
            )
            time.sleep(1)
        # 屏气
        for t in range(7, 0, -1):
            placeholder.markdown(
                f"""
                <div class="breathing-box" style="background-color: #CFE2FF;">
                    🌿 保持屏气... ({t}s)
                </div>
                """,
                unsafe_allow_html=True,
            )
            time.sleep(1)
        # 呼气
        for t in range(8, 0, -1):
            placeholder.markdown(
                f"""
                <div class="breathing-box" style="background-color: #F8D7DA;">
                    🍃 缓慢呼气... ({t}s)
                </div>
                """,
                unsafe_allow_html=True,
            )
            time.sleep(1)

    placeholder.markdown(
        """
        <div class="breathing-box" style="background-color: #E8F0EC;">
            ✨ 训练完成，感受内心的宁静。
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.session_state.breathing_active = False