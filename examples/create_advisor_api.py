import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n\t\"advisor\": {\r\n\t\t\"firstName\": \"John\",\r\n\t\t\"lastName\": \"Danis\",\r\n\t\t\"teamId\": \"16\",\r\n\t\t\"title\": \"Advisor\",\r\n\t\t\"country\": \"U.S.\",\r\n\t\t\"advisorType\": \"ADV\",\r\n\t\t\"company\": \"ASI Client\",\r\n\t\t\"addr1\": \"N. California Blvd.\",\r\n\t\t\"addr2\": \"Suite 400 - Walnut Creek\",\r\n\t\t\"city\": \"CA\",\r\n\t\t\"state\": \"CA\",\r\n\t\t\"email\": \"John@advisorsoftware.com\",\r\n\t\t\"phone\": \"2222322\",\r\n\t\t\"fax\": \"2222322\",\r\n\t\t\"zipCode\": \"94596\",\r\n\t\t\"login\": \"jDanis\",\r\n\t\t\"password\": \"123456\"\r\n\t}\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/advisor/create", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))