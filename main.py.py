import PIL
import streamlit as st
from ultralytics import YOLO
from ip2geotools.databases.noncommercial import DbIpCity
import requests

# Function to get the user's IP address
def get_user_ip():
    return requests.get('https://api64.ipify.org/').text

# Path to YOLO model (weight file)
model_path = '../pythonProject/best final.pt'

# Page layout
st.set_page_config(
    page_title="PolluVision",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Code
with st.sidebar:
    st.image("logo.png")
    st.header("Upload an Image:")
    # Adding file uploader to sidebar for uploading images
    source_img = st.file_uploader(
        "Upload a photo to check the visual pollution", type=("jpg", "jpeg", "png"))
with st.container():
    ## Main page Code
    ## LOGO
    # left_co, cent_co, last_co = st.columns(3)
    # with cent_co:
    #     st.image("logo.png")

    st.title("Visual Pollution Detection")
    st.caption('Upload a photo to check the visual pollution')
    st.caption('Then click the "Detect Visual Pollution" button and check the result.')

# Main page layout
# Create two columns on the main page
col1, col2 = st.columns(2)
# Add image to the first column if an image is uploaded
with st.container():
    with col1:
        if source_img:
            # Open the uploaded image
            uploaded_image = PIL.Image.open(source_img)

            # Add the uploaded image to the page with a caption
            st.image(source_img,
                     caption="Uploaded Image",
                     use_column_width=True)

            # Connection to YOLO model
            try:
                model = YOLO(model_path)
            except Exception as ex:
                st.error(f"Unable to load model. Check the specified path: {model_path}")
                st.error(ex)

            # Send the image to the YOLO model
            if st.sidebar.button('Detect Visual Pollution'):
                # Get the result and prediction from the Model
                res = model.predict(uploaded_image)
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]

                # Caption of the Image
                with col2:
                    st.image(res_plotted,
                             caption='Detected Image',
                             use_column_width=True)
                    st.subheader("Visual Pollution Location")

                    user_ip = get_user_ip()

                    if user_ip:
                        # Use the DbIpCity library to get the user's location
                        response = DbIpCity.get(user_ip, api_key='free')

                        # Display the retrieved location information
                        st.write("City:", response.city)
                        st.write("Region:", response.region)
                        st.write("Country:", response.country)
                        st.write("Latitude:", response.latitude)
                        st.write("Longitude:", response.longitude)
                    else:
                        st.write("User IP address not provided.")


# import PIL
# import streamlit as st
# from ultralytics import YOLO
# from ip2geotools.databases.noncommercial import DbIpCity
# import requests
#
# from geopy.geocoders import Nominatim
#
# import numpy as np
# from bokeh.models.widgets import Button
# from bokeh.models import CustomJS
# from streamlit_bokeh_events import streamlit_bokeh_events
#
#
# # path to YOLO model (weight file)
# model_path = 'best final.pt'
#
# # Page layout
# st.set_page_config(
#     page_title="PolluVision",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )
#
#
# # Sidebar Code
# with st.sidebar:
#     st.header("Upload an Image:")
#     # Adding file uploader to sidebar for upload an images
#     source_img = st.file_uploader(
#         "Upload a photo to check the visual pollution", type=("jpg", "jpeg", "png"))
#
#
# # Main page Code
# # LOGO
# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     st.image("logo.png")
#
#
# st.title("Visual Pollution Detection")
# st.caption('Upload a photo to check the visual pollution')
# st.caption('Then click the :blue[Detect the Visual Pollution] button and check the result.')
#
# # Main page layout
# # Create two columns on the main page
# col1, col2 = st.columns(2)
#
# # Add image to the first column if image is uploaded
# with col1:
#     if source_img:
#         # Open the uploaded image
#         uploaded_image = PIL.Image.open(source_img)
#
#         # Add the uploaded image to the page with a caption
#         st.image(source_img,
#                  caption="Uploaded Image",
#                  use_column_width=True
#                  )
#         #
#
#
#
#
# # Connection to YOLO model
# try:
#     model = YOLO(model_path)
# except Exception as ex:
#     st.error(
#         f"Unable to load model. Check the specified path: {model_path}")
#     st.error(ex)
#
# # Send the image to the YOLO model
# if st.sidebar.button('Detect Visual Pollution'):
#     # Get the result and prediction from the Model
#     res = model.predict(uploaded_image
#                         )
#     boxes = res[0].boxes
#     res_plotted = res[0].plot()[:, :, ::-1]
#
#
#     # Caption of the Image
#     with col2:
#         st.image(res_plotted,
#                  caption='Detected Image',
#                  use_column_width=True
#                  )
#
#
#
#
#         # st.write(f"User's IP address: {user_ip}")
#
#         # if user_ip:
#         #     # Use the DbIpCity library to get the user's location
#         #     response = DbIpCity.get(user_ip, api_key='free')
#         #
#         #     # Display the retrieved location information
#         #     st.write("IP Address:", response.ip_address)
#         #     st.write("City:", response.city)
#         #     st.write("Region:", response.region)
#         #     st.write("Country:", response.country)
#         #     st.write("Latitude:", response.latitude)
#         #     st.write("Longitude:", response.longitude)
#         # else:
#         #     st.write("User IP address not provided.")
#
#
# # Location Code
# st.title("Visual Pollution Location")
# st.write("Are you at the same location of the visual pollution?")
# st.caption('If Yes please share your location with us.')
#
#
# def get_user_ip():
#     return requests.get('https://api64.ipify.org/').text
#
#
# user_ip = get_user_ip()
#
# if st.button('Approve Share Your Location'):
#
#         #user_choice = st.radio("Are you at the same location of the visual pollution?", ("Yes", "No"))
#         #user_choice = st.radio("Do you want to fetch your location?", ("Yes", "No"), index=1)
#     if user_ip:
#         # Use the DbIpCity library to get the user's location
#         response = DbIpCity.get(user_ip, api_key='free')
#
#         # Display the retrieved location information
#         st.write("City:", response.city)
#         st.write("Region:", response.region)
#         st.write("Country:", response.country)
#         st.write("Latitude:", response.latitude)
#         st.write("Longitude:", response.longitude)
#     else:
#         st.write("User IP address not provided.")