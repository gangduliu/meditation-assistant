import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Meditation & Mindfulness Assistant",
    page_icon="🧘",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS Styles
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

# Sidebar: Tools & Information
st.sidebar.title("🧘 Meditation Assistant")
st.sidebar.markdown("---")
st.sidebar.info("💡 Close your eyes, adjust your breathing, and give yourself a few minutes of peace.")

with st.sidebar:
    st.markdown("### 🌐 Source Code")
    st.markdown(
        """
        <div style="margin-bottom: 12px;">
            <a href="https://github.com/gangduliu/meditation-assistant" target="_blank" style="text-decoration: none;">
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
            <p style="font-size: 0.85rem; opacity: 0.8; margin-bottom: 10px;">If this meditation tool has been helpful to you, feel free to buy me a lime! 🍋‍🟩</p>
            <a href="https://buymeacoffee.com/qingning618" target="_blank">
                <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a lime&emoji=🍋‍🟩&slug=qingning618&button_colour=0F766E&font_colour=ffffff&font_family=Inter&outline_colour=ffffff&coffee_colour=FFDD00" style="width: 100%;" alt="Buy Me A Lime">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==================== Core Module: Breathing Guide ====================
st.title("✨ Breathing & Mindfulness")
st.write(
    "The 4-7-8 breathing technique effectively relieves anxiety and relaxes the nervous system. Follow the prompts below to regulate your breathing rhythm:"
)
st.markdown(
    "- **Inhale** for 4 seconds\n"
    "- **Hold** for 7 seconds\n"
    "- **Exhale** for 8 seconds"
)

col1, col2 = st.columns(2)
with col1:
    start_btn = st.button("Start Breathing Exercise")
with col2:
    stop_btn = st.button("Stop")

placeholder = st.empty()

if "breathing_active" not in st.session_state:
    st.session_state.breathing_active = False

if start_btn:
    st.session_state.breathing_active = True

if stop_btn:
    st.session_state.breathing_active = False

if st.session_state.breathing_active:
    cycles = 3  # Demo 3 cycles
    for i in range(cycles):
        if not st.session_state.breathing_active:
            break
        # Inhale
        for t in range(4, 0, -1):
            placeholder.markdown(
                f"""
                <div class="breathing-box" style="background-color: #D1E7DD;">
                    🌱 Inhaling... ({t}s)
                </div>
                """,
                unsafe_allow_html=True,
            )
            time.sleep(1)
        # Hold
        for t in range(7, 0, -1):
            placeholder.markdown(
                f"""
                <div class="breathing-box" style="background-color: #CFE2FF;">
                    🌿 Holding breath... ({t}s)
                </div>
                """,
                unsafe_allow_html=True,
            )
            time.sleep(1)
        # Exhale
        for t in range(8, 0, -1):
            placeholder.markdown(
                f"""
                <div class="breathing-box" style="background-color: #F8D7DA;">
                    🍃 Exhaling slowly... ({t}s)
                </div>
                """,
                unsafe_allow_html=True,
            )
            time.sleep(1)

    placeholder.markdown(
        """
        <div class="breathing-box" style="background-color: #E8F0EC;">
            ✨ Exercise complete. Embrace the inner peace.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.session_state.breathing_active = False