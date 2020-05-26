""" Função Lambda que lê novos arquivos do S3 e gera mensagens no SQS.

A função lambda é disparada sempre que um novo arquivo é criado em um bucket do S3.
É esperado que o arquivo seja um JSON com uma lista de usuários que serão importados no sistema.
A função irá percorrer a lista e gerar uma mensagem no SQS com os dados de cada usuário.
Se configurado o destino da função lambda, o retorno da função será enviado ao destino.

Exemplo de arquivo JSON:

[
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
  },
  ...
]
"""

import json
import boto3


s3 = boto3.resource('s3')
sqs = boto3.resource('sqs')
queue = sqs.Queue('https://sqs.sa-east-1.amazonaws.com/787278094283/em-nome-do-py-users')


def index(event, context):
    print('Inicio')
    records = event['Records']
    
    for record in records:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        file = s3.Object(bucket, key).get()
        body = file['Body'].read()
        users = json.loads(body)
        
        for user in users:
            message_body = json.dumps(user)
            queue.send_message(MessageBody=message_body)
            print('Enviado a mensagem:', message_body)
            
    print('Fim')
    
    return {
        'status': True,
        'message': 'Processado com sucesso'
    }
