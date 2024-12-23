import streamlit as st
from streamlit_option_menu import option_menu  # Install: pip install streamlit-option-menu

# Function to apply the selected theme
def apply_theme():
    st.set_page_config(
        page_title="Enhanced Streamlit Demo",
        page_icon="🌟",
        layout="wide",
        initial_sidebar_state="expanded",
        theme={
            "base": "dark",
            "primaryColor": "#FFA421",
            "backgroundColor": "#1E1E1E",
            "secondaryBackgroundColor": "#282828",
            "textColor": "#FFFFFF",
            "font": "sans serif"
        }
    )

# Configure the page with default theme
apply_theme()

# Sidebar header with shadow box style
st.sidebar.markdown(
    """
    <div style="background-color: #FFA421; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);">
        <h2 style="color: white; margin: 0;">🌟 Enhanced Demo</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation with main pages
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

# Subpages for each main page in the sidebar
subpages = {
    "🏠 Home": ["Getting Started 🛠️", "Overview 🌟"],
    "📈 Analytics": ["Charts 📊", "Insights 🔍"],
    "📂 Reports": ["Create 📄", "Manage 🗂️"],
    "⚙️ Settings": ["Preferences ⚙️", "Tools 🔧"],
    "📜 About": ["Credits 📜", "Features 🌟"],
}

# Show subpage buttons in the sidebar based on selected main page
if selected_page in subpages:
    for subpage in subpages[selected_page]:
        if st.sidebar.button(subpage):
            selected_subpage = subpage
            break

# Add Settings Button in Sidebar
if st.sidebar.button("Update Theme"):
    apply_theme()  # Re-apply the theme configuration when button is pressed
    st.sidebar.success("Theme updated!")

# Display content based on selected subpage
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
st.sidebar.caption("© 2024 Enhanced Streamlit Demo App. All rights reserved.")








