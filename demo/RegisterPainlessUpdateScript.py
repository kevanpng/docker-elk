from elasticsearch.client import Elasticsearch
es = Elasticsearch()

with open('ReviewerProfileUpdater.painless', 'r') as myfile:
	scriptSource=myfile.read()

	loadScriptBody = {
	  "script": {
			"lang": "painless",
		"source": scriptSource
	  }
	}
results = es.transport.perform_request('POST', "/_scripts/ReviewerProfileUpdater", body=loadScriptBody)
