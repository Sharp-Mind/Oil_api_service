from time import sleep
import pytest
from django.urls import reverse


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()


@pytest.mark.django_db
@pytest.mark.parametrize(
   'date_start, date_fin, lag, res', [
       ('None', 'None', 'None', False),
       ('None', 'string', -11, False),
       ('user@example.com', '', 0, False),
       ('12-12-2020', '12-12-2020', 400, False),
       ("2020-12-12", "2020-12-12", 50, True),
   ]
)

def test_input_data_validation(
    date_start, date_fin, lag, res, api_client
    ):      
        url = reverse('calculations')
        data = {
            'date_start': date_start,
            'date_fin': date_fin,
            'lag': lag
        }
        response = api_client.post(url, data=data)
        
        assert ('cid' in response.data.keys()) == res


def test_input_dateformat_validation(api_client):     

        url = reverse('calculations')
        data = {
            'date_start': '12-12-2020',
            'date_fin': '12-12-2020',
            'lag': 34
        }
        response = api_client.post(url, data=data)
        
        assert (('Date has wrong format' in response.data['date_start'][0]) == True) and (('Date has wrong format' in response.data['date_fin'][0]) == True)

def test_input_requested_values_validation(api_client):     

        url = reverse('calculations')
        data = {
            'date_start': '2020-12-12',
            'date_fin': '2020-12-12',
            'lag': ''
        }
        response = api_client.post(url, data=data)
        
        assert ('A valid integer is required' in response.data['lag'][0]) == True

@pytest.mark.django_db
def test_task_start(api_client):  

        task_creation_url = reverse('calculations')        

        data = {
            'date_start': '2020-12-12',
            'date_fin': '2020-12-12',
            'lag': 35
        }
        cid = api_client.post(task_creation_url, data=data).data['cid']

        task_request_url = reverse('single_calculation', kwargs={'cid': cid})

        sleep(11)     

        result = api_client.get(task_request_url)
        
        assert 'cid' in result.data.keys()
