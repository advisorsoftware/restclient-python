import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n    \"returnSecurityDetails\": \"true\",\r\n    \"portfolios\": [\r\n        {\r\n            \"portfolioName\": \"portfolio 1\",\r\n            \"cashBalance\": 1000,\r\n            \"holdings\": [\r\n                {\r\n                    \"symbol\": \"IVV\",\r\n                    \"holdingValue\": 50000\r\n                },\r\n                {\r\n                    \"symbol\": \"IWM\",\r\n                    \"holdingValue\": 25000\r\n                },\r\n                {\r\n                    \"symbol\": \"VWO\",\r\n                    \"holdingValue\": 10000\r\n                },\r\n                {\r\n                    \"symbol\": \"AAPL\",\r\n                    \"holdingValue\": 5000\r\n                }\r\n            ]\r\n        },\r\n        {\r\n            \"portfolioName\": \"portfolio 2\",\r\n            \"cashBalance\": 1000,\r\n            \"holdings\": [\r\n                {\r\n                    \"symbol\": \"VIG\",\r\n                    \"holdingValue\": 50000\r\n                },\r\n                {\r\n                    \"symbol\": \"VO\",\r\n                    \"holdingValue\": 25000\r\n                },\r\n                {\r\n                    \"symbol\": \"VB\",\r\n                    \"holdingValue\": 10000\r\n                },\r\n                {\r\n                    \"symbol\": \"EFA\",\r\n                    \"holdingValue\": 5000\r\n                }\r\n            ]\r\n        }\r\n    ]\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/sectors", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))