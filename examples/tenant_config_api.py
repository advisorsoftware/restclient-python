import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "asidemo"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("PUT","/v1/tenant/config", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))