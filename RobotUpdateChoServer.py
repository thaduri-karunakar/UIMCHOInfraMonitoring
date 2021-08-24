from pypsexec.client import Client
import time
import sys # to raise specific exception using sys.exc_info()
start = time.time()
ip ='10.17.162.2'
try:
    c = Client('10.17.162.2', 'administrator', 'interOP@123', encrypt='False')
    c.connect()
    c.create_service()
    print('service created for following "{}".......\n\n'.format(ip))
    hubCount = 9
    #robotCount = 1
    for hub in range(hubCount,31):
        robotCount = 1
        for robot in range(1, 101):
            callback = r"""C:\Progra~1\Nimsoft\bin\pu -u administrator -p interOP@123 /CHOSERVER1_domain/CHOSERVER1_hub/CHOSERVER1/automated_deployment_engine deploy_probe robot_update 9.30 /CHOSERVER1_domain/chosechub{}/my{}robot{}""".format(hubCount,hubCount,robotCount)
            print(callback)
            stdout, stderr, rc= c.run_executable("cmd.exe",arguments='''/c "{}"'''.format(callback))
            stdout = str(stdout, 'utf-8')
            stderr = str(stderr, 'utf-8')
            # print (rc)
            #if rc == 0:
                #print('Call back executed successfully :\nCallBackName :\n{}\nOutPut :\n{}\n\n'.format(callback, stdout))
            if rc != 0:
                print('Call back failed with error :\nCallBackName :\n{}\nOutPut :\n{}\n\n{}\n\n'.format(callback, stderr,stdout))

            time.sleep(1)
            robotCount+=1
        print('=======================================================================')
        print('Sleeping for 1 minute..........')
        time.sleep(60)
        hubCount+=1
except Exception as e:
    print('Below exception occured .....\n')
    print(e)
    print()

finally:
    c.remove_service()
    c.disconnect()
print('service removed for following "{}"'.format(ip))
print ('Script has taken',(time.time()-start)/60, 'Minuts..')