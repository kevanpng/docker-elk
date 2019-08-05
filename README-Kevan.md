
load the entire 1GB of findings into elastic search. no errors
https://discuss.elastic.co/t/loading-many-big-json-files-into-elasticsearch/128078/13

```
pipenv run elasticsearch_loader  --http-auth elastic:changeme --index incidents --type incident json findings_clean
```

get the findings as a list
```
jq '.findings' findings_sandbox_201908041629.json > findings_clean.json
```

this is to inject findings and do preliminary event correalation.

prove the use of ELK as possible event correlation in findings in vulnerability management

Dont need to use logstash or file beats if my information is already in json. this is because logstash is used to convert text log files into json.
since findings are already in json, i can directly index in elasticsearch
