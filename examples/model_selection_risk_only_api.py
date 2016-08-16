import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n\t\"riskTolerance\": \"50\",\r\n\t\"modelSet\": \"default\"\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/model_selection/risk_only", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))