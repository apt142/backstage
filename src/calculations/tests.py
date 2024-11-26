from django.test import TestCase

from .utils import square_of_the_sum
from .utils import sum_of_the_squares


class TestSumOfSquares(TestCase):
    def test_sum_of_squares(self):
        values = [
            (1, 1),
            (2, 5),
            (3, 14),
            (10, 385),
        ]
        for pair in values:
            self.assertEqual(sum_of_the_squares(pair[0]), pair[1])


class TestSquareOfSums(TestCase):
    def test_square_of_sums(self):
        values = [
            (1, 1),
            (2, 9),
            (3, 36),
            (10, 3025),
        ]
        for pair in values:
            self.assertEqual(square_of_the_sum(pair[0]), pair[1])


class TestDifferenceView(TestCase):

    def test_happy_path(self):
        """Validate the basic happy path calculations"""
        response = self.client.get("/difference", data={"n": 10})
        content = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(content["datetime"])
        self.assertEqual(content["number"], 10)
        self.assertEqual(content["value"], 2640)
