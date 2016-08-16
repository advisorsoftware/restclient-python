import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n  \"portfolios\": [\r\n    {\r\n      \"targetPortfolioFlag\": true,\r\n      \"portfolioName\": \"target portfolio\",\r\n      \"cashBalance\" : 0,\r\n      \"holdings\": [\r\n        {\r\n          \"symbol\": \"IVV\",\r\n          \"holdingValue\": 2000\r\n        }\r\n      ]\r\n    },\r\n    {\r\n      \"targetPortfolioFlag\": false,\r\n      \"portfolioName\": \"some portfolio\",\r\n      \"cashBalance\" : 500,\r\n      \"holdings\": [\r\n        {\r\n          \"symbol\": \"IBM\",\r\n          \"holdingValue\": 1500\r\n        }\r\n      ]\r\n    }\r\n  ]\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/portfolio_risk_analysis", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))