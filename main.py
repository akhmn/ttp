import streamlit as st
st.title("Detect power of your lens")
st.text('Welcome to this website. This Website can tell you about your power of your lens ')
st.text ('just by entering your far point or near point value if you have ')
st.header("How does it works:")
st.text("Firstly enter how far can see based on options provided based on that you will ")
st.text("be able to know if you are suffering from myopia or hypermetropia . Then enter")
st.text(" your near point or far point value which you have and proceeding that you will")
st.text(" bw able to know the power of your eye")
st.selectbox('How far can u see',('not able to see near oject clearly','not able to see far object','trouble to see far as well as near object'))
q=st.number_input("Enter your far point value if you have")
e=st.number_input("Enter your near point value if you have")

option = st.selectbox('what would u like to check',
    ('hypermetropia', 'myopia', 'presbiopia'))
if option == "hypermetropia":
    if e > 25 :
        st.write("you are suffering from hypermetropia")
        g = ((1 / e) - (1 / 25))
        st.write("your power is", g)

    else :
        st.write("you are not suffering from hypermetropia")
if option == "myopia":
    if q<19 :
        st.write("you are suffering from myopia")
        c = float(- (1 / q))
        st.write("your power is", c)
if option== "presbiopia":
    if (e>25)and(q<19):
        st.write("you are suffering from prebiopia")
        f=g+e
        st.write("your power is",f)









