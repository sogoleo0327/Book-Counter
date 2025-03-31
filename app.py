from streamlit_extras.let_it_rain import rain
import streamlit as st
st.title("Library")
options=["I bought a book.","I read a book."]
dropdown=st.selectbox("Which option do you want to choose from below?",options,index=None)
if dropdown=="I bought a book.":
    name=st.text_input("Enter the name of your book:")
    author=st.text_input("Enter the author of your book:")
    date=st.date_input("When did you finish this book:")
    if date and author and name:
        st.balloons()
        rain(
        emoji="✨",  
        font_size=54,
        falling_speed=3,
        animation_length="200",
        )
elif dropdown=="I read a book.":
    place=["I read the book at Barnes and Noble.","I read the book at the Public Library.","I read this book at home."]
    place_selected=st.selectbox("Where did you read that book?",place,index=None)  
    book_name=st.text_input("Which book did you read?")
    book_liking=st.text_input("Did you like that book?")
    book_rating=st.number_input("What do you rate it from 1-5?",min_value=1,max_value=5,step=1)
    stars="🌟"*book_rating
    st.write(f"{stars}")    
    if book_rating>=3:
        st.balloons()
        rain(
        emoji="✨",  
        font_size=54,
        falling_speed=3,
        animation_length="200",
        )