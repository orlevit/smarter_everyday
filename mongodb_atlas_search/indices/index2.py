import json
import requests
from requests.auth import HTTPDigestAuth
from config_file import *

analyzers2 = [
    {
      "name": "levitas_analyzer",
      "charFilters": [],
      "tokenizer": {
        "type": "standard"
      },
      "tokenFilters": [
        {
          "type": "asciiFolding"
        },
        {
          "type": "lowercase"
        },
        {
          "type": "snowballStemming",
          "stemmerName": "english"
        },
        {
          "type": "stopword",
          "tokens": nltk_stop_words
        }
      ]
    }
  ]

mapping2 = {
    'dynamic': True,  # index all available BSON types (strings, dates, and numerics)
    'fields': {
        "message": {
            "type": "string"
        }
    }
}

def create_index2(cluster_id, database_name, collection_name, index_name):
    baseUrl = BASE_URL + "/clusters/" + cluster_id + "/fts/indexes/"
    index_definition = {
        'collectionName': collection_name,
        'database': database_name,
        'analyzer': "levitas_analyzer",
        'searchAnalyzer': "levitas_analyzer",
        'analyzers': analyzers2,
        'mappings': mapping2,
        'name': index_name
    }

    return requests.post(baseUrl, headers=headers, data=json.dumps(index_definition),
                         auth=HTTPDigestAuth(PUBLIC_KEY, PRIVATE_KEY))
