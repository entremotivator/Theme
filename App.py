import streamlit as st

# Set up sidebar
st.sidebar.markdown(
    """
    <div style="background-color:#FFA421; padding: 10px; border-radius: 5px; text-align: center;">
        <h1 style="color: white;">🌟 Streamlit Demo</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Define pages and subpages
pages = {
    "Page 1 🏠": ["Subpage 1.1 🌟", "Subpage 1.2 ✨"],
    "Page 2 📈": ["Subpage 2.1 🔍", "Subpage 2.2 📊"],
    "Page 3 📂": ["Subpage 3.1 🗂️", "Subpage 3.2 📁"],
    "Page 4 ⚙️": ["Subpage 4.1 🛠️", "Subpage 4.2 🔧"],
    "Page 5 📜": ["Subpage 5.1 📝", "Subpage 5.2 📚"],
}

# Sidebar full menu
st.sidebar.title("Full Menu")
for page, subpages in pages.items():
    with st.sidebar.expander(page):
        for subpage in subpages:
            st.write(subpage)

# Horizontal menu for each page
st.write(
    """
    <style>
    .horizontal-menu {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 20px;
    }
    .horizontal-menu a {
        color: #FFA421;
        text-decoration: none;
        font-weight: bold;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define the main app layout
page_selected = st.sidebar.selectbox("Choose a Page", list(pages.keys()))

# Display horizontal menu for the selected page
if page_selected in pages:
    subpages = pages[page_selected]
    st.markdown('<div class="horizontal-menu">' + ''.join(
        f'<a href="#">{subpage}</a>' for subpage in subpages
    ) + '</div>', unsafe_allow_html=True)

    # Page content
    st.title(page_selected)
    st.write(f"You are on {page_selected}.")
    for subpage in subpages:
        st.subheader(subpage)
        st.write(f"Details about {subpage} go here.")
