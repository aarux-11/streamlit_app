import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector as sql
import pymongo
from googleapiclient.discovery import build
from PIL import Image


# SETTING PAGE CONFIGURATIONS
#icon = Image.open("https://github.com/aarux-11/streamlit_app/blob/main/Youtube_logo.png")
st.set_page_config(page_title= "Youtube Data Project - Aarushi",
                   page_icon= "house-door-fill",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """This project is for submission purposes to GUVI only"""})

# CREATING OPTION MENU
with st.sidebar:
    selected = option_menu(None, ["Home","Extract & Transform","View"], 
                           icons=["house-door-fill","tools","card-text"],
                           default_index=0,
                           orientation="vertical",
                           styles={"nav-link": {"font-size": "20px", "text-align": "centre", "margin": "0px", 
                                                "--hover-color": "#A72283"},
                                   "icon": {"font-size": "20px"},
                                   "container" : {"max-width": "5000px"},
                                   "nav-link-selected": {"background-color": "#A72283"}})
