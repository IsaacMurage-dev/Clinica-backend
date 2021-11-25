
from django.test import Vaccine,Growth,MedicalHistory
import unittest


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a vaccine.
        self.client = Vaccine()

    def test_details(self):
        # Issue a GET request.
        response = self.vaccine.get('/patient/vaccines/brand_name/batch_number/drug_expiry/next-appointment/date_given')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 7 vaccine.
        self.assertEqual(len(response.context['vaccines']), 7)

        #growth

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs  growth.
        self.client = Growth()

    def test_details(self):
        # Issue a GET request.
        response = self.growth.get('/patient/age/weight/height/HO/date')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 6 growth.
        self.assertEqual(len(response.context['growth']), 6)        

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs  growth.
        self.client = MedicalHistory()

    def test_details(self):
        # Issue a GET request.
        response = self.growth.get('/patient/disease_history/doctor_recommendation')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 3 medical_history.
        self.assertEqual(len(response.context['medical_history']), 3)             