index=$1

curl -H "Content-Type: application/json" -XGET 172.31.23.21:9200/$index/_search?pretty -d '{"sort":{"@timestamp":"desc"}, "size":2}'
