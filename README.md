# ai-self-learning-teacher

This is a Streamlit application that uses OpenAI's Language Model to create personalized learning plans for any topic. It provides users with a learning plan, study schedule, learning resources, and project ideas tailored to their chosen subject.

Features

Enter a topic and get a personalized learning plan, complete with a study schedule, learning resources, and project ideas.
Expandable sections for easy navigation and content organization.
Uses OpenAI's Language Model to generate relevant and useful information.

Installation

Clone this repository:
git clone https://github.com/yourusername/your-repo-name.git

Navigate to the repository folder and install the required packages:
cd your-repo-name
pip install -r requirements.txt

Replace your-api-key with your actual OpenAI API key in the following line of code:
os.environ["OPENAI_API_KEY"] = "your-api-key"

Run the Streamlit app:
streamlit run app.py

Open the app in your browser at http://localhost:8501

Usage
Enter a topic you want to learn about in the text input field.
Click the "Create plan" button.
Explore the generated learning plan, study schedule, learning resources, and project ideas by expanding the corresponding sections.

License
This project is licensed under the MIT License - see the LICENSE file for details.
