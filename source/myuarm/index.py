import serial
import serial.tools.list_ports
import time
#import index as myu

print ('hello')
movelist = ['G0 X100 Y100 Z100 F100\n','G0 X65 Y132 Z80 F100\n','G0 X00 Y132 Z80 F100\n','G0 X-55 Y146 Z80 F100\n','G0 X73 Y200 Z80 F100\n','G0 X10 Y200 Z80 F100\n','G0 X-50 Y214 Z80 F100\n','G0 X80 Y268 Z80 F100\n','G0 X10 Y268 Z80 F100\n','G0 X-45 Y282 Z80 F100\n']
ports = list(serial.tools.list_ports.comports())

print (ports)

for p in ports:
    global ser
    print (p[1])
    if ("SERIAL" in p[1])or("Serial" in p[1])or("FT232R USB UART" in p[1]):
	    ser = serial.Serial(port=p[0],baudrate=115200)
    else :
        # ser = serial.Serial(port="24",baudrate=115200)
	    print ("No Serial or SERIAL Device was found connected to the computer")
#ser=serial.Serial(port='COM6')
def moveurm(action=0):
    id=1

    cmdtail = movelist[action]
    cmd='#'+str(id)+' '+cmdtail
    ser.write(cmd.encode())
    print(movelist[action])
    time.sleep(2)#1.5
def initzero(waitime=2): #waitime=1
    id =1
    cmdtail = 'G0 X100 Y100 Z100 F100\n'
    cmd='#'+str(id)+' '+cmdtail
    ser.write(cmd.encode())
    time.sleep(waitime)
def testuarm():
    for i in range(0,10) :
        moveurm(i)
        initzero(2)#1.5
def test():
    uarmcatch(5)
    uarmrelease()
def uarmcatch(waitime=2):#waitime=1
    cmd='#1 M231 V1\n'
    ser.write(cmd.encode())
    print(ser.readline())
    time.sleep(waitime)
def uarmrelease(waitime=1):
    cmd='#1 M231 V0\n'
    ser.write(cmd.encode())
    print(ser.readline())
    time.sleep(waitime)
def catchinit(waitime=1.5):
    routelist = ['G0 X100 Y80 Z200 F100\n','G0 X100 Y81 Z200 F100\n','G0 X100 Y82 Z80 F100\n']

    id=1
    for i in range(0,3):
        cmdtail = routelist[i]
        cmd='#'+str(id)+' '+cmdtail
        ser.write(cmd.encode())
        time.sleep(waitime)
        print(cmd)
        print(ser.readline())

def anywhere(cmdtail):
    waitime = 1
    id=1
    cmd='#'+str(id)+' '+cmdtail
    ser.write(cmd.encode())
    print(ser.readline())
    time.sleep(waitime)
def playchess():


    for i in range(1,6):
        catchinit(1.5)
        uarmcatch()
        anywhere('G0 X100 Y80 Z200 F100\n')
        moveurm(i)
        uarmrelease()
        initzero()

def run(a):
#    global a 
    
   # myu.uarminit()
   # myu.putchess(0)
    action = "aaa"
    id=1
#    while action != "q":
    while a != "10":
        id=id+1
        print ('select which tone do you want to play ? 1,2,3, q and others for quit')
#        action = input("> ")
        if (action == "0"or a==0):
            cmdtail='G0 X100 Y100 Z100 F100\n'
            a=10
        elif (action == "1"or a==1):
            cmdtail='G0 X65 Y132 Z80 F100\n'
            a=10
        elif (action == "2"or a==2):
            cmdtail='G0 X00 Y132 Z80 F100\n'
            a=10
        elif (action == "3"or a==3):
            cmdtail='G0 X-55 Y146 Z80 F100\n'
            a=10
        elif (action == "4"or a==4):
            cmdtail='G0 X73 Y200 Z80 F100\n'
            a=10
        elif (action == "5"or a==5):
            cmdtail='G0 X10 Y200 Z80 F100\n'
            a=10
        elif (action == "6"or a==6):
            cmdtail='G0 X-50 Y214 Z80 F100\n'
            a=10
        elif (action == "7"or a==7):
            cmdtail='G0 X80 Y268 Z80 F100\n'
            a=10
        elif (action == "8"or a==8):
            cmdtail='G0 X10 Y268 Z80 F100\n'
            a=10
        elif (action == "9"or a==9):
            cmdtail='G0 X-45 Y282 Z80 F100\n'
            a=10
        else :
            return
        cmd='#'+str(id)+' '+cmdtail
        time.sleep(2)
        ser.write(cmd.encode())
        print(cmd)
        print(ser.readline())
        time.sleep(2)
        cmd='#'+str(id)+' '+'G0 X100 Y100 Z100 F100\n'
        ser.write(cmd.encode())
        print(cmd)
        print(ser.readline())

run(a=10)
