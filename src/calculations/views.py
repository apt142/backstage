from datetime import datetime
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


def difference(request: HttpRequest) -> JsonResponse:
    n = request.GET.get("n")

    try:
        n = int(n)
    except ValueError:
        return JsonResponse(
            {"error": "Input value is not an integer"}, status=400
        )

    if n > 100 or n < 0:
        return JsonResponse(
            {"error": "Input value is not between 0 and 100"}, status=400
        )

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
