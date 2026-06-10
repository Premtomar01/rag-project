from query_router import route_query
from db_search import search_database


def hybrid_search(question):

    source = route_query(question)

    if source == "database":

        result = search_database(question)

        if result:

            return {
                "source": "database",
                "data": result
            }

    return {
        "source": "documents",
        "data": None
    }