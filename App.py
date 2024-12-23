import streamlit as st
from streamlit_option_menu import option_menu  # Install: pip install streamlit-option-menu

# Configure the page
st.set_page_config(page_title="Enhanced Streamlit Demo", page_icon="🌟", layout="wide")

# Sidebar header with shadow box style
st.sidebar.markdown(
    """
    <div style="background-color: #FFA421; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);">
        <h2 style="color: white; margin: 0;">🌟 Enhanced Demo</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar menu for navigation
selected_page = option_menu(
    menu_title=None,
    options=["🏠 Home", "📈 Analytics", "📂 Reports", "⚙️ Settings", "📜 About"],
    icons=["house", "bar-chart", "folder", "gear", "book"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical",
    styles={
        "container": {"padding": "5px", "background-color": "#282828"},
        "icon": {"color": "#FFA421", "font-size": "25px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "10px 0",
            "border-radius": "10px",
            "padding": "15px",
            "background-color": "rgba(255, 164, 33, 0.2)",
            "color": "#FFFFFF",
        },
        "nav-link-selected": {"background-color": "#FFA421", "color": "black"},
    },
)

# Subpage tabs for each main menu item
if selected_page == "🏠 Home":
    with st.sidebar:
        st.markdown("### 🏠 Home")
    tabs = st.tabs(["Getting Started 🛠️", "Overview 🌟"])
    if tabs[0].selected:
        st.title("🏠 Home - Getting Started")
        st.write("Details about how to get started.")
    elif tabs[1].selected:
        st.title("🏠 Home - Overview")
        st.write("Overview of the application.")

elif selected_page == "📈 Analytics":
    with st.sidebar:
        st.markdown("### 📈 Analytics")
    tabs = st.tabs(["Charts 📊", "Insights 🔍"])
    if tabs[0].selected:
        st.title("📈 Analytics - Charts")
        st.write("Details about analytics charts.")
    elif tabs[1].selected:
        st.title("📈 Analytics - Insights")
        st.write("Details about analytics insights.")

elif selected_page == "📂 Reports":
    with st.sidebar:
        st.markdown("### 📂 Reports")
    tabs = st.tabs(["Create 📄", "Manage 🗂️"])
    if tabs[0].selected:
        st.title("📂 Reports - Create")
        st.write("Details about creating reports.")
    elif tabs[1].selected:
        st.title("📂 Reports - Manage")
        st.write("Details about managing reports.")

elif selected_page == "⚙️ Settings":
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
    tabs = st.tabs(["Preferences ⚙️", "Tools 🔧"])
    if tabs[0].selected:
        st.title("⚙️ Settings - Preferences")
        st.write("Details about preferences.")
    elif tabs[1].selected:
        st.title("⚙️ Settings - Tools")
        st.write("Details about settings tools.")

elif selected_page == "📜 About":
    with st.sidebar:
        st.markdown("### 📜 About")
    tabs = st.tabs(["Credits 📜", "Features 🌟"])
    if tabs[0].selected:
        st.title("📜 About - Credits")
        st.write("Details about the app credits.")
    elif tabs[1].selected:
        st.title("📜 About - Features")
        st.write("Details about the app features.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 Enhanced Streamlit Demo App. All rights reserved.")






