from flask import Flask, request
import wikipedia
import wolframalpha
from twilio.twiml.messaging_response import Message, MessagingResponse

app_id = ""

app = Flask(__name__)


@app.route('/', methods=['POST'])
def sms():
	message_body = request.form['body']
	resp = MessagingResponse()
	replyText = getReply(Message_body)
	resp.message(replyText)
	return str(resp)
    
def getReply(mess):
	message = message.lower()
	answer = ""
	if 'wolfram' in message:
		message = message.replace('wolfram', '')
		client = wolframalpha.Client(app_id)
		res = client.query(message)
		try:
			answer = next(res.results).text
		except:
			answer = "There was an error processing your request"
	elif 'wiki' in message:
		message = message.replace('wiki', '')
		try:
			answer = wikipedia.summary(message, sentance=5)
		except:
			answer = 'Request was not found'
	else:
		answer = "Command not found\n these are the commands you can try\n wolframalpha [request], and wiki [request]"
if __name__ == '__MAIN__':
	app.run()
	