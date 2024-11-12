import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import streamlit_shadcn_ui as ui
import json
import webbrowser
import os

# Set up app configuration
st.set_page_config(page_title="Best of Worlds", page_icon="🌍", layout="centered")

# Function to load CSS
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"CSS file not found: {file_name}")

# Load Google Fonts for Roboto Slab and Font Awesome for icons
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto Slab', sans-serif;
        }
        .st-emotion-cache-16txt1c {
            font-family: 'Roboto Slab', sans-serif;
        }
        .stButton>button {
            font-size: 12px;
            padding: 5px 10px;
            margin: 2px;
        }
        .stButton>button i {
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

local_css("assets/style.css")

# Load SVG files
def load_svg(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            return file.read()
    else:
        st.error(f"SVG file not found: {filepath}")
        return ""

# Load icons
video_icon = load_svg("assets/video-solid.svg")
magnifying_glass_icon = load_svg("assets/magnifying-glass-solid.svg")
download_icon = load_svg("assets/download-solid.svg")

# Function to load Lottie animations
def load_lottie_animation(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            return json.load(file)
    else:
        st.error(f"Lottie animation file not found: {filepath}")
        return {}

# Load animations
welcome_animation = load_lottie_animation("assets/Animation.json")  # Animation for Welcome page
home_animation = load_lottie_animation("assets/panel.json")         # Animation for Home page
robot_animation = load_lottie_animation("assets/robot.json")

# Display logo above the menu
st.markdown(
    """
    <div class="top-right-logo-container">
        <img src="https://bestofworlds.se/img/BoWlogo.png" class="top-right-logo">
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation with Option Menu
selected_page = option_menu(
    menu_title=None,
    options=["Welcome", "Taas", "The Suite"],
    icons=["house", "info-circle", "list-task"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#FFCC00", "font-family": "Roboto Slab, sans-serif"},
        "icon": {"color": "#333", "font-size": "14px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#E6B800"},
        "nav-link-selected": {"background-color": "#E6B800"},
    }
)

# Variables to store the visitor's company name
if "company_name" not in st.session_state:
    st.session_state["company_name"] = ""

# Solutions Page with "Usage" Field in MetricCard
if selected_page == "The Suite":
    st.markdown(f"<h1 style='font-size: 30px;'>Transformation tools for {st.session_state['company_name']}</h1>", unsafe_allow_html=True)
    st.write("Explore the various tools in the Best of Worlds ecosystem designed to help you to engage with complexity in a way that’s intuitive and empowering.")

    # Define all specified solutions, including the usage type (Individual, Team, or Organizational)
    # Define all specified solutions outside the page selection block
    solutions = [
    {"name": "SAFE IDENTITY", "description": "Anonymous identification", "link": "https://bestofworlds.se/IDQR/", "usage": "Individual use"},
    {"name": "DATA POINT EXPLORER", "description": "Find your data sources", "link": "https://bestofworlds.se/dataexplorer/DataBrain.html", "usage": "Individual use"},
    {"name": "BIAS EXPLORER", "description": "Identify your bias", "link": "https://bestofworlds.se/worldview/worldview.html", "usage": "Individual use"},
    {"name": "DOTS OF SPACE", "description": "Spatial insight for a safe environment", "link": "https://dotsofbow.streamlit.app/", "extra_link": "https://www.icloud.com/shortcuts/0c164ac2c45c48dea430531effbd740f", "usage": "Individual/Team/Organizational"},
    {"name": "BALANCE", "description": "Find the best balance for your organization", "link": "https://balanceorg.streamlit.app/", "usage": "Individual/Team/Organizational"},
    {"name": "CONSENSUS", "description": "Shared wisdom for decision-making", "link": "https://consensus.streamlit.app/", "video_link": "https://youtu.be/GZMn3F03zQU", "usage": "Individual/Team"},
    {"name": "FILTER BUBBLE", "description": "Media bias in your organization", "link": "https://filterbubble.streamlit.app/", "usage": "Individual/Team/Organizational"},
    {"name": "WHISTLE PEEP 1", "description": "Authentic individual well-being", "link": "https://whistlepeep.streamlit.app/", "usage": "Individual use"},
    {"name": "WHISTLE PEEP 2", "description": "True organizational well-being", "link": "https://wptotal.streamlit.app/", "usage": "Organizational use"},
    {"name": "TRAVEL TRACKER", "description": "Preferences for time off and travel", "link": "https://summervacation.streamlit.app/", "usage": "Organizational use"},
    {"name": "HONESTIFY", "description": "Anonymous feedback on your question", "link": "https://bestofworlds.se/honestify/", "usage": "Individual/Team/Organizational"},
    {"name": "DILEMMA", "description": "Open up a problem into a dilemma", "link": "https://bestofworlds.se/dilemma/dilemma.png", "extra_link": "https://www.icloud.com/shortcuts/0c164ac2c45c48dea430531effbd740f", "video_link": "https://youtu.be/R1OvHj8qsC8", "usage": "Individual/Team"},
    {"name": "BRAND BOOTH", "description": "Imagine your sustainable brand", "link": "https://bestofworlds.se/booth/Screenshot.png", "usage": "Individual use"},
    {"name": "NETWORK ANALYSIS", "description": "Collaboration Network Analysis", "link": "https://bestofworlds.se/CNA/ScreenshotCNA.png", "usage": "Individual/Team/Organizational"},
]

# Solutions Page with "Usage" Field in MetricCard
if selected_page == "The Suite":
    st.markdown(f"<h1 style='font-size: 30px;'>Transformation tools for {st.session_state['company_name']}</h1>", unsafe_allow_html=True)
    st.write("Explore the various tools in the Best of Worlds ecosystem designed to help you to engage with complexity in a way that’s intuitive and empowering.")

    # Display each solution with a MetricCard and styled button links
    cols = st.columns(3)
    for i, solution in enumerate(solutions):
        with cols[i % 3]:
            ui.metric_card(
                title=solution["name"],
                content=solution["description"],
                description=solution["usage"],
                key=f"solution_card_{i}"
            )

            # Create HTML-styled button links with SVG icons below each MetricCard
            st.markdown(
                f"""
                <div style="display: flex; gap: 10px; margin-top: 8px;">
                    <a href="{solution['link']}" target="_blank" style="text-decoration: none;">
                        <button style="background-color: #FFCC00; color: black; padding: 8px 12px; border: none; cursor: pointer;">
                            {magnifying_glass_icon} Explore
                        </button>
                    </a>
                    <a href="{solution.get('extra_link', '#')}" target="_blank" style="text-decoration: none;">
                        <button style="background-color: #FFCC00; color: black; padding: 8px 12px; border: none; cursor: pointer;">
                            {download_icon} Download
                        </button>
                    </a>
                    <a href="{solution.get('video_link', '#')}" target="_blank" style="text-decoration: none;">
                        <button style="background-color: #FFCC00; color: black; padding: 8px 12px; border: none; cursor: pointer;">
                            {video_icon} Watch
                        </button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

# Additional CSS for SVG styling within buttons
st.markdown(
    """
    <style>
    .stButton>button svg {
        height: 16px;
        width: 16px;
        vertical-align: middle;
        margin-right: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Welcome Page with Two-Column Layout
if selected_page == "Welcome":
    col1, col2 = st.columns([1, 2])

    with col1:
        st_lottie(welcome_animation, height=400, key="welcome_animation")

    with col2:
        st.title("Welcome to Best of Worlds")
        st.markdown("**Transformation-as-a-Service** tailored to help you and your organization evolve...")
        company_name = st.text_input("Enter your personal name or your organization's name to personalize your experience:")
        if company_name:
            st.session_state["company_name"] = company_name
            st.success(f"Welcome, {company_name}! Explore how Best of Worlds can help your team thrive.")

# Home Page with Two-Column Layout
if selected_page == "Taas":
    col1, col2 = st.columns([1, 2])

    with col1:
        st_lottie(home_animation, height=420, key="home_animation")

    with col2:
        st.title(f"Welcome to your transformation, {st.session_state['company_name']}")
        st.markdown("Best of Worlds' **Transformation-as-a-Service** for organizations ready to evolve and thrive...")
    
    # Footer layout
    st.write("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div style="text-align: right;"><a href="mailto:info@bestofworlds.se"><img src="https://bestofworlds.se/img/email.svg" alt="Email" width="30"></a></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: right;"><a href="https://www.linkedin.com/company/best-of-worlds/" target="_blank"><img src="https://bestofworlds.se/img/LI-Logo.svg" alt="LinkedIn" width="30"></a></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("### We’d love to hear from you!")
        st.write("Some of the tools are only available if you contact us. Or do you have ideas for new apps or improvements? Let us know!")
        st.markdown("[team@bestofworlds.se](mailto:team@bestofworlds.se)")
        st.markdown("[Best of Worlds on LinkedIn](https://www.linkedin.com/company/best-of-worlds/)")

    with col3:
        st_lottie(robot_animation, height=160, key="robot_animation")
