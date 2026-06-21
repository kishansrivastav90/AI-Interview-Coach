import PyPDF2

# Extract text from PDF
def extract_text(pdf_path):

    text = ""

    with open(pdf_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return text


# List of skills to search for
skills_list = [

    "Python",

    "Flask",

    "Machine Learning",

    "Deep Learning",

    "Data Science",

    "Java",

    "C++",

    "SQL",

    "HTML",

    "CSS",

    "JavaScript"
]


# Extract skills from text
def extract_skills(text):

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return found_skills


# Generate interview questions
def generate_questions(skills):

    questions = {

        "Python": [
            "What are decorators in Python?",
            "Explain list comprehension."
        ],

        "Flask": [
            "What is Flask?",
            "What are routes in Flask?"
        ],

        "Machine Learning": [
            "What is overfitting?",
            "Difference between supervised and unsupervised learning?"
        ],

        "Java": [
            "Explain OOP concepts in Java.",
            "Difference between JDK, JRE and JVM?"
        ]

    }

    interview_questions = []

    for skill in skills:

        if skill in questions:

            interview_questions.extend(
                questions[skill]
            )

    return interview_questions