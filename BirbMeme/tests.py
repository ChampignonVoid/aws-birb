"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from .models import BirbMeme, BirbUser, MemeEvaluation
from .serializers import SignUpSerializer, BirbMemeSerializer
from django.test import Client
from rest_framework import status


# Models

class BirbMemeModelTest(TestCase):
    """
    Test for models.BirbMeme
    """

    def test_fields(self):
        user_id = 42
        username = 'toto'
        ref_user = BirbUser(id=user_id, username=username)

        birb_id = 24
        description = 'Yes!'

        ref_birbMeme = BirbMeme(id=birb_id, description=description,
                                creator=ref_user)
        self.assertEqual(birb_id, ref_birbMeme.id)
        self.assertEqual(description, ref_birbMeme.description)
        self.assertEqual(ref_user.id, ref_birbMeme.creator.id)
        self.assertEqual(ref_user.username, ref_birbMeme.creator.username)


class BirbUserModelTest(TestCase):
    """
    Tests for models.BirbUser
    """

    def test_fields(self):
        user_id = 5
        username = 'toto_usr'
        first_name = 'first_name_usr'
        last_name = 'whatever'
        email = 'toto@toto.fr'
        ref_user = BirbUser(id=user_id,
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            email=email)

        self.assertEqual(user_id, ref_user.id)
        self.assertEqual(username, ref_user.username)
        self.assertEqual(first_name, ref_user.first_name)
        self.assertEqual(last_name, ref_user.last_name)
        self.assertEqual(email, ref_user.email)
        self.assertFalse(ref_user.is_staff)
        self.assertTrue(ref_user.is_active)


class MemeEvaluationModelTest(TestCase):
    """
    Tests for models.BirbUser
    """

    def test_fields(self):
        first_user_id = 1
        second_user_id = 11
        first_ref_user = BirbUser(id=first_user_id)
        second_ref_user = BirbUser(id=second_user_id)

        birb_id = 2

        ref_birbMeme = BirbMeme(id=birb_id, creator=first_ref_user)

        meme_eval_id = 3
        meme_mark = 6
        meme_evaluation = MemeEvaluation(id=meme_eval_id,
                                         meme_eval=meme_mark,
                                         meme=ref_birbMeme,
                                         creator=second_ref_user)
        self.assertEqual(meme_eval_id, meme_evaluation.id)
        self.assertEqual(meme_mark, meme_evaluation.meme_eval)
        self.assertEqual(ref_birbMeme.id, meme_evaluation.meme.id)
        self.assertEqual(first_ref_user.id,
                         meme_evaluation.meme.creator.id)
        self.assertEqual(second_ref_user.id,
                         meme_evaluation.creator.id)


# Serializers

class BirbMemeSerializerTest(TestCase):
    """
    Testing birbmeme serializer
    """

    def test_nothing_valid(self):
        data = {}
        serializer = BirbMemeSerializer(data=data)
        serializer.is_valid()
        self.assertEqual(2, len(serializer.errors))
        self.assertIsNotNone(serializer.errors.get('description'))
        self.assertIsNotNone(serializer.errors.get('meme_image'))

    def test_imagefield_not_valid(self):
        data = {
            'description': 'toto'
        }
        serializer = BirbMemeSerializer(data=data)
        serializer.is_valid()
        self.assertEqual(1, len(serializer.errors))
        self.assertIsNone(serializer.errors.get('description'))
        self.assertIsNotNone(serializer.errors.get('meme_image'))


class SignUpSerializerTest(TestCase):
    """
    Testing SignUpSerializer
    """

    def test_nothing_valid(self):
        data = {}
        empty_error_msg = 'This field is required.'
        serializer = SignUpSerializer(data=data)
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        serializer.is_valid()
        self.assertEqual(5, len(serializer.errors))
        for key in fields:
            self.assertEqual(empty_error_msg, serializer.errors.get(key)[0])

    def test_email_format_not_valid(self):
        data = {
            'email': 'toto'
        }
        empty_error_msg = 'This field is required.'
        email_error_msg = 'Enter a valid email address.'
        serializer = SignUpSerializer(data=data)
        fields = [
            'username',
            'first_name',
            'last_name',
            'password'
        ]
        serializer.is_valid()
        self.assertEqual(5, len(serializer.errors))
        for key in fields:
            self.assertEqual(empty_error_msg, serializer.errors.get(key)[0])
        self.assertEqual(email_error_msg, serializer.errors.get('email')[0])


# Views

class IndexTest(TestCase):
    def test_get_status(self):
        c = Client()
        response = c.post('/api/v1/')
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)


class MemesTest(TestCase):
    def test_get_status(self):
        c = Client()
        response = c.post('/api/v1/memes')
        self.assertEqual(status.HTTP_301_MOVED_PERMANENTLY,
                         response.status_code)
