import http.client

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n    \"riskTolerance\": 65,\r\n    \"investableAssets\": 100000,\r\n    \"modelSet\": \"default\",\r\n    \"goal\": {\r\n        \"goalName\": \"Savings\",\r\n        \"goalAmount\": 1000000,\r\n        \"timeHorizon\": 20,\r\n        \"initialInvestment\": 20000,\r\n        \"contributionAmount\": 1000,\r\n        \"contributionFrequency\": \"Annual\"\r\n    }\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/model_selection", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))