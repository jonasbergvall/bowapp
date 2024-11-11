import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_shadcn_ui as ui
import json

# Set up app configuration
st.set_page_config(page_title="Best of Worlds", page_icon="🌍", layout="centered")

# Function to load Lottie animations
def load_lottie_animation(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

# Load animations
welcome_animation = load_lottie_animation("assets/Animation.json")
home_animation = load_lottie_animation("assets/panel.json")
robot_animation = load_lottie_animation("assets/robot.json")

# Sidebar Navigation with Option Menu
selected_page = option_menu(
    menu_title=None,
    options=["Welcome", "Taas", "The Suite"],
    icons=["house", "info-circle", "list-task"],
    default_index=0,
    orientation="horizontal",
)

if selected_page == "The Suite":
    st.markdown("<h1 style='font-size: 30px;'>Transformation tools</h1>", unsafe_allow_html=True)
    st.write("Explore the various tools in the Best of Worlds ecosystem.")

    # Define solutions
    solutions = [
        {"name": "SAFE IDENTITY", "description": "Anonymous identification", "link": "https://bestofworlds.se/IDQR/", "usage": "Individual use"},
        {"name": "DATA POINT EXPLORER", "description": "Find your data sources", "link": "https://bestofworlds.se/dataexplorer/DataBrain.html", "usage": "Individual use"},
        {"name": "BIAS EXPLORER", "description": "Identify your bias", "link": "https://bestofworlds.se/worldview/worldview.html", "usage": "Individual use"},
    ]

    # Create three columns for layout
    cols = st.columns(3)

    # Display each solution with an icon-only option_menu for actions
    for i, solution in enumerate(solutions):
        with cols[i % 3]:
            with st.container():
                ui.metric_card(
                    title=solution["name"],
                    content=solution["description"],
                    description=solution["usage"],
                    key=f"solution_card_{i}"
                )

                # Option menu with icon-only for "Open"
                action = option_menu(
                    menu_title="",
                    options=["", " "],  # Empty labels
                    icons=["", "box-arrow-up-right"],  # Icon for "Open"
                    menu_icon="cast",
                    default_index=0,
                    key=f"option_menu_{i}",
                    orientation="horizontal",
                    styles={
                        "container": {"padding": "0!important"},
                        "nav-link-selected": {"background-color": "#FFCC00"},
                        "nav-link": {"padding": "5px 10px"},
                    }
                )
                
                # Inject JavaScript to open the link in a new tab if icon is selected
                if action == " ":
                    js = f"""
                    <script>
                        window.open("{solution['link']}", "_blank");
                    </script>
                    """
                    st.markdown(js, unsafe_allow_html=True)
