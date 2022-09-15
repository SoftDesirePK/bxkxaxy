import streamlit as st
from deta import Deta
import datetime


# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("example-db")

# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items
#st.write(db_content)
st.table(db_content)

