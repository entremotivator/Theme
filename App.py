import streamlit as st
from streamlit_option_menu import option_menu  # Install: pip install streamlit-option-menu

# Configure the page
st.set_page_config(page_title="Streamlit Demo", page_icon="🌟", layout="wide")

# Sidebar header with shadow box style
st.sidebar.markdown(
    """
    <div style="background-color: #FFA421; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);">
        <h2 style="color: white; margin: 0;">🌟 Streamlit Demo</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation with full-size items
menu_options = ["🏠 Home", "📈 Analytics", "📂 Reports", "⚙️ Settings", "📜 About"]
selected_page = option_menu(
    menu_title=None,
    options=menu_options,
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
            "padding": "10px",
            "background-color": "rgba(255, 164, 33, 0.2)",
            "color": "#FFFFFF",
        },
        "nav-link-selected": {"background-color": "#FFA421", "color": "black"},
    },
)

# Subpages for each page
subpages = {
    "🏠 Home": ["Getting Started 🛠️", "Overview 🌟"],
    "📈 Analytics": ["Charts 📊", "Insights 🔍"],
    "📂 Reports": ["Create 📄", "Manage 🗂️"],
    "⚙️ Settings": ["Preferences ⚙️", "Tools 🔧"],
    "📜 About": ["Credits 📜", "Features 🌟"],
}

# Horizontal tabs for subpages
if selected_page in subpages:
    selected_subpage = st.tabs(subpages[selected_page])

# Content for each page and subpage
if selected_page == "🏠 Home":
    if selected_subpage == "Getting Started 🛠️":
        st.title("🏠 Home - Getting Started")
        st.write("Details about how to get started.")
    elif selected_subpage == "Overview 🌟":
        st.title("🏠 Home - Overview")
        st.write("Overview of the application.")
elif selected_page == "📈 Analytics":
    if selected_subpage == "Charts 📊":
        st.title("📈 Analytics - Charts")
        st.write("Details about analytics charts.")
    elif selected_subpage == "Insights 🔍":
        st.title("📈 Analytics - Insights")
        st.write("Details about analytics insights.")
elif selected_page == "📂 Reports":
    if selected_subpage == "Create 📄":
        st.title("📂 Reports - Create")
        st.write("Details about creating reports.")
    elif selected_subpage == "Manage 🗂️":
        st.title("📂 Reports - Manage")
        st.write("Details about managing reports.")
elif selected_page == "⚙️ Settings":
    if selected_subpage == "Preferences ⚙️":
        st.title("⚙️ Settings - Preferences")
        st.write("Details about preferences.")
    elif selected_subpage == "Tools 🔧":
        st.title("⚙️ Settings - Tools")
        st.write("Details about settings tools.")
elif selected_page == "📜 About":
    if selected_subpage == "Credits 📜":
        st.title("📜 About - Credits")
        st.write("Details about the app credits.")
    elif selected_subpage == "Features 🌟":
        st.title("📜 About - Features")
        st.write("Details about the app features.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 Streamlit Demo App. All rights reserved.")

