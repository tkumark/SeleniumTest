import unittest
import HTMLTestRunner 
import os
from AppLoad import TestSite

resultdir = os.getcwd()
loadTestSuite = unittest.TestLoader().loadTestsFromTestCase(TestSite)
smoke_test = unittest.TestSuite([loadTestSuite])

outputfile = open(resultdir+'/SmokeTestReport.html','w')

runner = HTMLTestRunner.HTMLTestRunner(stream=outputfile,title="TK Sanity Test Report",description='test description')

runner.run(smoke_test)