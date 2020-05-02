import requests
import sys

# url = 'http://localhost:8080/message'
url = 'https://throwaway0.herokuapp.com/message'

def send_message():
  if len(sys.argv) == 1:
    print('Please write a message as the argument !')
    return

  for message in sys.argv[1:]:
    print('Sending message: ' + message)
    body = {
      'message': message
    }
    response = requests.post(url, data=body)
    print('Status: ' + str(response.status_code))

send_message()