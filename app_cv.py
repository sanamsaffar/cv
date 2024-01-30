import streamlit as st

def create_cv():
    st.set_page_config(
        page_title="CV Creator",
        page_icon="✨",
        layout="wide"
    )

    st.title("Curriculum Vitae (CV) Creator")

    # Personal Information
    with st.beta_expander("Personal Information"):
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
        with col1:
            first_name = st.text_input("First Name")
        with col2:
            last_name = st.text_input("Last Name")
        with col3:
            email = st.text_input("Email")
        with col4:
            phone = st.text_input("Phone Number")

    # Education
    with st.beta_expander("Education"):
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
        with col1:
            degree = st.text_input("Degree")
        with col2:
            major = st.text_input("Major")
        with col3:
            university = st.text_input("University")
        with col4:
            graduation_year = st.text_input("Graduation Year")

    # Work Experience
    with st.beta_expander("Work Experience"):
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
        with col1:
            job_title = st.text_input("Job Title")
        with col2:
            company = st.text_input("Company")
        with col3:
            start_date = st.text_input("Start Date")
        with col4:
            end_date = st.text_input("End Date")
        job_description = st.text_area("Job Description")

    # Skills
    with st.beta_expander("Skills"):
        skills = st.text_area("List of Skills (comma-separated)")

    # Projects
    with st.beta_expander("Projects"):
        col1, col2 = st.columns([1, 2])
        with col1:
            project_name = st.text_input("Project Name")
        with col2:
            project_description = st.text_area("Project Description")

    # Display the generated CV
    st.title("Generated CV")
    st.write(f"**Name:** {first_name} {last_name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")

    st.subheader("Education")
    st.write(f"**Degree:** {degree}")
    st.write(f"**Major:** {major}")
    st.write(f"**University:** {university}")
    st.write(f"**Graduation Year:** {graduation_year}")

    st.subheader("Work Experience")
    st.write(f"**Job Title:** {job_title}")
    st.write(f"**Company:** {company}")
    st.write(f"**Dates:** {start_date} - {end_date}")
    st.write(f"**Description:** {job_description}")

    st.subheader("Skills")
    st.write(skills)

    st.subheader("Projects")
    st.write(f"**Project Name:** {project_name}")
    st.write(f"**Description:** {project_description}")

if __name__ == '__main__':
    create_cv()
