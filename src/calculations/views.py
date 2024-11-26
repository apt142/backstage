from datetime import datetime
from typing import Any
from typing import Optional

from django.http import HttpRequest
from django.http import JsonResponse
from django.utils import timezone

from calculations.models import DifferenceRequestLog
from calculations.utils import square_of_the_sum
from calculations.utils import sum_of_the_squares


def get_request_count(incoming_value: int) -> int:
    return DifferenceRequestLog.objects.filter(
        requested_number=incoming_value
    ).count()


def get_last_request(incoming_value: int) -> Optional[datetime]:
    last_request = (
        DifferenceRequestLog.objects.filter(requested_number=incoming_value)
        .order_by("-requested_at")
        .first()
    )
    if last_request:
        return last_request.requested_at

    return None


def convert_str_to_int(value: Any) -> Optional[int]:
    try:
        value = int(value)
    except ValueError:
        return None

    return value


def is_int(value: Any) -> bool:
    return isinstance(value, int)


def difference(request: HttpRequest) -> JsonResponse:
    n = convert_str_to_int(request.GET.get("n"))

    if not is_int(n):
        return JsonResponse(
            {"error": "Input value is not an integer"}, status=400
        )

    if n > 100 or n < 0:
        return JsonResponse(
            {"error": "Input value is not between 0 and 100"}, status=400
        )

    # Design decision: Since this is just math. It is likely faster to just
    # do the math than paying the round trip cost to access cache or
    # the database.
    # If it was more complicated but still deterministic calculation, I'd be
    # tempted to use the DB as a look up/cache.
    difference = square_of_the_sum(n) - sum_of_the_squares(n)

    response = {
        "datetime": timezone.now(),
        "value": difference,
        "number": n,
        "occurrences": get_request_count(n),
        "last_datetime": get_last_request(n),
    }

    DifferenceRequestLog.objects.create(
        requested_number=n,
        calculated_value=difference,
        requested_at=timezone.now(),
    )

    return JsonResponse(response)


def pythagorean(request: HttpRequest) -> JsonResponse:
    a = convert_str_to_int(request.GET.get("a"))
    b = convert_str_to_int(request.GET.get("b"))
    c = convert_str_to_int(request.GET.get("c"))

    if not is_int(a) or not is_int(b) or not is_int(c):
        return JsonResponse(
            {"error": "One or more input values are not an integer"},
            status=400,
        )

    response = {
        "datetime": timezone.now(),
        "is_pythagorean_triplet": True,
        "a": a,
        "b": b,
        "c": c,
        "product": a * b * c,
    }

    return JsonResponse(response)
