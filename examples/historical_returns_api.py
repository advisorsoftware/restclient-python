import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n    \"accountIDs\": [\r\n        11,\r\n        12\r\n    ],\r\n    \"limit\": \"200\",\r\n    \"offset\": \"2\",\r\n    \"startDate\": \"2014-05-01\"\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/accounts/historical_returns", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))