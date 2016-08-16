import http.client 

conn = http.client.HTTPConnection("https://sandbox.advisorsoftware.com:443") 

payload = "{\r\n\t\"loginName\": \"mm@asi.com\",\r\n\t\"questionnaire\": {\r\n\t\t\"questionnaireID\": \"asidemorq3\",\r\n\t\t\"questionnaireName\": \"ASI Default Risk Questionnaire.\",\r\n\t\t\"questions\": [{\r\n\t\t\t\"questionID\": 58,\r\n\t\t\t\"questionNumber\": 1,\r\n\t\t\t\"questionText\": \"In comparison to others, how would you rate your willingness to take financial risks?.\",\r\n\t\t\t\"answerCount\": 5,\r\n\t\t\t\"answers\": [{\r\n\t\t\t\t\"answerNumber\": 1,\r\n\t\t\t\t\"answerText\": \"Very Low\",\r\n\t\t\t\t\"answerWeight\": 5,\r\n\t\t\t\t\"selectedAnswer\": \"true\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 2,\r\n\t\t\t\t\"answerText\": \"Low\",\r\n\t\t\t\t\"answerWeight\": 10,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 3,\r\n\t\t\t\t\"answerText\": \"Average\",\r\n\t\t\t\t\"answerWeight\": 15,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 4,\r\n\t\t\t\t\"answerText\": \"High\",\r\n\t\t\t\t\"answerWeight\": 20,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 5,\r\n\t\t\t\t\"answerText\": \"Very High\",\r\n\t\t\t\t\"answerWeight\": 25,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}]\r\n\t\t}, {\r\n\t\t\t\"questionID\": 59,\r\n\t\t\t\"questionNumber\": 2,\r\n\t\t\t\"questionText\": \"Which statement explains your greatest concern when selecting an investment?.\",\r\n\t\t\t\"answerCount\": 4,\r\n\t\t\t\"answers\": [{\r\n\t\t\t\t\"answerNumber\": 1,\r\n\t\t\t\t\"answerText\": \"Potential for loss\",\r\n\t\t\t\t\"answerWeight\": 5,\r\n\t\t\t\t\"selectedAnswer\": \"true\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 2,\r\n\t\t\t\t\"answerText\": \"Mostly potential for loss, but some concern about potential for gain\",\r\n\t\t\t\t\"answerWeight\": 10,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 3,\r\n\t\t\t\t\"answerText\": \"Mostly potential for gain, but some concern about potential for loss\",\r\n\t\t\t\t\"answerWeight\": 15,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 4,\r\n\t\t\t\t\"answerText\": \"Potential for gain\",\r\n\t\t\t\t\"answerWeight\": 25,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}]\r\n\t\t}, {\r\n\t\t\t\"questionID\": 60,\r\n\t\t\t\"questionNumber\": 3,\r\n\t\t\t\"questionText\": \"Which statement best identifies your feelings about investment risk?.\",\r\n\t\t\t\"answerCount\": 4,\r\n\t\t\t\"answers\": [{\r\n\t\t\t\t\"answerNumber\": 1,\r\n\t\t\t\t\"answerText\": \"I would only choose investments with low risk associated with them\",\r\n\t\t\t\t\"answerWeight\": 5,\r\n\t\t\t\t\"selectedAnswer\": \"true\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 2,\r\n\t\t\t\t\"answerText\": \"A mix of investments, most having low risk and the minority having high risk, with potentially greater returns\",\r\n\t\t\t\t\"answerWeight\": 10,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 3,\r\n\t\t\t\t\"answerText\": \"An aggressive mix of investments, some with a lower risk, but more with a higher risk that may yield higher returns\",\r\n\t\t\t\t\"answerWeight\": 20,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 4,\r\n\t\t\t\t\"answerText\": \"Higher risk investments that had greater potential for higher returns\",\r\n\t\t\t\t\"answerWeight\": 25,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}]\r\n\t\t}, {\r\n\t\t\t\"questionID\": 61,\r\n\t\t\t\"questionNumber\": 4,\r\n\t\t\t\"questionText\": \"If the stock market and 1 of your stocks dropped 25% over 3 months, what would you do with your shares?.\",\r\n\t\t\t\"answerCount\": 4,\r\n\t\t\t\"answers\": [{\r\n\t\t\t\t\"answerNumber\": 1,\r\n\t\t\t\t\"answerText\": \"Sell them immediately\",\r\n\t\t\t\t\"answerWeight\": 5,\r\n\t\t\t\t\"selectedAnswer\": \"true\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 2,\r\n\t\t\t\t\"answerText\": \"Sell a portion of them\",\r\n\t\t\t\t\"answerWeight\": 10,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 3,\r\n\t\t\t\t\"answerText\": \"Hold them, the market and my stock value will turn around soon\",\r\n\t\t\t\t\"answerWeight\": 15,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}, {\r\n\t\t\t\t\"answerNumber\": 4,\r\n\t\t\t\t\"answerText\": \"Purchase more shares\",\r\n\t\t\t\t\"answerWeight\": 25,\r\n\t\t\t\t\"selectedAnswer\": \"false\"\r\n\t\t\t}]\r\n\t\t}]\r\n\t},\r\n\t\"riskToleranceStrategy\": [{\r\n\t\t\"strategyLowerBound\": 0,\r\n\t\t\"strategyName\": \"Conservative\",\r\n\t\t\"strategyUpperBound\": 55\r\n\t}, {\r\n\t\t\"strategyLowerBound\": 56,\r\n\t\t\"strategyName\": \"Moderate\",\r\n\t\t\"strategyUpperBound\": 70\r\n\t}, {\r\n\t\t\"strategyLowerBound\": 71,\r\n\t\t\"strategyName\": \"Growth\",\r\n\t\t\"strategyUpperBound\": 85\r\n\t}, {\r\n\t\t\"strategyLowerBound\": 86,\r\n\t\t\"strategyName\": \"Aggressive Growth\",\r\n\t\t\"strategyUpperBound\": 100\r\n\t}]\r\n}"

headers = { 
	'Accept': "application/json",
	'Content-Type': "application/json",
	'Authorization': "ASI_CLIENT client_id={YOUR CLIENT ID HERE} client_secret={YOUR CLIENT SECRET HERE}",
} 
conn.request("POST","/v1/questionnaireAnswer", payload, headers) 

res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))