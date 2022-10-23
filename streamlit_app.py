import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
# this will build the menu 
streamlit.title('👌My Parents New Healthy Dinner.')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & 🥞Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🍳Hard-Boiled Free-Range Egg')

# add another header
streamlit.header('🍌🍓Build your own friut smoothie')
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
#create the repeatable code block (function)
def get_fruityvice_data(fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return  fruityvice_normalized

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()   

#streamlit.stop()
streamlit.write('The user entered', fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output to the screen as a table
streamlit.dataframe(fruityvice_normalized)
#don't runm anything past here while we fix the code

streamlit.header("The Fruit load list contains")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("use warehouse pc_rivery_wh") 
        my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list;")
        return my_cur.fetchall()
        #my_data_rows = my_cur.fetchall()
        
#add a button to load the fruit
if streamlit.button ('Get Fruid Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
#Allow the user to add a fruit to the list
fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for entering', fruit_choice)
my_cur.execute ("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
