import http.client 
conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 
payload = "{ \"accountValue\": 10000, \"accountReturn\": 0.06, \"goals\": [ { \"goalName\": \"Savings\", \"goalAmount\": 1000000, \"timeHorizon\": 20, \"contributionAmount\": 1000, \"contributionFrequency\": \"Annual\", \"contributionStartYear\": 2016, \"contributionEndYear\": 2025 } ]}"
headers = { 
'Accept': "application/json",
'Content-Type': "application/json",
'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/progress_to_goal", payload, headers) 
res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))