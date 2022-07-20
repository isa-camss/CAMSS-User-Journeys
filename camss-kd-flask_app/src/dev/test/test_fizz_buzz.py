# -*- coding: utf-8 -*-
import unittest
from config import constants_test, messages
from com.nttdata.dgi.fizz_buzz.fizz_buzz import FizzBuzz


class TestDownloader(unittest.TestCase):

    def test_divisible_by_3(self):
        """
        Given a number,
        When it is divisible by 3,
        Then the system returns FIZZ".
        """
        expected_result = constants_test.TEST_RETURNS_FIZZ
        fizz_buzz = FizzBuzz()
        number = constants_test.TEST_DIVISIBLE_BY_3
        result, message, response = fizz_buzz.convert_number(number)
        print(dict)
        self.assertEqual(expected_result, result)

    def test_divisible_by_5(self):
        """
        Given a number,
        When it is divisible by 5,
        Then the system returns BUZZ".
        """
        expected_result = constants_test.TEST_RETURNS_BUZZ
        fizz_buzz = FizzBuzz()
        number = constants_test.TEST_DIVISIBLE_BY_5
        result, message, response = fizz_buzz.convert_number(number)
        self.assertEqual(expected_result, result)

    def test_divisible_by_3_and_5(self):
        """
        Given a number,
        When it is divisible by 3 and 5,
        Then the system returns FIZZBUZZ".
        """
        expected_result = constants_test.TEST_RETURNS_FIZZ_BUZZ
        fizz_buzz = FizzBuzz()
        number = constants_test.TEST_DIVISIBLE_BY_3_5
        result, message, response = fizz_buzz.convert_number(number)
        self.assertEqual(expected_result, result)

    def test_not_divisible_by_3_and_5(self):
        """
        Given a number,
        When it is not divisible by 3 and 5,
        Then the system returns an KO message 'The number provided is not divisible by 3 or 5'".
        """
        expected_result = messages.MESSAGE_KO_NO_DIVISIBLE
        fizz_buzz = FizzBuzz()
        number = constants_test.TEST_NOT_DIVISIBLE_BY_3
        with self.assertRaises(Exception) as context:
            result, message, response = fizz_buzz.convert_number(number)
        self.assertTrue(expected_result in str(context.exception))
