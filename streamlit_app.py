import streamlit
# this will build the menu 
streamlit.title('👌My Parents New Healthy Dinner.')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & 🥞Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🍳Hard-Boiled Free-Range Egg')

# add another header
streamlit.header('🍌🍓Build your own friut smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#choose the fruit name column as the index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a picklist here so they can pick the fruid they want to include
fruits_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page
#  Let's put a pick list here so they can pick the fruit they want to include
#streamlit.multiselect("Pick some  fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#display the table on the page
streamlit.dataframe(fruits_to_show)
#Lesson 9 - #New Section to display
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
