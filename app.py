import streamlit as st
import requests

# Defining Page Title,Icon
st.set_page_config(
    page_title="Quotify",
    page_icon="icon.png",
    menu_items={
        "About":"Welcome to Quotify, your go-to source for generating quotes on a wide range of topics! Whether you need a quote about love, life, success, humor, or any other category, Quotify has you covered. Simply choose your desired category and get a fresh quote in seconds. Perfect for adding a touch of wisdom, humor, or insight to your day, social media posts, or projects. Discover, share, and enjoy the power of words with Quotify!"
    }
)

lst=["age","alone","amazing","anger","architecture","art","attitude","beauty","best","birthday","business","car","change","communication","computers","cool","courage","dad","dating","death","design","dreams","education","environmental","equality","experience","failure","faith","family","famous","fear","fitness","food","forgiveness","freedom","friendship","funny","future","god","good","government","graduation","great","happiness","health","history","home","hope","humor","imagination","inspirational","intelligence","jealousy","knowledge","leadership","learning","legal","life","love","marriage","medical","men","mom","money","morning","movies","success",]

catgo={}
for i in lst:
    catgo[i.capitalize()]=i

st.write("<h2 style=color:#EF5A6F;font-size:32px;>Generate Quotes Effortlessly for Every Occasion.</h2>",unsafe_allow_html=True)

category=st.selectbox("Choose a Category",catgo.keys())

btn=st.button("Generate")
if btn:
    try:
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(catgo[category])
        response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
        if response.status_code == requests.codes.ok:
            data=response.json()[0]
            st.write(f"<h3 style=font-size:25px;color:orange;>“{data['quote']}”</h3>",unsafe_allow_html=True)
            st.write(f"<h4 style=text-align:right;font-size:24px;color:lightgreen;>~ {data['author']}</h4>",unsafe_allow_html=True)
    except:
        st.error("Network Error")