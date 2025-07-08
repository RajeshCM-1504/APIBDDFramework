import json
import time
from behave import *
import requests
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

@given(u'the stadium details to be fetched from deltatre sports platform with the team ID is {teamId} And the stadium ID is {stadiumId} And the season IDs are {seasonIds} And the locale is {locale}')
def step_impl(context,teamId,stadiumId,seasonIds,locale):
    context.url = f"{context.base_url}/v1/{context.projectCode}/football/seasons/{context.seasonIds}/stadiums?teamId=cpl::Football_Team::a92c57ab1d2041c4bfb1856a00645ace&stadiumId=cpl::Football_Stadium::0b84d157b99d4a22abe15dc4c3a59216&seasonIds=cpl::Football_Season::ef4074023d99497e9c973a1dc98007fb,&locale=en-us"
    context.params = {
        "teamId": teamId,
        "stadiumId": stadiumId,
        "seasonIds": seasonIds,
        "locale": locale


    }

@when(u'we execute the Get stadiums GETAPI method')
def step_impl(context):
    try:
        start_time = time.time()
        context.response = requests.get(context.url, params=context.params, timeout=5)
        elapsed_time = time.time() - start_time

        assert context.response.status_code == 200, "❌ Status code is not 200"
        print("✅ Status code is 200")

        assert elapsed_time < 60, "❌ API took too long to respond"
        print("✅ API took less than a minute to respond")

    except requests.exceptions.Timeout:
        print("❌ Request timed out!")


@then(u'stadium information is displayed')
def step_impl(context):
    context.json_data = context.response.text
    #print(context.json_data)
    context.json_data = json.loads(context.response.text)
    stadiums = context.json_data.get("stadiums", [])

    if stadiums:
        id = stadiums[0].get("id")
        assert id.startswith("cpl::Football_Stadium::"), f"❌ Unexpected competitionId format: {id}"
        print("✅ StadiumId Validation is Passed")

        providerId = stadiums[0].get("providerId")
        assert providerId.startswith("opta:Stadium:"), f"❌ providerId doesn't start with '20': {providerId}"
        print("✅ stadiums providerId Validation is Passed")

        name = stadiums[0].get("name")
        assert isinstance(name, str), f"❌ name is not a string: {type(name)}"
        print("✅ stadiums name Validation is Passed")

        cityName = stadiums[0].get("cityName")
        assert isinstance(cityName, str), f"❌ cityName is not a string: {type(cityName)}"
        print("✅ stadium cityName Validation is Passed")

        country = stadiums[0].get("country")
        assert isinstance(country, str), f"❌ country is not a string: {type(country)}"
        print("✅ stadium country Validation is Passed")

        address = stadiums[0].get("address")
        assert isinstance(address, str), f"❌ address is not a string: {type(address)}"
        print("✅ stadium address Validation is Passed")

        capacity = stadiums[0].get("capacity")
        assert isinstance(capacity, int) and capacity > 0, f"❌ Invalid capacity: {capacity}"
        print("✅ stadium capacity Validation is Passed")

        yearOfConstruction = stadiums[0].get("yearOfConstruction")
        assert isinstance(yearOfConstruction, int) and 1800 <= yearOfConstruction <= 2025, f"❌ Invalid yearOfConstruction: {yearOfConstruction}"
        print("✅ stadium capacity Validation is Passed")

        mapsGeoCodeLatitude = stadiums[0].get("mapsGeoCodeLatitude")
        assert mapsGeoCodeLatitude is None, f"❌ mapsGeoCodeLatitude should be null, got: {mapsGeoCodeLatitude}"
        print("✅ stadium mapsGeoCodeLatitude Validation is Passed")

        mapsGeoCodeLongitude = stadiums[0].get("mapsGeoCodeLongitude")
        assert mapsGeoCodeLongitude is None, f"❌ mapsGeoCodeLongitude should be null, got: {mapsGeoCodeLongitude}"
        print("✅ stadium mapsGeoCodeLongitude Validation is Passed")

    else:
        print("❌ No seasons found in the response.")

    try:
        validate(instance=context.response.json(), schema=context.stadiumschema)
        print("✅ Schema validation is Passed")
    except ValidationError as e:
        print(f"❌ Schema validation failed: {e.message}")



