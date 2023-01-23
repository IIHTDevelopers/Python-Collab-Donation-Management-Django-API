#python manage.py test donationapp.test.test_functional
from rest_framework.test import APITestCase
from donationapp.models import NGOModel,DonorModel,DonationModel,DonationRequestModel
from donationapp.test.TestUtils import TestUtils
class DonationManagementAPIFunctionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        NGOModel.objects.create(
        ngo_id= 1,
        ngo_name= "Ngo1",
        username="ngouser1",
        password= "ngopwd1",
        address= "#301,Plaza estate ,Hyderabad",
        phone_number= 9934567845,
        started_in= "2020-09-09",
        documents= "sample documents"
        )

        obj=DonorModel.objects.create(
        donar_id= 1,
        ngo_id= 1,
        donar_name= "Donar1",
        username= "donaruser1",
        password= "donarpwd1",
        email_id= "donar@gmail.com",
        phone_number= 98856498648,
        address= "Tirupathi")

        DonationModel.objects.create(
        donation_id= 1,
        donar_id=1,
        ngo_id= 1,
        donation_type= "Type1",
        amount= "10000.00",
        donation_date= "2022-04-13"
        )

        DonationRequestModel.objects.create(
        request_id= 1,
        amount= "25000.00",
        donar_id= 1,
        ngo_id= 1,
        donation_end_date= "2022-06-20"
        )

