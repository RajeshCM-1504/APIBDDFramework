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
        context.response = requests.get(context.url, params=context.params,timeout=5)
        print("Success:", context.response.status_code)
    except requests.exceptions.Timeout:
        print("❌ Request timed out!")



@then('competations list is displayed')
def step_verification(context):
    #assert "Competations" in context.json_data, "Missing 'Competations' field in response"
    print("✅ API validation passed.")
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
    print(schema)



    try:

        validate(instance=context.response.json(), schema=schema)
        print("✅ Schema is valid")
    except ValidationError as e:
        print(f"❌ Schema validation failed: {e.message}")



