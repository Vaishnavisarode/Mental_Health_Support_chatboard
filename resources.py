emergency_helplines = {
    "IN": "Call 9152987821 (iCall - India)",
    "US": "Call 988 (Suicide & Crisis Lifeline)",
    "UK": "Call 116 123 (Samaritans)"
}

def get_helpline(country_code="IN"):
    return emergency_helplines.get(country_code, "Visit WHO for local resources: https://www.who.int")
