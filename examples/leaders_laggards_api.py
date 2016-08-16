import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n   \"portfolios\": [\r\n        {\r\n            \"portfolioName\": \"Portfolio A\",\r\n            \"holdings\": [\r\n                {\r\n                    \"symbol\": \"IVV\"\r\n                },\r\n                {\r\n                    \"symbol\": \"IWM\"\r\n                },\r\n                {\r\n                    \"symbol\": \"VWO\"\r\n                },\r\n                {\r\n                    \"symbol\": \"AGG\"\r\n                }\r\n            ]\r\n        },\r\n        {\r\n            \"portfolioName\": \"Portfolio B\",\r\n            \"holdings\": [\r\n                {\r\n                    \"symbol\": \"AAPL\"\r\n                },\r\n                {\r\n                    \"symbol\": \"CAT\"\r\n                },\r\n                {\r\n                    \"symbol\": \"GS\"\r\n                }\r\n            ]\r\n        }\r\n    ]\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/leaders_laggards", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))