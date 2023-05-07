import os
import streamlit as st
from langchain import OpenAI

os.environ["OPENAI_API_KEY"] = "you-api-key"

llm = OpenAI(temperature=0)

def display_learning_plan(topic):
    st.markdown(f"**Learning Plan for {topic}:**")
    query = f"I want to learn {topic}. Can you use the Pareto Principle, which identifies the 20 percent of the topic that will yield 80 percent of the desired results to create a focused learing plan for me? Just write the numered list of topics nothing else"
    st.write(llm(query))

def display_study_schedule(topic):
    st.markdown(f"**Study Schedule for {topic}:**")
    query = f"Create a study schedule for {topic} in an appropriate amount of weeks. Please include time for revision and testing! Write just the schedule nothing else"
    st.write(llm(query))

def display_learning_resources(topic):
    st.markdown(f"**Learning Resources for {topic}:**")
    query = f"Sugest me various learning resources (like books, videos podcasts, interactive exercises) for {topic} that cater to different learing styles. Write just the resources nothing else"
    st.write(llm(query))

def display_project_ideas(topic):
    st.markdown(f"**Project Ideas for {topic}:**")
    query = f"Give me beginner project ideas to sharpen my {topic} skills? Write just the project ideas nothing else"
    st.write(llm(query))

def main():
    # Initialize session state if not already present
    if "create_clicked" not in st.session_state:
        st.session_state.create_clicked = False
    if "ask_clicked" not in st.session_state:
        st.session_state.ask_clicked = False
        
    st.title("Topic-based Learning App")

    topic = st.text_input("I want to learn about:", value="")
    create_button = st.button("Create plan")
    
    if create_button:
        st.session_state.create_clicked = True
    
    if st.session_state.create_clicked:
        with st.spinner('Loading...'):
            with st.expander("Learning Plan"):
                display_learning_plan(topic)

            with st.expander("Study Schedule"):
                display_study_schedule(topic)

            with st.expander("Learning Resources"):
                display_learning_resources(topic)

            with st.expander("Project Ideas"):
                display_project_ideas(topic)

if __name__ == "__main__":
    main()
