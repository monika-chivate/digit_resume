import streamlit as st
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import plotly.graph_objects as go
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import tensorflow as tf
from streamlit_player import st_player


with open(r"style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


#####################
# Header
st.write('''
# Jenny O'Connor
##### *Celebrate Every Tiny Victory* 
''')

image = Image.open(r'1597167684746.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I am a senior-level leader who is responsible for driving data-driven insights and reporting initiatives to inform and support key business decisions. I bring a strong background in data analytics and reporting tools, as well as experience in business strategy and project management. 
- I am a strategic thinker with a deep understanding of data analytics and reporting tools. I am passionate about using data to drive business growth and am committed to delivering high-quality insights and reporting to key stakeholders.
- I work closely with cross-functional teams to align data analytics solutions with business goals and objectives, ensuring that our insights and reporting are actionable and impactful.
''')

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/jenny-o-connor-492b4115/" target="_blank">Jenny O'Connor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills"> Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown('## Education 📖', unsafe_allow_html=True)

txt('**LeaderShip**, *Stanford University Graduate School of Business* ','Nov - 2020')

txt('**Master of Business Administration** , *National College of Ireland*, Dublin, leinster',
'Sept 2021-Aug 2023')


#####################
st.markdown('''
## Work Experience
''')
st.subheader('Career snapshot')

with st.spinner(text="Building line"):
    with open(r'timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=600)


#####################
st.markdown('''
## Skills
''')
info = {'skills':[ 'Leadership Management', 'Channel Partners',
'Program Management ', 'Team Work Management', 'Trouble Shooting','Training ',
'Microsoft Excel',' Cloud Computing','Data Strategies','Solution Selling',
'Analytical Skills','Account Management','Data Governance',
'Enterprise Software','Change Management',
'Budgeting','Team Motivation','Customer Relationship Management',
'Software As Service','Enterprise Customer Management','Business Process Management',
'Oracle Business Intelligence Enterprise Edition','Vendor Management','Business Process Management'
                   ]}
skill_col_size = 6

st.markdown('## Tools ⚒️', unsafe_allow_html=True)

def skill_tab():
  rows, cols = len(info['skills']) // skill_col_size, skill_col_size
  skills = iter(info['skills'])
  if len(info['skills']) % skill_col_size != 0:
    rows += 1
  for x in range(rows):
    columns = st.columns(skill_col_size)
    for index_ in range(skill_col_size):
      try:
        columns[index_].button(next(skills))
      except:
        break


with st.spinner(text="Loading section..."):
  skill_tab()
#####################

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/jenny-o-connor-492b4115/')

