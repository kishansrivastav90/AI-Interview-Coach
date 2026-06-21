from flask import Flask, render_template, request
import os
from resume_parser import extract_text, extract_skills, generate_questions
from evaluator import evaluate_answer
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload_resume():

    if 'resume' not in request.files:
        return "No file selected"

    file = request.files['resume']

    if file.filename == '':
        return "No file selected"

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    # Extract text from PDF
    text = extract_text(filepath)

    # Extract skills from text
    skills = extract_skills(text)

    # Generate interview questions
    questions = generate_questions(skills)

    return f"""

    <h2>Resume Uploaded Successfully!</h2>

    <h3>Skills Found:</h3>

    <ul>
        {"".join([f"<li>{skill}</li>" for skill in skills])}
    </ul>

    <h3>Interview Questions:</h3>

    <ol>
        {"".join([f"<li>{question}</li>" for question in questions])}
    </ol>

    <h3>Extracted Resume Text:</h3>

    <pre>
{text}
    </pre>

    """
@app.route('/evaluate', methods=['POST'])
def evaluate():

    answer = request.form['answer']

    score, feedback = evaluate_answer(answer)

    return f"""

    <h2>Evaluation Result</h2>

    <h3>Score:</h3>

    {score}/10

    <h3>Feedback:</h3>

    {feedback}

    """

if __name__ == "__main__":
    app.run(debug=True)