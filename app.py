from flask import Flask, render_template, request
from textblob import TextBlob
import random

app = Flask(__name__)

# Define a dictionary of possible career paths and their associated skills
CAREER_PATHS = {
    'Doctor': ['Medicine', 'Anatomy', 'Physiology', 'Biochemistry', 'Pathology', 'Microbiology', 'Pharmacology', 'Clinical Practice'],
    'Engineer': ['Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering'],
    'Data Scientist': ['Python', 'Machine Learning', 'Data Analysis', 'Statistics', 'Data Visualization'],
    'Software Engineer': ['Python', 'Java', 'C++', 'Data Structures', 'Algorithms', 'Web Development', 'Mobile Development'],
    'Web Developer': ['HTML', 'CSS', 'JavaScript', 'React', 'Angular', 'Node.js', 'Database Management'],
    'UX Designer': ['User Research', 'Wireframing', 'Prototyping', 'Visual Design', 'Interaction Design', 'Usability Testing'],
    'Data Analyst': ['Data Cleaning', 'Data Visualization', 'SQL', 'Excel', 'Tableau', 'Power BI'],
}

# Define a decision tree algorithm for making recommendations
def recommend_career_path(user_input):
    # Analyze the user input using TextBlob
    analysis = TextBlob(user_input.lower())

    # Initialize an empty list of recommended career paths
    recommended_career_paths = []

    # Iterate over each career path in the CAREER_PATHS dictionary
    for career_path, skills in CAREER_PATHS.items():
        # Initialize a count of matching skills
        matching_skills = 0

        # Iterate over each skill in the current career path
        for skill in skills:
            # Check if the skill is mentioned in the user input
            if skill in analysis.noun_phrases:
                # Increment the count of matching skills
                matching_skills += 1

        # If more than half of the skills in the current career path are mentioned in the user input, add it to the list of recommended career paths
        if matching_skills > len(skills) / 2:
            recommended_career_paths.append(career_path)

    # If there are no recommended career paths, choose a random one
    if not recommended_career_paths:
        recommended_career_paths.append(random.choice(list(CAREER_PATHS.keys())))

    # Return the list of recommended career paths
    return recommended_career_paths

# Define a function for generating LAMA prompts
def generate_lama_prompts(career_path):
    # Initialize an empty list of LAMA prompts
    lama_prompts = []

    # Define a dictionary of possible LAMA prompts for each career path
    lama_prompts_dict = {
        'Doctor': [
            'What are the steps to become a doctor in India?',
            'What are the eligibility criteria for NEET exam?',
            'What are the top government medical colleges in India?',
            'What are the career opportunities after MBBS?',
            'What is the salary of a doctor in India?',
        ],
        'Engineer': [
            'What are the steps to become an engineer in India?',
            'What are the eligibility criteria for JEE exam?',
            'What are the top government engineering colleges in India?',
            'What are the career opportunities after B.Tech?',
            'What is the salary of an engineer in India?',
        ],
        'Data Scientist': [
            'What are the steps to become a data scientist in India?',
            'What are the eligibility criteria for data science courses?',
            'What are the top data science institutes in India?',
            'What are the career opportunities after data science courses?',
            'What is the salary of a data scientist in India?',
        ],
        'Software Engineer': [
            'What are the steps to become a software engineer in India?',
            'What are the eligibility criteria for software engineering courses?',
            'What are the top software engineering institutes in India?',
            'What are the career opportunities after software engineering courses?',
            'What is the salary of a software engineer in India?',
        ],
        'Web Developer': [
            'What are the steps to become a web developer in India?',
            'What are the eligibility criteria for web development courses?',
            'What are the top web development institutes in India?',
            'What are the career opportunities after web development courses?',
            'What is the salary of a web developer in India?',
        ],
        'UX Designer': [
            'What are the steps to become a UX designer in India?',
            'What are the eligibility criteria for UX design courses?',
            'What are the top UX design institutes in India?',
            'What are the career opportunities after UX design courses?',
            'What is the salary of a UX designer in India?',
        ],
        'Data Analyst': [
            'What are the steps to become a data analyst in India?',
            'What are the eligibility criteria for data analyst courses?',
            'What are the top data analyst institutes in India?',
            'What are the career opportunities after data analyst courses?',
            'What is the salary of a data analyst in India?',
        ],
    }

    # Add LAMA prompts to the list based on the career path
    for prompt in lama_prompts_dict[career_path]:
        lama_prompts.append(prompt)

    # Return the list of LAMA prompts
    return lama_prompts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    age = request.form['age']
    studying = request.form['studying']

    # Analyze the user input using TextBlob
    analysis = TextBlob(studying.lower())

    # Recommend a career path based on the user input
    recommended_career_paths = recommend_career_path(studying)

    # Generate LAMA prompts based on the recommended career path
    lama_prompts = generate_lama_prompts(recommended_career_paths[0])

    # Return the recommended skills and LAMA prompts as a string
    recommended_skills_str = ', '.join(CAREER_PATHS[recommended_career_paths[0]])
    lama_prompts_str = '\n'.join(lama_prompts)

    return render_template('result.html', name=name, recommended_skills=recommended_skills_str, lama_prompts=lama_prompts_str)

if __name__ == '__main__':
    app.run(debug=True)