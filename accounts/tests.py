from django.test import TestCase
from django.template import Template, Context
from django.shortcuts import render_to_response
from datetime import date, timedelta
from .models import User


class TestUserModel(TestCase):

    def test_user_number_stay_the_same_after_save(self):
        user1 = User.objects.create(birthday='2006-05-06')
        initial_number = user1.number
        user1.birthday = '2005-05-06'
        user1.save()
        
        self.assertEqual(initial_number, user1.number)



class TestTemplateTags(TestCase):

    def test_bizzfuzz(self):
        template_to_render = Template('{% load accounts_tags %}{% bizzfuzz number %}')
        
        def rendered(num):
            context = Context({'number': num})
            return template_to_render.render(context)
        
        self.assertEqual(rendered(30), 'BizzFuzz')
        self.assertEqual(rendered(40), 'Fuzz')
        self.assertEqual(rendered(51), 'Bizz')
        self.assertEqual(rendered(24), 'Bizz')
        self.assertEqual(rendered(17), '17')
        self.assertEqual(rendered(8), '8')

    def test_is_allowed(self):
        template_to_render = Template('{% load accounts_tags %}{% is_allowed user %}')

        user1 = User.objects.create(birthday=date(2000, 1, 1), username='1')
        user2 = User.objects.create(birthday=date(2010, 2, 15), username='2')

        today = date.today()
        test_date = date(today.year-13, today.month, 1)

        legal_date = test_date + timedelta(days=today.day-1)
        illegal_date = test_date + timedelta(days=today.day)
        print('Today: '+ str(today))
        print(test_date)
        print(legal_date)
        print(illegal_date)
        user3 = User.objects.create(birthday=legal_date, username='3')
        user4 = User.objects.create(birthday=illegal_date, username='4')

        def rendered(user):
            context = Context({'user': user})
            return template_to_render.render(context)
        
        self.assertEqual(rendered(user1), 'allowed')
        self.assertEqual(rendered(user2), 'blocked')
        self.assertEqual(rendered(user3), 'allowed')
        self.assertEqual(rendered(user4), 'blocked')


    
