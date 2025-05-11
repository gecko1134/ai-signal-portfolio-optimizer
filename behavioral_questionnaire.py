
QUESTIONS = [
    {"question": "How do you typically react during market volatility?",
     "options": {"Stay the course": "high", "Feel concerned but wait": "moderate", "Want to sell immediately": "low"}},
    {"question": "What is your investment time horizon?",
     "options": {"10+ years": "high", "5–10 years": "moderate", "Less than 5 years": "low"}},
    {"question": "How important is portfolio stability to you?",
     "options": {"Not important – I want growth": "high", "Somewhat important": "moderate", "Very important": "low"}},
    {"question": "How do you define investment success?",
     "options": {"Beating the market": "high", "Matching market returns": "moderate", "Avoiding loss": "low"}},
    {"question": "How often do you want updates or meetings?",
     "options": {"Annually or as needed": "high", "Quarterly": "moderate", "Monthly or more": "low"}}
]

def calculate_behavior_score(responses):
    score_map = {"high": 3, "moderate": 2, "low": 1}
    total_score = sum(score_map.get(r, 2) for r in responses)
    if total_score >= 13:
        return "Confident Casey", total_score
    elif total_score >= 9:
        return "Anxious Alex", total_score
    else:
        return "Steady Sam", total_score
