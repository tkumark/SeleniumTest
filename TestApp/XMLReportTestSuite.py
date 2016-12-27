import unittest
from xmlrunner import xmlrunner
from AppLoad import TestSite

# get all tests from SearchProductTest and HomePageTest class
remote_tests = unittest.TestLoader().loadTestsFromTestCase(TestSite)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([remote_tests])
# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)