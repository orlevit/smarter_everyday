from nltk.corpus import stopwords

nltk_stop_words = stopwords.words('english')

CONN_STRING = <CONN_STRING>

DB_NAME = "test"
INDEX_NAME = "trying"
CLUSTER_NAME = "Cluster0"
COLLECTION_NAME = "sample"
SYN_COLLECTION_NAME = "synonyms"
SIMILARITY_THRESHOLD = 0.9
NUMBER_OF_SYNONYMS = 100
NUMBER_OF_RELATIVE_SYNONYMS = 3

# # Atlas API
GROUP_ID = <GROUP_ID>
PRIVATE_KEY = <PRIVATE>
PUBLIC_KEY = <PUBLIC_KEY>
API_ROOT_URL = "https://cloud.mongodb.com"
BASE_URL = API_ROOT_URL + "/api/atlas/v1.0/groups/" + GROUP_ID
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}