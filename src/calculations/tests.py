from django.test import TestCase

from calculations.utils import square_of_the_sum
from calculations.utils import sum_of_the_squares
from calculations.views import get_request_count


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
        requested_number = 10

        response = self.client.get("/difference", data={"n": requested_number})
        content = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(content["datetime"])
        self.assertEqual(content["number"], requested_number)
        self.assertEqual(content["occurrences"], 0)
        self.assertIsNone(content["last_datetime"])
        self.assertEqual(content["value"], 2640)

        # Confirm new log was added
        self.assertEqual(get_request_count(requested_number), 1)

        # Run again to see the occurrence count increase
        response = self.client.get("/difference", data={"n": requested_number})
        content = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(content["datetime"])
        self.assertEqual(content["number"], requested_number)
        self.assertEqual(content["occurrences"], 1)
        self.assertIsNotNone(content["last_datetime"])
        self.assertEqual(content["value"], 2640)

    def test_invalid_string(self):
        response = self.client.get("/difference", data={"n": "Ten"})
        content = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(content["error"], "Input value is not an integer")

    def test_value_too_small(self):
        response = self.client.get("/difference", data={"n": -1})
        content = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            content["error"], "Input value is not between 0 and 100"
        )

    def test_value_too_large(self):
        response = self.client.get("/difference", data={"n": 1000})
        content = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            content["error"], "Input value is not between 0 and 100"
        )
