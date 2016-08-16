import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n\t\"preferenceList\": {\r\n\t\t\"preferences\": [{\r\n\t\t\t\"name\": \"Goal Configuration\",\r\n\t\t\t\"value\": \"Risk And Goal\"\r\n\t\t}]\r\n\t}\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/tenant/preference/set", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))