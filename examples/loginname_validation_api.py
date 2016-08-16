import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n    \"loginNameList\": [\r\n        \"mm@asi.com\",\r\n        \"rr@asi.ai\",\r\n        \"testusername\",\r\n        \"bbragg\",\r\n        \"testusername\"\r\n    ]\r\n}\r"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/loginName_validation", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))