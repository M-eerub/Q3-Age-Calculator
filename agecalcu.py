# Age Calculator

import streamlit  as st 

from datetime import date

st.title("Age Calculatoor")
input_box = st.number_input("Add your Age ",min_value = 1900, max_value = 2025, step=1)

use_current_date = date.today().year

if input_box > 0:
    age_calculate = use_current_date - input_box
    st.success(f"Your age is {age_calculate}")

else:
    st.error("Please enter correct age")