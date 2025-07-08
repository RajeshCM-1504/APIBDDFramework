import json
import time
from behave import *
import requests
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

@given(u'the season details to be fetched based on ID from deltatre sports platform with parameter {locale} variable')
def step_impl(context,locale):
    context.url = f"{context.base_url}/v1/{context.projectCode}/football/seasons/{context.seasonId}"
    context.params = {
        "locale": "en-US"
    }


@when(u'we execute the Get season by ID GETAPI method')
def step_impl(context):
    try:
        start_time = time.time()
        context.response = requests.get(context.url, params=context.params, timeout=5)
        elapsed_time = time.time() - start_time
        #print(context.response.url)
        assert context.response.status_code == 200, "❌ Status code is not 200"
        print("✅ Status code is 200")

        assert elapsed_time < 60, "❌ API took too long to respond"
        print("✅ API took less than a minute to respond")

    except requests.exceptions.Timeout:
        print("❌ Request timed out!")


@then(u'season details is displayed based on ID')
def step_impl(context):
    context.json_data = context.response.text
    context.json_data = json.loads(context.response.text)
    season = context.json_data.get("season", {})
    seasonId = context.json_data.get("season", {}).get("seasonId")

    if season:
        seasonId = season.get("seasonId")
        assert seasonId.startswith("cpl::Football_Season::"), f"❌ Unexpected competitionId format: {seasonId}"
        print("✅ seasonId Validation is Passed")

        startDateUtc = season.get("startDateUtc")
        assert startDateUtc is None, "❌ startDateUtc is not null"
        print("✅ startDateUtc Validation is Passed")

        endDateUtc = season.get("endDateUtc")
        assert endDateUtc is None, "❌ endDateUtc is not null"
        print("✅ endDateUtc Validation is Passed")

        seasonName = season.get("seasonName")
        assert seasonName.startswith("20"), f"❌ seasonName doesn't start with '20': {seasonName}"
        print("✅ seasonName Validation is Passed")


        competitionId = season.get("competitionId")
        assert competitionId.startswith("cpl::Football_Competition::"), f"❌ competitionId doesn't start with: {competitionId}"
        print("✅ competitionId Validation is Passed")

        providerId = season.get("providerId")
        assert providerId.startswith("opta:Season:"), f"❌ providerId doesn't start with '20': {providerId}"
        print("✅ providerId Validation is Passed")

        name = season.get("name")
        assert isinstance(name, str), f"❌ name is not a string: {type(name)}"
        print("✅ name Validation is Passed")

        officialName = season.get("officialName")
        assert isinstance(officialName, str), f"❌ officialName is not a string: {type(officialName)}"
        print("✅ officialName Validation is Passed")

        shortName = season.get("shortName")
        assert isinstance(shortName, str), f"❌ shortName is not a string: {type(shortName)}"
        print("✅ officialName Validation is Passed")

        acronymName = season.get("acronymName")
        assert isinstance(acronymName, str), f"❌ acronymName is not a string: {type(acronymName)}"
        print("✅ acronymName Validation is Passed")

    else:
        print("❌ No seasons found in the response.")

    try:
        validate(instance=context.response.json(), schema=context.seasonschema)
        print("✅ Schema validation is Passed")
    except ValidationError as e:
        print(f"❌ Schema validation failed: {e.message}")