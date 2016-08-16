import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n\t\"riskAttr\": {\r\n\t\t\"id\": 110,\r\n\t\t\"name\": \"RA2\",\r\n\t\t\"order\": 1\r\n\t}\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("PUT","/v1/risk_attr/update", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))