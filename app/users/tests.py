from django.test import TestCase
from django.contrib.auth import get_user_model
# TDD : Test Driven Development(테스트 주도 개발)
class UserTestCase(TestCase):

    # 일반 유저 생성 테스트 함수
    def test_create_user(self):
        email = 'wns201908@gmail.com'
        password = 'park1256!'

        user = get_user_model().objects.create_user(email=email, password=password)

        # 유저가 생성 되었는지 확인
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)


    # 슈퍼 유저 생성 테스트 함수
    def test_create_superuser(self):
        email = 'wns201908@gmail.com'
        password = 'park1256!'

        user = get_user_model().objects.create_superuser(email=email, password=password)

        # 슈퍼 유저
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)