import json
import logging
import os

import requests
from requests.auth import HTTPBasicAuth

from elasticsearch import Elasticsearch

logger = logging.getLogger('example')
logging.basicConfig()  # Log to stdout
# info
logger.setLevel(logging.INFO)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
logger.info(f'{ROOT_DIR}')

user_pass = ('elastic', 'changeme')
res = requests.get('http://localhost:9200', auth=HTTPBasicAuth(*user_pass))
logger.info(res.content)
es = Elasticsearch(
    ['http://localhost:9200'],
    http_auth=user_pass
)

i = 1
FINDINGS_FILE_NAME = 'findings_sandbox_201908041629.json'
FINDINGS_FILE = os.path.join(ROOT_DIR, FINDINGS_FILE_NAME)

with open(FINDINGS_FILE, 'r') as f:
    findings = f.read()

    # send data to es
    result = es.index(
        index='myindex', ignore=400,
        id=i, body=json.loads(findings)
    )
    logger.info(result)
