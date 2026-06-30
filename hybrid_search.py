from query_router import route_query
from db_search import search_database


def hybrid_search(question):
    """
    Hybrid Search

    Returns:
    {
        "route": "...",
        "database": ...,
        "documents": ...,
        "confidence": ...
    }
    """

    routing = route_query(question)

    route = routing["route"]

    result = {
        "route": route,
        "database": None,
        "documents": None,
        "confidence": routing["confidence"],
        "reason": routing["reason"]
    }

    # ----------------------------
    # Greeting
    # ----------------------------
    if route == "greeting":

        result["documents"] = "Hello! How can I help you regarding company policies or employee information?"

        return result

    # ----------------------------
    # Out of Scope
    # ----------------------------
    if route == "out_of_scope":

        result["documents"] = (
            "Sorry, I can answer only questions related to "
            "Company Policies and Employee Database."
        )

        return result

    # ----------------------------
    # Database Only
    # ----------------------------
    if route == "database":

        db_result = search_database(question)

        result["database"] = db_result

        return result

    # ----------------------------
    # Documents Only
    # ----------------------------
    if route == "documents":

        result["documents"] = True

        return result

    # ----------------------------
    # Hybrid
    # ----------------------------
    if route == "hybrid":

        db_result = search_database(question)

        result["database"] = db_result

        result["documents"] = True

        return result

    return result


# ------------------------------------
# Testing
# ------------------------------------

if __name__ == "__main__":

    tests = [

        "Hi",

        "What is Rahul salary?",

        "What is Leave Policy?",

        "What is Rahul leave balance and Leave Policy?",

        "Who won IPL?"

    ]

    for question in tests:

        print("=" * 60)

        print("Question :", question)

        print(hybrid_search(question))