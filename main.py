import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Streamlit Demo")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is some text")

# Markdown
st.markdown("This is some **markdown**")

# Code
st.code("print('This is some code')")

# Dataframe
data = {'Name': ['John', 'Jane', 'Mike'],
    'Age': [25, 30, 35]}
df = pd.DataFrame(data)
st.dataframe(df)

# Plot
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot(plt)

# Checkbox
checkbox = st.checkbox("Check me!")
if checkbox:
    st.write("Checkbox is checked")

# Selectbox
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)

# Slider
slider = st.slider("Select a value", 0, 10)
st.write("Slider value:", slider)

# Button
button = st.button("Click me!")
if button:
    st.write("Button clicked")

# File uploader
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write("File uploaded")

# Progress bar
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.text("This is a sidebar")

# Expander
with st.expander("Click to expand"):
    st.write("This is some hidden content")
