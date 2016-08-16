import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n\t\"tenant\": {\r\n\t\t\"name\": \"test11\",\r\n\t\t\"email\": \"example@test.com\",\r\n\t\t\"isActive\": \"true\"\r\n\t}\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("PUT","/v1/tenant/update", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))