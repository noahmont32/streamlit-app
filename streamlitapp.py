import streamlit as st
import numpy as np

st.title('VOLTAGE CALCULATOR')
st.subheader('Built by Noah Monteforte')

V = (st.number_input('What is the voltage? '))

x = (st.number_input('How many resistors are there? '))

if x == 1:
    R = (st.number_input('What is the resistance of the resistor? '))
    I = V / R
    num = round(I, 2)
    st.text('The current is' + ' ' + str(num) + 'A')

elif x > 1:
    y = (st.text_input('What are the resistances? (Seperate by spaces): ')).split()
    y = [float(i) for i in y]
    if len(y) != x:
        st.text('Please enter one and only one resistance for every resistor present.')
        y = [int(i) for i in y]
    B = sum(y)
    I = V / B
    num = round(I, 2)
    st.text('The current is' + ' ' + str(num) + 'A')

    # Voltage Drop
    vd = []
    nv = []
    for j in y:
        nv = I * j
        Nv = round(nv, 2)
        vd.append(Nv)
        st.text('The Voltage drop off across the resistors in order are:' + str(Nv) + 'V')

    import matplotlib.pyplot as plt

    figure, ax = plt.subplots()
    plt.plot(np.arange(x), vd)
    plt.title('Voltage Drop Across Resistors')
    plt.xlabel('Resistors')
    plt.xscale('linear')
    plt.ylabel('Voltage Drops')
    plt.tight_layout()
    st.pyplot(figure)

import schemdraw
from schemdraw import elements as elm

st.sidebar.write('This is a basic circuit drawing using schemdraw')
with st.sidebar.expander('Click here to see the code'):
    st.sidebar.code(""" 

with schemdraw.Drawing() as d:
    d += elm.Resistor().label('100KΩ')
    d += elm.Capacitor().down().label('0.1μF', loc='bottom')
    d += elm.Line().left()
    d += elm.Ground()
    d += elm.SourceV().up().label('10V')
    d.draw()

                        """)

st.sidebar.image('Desktop/Figure_1.jpg')