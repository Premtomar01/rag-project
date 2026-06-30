"""
query_router.py
------------------------------------
Routes user questions to:
1. Database
2. Documents (PDF)
3. Hybrid (Database + PDF)
4. Greeting
5. Out of Scope
"""

import re


# -------------------------
# KEYWORDS
# -------------------------

DATABASE_KEYWORDS = [
    "employee",
    "salary",
    "leave balance",
    "department",
    "email",
    "phone",
    "employee id",
    "manager",
    "rahul",
    "amit",
    "priya"
]

DOCUMENT_KEYWORDS = [
    "policy",
    "leave policy",
    "hr policy",
    "guidelines",
    "attendance",
    "work from home",
    "wfh",
    "probation",
    "working hours",
    "password",
    "security",
    "confidential",
    "remote work",
    "code of conduct",
    "holiday"
]

GREETING_KEYWORDS = [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good evening",
    "good afternoon"
]

OUT_OF_SCOPE_KEYWORDS = [
    "ipl",
    "cricket",
    "movie",
    "weather",
    "bitcoin",
    "football",
    "youtube",
    "instagram",
    "netflix"
]


# -------------------------
# CLEAN QUESTION
# -------------------------

def clean_question(question):
    question = question.lower().strip()
    question = re.sub(r"\s+", " ", question)
    return question


# -------------------------
# FIND KEYWORDS
# -------------------------

def contains_keywords(question, keywords):
    return any(word in question for word in keywords)


# -------------------------
# ROUTER
# -------------------------

def route_query(question):

    question = clean_question(question)

    has_database = contains_keywords(question, DATABASE_KEYWORDS)
    has_document = contains_keywords(question, DOCUMENT_KEYWORDS)
    is_greeting = contains_keywords(question, GREETING_KEYWORDS)
    is_outside = contains_keywords(question, OUT_OF_SCOPE_KEYWORDS)

    # Greeting
    if is_greeting:
        return {
            "route": "greeting",
            "confidence": 1.0,
            "reason": "Greeting detected"
        }

    # Out of scope
    if is_outside:
        return {
            "route": "out_of_scope",
            "confidence": 1.0,
            "reason": "Question is outside company knowledge base"
        }

    # Hybrid
    if has_database and has_document:
        return {
            "route": "hybrid",
            "confidence": 0.98,
            "reason": "Database + Document query detected"
        }

    # Database
    if has_database:
        return {
            "route": "database",
            "confidence": 0.96,
            "reason": "Employee database query"
        }

    # Documents
    return {
        "route": "documents",
        "confidence": 0.95,
        "reason": "Company policy question"
    }


# -------------------------
# TEST
# -------------------------

if __name__ == "__main__":

    tests = [
        "Hi",
        "What is Rahul salary?",
        "What is leave policy?",
        "What is Rahul leave balance and leave policy?",
        "Who won IPL?"
    ]

    for q in tests:
        print(q)
        print(route_query(q))
        print("-" * 50)