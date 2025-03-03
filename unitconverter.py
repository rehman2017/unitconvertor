import streamlit as st

class UnitConverter:
    conversion_factors = {
        "length": {
            "meters": 1.0,
            "kilometers": 0.001,
            "miles": 0.000621371,
            "feet": 3.28084,
            "inches": 39.3701
        },
        "weight": {
            "grams": 1.0,
            "kilograms": 0.001,
            "pounds": 0.00220462,
            "ounces": 0.035274
        },
        "temperature": {},  # Special case
        "time": {
            "seconds": 1.0,
            "minutes": 1/60,
            "hours": 1/3600,
            "days": 1/86400
        }
    }

    @staticmethod
    def convert(value, from_unit, to_unit, category):
        if category not in UnitConverter.conversion_factors:
            raise ValueError("Invalid category")
        
        if category == "temperature":
            return UnitConverter.convert_temperature(value, from_unit, to_unit)
        
        if from_unit not in UnitConverter.conversion_factors[category] or to_unit not in UnitConverter.conversion_factors[category]:
            raise ValueError("Invalid unit")
        
        base_value = value / UnitConverter.conversion_factors[category][from_unit]
        converted_value = base_value * UnitConverter.conversion_factors[category][to_unit]
        return converted_value

    @staticmethod
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        if from_unit == "celsius":
            if to_unit == "fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "kelvin":
                return value + 273.15
        elif from_unit == "fahrenheit":
            if to_unit == "celsius":
                return (value - 32) * 5/9
            elif to_unit == "kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin":
            if to_unit == "celsius":
                return value - 273.15
            elif to_unit == "fahrenheit":
                return (value - 273.15) * 9/5 + 32
        
        raise ValueError("Invalid temperature unit")

st.title("Unit Converter")
category = st.selectbox("Select category", ["length", "weight", "temperature", "time"])
value = st.number_input("Enter value", min_value=0.0, format="%.6f")

if category:
    from_unit = st.selectbox("From unit", list(UnitConverter.conversion_factors[category].keys()))
    to_unit = st.selectbox("To unit", list(UnitConverter.conversion_factors[category].keys()))
    
    if st.button("Convert"):
        try:
            result = UnitConverter.convert(value, from_unit, to_unit, category)
            st.success(f"{value} {from_unit} = {result} {to_unit}")
        except Exception as e:
            st.error(f"Error: {e}")