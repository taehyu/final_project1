from django.contrib.auth.models import User
from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make('auth.User', _quantity=3)

    def test_should_list(self):
        self.client.force_authenticate(user=self.users[0])
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_create(self):
        self.client.force_authenticate(user=self.users[0])
        data = {
            'username': 'brooks',
            'password': 'password'
        }
        response = self.client.post('/api/users', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get('id'))
        self.assertEqual(response.data.get('username'), data['username'])

    def test_should_get(self):
        self.client.force_authenticate(user=self.users[0])
        response = self.client.get(f'/api/users/{self.users[0].pk}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.users[0].username, response.data.get('username'))

    def test_should_update(self):
        data = {
            "username": 'newname',
            "password": "password"
        }
        self.client.force_authenticate(user=self.users[0])
        response = self.client.patch(f'/api/users/{self.users[0].pk}', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(self.users[0].username, response.data.get('username'))

    def test_should_delete(self):
        self.client.force_authenticate(user=self.users[0])
        response = self.client.delete(f'/api/users/{self.users[0].pk}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(pk=self.users[0].id).count(), 0)

    def test_login(self):
        self.testUser = User(
            username='testTokenUser',
            email='testTokenUser@naver.com',
            password='1111'
        )
        self.testUser.set_password(self.testUser.password)
        self.testUser.save()
        data = {
            'username': 'testTokenUser',
            'email': 'testTokenUser@naver.com',
            'password': '1111'
        }
        response = self.client.post('/api/users/login', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logout(self):
        testUser = User(username='logoutUser', password='1111')
        testUser.save()
        token = Token.objects.create(user=testUser)
        token.save()
        response = self.client.delete(f'/api/users/{testUser.pk}/logout', HTTP_AUTHORIZATION='Token '+token.key)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Token.objects.filter(user=testUser).count(), 0)
        self.assertIsNone(Token.objects.filter(user=testUser).first())