import streamlit as st

def create_cv():
    st.title("Curriculum Vitae (CV) Creator")

    # Personal Information
    st.header("Personal Information")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

    # Education
    st.header("Education")
    degree = st.text_input("Degree")
    major = st.text_input("Major")
    university = st.text_input("University")
    graduation_year = st.text_input("Graduation Year")

    # Work Experience
    st.header("Work Experience")
    job_title = st.text_input("Job Title")
    company = st.text_input("Company")
    start_date = st.text_input("Start Date")
    end_date = st.text_input("End Date")
    job_description = st.text_area("Job Description")

    # Skills
    st.header("Skills")
    skills = st.text_area("List of Skills (comma-separated)")

    # Projects
    st.header("Projects")
    project_name = st.text_input("Project Name")
    project_description = st.text_area("Project Description")

    # Display the generated CV
    st.header("Generated CV")
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

# Run the application
if __name__ == '__main__':
    create_cv()
