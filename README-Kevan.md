this is to inject findings and do preliminary event correalation.

prove the use of ELK as possible event correlation in findings in vulnerability management

Dont need to use logstash or file beats if my information is already in json. this is because logstash is used to convert text log files into json.
since findings are already in json, i can directly index in elasticsearch

### Command to injest json file into elastic search
https://stackoverflow.com/questions/15936616/import-index-a-json-file-into-elasticsearch

```
curl -XPOST 'http://localhost:9200/test/_doc/1' -d @lane.json
```

