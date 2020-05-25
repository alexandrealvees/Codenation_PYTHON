from main import get_temperature
from unittest.mock import patch
import pytest

temperature_lat_lng_expected = [
    (62, -14.235004, -51.92528, 16),
    (32, 50.652544, 32.852458, 0),
    (50, -10.856584, 25.548, 10)
]


@pytest.mark.parametrize("temperature,lat,lng,expected", temperature_lat_lng_expected)
def test_get_temperature_by_lat_lng(temperature, lat, lng, expected):

    mock_get_patcher = patch('main.requests.get')

    temperature = {
        "currently": {
            "temperature": temperature,
        }
    }

    mock_get = mock_get_patcher.start()

    mock_get.return_value.json.return_value = temperature

    response = get_temperature(lat, lng)

    mock_get_patcher.stop()

    print(response)

    assert response == expected
