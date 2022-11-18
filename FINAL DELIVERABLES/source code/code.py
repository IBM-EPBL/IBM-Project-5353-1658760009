import time
import sys
import ibmiotf.application
import ibmiotf.device
import random


#Provide your IBM Watson Device Credentials
organization = "w1nouz"
deviceType = "riverwatermonitor1"
deviceId = "monitorsensor1"
authMethod = "token"
authToken = "!yjEh7zDC6(Cf@s&Rz"

# Initialize GPIO
def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    status=cmd.data['command']
    if status=="Light on":
        print ("LED is on")
    else:
        print ("LED is off")
   
    #print(cmd)
    
        


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
        
        temp=random.randint(0,100)
        pH=random.randint(0,100)
        turbidity = random.randint(0,100)
        
        data = { 'Temperature' : temp, 'pH' : pH, 'turbidity' : turbidity }
        #print data
        def myOnPublishCallback():
            print ("Published Temperature = %s C" % temp, "pH = %s %%" % pH, "turbidity = %s %%" %turbidity ,"to IBM Watson")

        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
