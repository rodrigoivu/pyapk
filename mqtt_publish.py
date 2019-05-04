import paho.mqtt.publish as publish
import time
import datetime
#from mscl import mscl

# try:
#     # connection = mscl.Connection.Serial(“/dev/ttyUSB0”,921600)
#     # baseStation = mscl.BaseStation(connection)
while True:
	# sweeps = baseStation.getData(500)
	# for sweep in sweeps:
	#     print ("Packet Received")
	#     print ("Node", sweep.nodeAddress())
	#     print ("Timestamp", sweep.timestamp())
	#     print ("Tick", sweep.tick())
	#     print ("Sample Rate", sweep.sampleRate().prettyStr())
	#     print ("Base RSSI: ", sweep.baseRssi())
	#     print ("Node RSSI: ", sweep.nodeRssi())
	#     print "DATA: ",
	#     for dataPoint in sweep.data():
	#         print dataPoint.channelName(), ":", dataPoint.as_string(),
	#     print ""
	time.sleep(30)
	tstamp = str(datetime.datetime.now())
	ch1_1  = str(100)
	ch2_1  = str(100)
	ch1_2  = str(100)
	ch2_2  = str(100)
	ch1_3  = str(100)
	ch2_3  = str(100)
	ch1_4  = str(100)
	ch2_4  = str(100)
	ch1_5  = str(100)
	ch2_5  = str(100)
	ch1_6  = str(100)
	ch2_6  = str(100)
	msj="{'timestamp':"+tstamp+",'ch1_1':"+ch1_1+",'ch2_1':"+ch2_1+",'ch1_2':"+ch1_2+",'ch2_2':"+ch2_2+",'ch1_3':"+ch1_3+",'ch2_3':"+ch2_3+",'ch1_4':"+ch1_4+",'ch2_4':"+ch2_4+",'ch1_5':"+ch1_5+",'ch2_5':"+ch2_5+",'ch1_6':"+ch1_6+",'ch2_6':"+ch2_6+"}"
	publish.single("aplik/esfuerzo/harnero1", msj, hostname="165.227.26.150")
# except :
#     print("Error:")




#Multiples
 
#msgs = [{'topic': "paho/test/multiple", 'payload': "multiple 1"}, ("paho/test/multiple", "multiple 2", 0, False)]
#publish.multiple(msgs, hostname="165.227.26.150")