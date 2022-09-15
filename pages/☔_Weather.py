
# Modules
import streamlit as st
import requests
from datetime import datetime , timedelta
import pandas as pd
#import matplotlib.pyplot as plt
import time 
import os
import pathlib
#import datetime


# INSERT YOUR API  KEY WHICH YOU PASTED IN YOUR secrets.toml file 
#api_key =  st.secrets["api_key"]
api_key = "7dbe7341764f682c2242e744c4f167b0"

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
url_1 = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}&appid={}'

city = st.sidebar.selectbox('Select City', ['Riyadh', 'Jeddah' ,'Lahore', 'Karachi', 'Islamabad', 'Faisalabad'])
show_hist = st.checkbox('Show me history')
st.header('Weather Report for '+ city)   
#st.markdown('https://openweathermap.org/api') 

# Function for LATEST WEATHER DATA
def getweather(city):
    result = requests.get(url.format(city, api_key))     
    if result:
        json = result.json()
        #st.write(json)
        country = json['sys']['country']
        temp = json['main']['temp'] - 273.15
        temp_feels = json['main']['feels_like'] - 273.15
        humid = json['main']['humidity'] - 273.15
        icon = json['weather'][0]['icon']
        lon = json['coord']['lon']
        lat = json['coord']['lat']
        des = json['weather'][0]['description']
        sunrise = country = json['sys']['sunrise']
        sunset = country = json['sys']['sunset']

        res = [country, round(temp,1),round(temp_feels,1),
                humid,lon,lat,icon,des,sunrise,sunset]
        return res , json
    else:
        print("error in search !")

#getweather(city)

# Function for HISTORICAL DATA
def get_hist_data(lat,lon,start):
    res = requests.get(url_1.format(lat,lon,start,api_key))
    data = res.json()
    temp = []
    for hour in data["hourly"]:
        t = hour["temp"]
        temp.append(t)     
    return data , temp

# Let's write the Application


im1,im2 = st.columns(2)
with im2:  
    #currentDir= os.path.abspath(os.path.dirname(__file__))  # gets the current pytho file, SendEmail.py and returns absolute path (parent directory)
    #filepath=os.path.join(currentDir,"download.jpg")
    #image0 = os.path.join(currentDir,"random4.png") 
    image0 = "./images/"+city+".jpg"
    #cwd = pathlib.Path.cwd()
    #filepath = cwd / "random4.jpg"
    #image0 = filepath
    st.image(image0,use_column_width=True,caption = '' + city)
with im1:    
    image1 = './images/OPENWEATHER.png'
    st.image(image1, caption='Data Source: Open Weather Map API',use_column_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    city_name = city
    #st.write(city)
    #show_hist = st.checkbox('Show me history')
with col2:  
		if city_name:
		        res , json = getweather(city_name)
		        #st.write(res)
		        st.success('Current: ' + str(round(res[1],2)))
		        st.info('Feels Like: ' + str(round(res[2],2)))
		        #st.info('Sunrise: ' + str(datetime.datetime.fromtimestamp(res[8])))
		        #st.info('Sunset: ' + str(datetime.datetime.fromtimestamp(res[9])))

		        
                #st.info('Humidity: ' + str(round(res[3],2)))
		        st.subheader('Status: ' + res[7])
		        web_str = "![Alt Text]"+"(http://openweathermap.org/img/wn/"+str(res[6])+"@2x.png)"
		        st.markdown(web_str)  



if city_name:        
    show_hist = st.expander(label = 'Last 5 Days History')
    with show_hist:
            start_date_string = st.date_input('Current Date')
            #start_date_string = str('2021-06-26')
            date_df = []
            max_temp_df = []
            for i in range(5):
                        date_Str = start_date_string - timedelta(i)
                        start_date = datetime.strptime(str(date_Str),"%Y-%m-%d")
                        timestamp_1 = datetime.timestamp(start_date)
                        #res , json = getweather(city_name)
                        his , temp = get_hist_data(res[5],res[4],int(timestamp_1))
                        date_df.append(date_Str)
                        max_temp_df.append(max(temp) - 273.5)
                
            df = pd.DataFrame()
            df['Date'] = date_df
            df['Max temp'] = max_temp_df
            st.table(df)

st.map(pd.DataFrame({'lat' : [res[5]] , 'lon' : [res[4]]},columns = ['lat','lon']))
