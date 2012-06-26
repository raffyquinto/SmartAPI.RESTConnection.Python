import sys, httplib

class SmartSMS(object):
#Class SmartSMS is a python class that allows a programmer to utilize Smart's 
#SMS infrastructire using REST Architecture. In order to use this, the 
#programmer must configure the class instance with Smart API credentials.
    
    def __init__(self,spID="",servID="",passwd="",creationTime="",nonce="",accessCode=""):
    #SmartSMS Class Constructor
        if(spID is not None and servID is not None and passwd is not None and creationTime is not None and nonce is not None and accessCode is not None):
            self.spID = spID
            self.servID = servID
            self.passwd = passwd
            self.creationTime = creationTime
            self.nonce = nonce
            self.accessCode = accessCode
        
    def setSPID(self,spID):
    #sets the Sp ID 
        self.spID = spID
    
    def setServiceID(self,servID):
    #sets the Service ID
        self.servID = servID
    
    def setPassword(self,passwd):
    #sets the password
        self.passwd = passwd
    
    def setCreationTime(self,creationTime):
    #sets the Creation Time
        self.creationTime = creationTime
    
    def setNonce(self,nonce):
    #sets the nonce
        self.nonce = nonce
    
    def setAccessCode(self,accessCode):
    #sets the access code
        self.accessCode = accessCode
    
    def getSPID(self):
    #returns the Sp ID
        return str(self.spID)
    
    def getServiceID(self):
    #returns the service ID
        return str(self.servID)
    
    def getPassword(self):
    #returns the password
        return str(self.passwd)
    
    def getCreationTime(self):
    #returns the creation time
        return str(self.creationTime)
    
    def getNonce(self):
    #returns the nonce
        return str(self.nonce)
    
    def getAccessCode(self):
    #returns the access code
        return str(self.accessCode)
    
    XML_TEMPLATE = """<sms:outboundSMSMessageRequest xmlns:sms="urn:oma:xml:rest:sms:1">
    <address>tel:%s</address>
    <senderAddress>%s</senderAddress>
    <senderName>MyName</senderName>
    <outboundSMSTextMessage>
    <message>%s</message>
    </outboundSMSTextMessage>
    </sms:outboundSMSMessageRequest>
    """
    
    
    def setMessage(self, msg):
    #sets the short message
        self.msg = msg

    def setRecipient(self, receiver):
    #sets the mobile number of the receiver
        self.receiver = receiver
        
    def getMessage(self):
    #returns the short message
        return str(self.msg)
    
    def getRecipeint(self):
    #returns the mobile number of the receiver
        return str(self.receiver)
    
    def sendSMS(self):
    #sends a POST to smart's server using RESTful service. Returns a tuple (statuscode, statusmessage, header)
        RestMessage = self.XML_TEMPLATE%(self.getRecipeint(),self.getAccessCode(),self.getMessage())
        webservice = httplib.HTTP("npwifi.smart.com.ph", 8080)
        webservice.putrequest("POST", "/1/smsmessaging/outbound/"+self.getAccessCode()+"/requests")
        webservice.putheader("Host", "npwifi.smart.com.ph:8080")
        webservice.putheader("Accept-Encoding", "gzip,deflate")
        webservice.putheader("User-Agent", "Python post")
        webservice.putheader("Content-type", "text/xml;charset=\"UTF-8\"")
        webservice.putheader("Content-length", "%d" % len(RestMessage))
        webservice.putheader("Authorization", "WSSE realm=\"SDP\",profile=\"UsernameToken\"")
        webservice.putheader("X-WSSE", "UsernameToken Username=\""+self.getSPID()+"\",PasswordDigest=\""+self.getPassword()+"\",Nonce=\""+self.getNonce()+"\", Created=\""+self.getCreationTime()+"\"")
        webservice.putheader("X-RequestHeader", "request TransId=\"123456789012345678901234567890\",ServiceId=\""+self.getServiceID()+"\"")
        
        webservice.endheaders()
        webservice.send(RestMessage)
        
        return webservice.getreply()