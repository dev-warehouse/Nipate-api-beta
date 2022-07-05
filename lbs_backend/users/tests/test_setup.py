from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import Gender
from locations.models import CountyModel, TownsModel


User = get_user_model()

class TestSetup(APITestCase):
    
    def setUp(self):
        self.register_url = reverse("user")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")

        self.user_a = {
            "IDNumber": 38598118, "FirstName": "Amos",
            "MobileNumber": "0794818111", "password": "amos2001"
        }
        self.user_b = {
            "IDNumber": 38598119, "FirstName": "Banda",
            "MobileNumber": "0794818112", "password": "amos2001"
        }
        self.gender = {
            "name": "Male"
        }
        Gender.objects.create(**self.gender)
        User.objects.create(**self.user_a, GenderID_id=Gender.objects.get(id=1).id)

        """create Location"""
        CountyModel.objects.create(Name="Nakuru")
        self.county_id = CountyModel.objects.get(id=1)
        TownsModel.objects.create(Name="Kabarak", County=self.county_id)
        self.town_id = TownsModel.objects.get(id=1)

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()