import pytest
from django.urls import reverse
from mainapp.models import Calculation
from mainapp.serializers import SingleCalculationResultSerializer, TaskResult


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "date_start, date_fin, lag, res",
    [
        ("None", "None", "None", False),
        ("None", "string", -11, False),
        ("user@example.com", "", 0, False),
        ("12-12-2020", "12-12-2020", 400, False),
        ("2020-12-12", "2020-12-12", 50, True),
    ],
)
def test_input_data_validation(date_start, date_fin, lag, res, api_client):
    url = reverse("calculations")
    data = {"date_start": date_start, "date_fin": date_fin, "lag": lag}
    response = api_client.post(url, data=data)

    assert ("cid" in response.data.keys()) == res


def test_input_dateformat_validation(api_client):

    url = reverse("calculations")
    data = {"date_start": "12-12-2020", "date_fin": "12-12-2020", "lag": 34}
    response = api_client.post(url, data=data)

    assert ("Date has wrong format" in response.data["date_start"][0]) and (
        "Date has wrong format" in response.data["date_fin"][0]
    )


def test_input_requested_values_validation(api_client):

    url = reverse("calculations")
    data = {"date_start": "2020-12-12", "date_fin": "2020-12-12", "lag": ""}
    response = api_client.post(url, data=data)

    assert "A valid integer is required" in response.data["lag"][0]


def test_celery_task_created(api_client):

    url = reverse("calculations")

    data = {"date_start": "2020-12-12", "date_fin": "2020-12-12", "lag": 50}

    response = api_client.post(url, data=data)

    assert "cid" in response.data


def test_celery_task_request_inprogress(db, api_client):

    post_url = reverse("calculations")

    data = {"date_start": "2020-12-12", "date_fin": "2020-12-12", "lag": 50}

    response = api_client.post(post_url, data=data)
    cid = response.data["cid"]

    get_url = reverse("single_calculation", kwargs={"cid": cid})

    result = api_client.get(get_url)

    assert "Does not exist" in result.data["result"]


def test_celery_task_request(db, api_client):

    CID = "75b1a42e-562f-441d-a352-f384f4d0f504"

    test_task = Calculation.objects.create(
        cid=CID,
        task_created="2022-08-08T06:56:56.120707",
        date="{0: Timestamp('2020-12-12 00:00:00'), 1: Timestamp('2021-01-31 00:00:00'), 2: Timestamp('2021-03-22 00:00:00'), 3: Timestamp('2021-05-11 00:00:00'), 4: Timestamp('2021-06-30 00:00:00'), 5: Timestamp('2021-08-19 00:00:00'), 6: Timestamp('2021-10-08 00:00:00'), 7: Timestamp('2021-11-27 00:00:00')}",
        liquid="{0: 69.136584196136, 1: 67.00657004665307, 2: 74.15636881156234, 3: 74.09089640381751, 4: 61.383132584314964, 5: 60.45732971225061, 6: 62.30917297346143, 7: 61.64005566554937}",
        oil="{0: 59.83504760672463, 1: 53.07338934852999, 2: 47.06142647051125, 3: 40.957233693025366, 4: 32.507084307408284, 5: 27.168736944886273, 6: 21.472120956977246, 7: 14.145847434473781}",
        water="{0: 9.30153658941137, 1: 13.933180698123074, 2: 27.094942341051095, 3: 33.133662710792144, 4: 28.87604827690668, 5: 33.288592767364335, 6: 40.83705201648418, 7: 47.49420823107559}",
        wct="{0: 0.13453856156710772, 1: 0.20793753043055554, 2: 0.3653757967828988, 3: 0.44720288617111326, 4: 0.470423177527523, 5: 0.5506130179054036, 6: 0.6553939021767693, 7: 0.7705088471816567}",
    )

    task_result = TaskResult.objects.create(task_id=CID, status="SUCCEED")

    get_url = reverse("single_calculation", kwargs={"cid": CID})
    result = api_client.get(get_url)

    assert "cid" in result.data["result"]
