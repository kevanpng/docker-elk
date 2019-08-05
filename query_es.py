from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

import logging

logger = logging.getLogger("example")
logging.basicConfig()  # Log to stdout

# info
logger.setLevel(logging.INFO)
es_client = Elasticsearch(http_auth="elastic:changeme")

# s = Search(using=client, index="my-index") \
#     .filter("term", category="search") \
#     .query("match", title="python")   \
#     .exclude("match", description="beta")

# s = Search(using=es_client, index="my-index") \
#     .filter("term", category="search") \
#     .query("match", title="python")   \
#     .exclude("match", description="beta")
# response = s.execute()

# for hit in response:
#     print(hit.meta.score, hit.title)

# res = es_client.get(index='incidents', doc_type="incident", id=1)
res = es_client.search(index='incidents', body={"query": {"match_all": {}}})

logger.info(f'{res}')
# logger.info(res["_source"])
