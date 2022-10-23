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
#Lesson 9 - #New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output to the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
streamlit.text("The Fruit load list contains")
streamlit.text(my_data_row)
