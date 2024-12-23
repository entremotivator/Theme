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

# Sidebar buttons for navigation
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

# Content for each selected sidebar option
if selected_page == "🏠 Home":
    st.title("🏠 Home")
    st.write("Welcome to the Enhanced Demo App! Start exploring the features.")
elif selected_page == "📈 Analytics":
    st.title("📈 Analytics")
    st.write("Analyze your data with charts and insights.")
elif selected_page == "📂 Reports":
    st.title("📂 Reports")
    st.write("Create and manage your reports.")
elif selected_page == "⚙️ Settings":
    st.title("⚙️ Settings")
    st.write("Customize your app settings and preferences.")
elif selected_page == "📜 About":
    st.title("📜 About")
    st.write("Learn more about this application and its features.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 Enhanced Streamlit Demo App. All rights reserved.")




