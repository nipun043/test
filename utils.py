import requests
import os
import re
import sys
import time
import collections
import logging
import json
from ats.log.utils import banner
log = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
###################################################################
###                     COMMOM UTIL API SECTION                 ###
###################################################################

###########################################################################################
#   all common rest API calls are defined in the class below                              #
#                                                                                         #
###########################################################################################


class api():

   
   def __init__(self,testbed=None):
       self.testbed = testbed
   
   def post(self,url=None,params=None,verify=None,auth=None,filename=None,headers=None,data=None):

       if filename:
          with open(filename,'rb') as f:
              self.res = requests.post(url=url,params=params,verify=verify,auth=auth, files={'file':f},headers=headers,json=data)
       else:
            self.res = requests.post(url=url,params=params,verify=verify,auth=auth,headers=headers,json=data)

       self.httpStatus = self.res.status_code
       self.apiOutput = json.loads(self.res.text)


       return(self.httpStatus,self.apiOutput)
   
   def get(self,url=None,params=None,verify=None,auth=None,filename=None,data=None):

       self.res = requests.get(url=url, verify=verify, auth=auth, params=params,files=filename,json=data)
       self.httpStatus = self.res.status_code
       self.apiOutput = json.loads(self.res.text)

       return (self.httpStatus,self.apiOutput)

   def put(self,url=None,params=None,verify=None,auth=None,filename=None,data=None, headers=None):

       self.res = requests.put(url=url, verify=verify, auth=auth, params=params, files=filename,json=data, headers=headers)

       self.httpStatus = self.res.status_code
       self.apiOutput = json.loads(self.res.text)

       return (self.httpStatus, self.apiOutput)


   def delete(self,url=None,params=None,verify=None,auth=None,filename=None,headers=None,data=None):

       self.res = requests.delete(url=url, verify=verify, auth=auth, params=params, files=filename,headers=headers,json=data)
       self.httpStatus = self.res.status_code
       self.apiOutput = json.loads(self.res.text)

       return (self.httpStatus, self.apiOutput)
   

   
