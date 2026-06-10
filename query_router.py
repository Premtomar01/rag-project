def route_query(question):

    question=question.lower()

    keywords=[

    "salary",

    "employee",

    "leave balance",

    "rahul",

    "amit",

    "priya"

    ]

    for word in keywords:

        if word in question:

            return "database"

    return "documents"