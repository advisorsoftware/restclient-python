import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{ \n\t\"contact\": {\r\n\t\t\"company\": \"test1\",\r\n\t\t\"tenant\": \"asidemo\"\r\n\t}\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/tenant/contact", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))