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

# Sidebar navigation menu
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
            "padding": "15px",
            "background-color": "rgba(255, 164, 33, 0.2)",
            "color": "#FFFFFF",
        },
        "nav-link-selected": {"background-color": "#FFA421", "color": "black"},
    },
)

# Define subpages and tabs for each main page
subpages = {
    "🏠 Home": ["Getting Started 🛠️", "Overview 🌟"],
    "📈 Analytics": ["Charts 📊", "Insights 🔍"],
    "📂 Reports": ["Create 📄", "Manage 🗂️"],
    "⚙️ Settings": ["Preferences ⚙️", "Tools 🔧"],
    "📜 About": ["Credits 📜", "Features 🌟"],
}

# Apply consistent styles for tabs
tab_styles = """
    <style>
    div[role="tab"] {
        font-size: 18px;
        padding: 10px 20px;
        margin: 5px;
        border-radius: 10px;
        background-color: rgba(255, 164, 33, 0.2);
        color: white;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
    }
    div[role="tab"][aria-selected="true"] {
        background-color: #FFA421;
        color: black;
    }
    div[role="tab"]:hover {
        background-color: rgba(255, 164, 33, 0.5);
    }
    </style>
"""
st.markdown(tab_styles, unsafe_allow_html=True)

# Display tabs based on selected sidebar option
if selected_page in subpages:
    selected_tab = st.tabs(subpages[selected_page])

    # Render content for each tab
    for index, tab in enumerate(subpages[selected_page]):
        with selected_tab[index]:
            st.title(f"{selected_page} - {tab}")
            st.write(f"Content for {tab.lower()}.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 Enhanced Streamlit Demo App. All rights reserved.")



