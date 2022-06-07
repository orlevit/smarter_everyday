def get_query1(word_to_search):
    query = [
        {
            "$search": {
                "index": 'trying',
                "text": {"path": "message", "query": word_to_search},
                "highlight": {"path": "message"}

            }
        },
        {
            "$project": {
                "_id": 1,
                "highlights": {"$meta": "searchHighlights"},
                "score": {"$meta": "searchScore"},
                "title": 1,
                "message": 1,
            }
        }
    ]
    return query

def get_query2(word_to_search):
    query = [
        {
            "$search": {
                "index": 'trying',
                "text": {"path": "message", "query": word_to_search, "synonyms": 'mySynonyms'},
                "highlight": {"path": "message"}
            }
        },
        {
            "$project": {
                "_id": 1,
                "highlights": {"$meta": "searchHighlights"},
                "score": {"$meta": "searchScore"},
                "title": 1,
                "message": 1,
            }
        }
    ]
    return query

def get_query3(word_to_search):
    query = [
        {
            "$search": {
                "index": 'trying',
                "highlight": {"path": "message"},
                "compound": {
                    "should": [{
                            "text": {"path": "message", "query": word_to_search, "synonyms": 'mySynonyms'}
            },
            {
                            "text": {"path": "message", "query": word_to_search}
            }]
        }}},
        {
            "$project": {
                "_id": 1,
                "highlights": {"$meta": "searchHighlights"},
                "score": {"$meta": "searchScore"},
                "title": 1,
                "message": 1,
            }
        }
    ]
    return query

