import hmac
import hashlib
import base64
import json

from datetime import datetime

key = 'senha'
method = 'post'
dataPed = '{"CpfCnpj": "02733105345", "CodigoOperacao": "500", "Data": "2022-02-10T15:00:00", "Produtos": [{"Codigo": "1", "CodigoCor": null, "CodigoTamanho": null, "Quantidade": 1.0000, "PrecoUnitario": 100.34, "DescontoUnitario": 0.00}], "Recebimentos": [{"ValorParcelas": 100.34, "Tipo": "CR"}], "DadosEntrega": {"Valor": 10.00, "NaoSomarFreteTotalNota": true, "OutroEndereco": {"Cep": "82600380", "Endereco": "Rua Nunia", "Numero": "11", "Complemento": null, "Bairro": "Teste", "Cidade": "Curitiba", "Uf": "PR"}}}'
dataPedido = str.encode(dataPed)
body2 = base64.b64encode(dataPedido)
body = str(body2)[2:-1]
print('--- Body ---')
print(body)

now = datetime.now()
timestamp = str(datetime.timestamp(now))[:10]
#encodedkey = str.encode(key)
encodedkey = key.encode('UTF-8')
sha256_hash = hashlib.sha256()

valoresContatenados = f'{method}{timestamp}{body}'
concatenados = valoresContatenados.encode('UTF-8')

print('--- Concatenado ---')
print(concatenados)

hash256 = hmac.new(encodedkey, concatenados, hashlib.sha256).hexdigest()
print('--- Encriptado com hmac sha256 ---')
print(hash256)

hashAscii = bytes.fromhex(hash256)
print('--- Dados ASCII ---')
print(hashAscii)

signature = str(base64.b64encode(hashAscii))
print('Signature')
print(signature)

#input('bu')



### reference 

## HMAC e SHA
# youtube.com/watch?v=uyPr4PYN2zE