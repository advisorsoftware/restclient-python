import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("GET","/v1/model_portfolio/select_params", headers=headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))