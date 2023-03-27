import streamlit as st
import pandas as pd
from io import StringIO

st.image('./LOGO_091622.png')
st.header('SITUS, By Edy Quin')
st.subheader('Real Tech Management')

# uploaded_file = st.file_uploader("Choose a file")
# if uploader_file is not None:
    # To read file as bytes:
   # byte_data = uploaded_file.getvalue()
    # st.write(bytes_data)

uploaded_files = st.file_uploader("Choose files to upload", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
   # st.write(bytes_data)

# To convert to a stringbased IO:
    strongio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    
    st.write(stringio)
    
    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
    
    # Can be used wherever a "file like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

# Camera input

photo_1 = st.camera_input("Take photo 1")

if photo_1:
    st.image(photo_1)

photo_2 = st.camera_input("Takee photo 1")

if photo_2:
    st.image(photo_2)

photo_3 = st.camera_input("Takee photo 1")

if photo_3:
    st.image(photo_3)
    
photo_4 = st.camera_input("Takee photo 1")

if photo_4:
    st.image(photo_4)
    
photo_5 = st.camera_input("Takee photo 1")

if photo_5:
    st.image(photo_5)


# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
db = deta.Base("SITUS")

# If the user clicked the submit button
# write the data from the form to the database.
# You can store any data you want here. Just modify the dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "address": address, "date": date, "manager": manager, 
            "q1": qone, "q2": qtwo, "q3": qthree})
    if submitted:
        st.write("Your reports has been successfully received. For any questions or concerns please contact the office @ equin@assetmana.com. Please close your browser when you are finished.")
"---"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch(query=None, limit=None, last=None).items
