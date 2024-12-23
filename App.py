import streamlit as st

# Sidebar header
st.sidebar.markdown(
    """
    <div style="background-color:#FFA421; padding: 15px; border-radius: 5px; text-align: center;">
        <h2 style="color: white; margin: 0;">🌟 Streamlit Demo</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# Define main menu items (pages) and their descriptions
menu = {
    "🏠 Home": "Welcome to the home page. Explore the app features here.",
    "📈 Analytics": "Dive into data analytics and visualizations.",
    "📂 Reports": "Generate and manage reports for your projects.",
    "⚙️ Settings": "Configure your preferences and tools.",
    "📜 About": "Learn more about this Streamlit app and its features."
}

# Sidebar navigation
selected_page = st.sidebar.radio(
    "Navigation", 
    list(menu.keys()), 
    key="main_menu",
    format_func=lambda x: f"🔘 {x}",
    help="Choose a page to explore."
)

# Make sidebar buttons look more interactive
st.sidebar.markdown(
    """
    <style>
    .stRadio > label {
        display: flex;
        justify-content: center;
        font-weight: bold;
        font-size: 18px;
        color: #FFA421;
        text-align: center;
        margin: 10px 0;
    }
    .stRadio > div > label:hover {
        background-color: #FFA421;
        color: black !important;
        border-radius: 10px;
        padding: 5px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Horizontal menu for sub-pages
st.markdown(
    """
    <style>
    .horizontal-menu {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin: 20px 0;
    }
    .horizontal-menu a {
        color: #FFA421;
        text-decoration: none;
        font-size: 18px;
        font-weight: bold;
        padding: 5px 10px;
        border: 2px solid #FFA421;
        border-radius: 5px;
    }
    .horizontal-menu a:hover {
        background-color: #FFA421;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sub-pages for the current page
sub_pages = {
    "🏠 Home": ["Getting Started 🛠️", "Overview 🌟"],
    "📈 Analytics": ["Charts 📊", "Insights 🔍"],
    "📂 Reports": ["Create 📄", "Manage 🗂️"],
    "⚙️ Settings": ["Preferences ⚙️", "Tools 🔧"],
    "📜 About": ["Credits 📜", "Features 🌟"],
}

st.markdown('<div class="horizontal-menu">' + ''.join(
    f'<a href="#">{sub_page}</a>' for sub_page in sub_pages[selected_page]
) + '</div>', unsafe_allow_html=True)

# Page Content
st.title(selected_page)
st.write(menu[selected_page])  # Display the page description

for sub_page in sub_pages[selected_page]:
    st.subheader(sub_page)
    st.write(f"Details about {sub_page} go here.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 Streamlit Demo App. All rights reserved.")
