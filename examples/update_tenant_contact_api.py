import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{  \r\n   \"contact\":{  \r\n      \"tenant\":\"asidemo\",\r\n      \"company\":\"ASI\"\r\n   }\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("PUT","/v1/tenant/contact", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))