from django.test import TestCase


class TestUserModel(TestCase):

    def test_different_number_for_different_users(self):

        user1 = User.objects.create()
        user2 = User.objects.create()
    
