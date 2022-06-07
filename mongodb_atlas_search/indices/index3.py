import json
import requests
from requests.auth import HTTPDigestAuth
from config_file import *

analyzers3 = [
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

mapping3 = {
    'dynamic': True,  # index all available BSON types (strings, dates, and numerics)
    'fields': {
        "message": {
            "type": "string"
        }
    }
}

synonyms3 = [
    {
      "analyzer": "lucene.standard",#"levitas_analyzer",
      "name": "mySynonyms",
      "source": {
        "collection": "synonyms"
      }
    }
  ]

def create_index3(cluster_id, database_name, collection_name, index_name):
    baseUrl = BASE_URL + "/clusters/" + cluster_id + "/fts/indexes/"
    index_definition = {
        'collectionName': collection_name,
        'database': database_name,
        'analyzer': "levitas_analyzer",
        'searchAnalyzer': "levitas_analyzer",
        'analyzers': analyzers3,
        'mappings': mapping3,
        'name': index_name,
        'synonyms': synonyms3
    }

    return requests.post(baseUrl, headers=headers, data=json.dumps(index_definition),
                         auth=HTTPDigestAuth(PUBLIC_KEY, PRIVATE_KEY))
