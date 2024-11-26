from django.http import HttpRequest
from django.http import JsonResponse
from django.utils import timezone

from .utils import square_of_the_sum
from .utils import sum_of_the_squares


def difference(request: HttpRequest):
    n = request.GET.get("n")

    if not isinstance(n, int):
        JsonResponse({"error": "Input value is not an integer"}, status=400)

    n = int(n)
    if n > 100 or n < 0:
        JsonResponse(
            {"error": "Input value is not between 0 and 100"}, status=400
        )

    difference = square_of_the_sum(n) - sum_of_the_squares(n)

    response = {
        "datetime": timezone.now(),
        "value": difference,
        "number": n,
        "occurrences": 0,  # the number of times n has been requested
        "last_datetime": None,  # datetime_of_last_request
    }

    return JsonResponse(response)
