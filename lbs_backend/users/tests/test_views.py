from django.contrib.auth import get_user_model

from ..tests.test_setup import TestSetup

User = get_user_model()


class TestViews(TestSetup):

    def test_user_registration_with_endpoints(self):
        user = self.client.post(self.register_url, data={
            **self.user_b, 'LastName': "Kipyegon", "LocationID": self.townObj.id, "GenderID": self.genderObj.id
        })
        self.assertEqual(201, user.status_code)
        self.assertEqual(2, user.data["id"])

    def test_user_registration_with_wrong_values(self):
        user_data = {**self.user_a}
        user_data.pop("IDNumber")
        user = self.client.post(self.register_url, data=user_data)
        self.assertEqual(400, user.status_code)
