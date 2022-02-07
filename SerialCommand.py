
import serial
import time

class Lock:
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.parity = serial.PARITY_NONE
        self.ser.bytesize =8
        self.ser.stopbits = 1
        self.ser.port = "COM20"
        self.ser.timeout = 1
        if self.ser.isOpen():
            print( "["+ self.ser.portstr + '] is Open')
    def open (self) :
        print("[INFO]Opening in progress ...")
        for val in range(90,200):
            self.ser.open()
            self.ser.write([val])
            time.sleep(0.03)
            self.ser.close()
    def close (self):
        val =200
        print("[INFO]Closing in progress ...")

        while val !=90:
            val-=1
            self.ser.open()
            self.ser.write([val])
            time.sleep(0.03)
            self.ser.close()






# val  =90
# while 1:
#
#     ser.open()
#     ser.write([val])
#     # time.sleep()
#     ser.close()
#     val  = int(input("Enter !"))
# # Ctrl+C to Close Python Window