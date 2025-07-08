def before_all(context):
    context.base_url = "https://concacaf-api.dev.sdp.deltatre.digital"
    context.token = None
    context.config_data = {"env": "dev"}
    context.competitionId = "cpl::Football_Competition::854b8253300c4811a11094bbe0da81ee"
    context.projectCode = "cpl"
    context.teamId = "cpl::Football_Team::a92c57ab1d2041c4bfb1856a00645ace"
    context.stadiumId = "cpl::Football_Stadium::0b84d157b99d4a22abe15dc4c3a59216"
    context.seasonIds = "cpl::Football_Season::ef4074023d99497e9c973a1dc98007fb"
    context.seasonId = "cpl::Football_Season::ef4074023d99497e9c973a1dc98007fb"
    context.competationsschema = {
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

    context.competationsbyidschema = {
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

    context.competationseasonbyidschema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "seasons": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "seasonId": {
            "type": "string"
          },
          "startDateUtc": {},
          "endDateUtc": {},
          "seasonName": {
            "type": "string"
          },
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
          "seasonId",
          "startDateUtc",
          "endDateUtc",
          "seasonName",
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
    "seasons",
    "apiCallRequestTime"
  ]
}

    context.stadiumschema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "competitions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "seasonId": {
            "type": "string"
          },
          "startDateUtc": {},
          "endDateUtc": {},
          "seasonName": {
            "type": "string"
          },
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
          "seasonId",
          "startDateUtc",
          "endDateUtc",
          "seasonName",
          "competitionId",
          "providerId",
          "name",
          "officialName",
          "shortName",
          "acronymName"
        ]
      }
    },
    "stadiums": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "providerId": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "cityName": {
            "type": "string"
          },
          "country": {
            "type": "string"
          },
          "address": {
            "type": "string"
          },
          "capacity": {
            "type": "number"
          },
          "yearOfConstruction": {
            "type": "number"
          },
          "mapsGeoCodeLatitude": {},
          "mapsGeoCodeLongitude": {}
        },
        "required": [
          "id",
          "providerId",
          "name",
          "cityName",
          "country",
          "address",
          "capacity",
          "yearOfConstruction",
          "mapsGeoCodeLatitude",
          "mapsGeoCodeLongitude"
        ]
      }
    },
    "apiCallRequestTime": {
      "type": "string"
    }
  },
  "required": [
    "competitions",
    "stadiums",
    "apiCallRequestTime"
  ]
}
    context.seasonschema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "season": {
      "type": "object",
      "properties": {
        "seasonId": {
          "type": "string"
        },
        "startDateUtc": {},
        "endDateUtc": {},
        "seasonName": {
          "type": "string"
        },
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
        "seasonId",
        "startDateUtc",
        "endDateUtc",
        "seasonName",
        "competitionId",
        "providerId",
        "name",
        "officialName",
        "shortName",
        "acronymName"
      ]
    },
    "apiCallRequestTime": {
      "type": "string"
    }
  },
  "required": [
    "season",
    "apiCallRequestTime"
  ]
}