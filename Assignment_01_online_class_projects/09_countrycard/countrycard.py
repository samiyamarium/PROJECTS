import streamlit as st
import requests

# Set up the page configuration
st.set_page_config(page_title="Country Information Card", page_icon="🌍",layout="centered")

# App title
st.title("🌍 Country Information Card ")

# Country input
country_name = st.text_input("Enter a country name", "")

# Fetch and display country information
if country_name:
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        name = data.get('name', {}).get('common', 'N/A')
        capital = data.get('capital', ['N/A'])[0]
        region = data.get('region', 'N/A')
        population = data.get('population', 'N/A')
        languages = ', '.join(data.get('languages', {}).values()) if 'languages' in data else 'N/A'
        currencies = ', '.join([v.get('name', 'N/A') for v in data.get('currencies', {}).values()]) if 'currencies' in data else 'N/A'
        flag_url = data.get('flags', {}).get('png', '')
        area=data.get('area','N/A')
        landmark=data.get('landmark','N/A')
        # Display country information
        st.image(flag_url, caption=f"Flag of {name}", width=200)
        st.subheader(f"Information for {name}")
        st.write(f"**Capital:** {capital}")
        st.write(f"**Region:** {region}")
        st.write(f"**Landmark:** {landmark}")
        st.write(f"**Population:** {population}")
        st.write(f"**Languages:** {languages}")
        st.write(f"**Currencies:** {currencies}")
        st.write(f"**Area:** {area}")
    else:
        st.error("Country not found. Please check the spelling.")
