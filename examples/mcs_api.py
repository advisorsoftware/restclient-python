import http.client 
conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 
payload = "{\r\n\t\"startDate\": \"2015-01-01\",\r\n\t\"timePeriod\": 10,\r\n\t\"simulations\": 1000,\r\n\t\"rebalFrequency\": \"quarterly\",\r\n\t\"taxStatus\": \"tax\",\r\n\t\"taxRates\": {\r\n\t\t\"incomeRate\": 1,\r\n\t\t\"ltcgRate\": 1\r\n\t},\r\n\t\"portfolios\": [{\r\n\t\t\"name\": \"Current Portfolio\",\r\n\t\t\"cashBalance\": 10000,\r\n\t\t\"holdings\": [{\r\n\t\t\t\"lotId\": \"Lot-1\",\r\n\t\t\t\"symbol\": \"IBM\",\r\n\t\t\t\"purchaseDate\": \"2014-12-01\",\r\n\t\t\t\"quantity\": 100,\r\n\t\t\t\"currentValue\": 500,\r\n\t\t\t\"costBasis\": 1200\r\n\t\t}],\r\n\t\t\"incomes\": [{\r\n\t\t\t\"name\": \"Income1\",\r\n\t\t\t\"startMonth\": 1,\r\n\t\t\t\"startYear\": 2015,\r\n\t\t\t\"endMonth\": 12,\r\n\t\t\t\"endYear\": 2025,\r\n\t\t\t\"amount\": 1000,\r\n\t\t\t\"inflationSensitivity\": \"false\",\r\n\t\t\t\"frequency\": \"annual\"\r\n\t\t}],\r\n\t\t\"goals\": [{\r\n\t\t\t\"name\": \"Retirement\",\r\n\t\t\t\"startMonth\": 1,\r\n\t\t\t\"startYear\": 2020,\r\n\t\t\t\"endMonth\": 12,\r\n\t\t\t\"endYear\": 2025,\r\n\t\t\t\"amount\": 1000,\r\n\t\t\t\"inflationSensitivity\": \"false\",\r\n\t\t\t\"frequency\": \"annual\"\r\n\t\t}]\r\n\t}]\r\n}"
headers = { 
'Accept': "application/json",
'Content-Type': "application/json",
'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/mcs", payload, headers) 
res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))