import SmartAPI

#calling and using Smart SMS API using a Constructor (optional)
messaging = SmartAPI.SmartSMS(spID="001259",
                                  servID="0012592000001346",
                                  passwd="Fu9wPaknmbsIx2kk+kAMyX0I/7s=a",
                                  creationTime="2010-08-21T08:33:46Z",
                                  nonce="2010082108334600001",
                                  accessCode="406821")

#calling and using Smart SMS API without using
#constructor to instantiate credentials.
#Instead, using Setters... (optional)
"""
messaging = smsConnector.SmartSMS()
messaging.setSPID("001259")
messaging.setServiceID("0012592000001346")
messaging.setPassword("Fu9wPaknmbsIx2kk+kAMyX0I/7s=")
messaging.setCreationTime("2010-08-21T08:33:46Z")
messaging.setNonce("2010082108334600001")
messaging.setAccessCode("406821")
"""


messaging.setMessage("Sample Message") #Sets the Short Message that is to be sent. parameter
messaging.setRecipient("639177192127")#Sets the mobile number of the recipient. parameter, the number should start with 63**********
statuscode, statusmessage, header = messaging.sendSMS()#Sends the SMS and returns a Tuple

print statuscode
print statusmessage
print header