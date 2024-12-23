import streamlit as st
from streamlit.components.v1 import html

# Function to apply the theme and page configuration
def apply_theme():
    try:
        # Set the page configuration only once
        st.set_page_config(
            page_title="Professional Streamlit App",   # Set the page title
            page_icon="🚀",                         # Set the page icon
            layout="wide",                          # Set the layout to wide
            initial_sidebar_state="expanded",       # Expand the sidebar by default
            theme={
                "base": "dark",                    # Use dark theme
                "primaryColor": "#FFA421",         # Set the primary color
                "backgroundColor": "#1E1E1E",      # Set the background color
                "secondaryBackgroundColor": "#282828",  # Set the secondary background color
                "textColor": "#FFFFFF",            # Set the text color to white
                "font": "sans serif"               # Set the font to sans-serif
            }
        )
        print("Page configuration applied successfully.")
    except Exception as e:
        print(f"Error setting page config: {e}")
        # Handle or log error as needed

# Call the apply_theme function (ensure this is done only once at the start)
apply_theme()

# Sidebar with logo and navigation options, styled with CSS
sidebar = st.sidebar

# HTML code for the logo
sidebar.markdown("""
    <div style="text-align:center;">
        <img src="https://your-logo-url.com/logo.png" alt="Demo Logo" width="200"/>
    </div>
""", unsafe_allow_html=True)

# Custom CSS to style the sidebar buttons, overall layout, and logo
sidebar.markdown("""
    <style>
        /* Style the sidebar itself */
        .stSidebar {
            background-color: #282828;  /* Dark background for the sidebar */
            border-radius: 12px;        /* Rounded corners for a sleek look */
            padding: 20px;              /* Add padding around the content */
        }

        /* Style the logo */
        .stSidebar img {
            width: 100%;                /* Make the logo fit the sidebar */
            max-width: 200px;           /* Limit the logo width */
            margin-bottom: 30px;        /* Space between logo and sidebar buttons */
        }

        /* Style the sidebar heading */
        .stSidebar h1 {
            font-size: 24px;
            color: #FFA421;
            text-align: center;
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Style the buttons (radio options) */
        .stSidebar .stRadio label {
            font-size: 18px;
            font-weight: 600;         /* Slightly lighter weight for readability */
            text-align: center;
            background-color: #FFA421;
            color: #FFFFFF;
            padding: 15px 20px;
            border-radius: 10px;
            width: 100%;              /* Make buttons stretch full width */
            margin: 10px 0;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            cursor: pointer;
            transition: all 0.3s ease;
        }

        /* Button hover effect */
        .stSidebar .stRadio label:hover {
            background-color: #FF6F00;
            transform: scale(1.05);
        }

        /* Style the selected button */
        .stSidebar .stRadio label.st-active {
            background-color: #FF6F00;
            font-weight: 700;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4);
        }

        /* Style the page content area */
        .stMain {
            background-color: #1E1E1E;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4);
        }

        /* Style the content headers */
        .stMain h1 {
            font-size: 28px;
            color: #FFA421;
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Style the content text */
        .stMain p {
            font-size: 16px;
            color: #FFFFFF;
            line-height: 1.6;
        }

        /* Style the subpage buttons */
        .stSidebar .stRadio .st-bd {
            padding: 10px;
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
        st.write("Welcome to the Getting Started guide. This section will help you set up and use the app effectively.")
    elif selected_subpage == "Overview 🌟":
        st.title("🏠 Home - Overview")
        st.write("Overview of the application, its features, and how it can help you achieve your goals.")
elif selected_page == "📈 Analytics":
    if selected_subpage == "Charts 📊":
        st.title("📈 Analytics - Charts")
        st.write("Explore the charts and analytics related to your data. Visualize trends and insights.")
    elif selected_subpage == "Insights 🔍":
        st.title("📈 Analytics - Insights")
        st.write("Dive into deeper insights and learn how your data drives decisions.")
elif selected_page == "📂 Reports":
    if selected_subpage == "Create 📄":
        st.title("📂 Reports - Create")
        st.write("Learn how to create custom reports tailored to your needs.")
    elif selected_subpage == "Manage 🗂️":
        st.title("📂 Reports - Manage")
        st.write("Manage and organize your reports in an efficient and effective manner.")
elif selected_page == "⚙️ Settings":
    if selected_subpage == "Preferences ⚙️":
        st.title("⚙️ Settings - Preferences")
        st.write("Adjust your personal preferences and settings to tailor the app to your needs.")
    elif selected_subpage == "Tools 🔧":
        st.title("⚙️ Settings - Tools")
        st.write("Explore the various tools available for advanced users and developers.")
elif selected_page == "📜 About":
    if selected_subpage == "Credits 📜":
        st.title("📜 About - Credits")
        st.write("Acknowledgements and credits for the developers and contributors to this project.")
    elif selected_subpage == "Features 🌟":
        st.title("📜 About - Features")
        st.write("Detailed list of features and functionality available in the app.")















