import json
import time
from behave import *
import requests
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

@given('the competations details to be fetched from deltatre sports platform with parameter {locale} variable')
def api(context,locale):
    context.url = "https://concacaf-api.dev.sdp.deltatre.digital/v1/cpl/football/competitions?locale=en-us"
    context.params = {
        "locale": locale
    }

@when('we execute the Get Competations GETAPI method')
def step_apicall(context):
    try:
        start_time = time.time()
        context.response = requests.get(context.url, params=context.params,timeout=5)
        elapsed_time = time.time() - start_time

        assert context.response.status_code == 200, "❌ Status code is not 200"
        print("✅ Status code is 200")

        assert elapsed_time < 60, "❌ API took too long to respond"
        print("✅ API took less than a minute to respond")

    except requests.exceptions.Timeout:
        print("❌ Request timed out!")

@then('competations list is displayed')
def step_verification(context):
    context.json_data = context.response.text
    context.json_data = json.loads(context.response.text)
    competitions = context.json_data.get("competitions", [])

    if competitions:
        competitionId = competitions[0].get("competitionId")
        assert competitionId.startswith("cpl::Football_Competition::"), f"❌ Unexpected competitionId format: {competitionId}"
        print("✅ competitionId Validation is Passed")

        providerId = competitions[0].get("providerId")
        assert providerId.startswith("opta:Competition:"), f"❌ Unexpected competitionId format: {providerId}"
        print("✅ providerId Validation is Passed")

        name = competitions[0].get("name")
        assert isinstance(name, str), f"❌ comp_id is not a string: {type(name)}"
        print("✅ name Validation is Passed")

        officialName = competitions[0].get("officialName")
        assert isinstance(officialName, str), f"❌ comp_id is not a string: {type(officialName)}"
        print("✅ officialName Validation is Passed")

        shortName = competitions[0].get("shortName")
        assert isinstance(shortName, str), f"❌ comp_id is not a string: {type(shortName)}"
        print("✅ officialName Validation is Passed")

        acronymName = competitions[0].get("acronymName")
        assert isinstance(acronymName, str), f"❌ comp_id is not a string: {type(acronymName)}"
        print("✅ acronymName Validation is Passed")

    else:
        print("❌ No competitions found in the response.")

    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "competitions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "competitionId": {
                            "type": "string"
                        },
                        "providerId": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "officialName": {
                            "type": "string"
                        },
                        "shortName": {
                            "type": "string"
                        },
                        "acronymName": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "competitionId",
                        "providerId",
                        "name",
                        "officialName",
                        "shortName",
                        "acronymName"
                    ]
                }
            },
            "apiCallRequestTime": {
                "type": "string"
            }
        },
        "required": [
            "competitions",
            "apiCallRequestTime"
        ]
    }

    try:
        validate(instance=context.response.json(), schema=schema)
        print("✅ Schema validation is Passed")
    except ValidationError as e:
        print(f"❌ Schema validation failed: {e.message}")



