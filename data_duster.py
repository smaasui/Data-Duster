import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="Data Duster", 
    page_icon="🇵🇸", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://www.google.com/search?q=help",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": """# SMAASU Corporation©️  
        https://tinyurl.com/smaasu"""}
    )

# Sidebar
st.sidebar.title("🛠️ DataSet Duster")
tabs = st.sidebar.radio("", ["DataSet Dusting", "About App", "About Us", "About Me"])

if tabs == "DataSet Dusting":
    st.write("# 🌍 SMAASU's DataSet Duster ! 🥋")
    files = st.file_uploader("Upload", type=["csv", "xlsx"], accept_multiple_files=True)
    for file in files:
        # Convert file to pandas dataframe
        file_ext = os.path.splitext(file.name)[-1].lower()
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.write(f"Error {file_ext} is not supported 🤪")
        
        
        st.write(f"**Name :** {file.name}")
        st.write(f"**Size :** {file.size/1024:.2f} KB")
        # st.write(f"**Description :** {file.description}")
        # see_df = st.checkbox("Preview DataSet")
        if st.checkbox("Preview DataSet"):
            #df = pd.read_csv(file)
            st.dataframe(df.head())
        st.write("# Data Cleaning")
        if st.checkbox("Clean DataSet"):
            col1, col2, col3 = st.columns([1,1,2])
            with col1:
                if st.checkbox("Clean Duplicates"):
                    st.write(f"**Rows Before** {df.size/len(df.columns)}")
                    df.drop_duplicates(inplace=True)
                    st.write(f"**Rows After** {df.size/len(df.columns)}")
                    st.success("All Duplicates were successfully Cleaned up", icon="😇")
            with col2:
                if st.checkbox("Clean Nully Values"):
                    st.write(f"**Rows Before** {df.size/len(df.columns)}")
                    df.dropna(inplace=True)
                    # z  len(df.columns)
                    st.write(f"**Rows After** {df.size/len(df.columns)}")
                    st.success("All Nully were successfully Dusted up", icon="😎")
            with col3:
                if st.checkbox("Clean Missing Values"):
                    col3_1, col3_2 = st.columns(2)
                    with col3_1:
                        st.write("**Null Before After**")
                        num_col = df.select_dtypes('number').columns
                        for col in num_col:  # Assuming num_col is a list of numerical column names
                            st.write(f"**{" ".join(word.capitalize() for word in col.split())}**: {df[col].isnull().sum()}")
                    with col3_2:
                        st.write("**Null Value After**")
                        df[num_col] = df[num_col].fillna(df[num_col].mean())
                        for col in num_col:  # Assuming num_col is a list of numerical column names
                            st.write(f"**{" ".join(word.capitalize() for word in col.split())}**: {df[col].isnull().sum()}")
                    st.success("All Missing Values were successfully Filled up", icon="🎉")

        #Select the Columns to remain  
        st.header("Select Column")
        elect_col = st.multiselect("Select Column :", options=df.columns, default=df.columns)
        df = df[elect_col]  
        st.write(df.head(5))

        #Visualize any columns
        st.header("Select any two columns to visualize")
        if st.checkbox("Select any two columns to visualize"):
            #visual_col = st.multiselect("Select any two columns to visualize", df.columns, default=df.columns)
            st.bar_chart(df.select_dtypes('number').iloc[:,:2] )

        conversion_type = st.radio("Click to convert the file format !", ["csv", "xlsx"])
        if st.button("Just Convert It"):
            buffer = BytesIO()
            if conversion_type == "csv":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext,".csv")
                mime_type = "text/csv"
            
            elif conversion_type == "xlsx":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext,".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml"
            buffer.seek(0)
        
            #Download File
            st.download_button(
                label="Download",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

elif tabs == "About App":

    st.write("# SMAASU Corporation")
    # App Title
    
    st.write("# 🧹 Data Duster – The Ultimate Data Cleaning & Processing Tool")

    # Description
    st.markdown(
        """
        **Developed by SMAASU Corporation**, **Data Duster** is an intelligent web application designed to streamline data processing with ease and efficiency.
        Whether you're dealing with messy datasets in **CSV or XLSX format**, Data Duster ensures **clean, structured, and optimized** data in just a few clicks.
        """
    )

    # Features Section
    st.header("✨ Key Features")
    st.markdown("""
    - 📂 **Upload Dataset** – Supports CSV and XLSX files.  
    - 🧹 **Smart Cleaning** – Remove duplicates, handle null values, and fill missing data.  
    - 📊 **Selective Processing** – Choose specific columns for refinement.  
    - 📈 **Data Visualization** – Generate insightful graphs for better analysis.  
    - 🔄 **Format Conversion** – Convert files into different formats effortlessly.  
    - 💾 **Download Processed Data** – Get the refined dataset instantly.  
    """)

    # Call to Action
    st.markdown(
        """
        🚀 **Try Data Duster today and experience seamless data transformation!**
        """,
        unsafe_allow_html=True
    )
            
elif tabs == "About Me":

    # Personal Title 🏅🌟💡🌱🌍👤
    st.write("# 🏅 Syed Muhammad Abdullah Abdulbadeeii")
    st.write("# 🌱 About Me")

    # Introduction
    st.markdown(
        """
        I am **Syed Muhammad Abdullah Abdulbadeeii**, a **civil engineering student at NED University of Engineering & Technology, entrepreneur, innovator, and philanthropist**. 
        With a deep passion for **artificial intelligence, architecture, and sustainable urbanization**, I am committed to pioneering **transformative solutions** that seamlessly integrate technology with real-world applications.
        
        My work is driven by a vision to **build a smarter, more sustainable future**, where cutting-edge innovations enhance efficiency, improve urban living, and empower businesses. 
        Beyond my professional pursuits, I am dedicated to **philanthropy**, striving to **uplift Muslims and support underprivileged communities**, fostering a society rooted in compassion, empowerment, and progress.
        """
    )

    # Expertise & Interests
    st.header("🚀 Areas of Expertise")
    st.markdown(
        """
        - 🏗️ **Civil Engineering & Smart Infrastructure** – Engineering sustainable and innovative urban solutions.
        - 💻 **Software & Web Development** – Creating intelligent digital solutions to optimize efficiency.
        - 🤖 **Artificial Intelligence & Data Science** – Harnessing AI-driven technologies for smarter decision-making.
        - 📊 **Data Processing & Automation** – Streamlining complex workflows through advanced automation.
        - 🚀 **Entrepreneurship & Technological Innovation** – Spearheading startups that drive meaningful change.
        - ❤️ **Philanthropy & Social Impact** – Advocating for and supporting communities in need.
        """
    )

    # Vision & Journey
    st.header("🌍 My Vision & Journey")
    st.markdown(
        """
        As the founder of **SMAASU Corporation**, I have led groundbreaking initiatives such as **Data Duster**, a web-based platform revolutionizing data processing and automation. 
        My entrepreneurial journey is fueled by a relentless drive to **bridge the gap between technology and urban development**, delivering impactful solutions that **redefine the future of cities and industries**.
        
        **I believe in innovation, sustainability, and the power of technology to transform lives.** Through my work, I strive to create solutions that not only drive efficiency but also foster inclusivity and social well-being.
        
        **Let’s collaborate to build a brighter, more progressive future!**
        """
    )

elif tabs == "About Us":

    # Company Title
    st.write("# 🏢 About SMAASU Corporation")

    # Introduction
    st.markdown(
        """
        **SMAASU Corporation** is a forward-thinking company committed to innovation in **technology, architecture, and sustainable urbanization**.
        Our vision is to create cutting-edge solutions that simplify workflows, enhance productivity, and contribute to a smarter, more efficient future.
        """
    )

    # Mission Section
    st.header("🌍 Our Mission")
    st.markdown(
        """
        At **SMAASU Corporation**, we aim to:
        - 🚀 **Develop pioneering software solutions** that enhance business efficiency.
        - 🏗️ **Revolutionize architecture and urban planning** with smart, sustainable designs.
        - 🌱 **Promote sustainability** in every project we undertake.
        - 🤝 **Empower businesses and individuals** with next-gen technology.
        """
    )

    # Core Values Section
    st.header("💡 Our Core Values")
    st.markdown(
        """
        - **Innovation** – Continuously pushing boundaries with cutting-edge technology.
        - **Sustainability** – Building a future that is eco-friendly and efficient.
        - **Excellence** – Delivering top-tier solutions with precision and quality.
        - **Integrity** – Upholding transparency and trust in every endeavor.
        """
    )

    # Call to Action
    st.markdown(
        """
        🚀 **Join us on our journey to create a smarter, more sustainable world with SMAASU Corporation!**
        """,
        unsafe_allow_html=True
    )

            
