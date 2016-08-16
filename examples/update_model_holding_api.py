import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n\t\"id\": \"19458\",\r\n\t\"modelPortfolio\": \"85\",\r\n\t\"symbol\": \"IBM\",\r\n\t\"allocPercent\": \"10\",\r\n\t\"dataOwner\": \"3\",\r\n\t\"assetClass\": \"FI\",\r\n\t\"security\": 54321\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("PUT","/v1/model_holding", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))