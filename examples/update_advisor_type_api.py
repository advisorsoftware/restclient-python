import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n\t\"advisor\": {\r\n\t\t\"advisorId\": \"192\",\r\n\t\t\"advisorType\": \"ADV\"\r\n\t}\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("PUT","/v1/advisor/updateAdvisorType", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))