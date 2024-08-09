import streamlit as st
import time

# Layout Columns
st.header('Columns: st.columns')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('columns-1')
    st.image('./media/image.jpg')

with col2:
    st.subheader('column-2')
    st.image('./media/image.jpg')

with col3:
    st.subheader('column-3')
    st.image('./media/image.jpg')


# expander
st.header('Expander: st.expander')

with st.expander('Some explanation'):
    st.write("""
             Insert a multi-element container that can be expanded/collapsed.

Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed by the user. 
When collapsed, all that is visible is the provided label.
    """)
    st.code("""
# you create expander with st.write

import streamlit as st
st.exander('message')
            
            """, language='python')


# container
st.header('Container st.container')

with st.container():
    st.write('you are inside the container')

# Empty

st.header('Empty: st.empty')

placeholder = st.empty()

for i in range(1, 11):
    placeholder.write('This message will disappear in {} seconds'.format(10-i))
    time.sleep(1)

placeholder.empty()
