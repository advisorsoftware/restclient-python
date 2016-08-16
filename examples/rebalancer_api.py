import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n    \"accountId\": \"1234-4567\",\r\n    \"holdings\": [\r\n        {\r\n            \"aggregatedHoldings\": [\r\n                {\r\n                    \"assetId\": \"IVV\",\r\n                    \"quantity\": 100000\r\n                }\r\n            ]\r\n        }\r\n    ],\r\n    \"modelPortfolio\": [\r\n        {\r\n            \"modelHoldings\": [\r\n                {\r\n                    \"assetId\": \"IVV\",\r\n                    \"weight\": 1\r\n                }\r\n            ]\r\n        }\r\n    ],\r\n    \"securityPriceList\": [\r\n        {\r\n            \"securityPrices\": [\r\n                {\r\n                    \"assetId\": \"IVV\",\r\n                    \"price\": 100\r\n                }\r\n            ]\r\n        }\r\n    ]\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/rebalancer", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))