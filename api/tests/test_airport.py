import pytest
from api.controllers.airport_gap_controller import AirportGapClient


@pytest.fixture(scope="module")
def airports_api():
    return AirportGapClient()


@pytest.mark.api
def test_verify_airport_count(airports_api):
    """Scenario 1: Verify Airport Count is equal 30"""
    response = airports_api.get_airports()
    airports_api.assert_response_code(response, 200)
    assert len(response.json().get("data", [])) == 30, "Expected 30 airports"


@pytest.mark.api
def test_verify_specific_airports(airports_api):
    """Scenario 2: Verify Specific Airports"""
    required_airports = ["Akureyri Airport", "St. Anthony Airport", "CFB Bagotville"]
    airport_names = airports_api.get_airport_names()
    missing_airports = [airport for airport in required_airports if airport not in airport_names]
    assert not missing_airports, f"Missing airports: {', '.join(missing_airports)}"


@pytest.mark.api
def test_verify_distance_between_airports(airports_api):
    """Scenario 3: Проверка, что расстояние между KIX и NRT > 400 км"""
    response = airports_api.get_distance("KIX", "NRT")
    distance_km = response["data"]["attributes"]["kilometers"]
    assert distance_km > 400, f"Distance between KIX and NRT should be > 400 km, but was {distance_km} km"