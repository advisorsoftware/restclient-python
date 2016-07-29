import http.client 
conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com") 
payload = "{\r\n\t\"accountValue\": \"5000\",\r\n\t\"accountReturn\": \"6\",\r\n\t\"goals\": [{\r\n\t\t\"goalName\": \"Rainy Day Fund\",\r\n\t\t\"goalAmount\": \"25000\",\r\n\t\t\"timeHorizon\": \"5\"\r\n\t}]\r\n}"
headers = { 
'Accept': "application/json",
'Content-Type': "application/json",
'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/goal_solver/lump_sum", payload, headers) 
res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))