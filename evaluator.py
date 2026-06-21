def evaluate_answer(answer):

    score = 0

    feedback = []

    if len(answer) >= 20:
        score += 4
        feedback.append("Good answer length")
    else:
        feedback.append("Answer is too short")

    if "because" in answer.lower():
        score += 3
        feedback.append("Explanation provided")

    if len(answer.split()) >= 15:
        score += 3
        feedback.append("Detailed answer")

    return score, feedback