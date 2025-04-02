import streamlit as st

st.title('Unit Converter')

option = st.selectbox('Select conversion type:', ('Length', 'Weight', 'Temperature'))

if option == 'Length':
    st.subheader('Length Conversion')
    length = st.number_input('Enter length in meters:', min_value=0.0, format="%.2f")
    choice = st.radio('Convert to:', ('Kilometers', 'Centimeters', 'Millimeters'))
    if st.button('Convert'):
        if choice == 'Kilometers':
            result = length / 1000
            unit = 'km'
        elif choice == 'Centimeters':
            result = length * 100
            unit = 'cm'
        else:
            result = length * 1000
            unit = 'mm'
        st.success(f'{length} meters is equal to {result} {unit}')

elif option == 'Weight':
    st.subheader('Weight Conversion')
    weight = st.number_input('Enter weight in kilograms:', min_value=0.0, format="%.2f")
    choice = st.radio('Convert to:', ('Grams', 'Pounds', 'Ounces'))
    if st.button('Convert'):
        if choice == 'Grams':
            result = weight * 1000
            unit = 'g'
        elif choice == 'Pounds':
            result = weight * 2.20462
            unit = 'lbs'
        else:
            result = weight * 35.274
            unit = 'oz'
        st.success(f'{weight} kg is equal to {result} {unit}')

elif option == 'Temperature':
    st.subheader('Temperature Conversion')
    temperature = st.number_input('Enter temperature in Celsius:', format="%.2f")
    choice = st.radio('Convert to:', ('Fahrenheit', 'Kelvin'))
    if st.button('Convert'):
        if choice == 'Fahrenheit':
            result = (temperature * 9/5) + 32
            unit = '°F'
        else:
            result = temperature + 273.15
            unit = 'K'
        st.success(f'{temperature}°C is equal to {result} {unit}')