from pypsexec.client import Client
import time

start = time.time()
ip = '10.17.162.4'
'''robotList = ['myBhutanrobot', 'myChinarobot', 'myIndiarobot', 'myIranrobot', 'myIraqrobot',
             'myIsraelrobot', 'myJapanrobot', 'myJordanrobot','myKuwaitrobot', 'myNKorearobot', 'myNepalrobot',
             'myOmanrobot', 'myQatarrobot', 'mySKorearobot', 'mySrilankarobot', 'myTaiwanrobot', 'myThailandrobot',
             'myVietnamrobot', 'myYemenrobot']'''
robotList = ['myYemenrobot']
probeList = ['cdm', 'processes']
probeStatus = 'probe_deactivate'
try:
    c = Client(ip, 'administrator', 'CHOUMP1123$', encrypt='False')
    c.connect()
    c.create_service()
    print('service created for following "{}".......\n\n'.format(ip))

    #robotCount = 1
    for robot in robotList:
        for robotCount in range(1, 101):
            for probe in probeList:
                callback = r"""C:\Progra~1\Nimsoft\bin\pu -u administrator -p interOP@123 /CHOSERVER1_domain/chosechub1/{}{}/controller {} {} """.format(robot, robotCount, probeStatus, probe)
                print(callback)
                stdout, stderr, rc= c.run_executable("cmd.exe",arguments='''/c "{}"'''.format(callback))
                stdout = str(stdout, 'utf-8')
                stderr = str(stderr, 'utf-8')
                # print (rc)
                #if rc == 0:
                #print('Call back executed successfully :\nCallBackName :\n{}\nOutPut :\n{}\n\n'.format(callback, stdout))
                if rc != 0:
                    print('Call back failed with error :\nCallBackName :\n{}\nOutPut :\n{}\n\n{}\n\n'.format(callback, stderr,stdout))

                # time.sleep(1)
            print('='*90)
        # print('=======================================================================')
        print('Sleeping for 10 Seconds..........')
        time.sleep(10)
except Exception as e:
    print('Below exception occured .....\n')
    print(e)
    print()

finally:
    c.remove_service()
    c.disconnect()
print('service removed for following "{}"'.format(ip))
print ('Script has taken',(time.time()-start)/60, 'Minuets..')