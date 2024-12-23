import streamlit as st

# Function to apply the theme and page configuration
def apply_theme():
    try:
        # Set the page configuration only once
        st.set_page_config(
            page_title="Enhanced Streamlit Demo",   # Set the page title
            page_icon="🌟",                        # Set the page icon
            layout="wide",                         # Set the layout to wide
            initial_sidebar_state="expanded",      # Expand the sidebar by default
            theme={
                "base": "dark",                  # Use dark theme
                "primaryColor": "#FFA421",      # Set the primary color
                "backgroundColor": "#1E1E1E",   # Set the background color
                "secondaryBackgroundColor": "#282828",  # Set the secondary background color
                "textColor": "#FFFFFF",         # Set the text color to white
                "font": "sans serif"            # Set the font to sans-serif
            }
        )
        print("Page configuration applied successfully.")
    except Exception as e:
        print(f"Error setting page config: {e}")
        # Handle or log error as needed

# Call the apply_theme function (ensure this is done only once at the start)
apply_theme()

# Sidebar with navigation options, styled with CSS
sidebar = st.sidebar

# Custom CSS to style the sidebar buttons
sidebar.markdown("""
    <style>
        .stSidebar .css-1d391kg {
            border: none;
            background-color: #1E1E1E;
        }
        .stSidebar .st-bd {
            border-radius: 8px;
        }
        .stSidebar .stRadio label {
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            background-color: #FFA421;
            color: #FFFFFF;
            padding: 10px;
            border-radius: 10px;
            width: 250px;
            margin: 5px auto;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            cursor: pointer;
        }
        .stSidebar .stRadio label:hover {
            background-color: #FF6F00;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
selected_page = sidebar.radio(
    "Select a page", 
    ["🏠 Home", "📈 Analytics", "📂 Reports", "⚙️ Settings", "📜 About"],
    label_visibility="collapsed"
)

# Dictionary to hold subpages for each page
subpages = {
    "🏠 Home": ["Getting Started 🛠️", "Overview 🌟"],
    "📈 Analytics": ["Charts 📊", "Insights 🔍"],
    "📂 Reports": ["Create 📄", "Manage 🗂️"],
    "⚙️ Settings": ["Preferences ⚙️", "Tools 🔧"],
    "📜 About": ["Credits 📜", "Features 🌟"]
}

# Sidebar subpage selection
selected_subpage = sidebar.radio(
    "Select a subpage", 
    subpages[selected_page],
    label_visibility="collapsed"
)

# Content display based on the selected page and subpage
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











