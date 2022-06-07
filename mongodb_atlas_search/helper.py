import json
import requests
from requests.auth import HTTPDigestAuth
from config_file import *


def create_auth():
    return HTTPDigestAuth(PUBLIC_KEY, PRIVATE_KEY)


def fetch_index(cluster_id, database_name, collection_name, index_name):
    api_url = BASE_URL + "/clusters/" + cluster_id + "/fts/indexes/" + database_name + "/" + collection_name
    response = requests.get(api_url, auth=create_auth())
    collections = response.json()
    index = next((x for x in collections if x['collectionName'] == collection_name and x['name'] == index_name), None)
    return index


def create_index(cluster_id, database_name, collection_name, index_name, index_mappings):
    baseUrl = BASE_URL + "/clusters/" + cluster_id + "/fts/indexes/"
    index_definition = {
        'collectionName': collection_name,
        'database': database_name,
        'mappings': index_mappings,
        'name': index_name
    }

    return requests.post(baseUrl, headers=headers, data=json.dumps(index_definition),
                         auth=HTTPDigestAuth(PUBLIC_KEY, PRIVATE_KEY))


def update_index(cluster_id, database_name, collection_name, index_id, index_name, index_mappings):
    baseUrl = BASE_URL + "/clusters/" + cluster_id + "/fts/indexes/" + index_id
    index_definition = {
        'collectionName': collection_name,
        'database': database_name,
        'mappings': index_mappings,
        'name': index_name
    }

    return requests.patch(baseUrl, headers=headers, data=json.dumps(index_definition),
                          auth=HTTPDigestAuth(PUBLIC_KEY, PRIVATE_KEY))


def create_or_update_index(cluster_id, database_name, collection_name, index_name, index_mappings):
    index = fetch_index(cluster_id, database_name, collection_name, index_name)
    if index is None:
        return create_index(cluster_id, database_name, collection_name, index_name, index_mappings)

    return update_index(cluster_id, database_name, collection_name, index["indexID"], index_name, index_mappings)


def delete_index(cluster_id, database_name, collection_name, index_name):
    index = fetch_index(cluster_id, database_name, collection_name, index_name)
    if index is None:
        print("index not found")
        return

    baseUrl = BASE_URL + "/clusters/" + cluster_id + "/fts/indexes/" + index["indexID"]

    return requests.delete(baseUrl, headers=headers, auth=HTTPDigestAuth(PUBLIC_KEY, PRIVATE_KEY))


# same as "display_highlights" but display results with markdown
# from IPython.display import display, Markdown, Latex
# def display_highlights_markdown(results):
#     for ii, result in enumerate(results, 1):
#         print(f'------------------- Instance:{ii}------------------------')
#         display(Markdown('**score:** ' + str(round(result["score"], 4))))
#         display(Markdown('**Title:** ' + result["title"]))
#         display(Markdown(' **Message:** ' + result["message"]))
#
#         for highlight in result['highlights']:
#             line = "> "
#             for text in highlight["texts"]:
#                 if text["type"] == "text":
#                     line = line + text["value"]
#
#                 if text["type"] == "hit":
#                     line = line + "[[" + text["value"] + "]]"
#             display(Markdown(line))

def display_highlights(results):
    for ii, result in enumerate(results, 1):
        print(f'------------------- Instance:{ii}------------------------')
        print('**score:** ' + str(round(result["score"], 4)))
        print('**Title:** ' + result["title"])
        print(' **Message:** ' + result["message"])

        for highlight in result['highlights']:
            line = "> "
            for text in highlight["texts"]:
                if text["type"] == "text":
                    line = line + text["value"]

                if text["type"] == "hit":
                    line = line + "[[" + text["value"] + "]]"
            print(line)

