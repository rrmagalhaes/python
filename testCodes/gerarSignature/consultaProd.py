import hmac
import hashlib
import base64

from datetime import datetime

key = 'senha'
method = 'get'
body = ''

now = datetime.now()
timestamp = str(datetime.timestamp(now))[:10]
encodedkey = str.encode(key)
sha256_hash = hashlib.sha256()

valoresContatenados = f'{method}{timestamp}{body}'

hash256 = hmac.new(encodedkey, valoresContatenados.encode('UTF-8'), hashlib.sha256).hexdigest()
hashAscii = bytes.fromhex(hash256)
signature = str(base64.b64encode(hashAscii))


print('--- Cabeçalho ---')
print(valoresContatenados)
print('--- Encriptado com hmac sha256 ---')
print(hash256)
print('--- Dados ASCII ---')
print(hashAscii)
print('Signature')
print(signature)

#input('bu')



### reference 

## HMAC e SHA
# youtube.com/watch?v=uyPr4PYN2zE