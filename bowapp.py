import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import streamlit_shadcn_ui as ui
from streamlit_navigation_bar import st_navbar
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

# Load Google Fonts for Roboto Slab
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto Slab', sans-serif;
        }
        .st-emotion-cache-16txt1c {
            font-family: 'Roboto Slab', sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)

local_css("assets/style.css")

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

# Function to handle link navigation
def navigate_to_link(key):
    action = st.session_state[key]
    if action != "Select":
        webbrowser.open_new_tab(menu_links[action])

# Solutions Page with "Usage" Field in MetricCard
if selected_page == "The Suite":
    st.markdown(f"<h1 style='font-size: 30px;'>Transformation tools for {st.session_state['company_name']}</h1>", unsafe_allow_html=True)
    st.write("Explore the various tools in the Best of Worlds ecosystem designed to help you to engage with complexity in a way that’s intuitive and empowering.")

    # Define all specified solutions, including the usage type (Individual, Team, or Organizational)
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

    # Initialize session state for each option's previous selection and user interaction flag if not already set
    for i, solution in enumerate(solutions):
        # Track the previous selection to avoid auto-triggering on reload
        if f"prev_option_{i}" not in st.session_state:
            st.session_state[f"prev_option_{i}"] = "Select"  # Set default to non-action to ensure fresh selection
        if f"user_selected_{i}" not in st.session_state:
            st.session_state[f"user_selected_{i}"] = False  # Flag to check if user has interacted

    # Create three columns for layout
    cols = st.columns(3)

    # Display each solution in a MetricCard with option_menu for actions
    for i, solution in enumerate(solutions):
        with cols[i % 3]:  # Rotate through columns
            # Display MetricCard with title, description, and usage fields
            ui.metric_card(
                title=solution["name"],
                content=solution["description"],
                description=solution["usage"],
                key=f"solution_card_{i}"
            )

            # Define options for option_menu based on available links
            menu_options = ["Open"]
            menu_links = {"Open": solution["link"]}

            # Add "Download" option if extra_link exists
            if "extra_link" in solution:
                menu_options.append("Download")
                menu_links["Download"] = solution["extra_link"]

            # Add "Video" option if video_link exists
            if "video_link" in solution:
                menu_options.append("Video")
                menu_links["Video"] = solution["video_link"]

            # Option menu for actions with `default_index=0` to pre-select "Open"
            action = option_menu(
                menu_title="",
                options=["Select"] + menu_options,  # Add a non-actionable "Select" option
                icons=[""] + ["box-arrow-up-right"] * len(menu_options),
                menu_icon="cast",
                default_index=0,
                key=f"option_menu_{i}",
                orientation="horizontal",
                styles={
                    "container": {"padding": "0!important"},
                    "nav-link-selected": {"background-color": "#FFCC00"},
                    "nav-link": {"font-size": "12px", "text-align": "center", "padding": "5px 10px"},
                },
                on_change=navigate_to_link
            )

# Welcome Page with Two-Column Layout
if selected_page == "Welcome":
    col1, col2 = st.columns([1, 2])  # Two-column layout

    with col1:
        # Lottie animation on the left
        st_lottie(welcome_animation, height=400, key="welcome_animation")

    with col2:
        # Text and input on the right
        st.title("Welcome to Best of Worlds")
        st.markdown("**Transformation-as-a-Service** tailored to help you and your organization evolve. In a world abundant with complex challenges and rich with opportunity, organizations have vast, often untapped potential to grow, evolve, and contribute meaningfully. We believe that within every organization lies the capacity not only to improve but to thrive, to harness collective intelligence, and to address complex challenges with clarity and purpose. The journey isn’t about fixing what’s broken, but about empowering teams to bring their best to every challenge.")

        # Default Streamlit Input
        company_name = st.text_input("Enter your personal name or your organization's name to personalize your experience:")
        if company_name:
            st.session_state["company_name"] = company_name
            st.success(f"Welcome, {company_name}! Explore how Best of Worlds can help your team thrive.")

# Home Page with Two-Column Layout
if selected_page == "Taas":
    col1, col2 = st.columns([1, 2])  # Two-column layout for Home page

    with col1:
        st_lottie(home_animation, height=420, key="home_animation")

    with col2:
        st.title(f"Welcome to your transformation, {st.session_state['company_name']}")

        st.markdown("""
            Best of Worlds' **Transformation-as-a-Service** for organizations ready to evolve and thrive.
            Our mission is to empower organizations with insights and tools for a meaningful, human-centered transformation strategy.
        """)

        st.markdown(f"""
            Our technology isn’t complex—it’s humane. Best of Worlds is a powerful vehicle for deep, human-driven change.<br><br>
            - The Suite contains a wide range of tools att different stages of development for {st.session_state['company_name']} to explore, and more is added frequently.
        """, unsafe_allow_html=True)

    # New Three-Column Layout for Suggestions with Email and LinkedIn Links
    st.write("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        # Right-align email and LinkedIn SVG icons in the first column with vertical adjustment
        email_icon_svg = """
        <div style="text-align: right;">
            <a href="mailto:info@bestofworlds.se">
                <img src="https://bestofworlds.se/img/email.svg" alt="Email" width="30" style="margin-top: 220px;">
            </a>
        </div>
        """
        linkedin_icon_svg = """
        <div style="text-align: right;">
            <a href="https://www.linkedin.com/company/best-of-worlds/" target="_blank">
                <img src="https://bestofworlds.se/img/LI-Logo.svg" alt="LinkedIn" width="30" style="margin-top: 11px;">
            </a>
        </div>
        """
        st.markdown(email_icon_svg, unsafe_allow_html=True)
        st.markdown(linkedin_icon_svg, unsafe_allow_html=True)

    with col2:
        st.markdown("### We’d love to hear from you!")
        st.write("Some of the tools are only available if you contact us. Or do you have ideas for new apps or improvements? Let us know!")

        # Clickable text links
        st.markdown("[team@bestofworlds.se](mailto:team@bestofworlds.se)")
        st.markdown("[Best of Worlds on LinkedIn](https://www.linkedin.com/company/best-of-worlds/)")

    with col3:
        st_lottie(robot_animation, height=160, key="robot_animation")
