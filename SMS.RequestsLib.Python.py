import requests
import json

url = 'http://npwifi.smart.com.ph:8080/1/smsmessaging/outbound/4067/requests'
payload = { "outboundSMSMessageRequest": { "address":["tel:639177192127"], "senderAddress":"4067", "outboundSMSTextMessage": { "message":"hello" } } }

headers = {'Authorization': 'WSSE realm="SDP",profile="UsernameToken"','Content-Type': 'application/json','X-WSSE': 'UsernameToken Username="001007",PasswordDigest="msXnMGOepXf+5KInX1Gbm6tfVZg=",Nonce="2010082108334600001", Created="2010-08-21T08:33:46Z"','Accept-Encoding': 'gzip,deflate','Accept': 'application/json','X-RequestHeader': 'request TransId="200903241230451000000000000000",ServiceId="0010072000001279"'}

r = requests.post(url,data=json.dumps(payload),headers=headers)
print r.status_code
