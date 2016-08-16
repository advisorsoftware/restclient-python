import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n    \"allocationsDisplayLevel\": \"1\",\r\n    \"compareAllocations\": \"1\",\r\n    \"compareSectors\": \"1\",\r\n    \"compareGeos\": \"1\",\r\n    \"portfolios\": [\r\n        {\r\n            \"portfolioName\": \"Portfolio A\",\r\n            \"cashBalance\": \"20000\",\r\n            \"holdings\": [\r\n                {\r\n                    \"symbol\": \"IVV\",\r\n                    \"holdingValue\": \"40000\"\r\n                },\r\n                {\r\n                    \"symbol\": \"VWO\",\r\n                    \"holdingValue\": \"40000\"\r\n                }\r\n            ]\r\n        },\r\n        {\r\n            \"portfolioName\": \"portfolio B\",\r\n            \"cashBalance\": \"10000\",\r\n            \"holdings\": [\r\n                {\r\n                    \"symbol\": \"IVV\",\r\n                    \"holdingValue\": \"90000\"\r\n                }\r\n            ]\r\n        },\r\n        {\r\n            \"portfolioName\": \"portfolio C\",\r\n            \"cashBalance\": \"10000\",\r\n            \"holdings\": [\r\n                {\r\n                    \"symbol\": \"VWO\",\r\n                    \"holdingValue\": \"90000\"\r\n                }\r\n            ]\r\n        }\r\n    ]\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/portfolio_comparisons/exposures", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))