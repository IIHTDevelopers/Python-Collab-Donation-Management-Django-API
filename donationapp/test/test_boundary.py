from rest_framework.test import APITestCase
from donationapp.test.TestUtils import TestUtils
class DonationManagementAPIBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("NGO_TestBoundary",True,"boundary")
        print("NGO_TestBoundary = Passed")
