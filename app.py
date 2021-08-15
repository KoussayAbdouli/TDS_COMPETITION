import streamlit as st
import numpy as np
import datetime
import base64
import os
from path import Path
import numpy as np
import requests
from bs4 import BeautifulSoup
URL = 'https://www.worldometers.info/coronavirus/country/tunisia/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
job_elems = soup.find_all('div', class_='maincounter-number')
d = {}
d["Coronavirus Cases:"] = job_elems[0].text
d["Deaths:"] = job_elems[1].text
d["Recovered:"] = job_elems[2].text




url1 = "https://covid19.who.int/region/emro/country/tn/"
page1 = requests.get(url1)

soup1 = BeautifulSoup(page1.content, 'html.parser')
j = soup1.find_all('span')

d["Vaccinated:"] = j[10].text.split(" ")[0]




def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

st.set_page_config(layout="wide",page_title="Government Indicators",page_icon="./images/joumhouria.png")
st.markdown("<h1 style='text-align: center;'>🇹🇳 Government Covid19 Indicators</h1>", unsafe_allow_html=True)


col1, col2, col3 = st.sidebar.beta_columns(3)

col1.write("")

col2.markdown(
        """
        [<img src='data:image/png;base64,{}' class='center' width=100>](http://www.tunisie.gov.tn/)""".format(
            img_to_bytes("images/gov.png")
        ),

        unsafe_allow_html=True)
col3.write("")
date = st.sidebar.date_input("Today:", datetime.date.today())
st.sidebar.subheader("Improve The Public Trust:")
st.sidebar.subheader("")
st.sidebar.markdown("---")
st.sidebar.subheader("Media Communication:")
com = st.sidebar.selectbox(
    "",
    (   "None",
        "Text",
        "Image",
        "Video"
    )
)
st.sidebar.subheader("Economic Decisions:")
st.sidebar.selectbox(
    "",
    (
        "Fiscalité",
        "Work Hours Reduction"
        "crédit",
    )
)
st.sidebar.subheader("Social Decisions:")
st.sidebar.selectbox(
    "",
    (
        "Grants",
    )
)
st.sidebar.subheader("General Policies:")
st.sidebar.selectbox(
    "",
    (
        "Lockdown",
        "mitigation"
    )
)
st.markdown("---")
st.subheader("")
st.subheader("")
s = st.beta_columns(4)
s[0].markdown(f"<h1 style='border: 2px solid red'><center>Covid Cases: <br><br>{d['Coronavirus Cases:']}</center></h1>",unsafe_allow_html=True)
s[1].markdown(f"<h1 style='border: 2px solid #808284'><center>Deaths: <br><br>{d['Deaths:']}</center></h1>",unsafe_allow_html=True)
s[2].markdown(f"<h1 style='border: 2px solid green'><center>Recovered: <br><br>{d['Recovered:']}</center></h1>",unsafe_allow_html=True)
s[3].markdown(f"<h1 style='border: 2px solid yellow'><center>Vaccinated: <br><br>{d['Vaccinated:']}</center></h1>",unsafe_allow_html=True)

s = st.beta_columns(4)


st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")
s = st.beta_columns(2)
trust = np.random.randn(100)
covid = np.random.randn(100)
st.markdown("---")
s = st.beta_columns(2)
s[0].markdown("<h1 style='text-align: center;'>Government Public Trust related to Covid-19</h1>", unsafe_allow_html=True)
s[1].markdown("<h1 style='text-align: center;'>Covid-19 cases Evolution</h1>", unsafe_allow_html=True)

s = st.beta_columns(2)

s[0].line_chart(trust)
s[1].line_chart(covid)

if com=="Text":
    p = st.beta_columns(2)
    p[0].subheader("Test Your Script:")
    p[0].text_area("",height=500)
    p[0].markdown("<center><button>Test Scipt!</button></center>",unsafe_allow_html=True)
    p[1].subheader("")
    p[1].subheader("")
    p[1].subheader("")
    p[1].subheader("")
    p[1].subheader("")
    p[1].subheader("")
    p[1].subheader("")
    p[1].subheader("")
    p[1].subheader("")
    p[1].markdown("<h1>✔️</h1>",unsafe_allow_html=True)
    p[1].markdown(
        """
        [<img src='data:image/png;base64,{}' class='center' width=40 >](http://www.tunisie.gov.tn/)""".format(
            img_to_bytes("images/cancel.png")
        ),

        unsafe_allow_html=True)


if com=="Image":
    p = st.beta_columns(2)
    p[0].subheader("Test Your Poster:")
    uploaded_image = p[0].file_uploader('Choose your Poster:', type=["png","jpg"])
    if (uploaded_image is not None):

        file_details = {"FileName": uploaded_image.name, "FileType": uploaded_image.type}

        with open(os.path.join("tempDir", uploaded_image.name), "wb") as f:
            f.write(uploaded_image.getbuffer())
    p[1].subheader("")
    p[1].subheader("")
    p[1].markdown("<h1>✔️</h1>",unsafe_allow_html=True)
    p[1].markdown(
        """
        [<img src='data:image/png;base64,{}' class='center' width=30 >](http://www.tunisie.gov.tn/)""".format(
            img_to_bytes("images/cancel.png")
        ),

        unsafe_allow_html=True)
if com=="Video":
    p = st.beta_columns(3)
    p[0].subheader("Choose the Date")
    p[0].date_input("",datetime.datetime.now())
    p[1].subheader("Choose the Time")
    p[1].text_input("")
    p[2].subheader("Choose The speaker")
    p[2].selectbox(
        " ",
        (
            "Mr. X",
            "Mrs. Y",
            "Mr. Z",
        )
    )


