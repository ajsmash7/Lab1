import Question4

from unittest import TestCase


class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', Question4.camel_case('Hello World'))
        self.assertEqual('', Question4.camel_case(''))
        self.assertEqual('helloWorld', Question4.camel_case('        Hello          World        '))
        self.assertEqual(' 😂 🤣 😃 😄 😅 😆 😉 😊 😋 😎 😍 😘', Question4.camel_case( '😂 🤣 😃 😄 😅 😆 😉 😊 😋 😎 😍 😘'))

