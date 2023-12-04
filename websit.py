# Python In-built packages
from pathlib import Path


# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="PolluVision",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading

with st.sidebar:
    st.image("logo.png")

with st.container():

    st.title("Visual Pollution Detection")
    st.caption('check the visual pollution')
    st.caption('Then click the "Detect Visual Pollution" button and check the result.')


# Model Options


confidence = float(25) / 100

model_path = Path(settings.DETECTION_MODEL)

try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

# st.sidebar.header("Video Config")
source_radio = 'Video'

source_img = None

helper.play_stored_video(confidence, model)
