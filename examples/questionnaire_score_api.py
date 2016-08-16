import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n    \"questionnaireID\": \"asidemorq2\",\r\n    \"questionList\": [\r\n        {\r\n            \"questionNumber\": \"1\",\r\n            \"selectedAnswerNumber\": \"2\"\r\n        },\r\n        {\r\n            \"questionNumber\": \"2\",\r\n            \"selectedAnswerNumber\": \"2\"\r\n        }\r\n    ]\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/questionnaire_score", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))