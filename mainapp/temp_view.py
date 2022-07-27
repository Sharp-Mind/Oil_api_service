from ast import While
from urllib import request
from mainapp.models import Reports
from mainapp.serializers import ReportsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import queue
import asyncio
from typing import List
from time import sleep
import httpx
from django.http import HttpResponse

async def smoke(smokables: List[str] = None, flavor: str = "Sweet Baby Ray's") -> None:
    """ Smokes some meats and applies the Sweet Baby Ray's """

    if smokables is None:
        smokables = [
            "ribs",
            "brisket",
            "lemon chicken",
            "salmon",
            "bison sirloin",
            "sausage",
        ]

    if (loved_smokable := smokables[0]) == "ribs":
        loved_smokable = "meats"

    for smokable in smokables:
        print(f"Smoking some {smokable}....")
        await asyncio.sleep(1)
        print(f"Applying the {flavor}....")
        await asyncio.sleep(1)
        print(f"{smokable.capitalize()} smoked.")

    print(f"Who doesn't love smoked {loved_smokable}?")


# hello_async/views.py

async def smoke_some_meats(request) -> HttpResponse:
    loop = asyncio.get_event_loop()
    smoke_args = []

    if to_smoke := request.GET.get("to_smoke"):
        # Grab smokables
        to_smoke = to_smoke.split(",")
        smoke_args += [[smokable.lower().strip() for smokable in to_smoke]]

        # Do some string prettification
        if (smoke_list_len := len(to_smoke)) == 2:
            to_smoke = " and ".join(to_smoke)
        elif smoke_list_len > 2:
            to_smoke[-1] = f"and {to_smoke[-1]}"
            to_smoke = ", ".join(to_smoke)

    else:
        to_smoke = "meats"

    if flavor := request.GET.get("flavor"):
        smoke_args.append(flavor)

    loop.create_task(smoke(*smoke_args))

    return HttpResponse(f"Smoking some {to_smoke}....")