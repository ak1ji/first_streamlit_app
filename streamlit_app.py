import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬Kale, Spinach,& Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

# create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

# New section to display fruityvice api response, # import requests
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error ("Please select a fruit to get iformation.")
  else: 
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
 
# except URLError as e:
#    streamlit.error()

# don't run anything past here while we troubleshoot
# requirements.txt
#import snowflake.connector

#streamlit.dataframe(my_data_row)
# Snowflake-related functions
#def get_fruit_load_list():
#   with my_cnx.cursor() as my_cur
#   my_cur.execute("select * from fruit_load_list")
#   returm my_cur.fetchall()
 
#streamlit.stop()
# Add a button to load the fruit
 #  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 #  my_data_rows = get_fruit_load_list()
 #  streamlit.dataframe(my_data_rows)



# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# my_data_row = my_cur.fetchall() moved to func

#streamlit.text("Hello from Snowflake:") 
#streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row)
#streamlit.dataframe(my_data_row)



# Allow the end user to add a fruit to the list
#def insert_row_snowflake (new_fruit)
#    with my_cnx.cursor() as my_cur
#       my_cur.execute("insert into fruit_load_list values ('from strealit')")
#       return "Thanks for adding" + new_fruit  

#Add_my_fruit =  streamlit.text_input("What fruit would you like o add? ")  
# if streamlit.button ('add fruit to the list'):
#       my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#       back_from_function = insert_row_snowflake(add_my_fruit)
#       streamlit.text(back from function)


# streamlit.write('Thank you for adding ', add_my_fruit)
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
# my_cur.execute("insert into fruit_load_list values ('from strealit')")
