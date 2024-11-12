import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import streamlit_shadcn_ui as ui
import json
import webbrowser

# Set up app configuration
st.set_page_config(page_title="Best of Worlds", page_icon="🌍", layout="centered")

# Apply CSS styling with the updated universal selector approach
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

# Function to load Lottie animations
def load_lottie_animation(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

# Load animations
welcome_animation = load_lottie_animation("assets/Animation.json")  # Animation for Welcome page
home_animation = load_lottie_animation("assets/panel.json")         # Animation for Home page



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


# Define SVG URLs
video_svg_url = "https://bestofworlds.se/img/video-solid.svg"
magnifying_svg_url = "https://bestofworlds.se/img/magnifying-glass-solid.svg"
download_svg_url = "https://bestofworlds.se/img/download-solid.svg"


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
    {"name": "DILEMMA", "description": "Open up a problem into a dilemma", "link": "https://bestofworlds.se/dilemma/dilemma.png", "video_link": "https://youtu.be/R1OvHj8qsC8", "usage": "Individual/Team"},
    {"name": "BRAND BOOTH", "description": "Imagine your sustainable brand", "link": "https://brandbooth.streamlit.app/", "usage": "Individual use"},
    {"name": "NETWORK ANALYSIS", "description": "Collaboration Network Analysis", "link": "https://bestofworlds.se/CNA/ScreenshotCNA.png", "usage": "Individual/Team/Organizational"},
]


# Display solutions in MetricCard with SVG buttons
if selected_page == "The Suite":
    st.markdown(f"<h1 style='font-size: 30px;'>Transformation tools for {st.session_state['company_name']}</h1>", unsafe_allow_html=True)
    st.write("Explore the expanding set of tools in the Best of Worlds ecosystem designed to help you to engage with transformation in a way that’s intuitive and empowering. Mind you, these tools are under development and all are not yet fully functional without assistance. Please contact us for further exploration.")
    cols = st.columns(3)

    for i, solution in enumerate(solutions):
        with cols[i % 3]:  # Rotate through columns
            # Display the MetricCard
            ui.metric_card(
                title=solution["name"],
                content=solution["description"],
                description=solution["usage"],
                key=f"solution_card_{i}"
            )

            # Adjust icon placement with CSS
            buttons_html = """
            <div style='display: flex; gap: 10px; margin-top: -15px; justify-content: center;'>
            """
            
            # Only add the relevant icons if links are available
            if "link" in solution:
                buttons_html += f"<a href='{solution['link']}' target='_blank'><img src='{magnifying_svg_url}' alt='Open Link' style='height: 24px;'/></a>"
            
            if "extra_link" in solution:
                buttons_html += f"<a href='{solution['extra_link']}' target='_blank'><img src='{download_svg_url}' alt='Download' style='height: 24px;'/></a>"
            
            if "video_link" in solution:
                buttons_html += f"<a href='{solution['video_link']}' target='_blank'><img src='{video_svg_url}' alt='Watch Video' style='height: 24px;'/></a>"
            
            buttons_html += "</div>"

            # Render the HTML with st.markdown
            st.markdown(buttons_html, unsafe_allow_html=True)




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
            Our technology isn’t complex—it’s humane. Best of Worlds is a powerful vehicle for deep, human-driven change.<br>
            - The Suite contains a wide range of tools at different stages of development for {st.session_state['company_name']} to explore, and more is added frequently. 
        """, unsafe_allow_html=True)

    # New Three-Column Layout for Suggestions with Email, LinkedIn, and Substack Links
    col1, col2, col3 = st.columns(3)

    with col1:
        # Jonas's image and title with contact icons aligned to the right
        st.markdown(
            """
            <div style="text-align: right; margin-top: 60px;">
                <img src="https://bestofworlds.se/img/jonasbow.png" alt="Jonas Bergvall" style="width: 100px;">
                <div style="font-size: 12px; margin-top: 10px; color: #555;">Jonas Bergvall<br>Founder, Best of Worlds</div>
            </div>
            """, 
            unsafe_allow_html=True
        )

        # Email Icon
        st.markdown(
            """
            <div style="text-align: right;">
                <a href="mailto:info@bestofworlds.se">
                    <img src="https://bestofworlds.se/img/email.svg" alt="Email" width="30" style="margin-top: 15px;">
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )

        # LinkedIn Icon
        st.markdown(
            """
            <div style="text-align: right;">
                <a href="https://www.linkedin.com/company/best-of-worlds/" target="_blank">
                    <img src="https://bestofworlds.se/img/LI-Logo.svg" alt="LinkedIn" width="30" style="margin-top: 11px;">
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )

    with col2:
        # Middle Column: Contact Information
        st.markdown("### We’d love to hear from you!")
        st.write("Some of the tools are only available if you contact us. Or do you have ideas for new apps or improvements? Let us know!")

        # Clickable text links
        st.write("team[at]bestofworlds.se")
        st.write("Best of Worlds on LinkedIn")

    with col3:
        # Substack Section with Caption and Clickable Image
        st.markdown(
            """
            <div style="text-align: right; margin-top: -50px;">
                <div style="font-size: 12px; margin-top: -20px; color: #555;">Best of Worlds funny short-stories.</div>
                <a href="https://jonasbergvall.substack.com/" target="_blank">
                    <img src="https://bestofworlds.se/img/substack.jpg" alt="Substack" style="width: 90%; border-radius: 8px;">
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )
