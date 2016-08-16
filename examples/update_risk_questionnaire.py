import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n\t\"riskQuestionnaire\": {\r\n\t\t\"serviceName\": \"UPDATE_TENANT_RQ\",\r\n\t\t\"questionnaireName\": \"Enterprise RQ\",\r\n\t\t\"description\": \"Asidemo Questionnaire description\",\r\n\t\t\"tenantName\": \"ent\",\r\n\t\t\"questionnaireID\": \"ent_rq1\",\r\n\t\t\"questions\": [{\r\n\t\t\t\"questionNumber\": 1,\r\n\t\t\t\"questionText\": \"If the stock market and 1 of your stocks dropped 25% over 3 months, what would you do with your shares?\",\r\n\t\t\t\"questionID\": \"545\",\r\n\t\t\t\"answers\": [{\r\n\t\t\t\t\"answerNumber\": 1,\r\n\t\t\t\t\"answerText\": \"Sell a portion of them\",\r\n\t\t\t\t\"answerWeight\": \"50\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 2,\r\n\t\t\t\t\"answerText\": \"Purchase more shares\",\r\n\t\t\t\t\"answerWeight\": \"50\"\r\n\t\t\t}]\r\n\t\t}, {\r\n\t\t\t\"questionNumber\": 2,\r\n\t\t\t\"questionText\": \"Which statement explains your greatest concern when selecting an investment?\",\r\n\t\t\t\"questionID\": \"546\",\r\n\t\t\t\"answers\": [{\r\n\t\t\t\t\"answerNumber\": 1,\r\n\t\t\t\t\"answerText\": \"Potential for loss\",\r\n\t\t\t\t\"answerWeight\": \"50\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 2,\r\n\t\t\t\t\"answerText\": \"I would only choose investments with low risk associated with them\",\r\n\t\t\t\t\"answerWeight\": \"50\"\r\n\t\t\t}]\r\n\t\t}],\r\n\t\t\"riskToleranceStrategy\": [{\r\n\t\t\t\"strategyName\": \"Conservative\",\r\n\t\t\t\"label\": \"Conservative\",\r\n\t\t\t\"value\": \"50\"\r\n\t\t}, {\r\n\t\t\t\"strategyName\": \"Aggressive\",\r\n\t\t\t\"label\": \"Aggressive\",\r\n\t\t\t\"value\": \"100\"\r\n\t\t}]\r\n\t}\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("PUT","/v1/rq/update", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))