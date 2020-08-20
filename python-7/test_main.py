from main import get_temperature
import pytest


list_location = [
    (-14.235004, -51.92528, 62, 16),
    (64.2008, 149.4937, 55, 11)
]

list_location_fail = [
    (0, 0, 0, 0),
]

@pytest.mark.parametrize('lat, lng, temperature, expected', list_location)
def test_get_temperature_by_lat_lng(lat, lng, temperature, expected):
    result = get_temperature(lat, lng)
    assert expected == result

@pytest.mark.parametrize('lat, lng, temperature, expected', list_location_fail)
def test_get_temperature_by_lat_lng_fail(lat, lng, temperature, expected):
    result = get_temperature(lat, lng)
    assert expected != result
