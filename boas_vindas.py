""" Função lambda que consome uma fila SQS e "simula" o envio de e-mail de boas-vindas.

A função lambda é disparada sempre que uma mensagem nova chega na fila SQS.
Para cada mensagem é executada a função, que consome a mensagem, extrai as informações e simula o envio de e-mail.

Exemplo de conteúdo na fila SQS:

  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  }
"""

import json

def lambda_handler(event, context):
    records = event['Records']
    for record in records:
        body = record['body']
        user = json.loads(body)
        print(f'Enviando e-mail para o usuário', user['name'], user['email'])
    
