import yaml
#from ats import tcl
import os
import sys
import logging
import time
import requests
from ats import aetest
from ats import easypy
from ats import results
log = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)
from ats import topology
from ats.topology import loader
import json
#import csccon
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from utils import api

global testbed
global test
global error
error = []

## instance of utils class ###

test = api()

print('STARTING TESTS')




class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def load_testbed(self,testbed):

        logging.basicConfig(format='%(asctime)s %(message)s')
        log.info("******* LOADING TESTBED TOPOLOGY ********")

        try:
            assert testbed
            testbed.devices['rainer-isr1'].connect()
        except AssertionError:
            self.failed('********* DEVICES WERE NOT FOUND IN THE TESTBED FILE  **********')
        log.info('Testbed object is loaded as ' + str(testbed))
        log.info("******* LOADED TESTBED TOPOLOGY ********")



class tests(aetest.Testcase):

   #### PUT test function here #####

    @aetest.test
    def connectAndTest(self, testbed):
        out1 = testbed.devices['rainer-isr1'].execute('show ip interface brief')
        print(out1)


    @aetest.test
    def claimGateway(self, testbed):
        log.info("******* CLAIMING GATEWAY on CORE SVC ********")

        #GATHER TEST PROPERTIES FOR API CALL
        testcases = testbed.devices['rainier'].custom
        url = str(testcases['Claim']['url'])
        auth = (str(testcases['Claim']['username']), str(testcases['Claim']['password']))
        headers = (testcases['Claim']['headers'])
        data = (testcases['Claim']['json'])
        httpStatus = str(testcases['Claim']['expectedHttp'])
        appStatus = str(testcases['Claim']['expectedStatus'])

        #Test POST API -> CLAIMING GW
        log.info("******* API CALL ********")

        #result = test.post(url, verify=False, headers=headers, auth=auth, data=data)
        result = test.get(url)
        print(result)
        #CHECK IF DEVICE WAS ADDED
        try:
            time.sleep(5)
            assert str(result[0]) == httpStatus 
            print(httpStatus)
            log.info("Added gateway to Core , status code is %s" % (httpStatus))
        except AssertionError:
            self.failed('********* Failed to add Gateway to Core SVC **********')

        return True


class CommonCleanup(aetest.CommonCleanup):


    @aetest.subsection
    def disconnect_from_devices(self, testbed):

        log.info("******* DISCONNECTING FROM DEVICES IN TESTBED  ********")

        ######## Disconnect from devices and check if successful #########
        testbed.devices['rainer-isr1'].disconnect()

        log.info("******* DISCONNECTED FROM DEVICES IN TESTBED  ********")


######## script starts executing here #########

if __name__ == '__main__':

        import argparse
        parser = argparse.ArgumentParser()

        parser.add_argument('--testbed', type = topology.loader.load)

        args, unknwon = parser.parse_known_args()
        aetest.main(**vars(args))
