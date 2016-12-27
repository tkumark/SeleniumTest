import unittest
#from RemoteTest import Test
import HTMLTestRunner 
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("testsuites", help="pass testsuite")

args = parser.parse_args()

testSuites = args.testsuites.split(',')

resultdir = os.getcwd()

loadedTestSuites=[]

for testSuite in testSuites:
    testMod = __import__(testSuite.split('.')[0])
    testClass = getattr(testMod,testSuite.split('.')[1])
    loadTestSuite = unittest.TestLoader().loadTestsFromTestCase(testClass)
    loadedTestSuites.append(loadTestSuite)      
      
smoke_test = unittest.TestSuite(loadedTestSuites)

outputfile = open(resultdir+'/SmokeTestReport.html','w')

runner = HTMLTestRunner.HTMLTestRunner(stream=outputfile,title="TK Sanity Test Report",description='test description')


runner.run(smoke_test)