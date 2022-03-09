import requests
import queries

url="http://20.62.141.224:9021/graphql"
print("query is "+queries.getStudentQuery(1))
r = requests.post(url, json={'query': queries.getStudentQuery(1)})
print(r.status_code)
print(r.text)