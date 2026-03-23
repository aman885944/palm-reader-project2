import random

def predict_future():
    personality = random.choice([
        "You are confident and strong-minded",
        "You are creative and emotional",
        "You are practical and logical"
    ])

    career = random.choice([
        "Successful career in IT field",
        "Business opportunities will grow",
        "Government job chances are high"
    ])

    love = random.choice([
        "Strong and stable relationship",
        "Late but true love",
        "Emotional ups and downs"
    ])

    health = random.choice([
        "Good health overall",
        "Need to focus on fitness",
        "Take care of stress levels"
    ])

    return personality, career, love, health