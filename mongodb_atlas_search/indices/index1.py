import json
import requests
from requests.auth import HTTPDigestAuth
from config_file import *


mapping1 = {
    'dynamic': True,  # index all available BSON types (strings, dates, and numerics)
    'fields': {
        "message": {
            "type": "string"
        }
    }
}


def create_index1(cluster_id, database_name, collection_name, index_name):
    baseUrl = BASE_URL + "/clusters/" + cluster_id + "/fts/indexes/"
    index_definition = {
        'collectionName': collection_name,
        'database': database_name,
        'analyzer': "lucene.standard",
        'mappings': mapping1,
        'name': index_name
    }

    return requests.post(baseUrl, headers=headers, data=json.dumps(index_definition),
                         auth=HTTPDigestAuth(PUBLIC_KEY, PRIVATE_KEY))
