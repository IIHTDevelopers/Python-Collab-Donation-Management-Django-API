#python manage.py test donationapp.test.test_exceptional
from rest_framework.test import APITestCase
from donationapp.models import NGOModel,DonorModel,DonationModel,DonationRequestModel
from donationapp.test.TestUtils import TestUtils
class DonationManagementAPIExceptionalTest(APITestCase):
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

    def test_get_all_ngo_error(self):
        url='http://127.0.0.1:8000/ngox/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==404:
            test_obj.yakshaAssert("NGO_TestGetAllNgosError", True, "exception")
            print("NGO_TestGetAllNgosError = Passed")
        else:
            test_obj.yakshaAssert("NGO_TestGetAllNgosError", False, "exception")
            print("NGO_TestGetAllNgosError = Failed")
    def test_get_single_ngo_error(self):
        url='http://127.0.0.1:8000/ngo_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("NGO_TestGetSingleNgoError", True, "exception")
            print("NGO_TestGetSingleNgoError = Passed")
        else:
            test_obj.yakshaAssert("NGO_TestGetSingleNgoError", False, "exception")
            print("NGO_TestGetSingleNgoError = Failed")

    def test_post_ngo_error(self):
        url='http://127.0.0.1:8000/ngo/'
        data= {
        "ngo_id": 1,
        "ngo_name": "Ngo1",
        "username": "ngouser1",
        "password": "ngopwd1",
        "address": "#301,Plaza estate\r\nHyderabad",
        "phone_number": 9934567845,
        # "started_in": "2020-09-09",
        # "documents": "sample documents"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("NGO_TestPostNgoError", True, "exception")
            print("NGO_TestPostNgoError = Passed")
        else:
            test_obj.yakshaAssert("NGO_TestPostNgoError", False, "exception")
            print("NGO_TestPostNgoError = Failed")

    def test_update_ngo_error(self):
        url='http://127.0.0.1:8000/ngo_pk/111/'
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
        if response.status_code==500:
            test_obj.yakshaAssert("NGO_TesUpdateNgoError", True, "exception")
            print("NGO_TesUpdateNgoError = Passed")
        else:
            test_obj.yakshaAssert("NGO_TesUpdateNgoError", False, "exception")
            print("NGO_TesUpdateNgoError = Failed")

    def test_delete_ngo_error(self):
        url='http://127.0.0.1:8000/ngo_pk/111/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("NGO_TestDeleteNgoError", True, "exception")
            print("NGO_TestDeleteNgoError = Passed")
        else:
            test_obj.yakshaAssert("NGO_TestDeleteNgoError", False, "exception")
            print("NGO_TestDeleteNgoError = Failed")

#Donar

    def test_get_all_donar_error(self):
        url='http://127.0.0.1:8000/donarx/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==404:
            test_obj.yakshaAssert("Donar_TestGetAllDonarError", True, "exception")
            print("Donar_TestGetAllDonarError = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestGetAllDonarError", False, "exception")
            print("Donar_TestGetAllDonarError = Failed")

    def test_get_single_donar_error(self):
        url='http://127.0.0.1:8000/donar_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Donar_TestGetSingleDonarError", True, "exception")
            print("Donar_TestGetSingleDonarError = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestGetSingleDonarError", False, "exception")
            print("Donar_TestGetSingleDonarError = Failed")

    def test_post_donar_error(self):
        url='http://127.0.0.1:8000/donar/'
        data= {
        "donar_id": 1,
        "ngo_id": 1,
        "donar_name": "Donar1",
        "username": "donaruser1",
        "password": "donarpwd1",
        "email_id": "donar@gmail.com",
        # "phone_number": 98856498648,
        # "address": "Tirupathi"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Donar_TestPostDonarError", True, "exception")
            print("Donar_TestPostDonarError = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestPostDonarError", False, "exception")
            print("Donar_TestPostDonarError = Failed")

    def test_update_donar_error(self):
        url='http://127.0.0.1:8000/donar_pk/111/'
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
        if response.status_code==500:
            test_obj.yakshaAssert("Donar_TesUpdateDonarError", True, "exception")
            print("Donar_TesUpdateDonarError = Passed")
        else:
            test_obj.yakshaAssert("Donar_TesUpdateDonarError", False, "exception")
            print("Donar_TesUpdateDonarError = Failed")

    def test_delete_donar_error(self):
        url='http://127.0.0.1:8000/donar_pk/111/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Donar_TestDeleteDonarError", True, "exception")
            print("Donar_TestDeleteDonarError = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestDeleteDonarError", False, "exception")
            print("Donar_TestDeleteDonarError = Failed")

    def test_get_donar_by_ngo_error(self):
        url='http://127.0.0.1:8000/donar_ngo_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Donar_TestGetDonarByNgoError", True, "exception")
            print("Donar_TestGetDonarByNgoError = Passed")
        else:
            test_obj.yakshaAssert("Donar_TestGetDonarByNgoError", False, "exception")
            print("Donar_TestGetDonarByNgoError = Failed")

#Donation

    def test_get_all_donation_error(self):
        url='http://127.0.0.1:8000/donationx/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==404:
            test_obj.yakshaAssert("Donation_TestGetAllDonationError", True, "exception")
            print("Donation_TestGetAllDonationError = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestGetAllDonationError", False, "exception")
            print("Donation_TestGetAllDonationError = Failed")
    def test_get_single_donation_error(self):
        url='http://127.0.0.1:8000/donation_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Donation_TestGetSingleDonationError", True, "exception")
            print("Donation_TestGetSingleDonationError = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestGetSingleDonationError", False, "exception")
            print("Donation_TestGetSingleNgoError = Failed")

    def test_post_donation_error(self):
        url='http://127.0.0.1:8000/donation/'
        data= {
        "donation_id": 1,
        "ngo_id": 1,
        "donation_type": "Type1",
        "amount": "10000.00",
        # "donation_date": "2022-04-13",
        # "donar_id": 1
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Donation_TestPostDonationError", True, "exception")
            print("Donation_TestPostDonationError = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestPostDonationError", False, "exception")
            print("Donation_TestPostDonationError = Failed")

    def test_update_donation_error(self):
        url='http://127.0.0.1:8000/donation_pk/111/'
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
        if response.status_code==500:
            test_obj.yakshaAssert("Donation_TestUpdateDonationError", True, "exception")
            print("Donation_TestUpdateDonationError = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestUpdateDonationError", False, "exception")
            print("Donation_TestUpdateDonationError = Failed")

    def test_delete_donation_error(self):
        url='http://127.0.0.1:8000/donation_pk/111/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Donation_TestDeleteDonationError", True, "exception")
            print("Donation_TestDeleteDonationError = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestDeleteDonationError", False, "exception")
            print("Donation_TestDeleteDonationError = Failed")

    def test_get_donation_by_donar_error(self):
        url='http://127.0.0.1:8000/donation_donar_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Donation_TestGetDonationByDonarError", True, "exception")
            print("Donation_TestGetDonationByDonarError = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestGetDonationByDonarError", False, "exception")
            print("Donation_TestGetDonationByDonarError = Failed")

    def test_get_donation_by_ngo_error(self):
        url='http://127.0.0.1:8000/donation_ngo_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Donation_TestGetDonationByNgoError", True, "exception")
            print("Donation_TestGetDonationByNgoError = Passed")
        else:
            test_obj.yakshaAssert("Donation_TestGetDonationByNgoError", False, "exception")
            print("Donation_TestGetDonationByNgoError = Failed")


#DonationRequest

    def test_post_donation_request_error(self):
        url='http://127.0.0.1:8000/donation_request/'
        data=     {
        "request_id": 1,
        "amount": "25000.00",
        "donar_id": 1,
        # "ngo_id": 1,
        # "donation_end_date": "2022-06-20"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("DonationRequest_TestPostDonationRequestError", True, "exception")
            print("DonationRequest_TestPostDonationRequestError = Passed")
        else:
            test_obj.yakshaAssert("DonationRequest_TestPostDonationRequestError", False, "exception")
            print("DonationRequest_TestPostDonationRequestError = Failed")

    def test_get_donation_request_by_donar_error(self):
        url='http://127.0.0.1:8000/donation_request_donar_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("DonationRequest_TestGetDonationRequestByDonarError", True, "exception")
            print("DonationRequest_TestGetDonationRequestByDonarError = Passed")
        else:
            test_obj.yakshaAssert("DonationRequest_TestGetDonationRequestByDonarError", False, "exception")
            print("DonationRequest_TestGetDonationRequestByDonarError = Failed")

    def test_get_donation_request_by_ngo_error(self):
        url='http://127.0.0.1:8000/donation_request_ngo_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("DonationRequest_TestGetDonationRequestByNgoError", True, "exception")
            print("DonationRequest_TestGetDonationRequestByNgoError = Passed")
        else:
            test_obj.yakshaAssert("DonationRequest_TestGetDonationRequestByNgoError", False, "exception")
            print("DonationRequest_TestGetDonationRequestByNgoError = Failed")
