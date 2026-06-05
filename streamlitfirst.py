import streamlit as st
import random

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Streamlit Full Properties Demo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# TITLE / TEXT
# -------------------------------------------------
st.title("🚀 Streamlit Complete Demo")

st.header(
    "Header Example",
    divider="rainbow"
)

st.subheader(
    "Subheader Example",
    divider="blue"
)

st.text("Simple Text")

st.write("Write Function")

st.caption("Caption Text")

st.markdown("""
# Markdown H1
## Markdown H2
### Markdown H3

**Bold Text**

*Italic Text*

~~Strike~~

- List 1
- List 2
""")

# -------------------------------------------------
# CODE
# -------------------------------------------------
st.code(
    '''
def hello():
    print("Hello")
''',
    language="python"
)

# -------------------------------------------------
# LATEX
# -------------------------------------------------
st.latex(r'''
a^2 + b^2 = c^2
''')

# -------------------------------------------------
# MESSAGES
# -------------------------------------------------
st.success(
    "Success Message",
    icon="✅"
)

st.error(
    "Error Message",
    icon="🚨"
)

st.warning(
    "Warning Message",
    icon="⚠️"
)

st.info(
    "Info Message",
    icon="ℹ️"
)

# -------------------------------------------------
# BUTTONS
# -------------------------------------------------
st.button(
    "Normal Button",
    type="primary",
    use_container_width=True
)

st.download_button(
    label="Download File",
    data="Hello Streamlit",
    file_name="demo.txt",
    mime="text/plain"
)

st.link_button(
    "Open Google",
    "https://google.com"
)

# -------------------------------------------------
# INPUTS
# -------------------------------------------------
name = st.text_input(
    "Enter Name",
    value="Rohan",
    max_chars=20,
    placeholder="Type here...",
    help="Enter your full name"
)

password = st.text_input(
    "Enter Password",
    type="password",
    placeholder="Password"
)

age = st.number_input(
    "Enter Age",
    min_value=1,
    max_value=100,
    value=18,
    step=1
)

message = st.text_area(
    "Enter Message",
    height=150,
    max_chars=200,
    placeholder="Write something..."
)

date = st.date_input(
    "Select Date"
)

time = st.time_input(
    "Select Time"
)

# -------------------------------------------------
# SELECTION
# -------------------------------------------------
gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"],
    horizontal=True
)

course = st.selectbox(
    "Select Course",
    ["Python", "Java", "MERN"],
    index=0
)

skills = st.multiselect(
    "Select Skills",
    ["HTML", "CSS", "JS", "React", "Node"],
    default=["React"],
    max_selections=2
)

rating = st.slider(
    "Rate Us",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

experience = st.select_slider(
    "Experience Level",
    options=[
        "Beginner",
        "Intermediate",
        "Advanced"
    ],
    value="Intermediate"
)

color = st.color_picker(
    "Pick Color",
    "#00f900"
)

# -------------------------------------------------
# CHECKBOX
# -------------------------------------------------
agree = st.checkbox(
    "I Agree Terms",
    value=False
)

# -------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload File",
    type=["png", "jpg", "pdf", "txt", "mp3"],
    accept_multiple_files=False
)

# -------------------------------------------------
# IMAGE
# -------------------------------------------------
# st.image(
#     uploaded_file,
#     width=400     
# )

# -------------------------------------------------
# AUDIO
# -------------------------------------------------
# audio_file = open(str(uploaded_file),'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format='audio/mp3', start_time=0)

# -------------------------------------------------
# AUDIO
# -------------------------------------------------
# st.video('https://www.youtube.com/watch?v=7nGN11DW-b0')

# -------------------------------------------------
# CAMERA
# -------------------------------------------------
camera = st.camera_input(
    "Take Picture"
)

# -------------------------------------------------
# METRICS
# -------------------------------------------------
st.metric(
    label="Revenue",
    value="$5000",
    delta="$500"
)

# -------------------------------------------------
# PROGRESS
# -------------------------------------------------
progress = st.progress(0)

for i in range(100):
    progress.progress(i + 1)

# -------------------------------------------------
# SPINNER
# -------------------------------------------------
with st.spinner("Loading Data..."):
    pass

# -------------------------------------------------
# STATUS
# -------------------------------------------------
with st.status("Processing...", expanded=True) as status:
    st.write("Step 1 Completed")
    st.write("Step 2 Completed")
    status.update(
        label="Completed",
        state="complete"
    )

# -------------------------------------------------
# BALLOONS / SNOW
# -------------------------------------------------
if st.button("Show Balloons"):
    st.balloons()

if st.button("Show Snow"):
    st.snow()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("Sidebar")

st.sidebar.write("Sidebar Content")

sidebar_name = st.sidebar.text_input(
    "Sidebar Input"
)

# -------------------------------------------------
# COLUMNS
# -------------------------------------------------
col1, col2, col3 = st.columns(
    3,
    gap="medium"
)

with col1:
    st.write("Column 1")

with col2:
    st.write("Column 2")

with col3:
    st.write("Column 3")

# -------------------------------------------------
# TABS
# -------------------------------------------------
tab1, tab2, tab3 = st.tabs(
    ["Tab 1", "Tab 2", "Tab 3"]
)

with tab1:
    st.write("Inside Tab 1")

with tab2:
    st.write("Inside Tab 2")

with tab3:
    st.write("Inside Tab 3")

# -------------------------------------------------
# EXPANDER
# -------------------------------------------------
with st.expander(
    "See More",
    expanded=False
):
    st.write("Hidden Content")

# -------------------------------------------------
# CONTAINER
# -------------------------------------------------
with st.container(border=True):
    st.write("Inside Container")

# -------------------------------------------------
# EMPTY
# -------------------------------------------------
placeholder = st.empty()

placeholder.write("Placeholder Content")

# -------------------------------------------------
# DATA
# -------------------------------------------------
data = {
    "Name": ["Rohan", "Aman", "Rahul"],
    "Age": [21, 22, 23],
    "Course": ["MERN", "Python", "Java"]
}

st.table(data)

st.dataframe(
    data,
    use_container_width=True
)

st.json(data)

# -------------------------------------------------
# CHARTS
# -------------------------------------------------
chart_data = {
    "Jan": random.randint(10, 100),
    "Feb": random.randint(10, 100),
    "Mar": random.randint(10, 100),
    "Apr": random.randint(10, 100)
}

st.line_chart(chart_data)

st.bar_chart(chart_data)

st.area_chart(chart_data)

# -------------------------------------------------
# MAP
# -------------------------------------------------
map_data = {
    "lat": [22.7196, 28.7041],
    "lon": [75.8577, 77.1025]
}

st.map(
    map_data,
    zoom=4
)

# -------------------------------------------------
# FORM
# -------------------------------------------------
with st.form(
    "registration_form",
    clear_on_submit=False
):
    username = st.text_input("Username")

    email = st.text_input("Email")

    submit = st.form_submit_button(
        "Register",
        type="primary"
    )

    if submit:
        st.success("Form Submitted")

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(
    "Counter:",
    st.session_state.count
)

# -------------------------------------------------
# DIVIDER
# -------------------------------------------------
st.divider()

# -------------------------------------------------
# STOP
# -------------------------------------------------
# st.stop()

# -------------------------------------------------
# FINAL
# -------------------------------------------------
st.write("🎉 Streamlit Full Demo Completed")