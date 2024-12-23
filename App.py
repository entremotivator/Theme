import streamlit as st
from streamlit_option_menu import option_menu  # Importing streamlit-option-menu

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

        /* Style the option menu buttons */
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

# Sidebar navigation using option_menu for pages
selected_page = option_menu(
    menu_title="Main Menu",   # The main menu title
    options=["🏠 Home", "📈 Analytics", "📂 Reports", "⚙️ Settings", "📜 About"],  # Main pages
    icons=["house", "bar-chart", "file-earmark-text", "gear", "info-circle"],  # Icons for the pages
    menu_icon="cast",  # Main menu icon
    default_index=0,  # Default to Home page
    orientation="vertical",  # Arrange menu vertically
    styles={
        "container": {"padding": "5px", "background-color": "#282828"},
        "icon": {"color": "#FFA421", "font-size": "18px"},
        "menu-title": {"font-size": "22px", "font-weight": "bold", "color": "#FFA421"},
        "nav-link": {
            "font-size": "18px",
            "font-weight": "600",
            "text-align": "center",
            "background-color": "#FFA421",
            "color": "#FFFFFF",
            "border-radius": "10px",
            "padding": "12px",
            "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.3)",
        },
        "nav-link-selected": {"background-color": "#FF6F00", "font-weight": "700"}
    }
)

# Subpage navigation using option_menu based on the selected page
if selected_page == "🏠 Home":
    subpage = option_menu(
        menu_title="Home Subpages",  
        options=["Getting Started 🛠️", "Overview 🌟"],
        icons=["wrench", "star"],
        menu_icon="house",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "5px", "background-color": "#1E1E1E"},
            "icon": {"color": "#FFA421", "font-size": "18px"},
            "menu-title": {"font-size": "20px", "font-weight": "bold", "color": "#FFA421"},
            "nav-link": {
                "font-size": "16px",
                "font-weight": "600",
                "text-align": "center",
                "background-color": "#FFA421",
                "color": "#FFFFFF",
                "border-radius": "10px",
                "padding": "12px",
                "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.3)",
            },
            "nav-link-selected": {"background-color": "#FF6F00", "font-weight": "700"}
        }
    )

    if subpage == "Getting Started 🛠️":
        st.title("🏠 Home - Getting Started")
        st.write("Welcome to the Getting Started guide. This section will help you set up and use the app effectively.")
    elif subpage == "Overview 🌟":
        st.title("🏠 Home - Overview")
        st.write("Overview of the application, its features, and how it can help you achieve your goals.")

elif selected_page == "📈 Analytics":
    subpage = option_menu(
        menu_title="Analytics Subpages",  
        options=["Charts 📊", "Insights 🔍"],
        icons=["chart-bar", "search"],
        menu_icon="bar-chart",
        default_index=0,
        orientation="horizontal"
    )

    if subpage == "Charts 📊":
        st.title("📈 Analytics - Charts")
        st.write("Explore the charts and analytics related to your data. Visualize trends and insights.")
    elif subpage == "Insights 🔍":
        st.title("📈 Analytics - Insights")
        st.write("Dive into deeper insights and learn how your data drives decisions.")

elif selected_page == "📂 Reports":
    subpage = option_menu(
        menu_title="Reports Subpages",  
        options=["Create 📄", "Manage 🗂️"],
        icons=["file-earmark-plus", "folder"],
        menu_icon="file-earmark-text",
        default_index=0,
        orientation="horizontal"
    )

    if subpage == "Create 📄":
        st.title("📂 Reports - Create")
        st.write("Learn how to create custom reports tailored to your needs.")
    elif subpage == "Manage 🗂️":
        st.title("📂 Reports - Manage")
        st.write("Manage and organize your reports in an efficient and effective manner.")

elif selected_page == "⚙️ Settings":
    subpage = option_menu(
        menu_title="Settings Subpages",  
        options=["Profile ⚙️", "Tools 🛠️"],
        icons=["person", "tools"],
        menu_icon="gear",
        default_index=0,
        orientation="horizontal"
    )

    if subpage == "Profile ⚙️":
        st.title("⚙️ Settings - Profile")
        st.write("Update your profile settings, preferences, and security options.")
    elif subpage == "Tools 🛠️":
        st.title("⚙️ Settings - Tools")
        st.write("Access and manage the various tools available in the app.")

elif selected_page == "📜 About":
    st.title("📜 About Us")
    st.write("Learn more about the team and the purpose of the application.")