#NGO

    def test_get_all_ngo(self):
        url='http://127.0.0.1:8000/ngo/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("NGO_TestGetAllNgos", True, "functional")
            print("NGO_TestGetAllNgos = Passed")
        else:
            test_obj.yakshaAssert("NGO_TestGetAllNgos", False, "functional")
            print("NGO_TestGetAllNgos = Failed")

    def test_get_single_ngo(self):
        url='http://127.0.0.1:8000/ngo_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("NGO_TestGetSingleNgo", True, "functional")
            print("NGO_TestGetSingleNgo = Passed")
        else:
            test_obj.yakshaAssert("NGO_TestGetSingleNgo", False, "functional")
            print("NGO_TestGetSingleNgo = Failed")

    def test_post_ngo(self):
        url='http://127.0.0.1:8000/ngo/'
        data= {
        "ngo_id": 1,
        "ngo_name": "Ngo1",
        "username": "ngouser1",
        "password": "ngopwd1",
        "address": "#301,Plaza estate\r\nHyderabad",
        "phone_number": 9934567845,
        "started_in": "2020-09-09",
        "documents": "sample documents"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("NGO_TestPostNgo", True, "functional")
            print("NGO_TestPostNgo = Passed")
        else:
            test_obj.yakshaAssert("NGO_TestPostNgo", False, "functional")
            print("NGO_TestPostNgo = Failed")

    def test_update_ngo(self):
        url='http://127.0.0.1:8000/ngo_pk/1/'
        data= {
        "ngo_id": 1,
        "ngo_name": "Ngo1",
        "username": "ngouser1",
        "password": "ngopwd1",
        "address": "#301,Plaza estate\r\nHyderabad",
        "phone_number": 9934567840,
        "started_in": "2020-09-09",
        "documents": "sample documents"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("NGO_TesUpdateNgo", True, "functional")
            print("NGO_TesUpdateNgo = Passed")
        else:
            test_obj.yakshaAssert("NGO_TesUpdateNgo", False, "functional")
            print("NGO_TesUpdateNgo = Failed")

    def test_delete_ngo(self):
        url='http://127.0.0.1:8000/ngo_pk/1/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("NGO_TestDeleteNgo", True, "functional")
            print("NGO_TestDeleteNgo = Passed")
        else:
            test_obj.yakshaAssert("NGO_TestDeleteNgo", False, "functional")
            print("NGO_TestDeleteNgo = Failed")

#Donar

    def test_get_all_donar(self):
        url='http://127.0.0.1:8000/donar/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donar_TestGetAllDonar", True, "functional")
            print("Donar_TestGetAllDonar = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestGetAllDonar", False, "functional")
            print("Donar_TestGetAllDonar = Failed")

    def test_get_single_donar(self):
        url='http://127.0.0.1:8000/donar_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donar_TestGetSingleDonar", True, "functional")
            print("Donar_TestGetSingleDonar = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestGetSingleDonar", False, "functional")
            print("Donar_TestGetSingleDonar = Failed")

    def test_post_donar(self):
        url='http://127.0.0.1:8000/donar/'
        data= {
        "donar_id": 1,
        "ngo_id": 1,
        "donar_name": "Donar1",
        "username": "donaruser1",
        "password": "donarpwd1",
        "email_id": "donar@gmail.com",
        "phone_number": 98856498648,
        "address": "Tirupathi"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("Donar_TestPostDonar", True, "functional")
            print("Donar_TestPostDonar = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestPostDonar", False, "functional")
            print("Donar_TestPostDonar = Failed")

    def test_update_donar(self):
        url='http://127.0.0.1:8000/donar_pk/1/'
        data=  {
        "donar_id": 1,
        "ngo_id": 1,
        "donar_name": "Donar1",
        "username": "donaruser1",
        "password": "donarpwd1",
        "email_id": "donar@yahoo.com",
        "phone_number": 98856498640,
        "address": "Tirupathi"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donar_TesUpdateDonar", True, "functional")
            print("Donar_TesUpdateDonar = Passed")
        else:
            test_obj.yakshaAssert("Donar_TesUpdateDonar", False, "functional")
            print("Donar_TesUpdateDonar = Failed")

    def test_delete_donar(self):
        url='http://127.0.0.1:8000/donar_pk/1/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donar_TestDeleteDonar", True, "functional")
            print("Donar_TestDeleteDonar = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestDeleteDonar", False, "functional")
            print("Donar_TestDeleteDonar = Failed")

    def test_get_donar_by_ngo(self):
        url='http://127.0.0.1:8000/donar_ngo_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donar_TestGetDonarByNgo", True, "functional")
            print("Donar_TestGetDonarByNgo = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestGetDonarByNgo", False, "functional")
            print("Donar_TestGetDonarByNgo = Failed")

#Donation

    def test_get_all_donation(self):
        url='http://127.0.0.1:8000/donation/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donation_TestGetAllDonation", True, "functional")
            print("Donation_TestGetAllDonation = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestGetAllDonation", False, "functional")
            print("Donation_TestGetAllDonation = Failed")
    def test_get_single_donation(self):
        url='http://127.0.0.1:8000/donation_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donation_TestGetSingleDonation", True, "functional")
            print("Donation_TestGetSingleDonation = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestGetSingleDonation", False, "functional")
            print("Donation_TestGetSingleNgo = Failed")

    def test_post_donation(self):
        url='http://127.0.0.1:8000/donation/'
        data= {
        "donation_id": 1,
        "ngo_id": 1,
        "donation_type": "Type1",
        "amount": "10000.00",
        "donation_date": "2022-04-13",
        "donar_id": 1
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("Donation_TestPostDonation", True, "functional")
            print("Donation_TestPostDonation = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestPostDonation", False, "functional")
            print("Donation_TestPostDonation = Failed")

    def test_update_donation(self):
        url='http://127.0.0.1:8000/donation_pk/1/'
        data=     {
        "donation_id": 1,
        "ngo_id": 1,
        "donation_type": "Type1",
        "amount": "11000.00",
        "donation_date": "2022-04-13",
        "donar_id": 1
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donation_TesUpdateDonation", True, "functional")
            print("Donation_TesUpdateDonation = Passed")
        else:
            test_obj.yakshaAssert("Donation_TesUpdateDonation", False, "functional")
            print("Donation_TesUpdateDonation = Failed")

    def test_delete_donation(self):
        url='http://127.0.0.1:8000/donation_pk/1/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donation_TestDeleteDonation", True, "functional")
            print("Donation_TestDeleteDonation = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestDeleteDonation", False, "functional")
            print("Donation_TestDeleteDonation = Failed")

    def test_get_donation_by_donar(self):
        url='http://127.0.0.1:8000/donation_donar_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donation_TestGetDonationByDonar", True, "functional")
            print("Donation_TestGetDonationByDonar = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestGetDonationByDonar", False, "functional")
            print("Donation_TestGetDonationByDonar = Failed")

    def test_get_donation_by_ngo(self):
        url='http://127.0.0.1:8000/donation_ngo_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Donation_TestGetDonationByNgo", True, "functional")
            print("Donation_TestGetDonationByNgo = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestGetDonationByNgo", False, "functional")
            print("Donation_TestGetDonationByNgo = Failed")


#DonationRequest

    def test_post_donation_request(self):
        url='http://127.0.0.1:8000/donation_request/'
        data=     {
        "request_id": 1,
        "amount": "25000.00",
        "donar_id": 1,
        "ngo_id": 1,
        "donation_end_date": "2022-06-20"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("DonationRequest_TestPostDonationRequest", True, "functional")
            print("DonationRequest_TestPostDonationRequest = Passed")
        else:
            test_obj.yakshaAssert("DonationRequest_TestPostDonationRequest", False, "functional")
            print("DonationRequest_TestPostDonationRequest = Failed")

    def test_get_donation_request_by_donar(self):
        url='http://127.0.0.1:8000/donation_request_donar_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("DonationRequest_TestGetDonationRequestByDonar", True, "functional")
            print("DonationRequest_TestGetDonationRequestByDonar = Passed")
        else:
            test_obj.yakshaAssert("DonationRequest_TestGetDonationRequestByDonar", False, "functional")
            print("DonationRequest_TestGetDonationRequestByDonar = Failed")

    def test_get_donation_request_by_ngo(self):
        url='http://127.0.0.1:8000/donation_request_ngo_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("DonationRequest_TestGetDonationRequestByNgo", True, "functional")
            print("DonationRequest_TestGetDonationRequestByNgo = Passed")
        else:
            test_obj.yakshaAssert("DonationRequest_TestGetDonationRequestByNgo", False, "functional")
            print("DonationRequest_TestGetDonationRequestByNgo = Failed")
