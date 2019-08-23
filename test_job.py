# To run the job:
# easypy $VIRTUAL_ENV/examples/basic/job/basic_example_job.py
# Description: This example shows the basic functionality of pyats
#              with few passing tests
import logging
import os
from ats.easypy import run
from ats.easypy import Task
log = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)


# All run() must be inside a main function
def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testscript1 = os.path.join(test_path, '/test/test.py')

    
    result = run(testscript=testscript1)
    
    log.info('*****************************************************************')
    log.info('********* RESULT OF VEGA SANITY IS %s **********', str(result).upper())
    log.info('*****************************************************************')
