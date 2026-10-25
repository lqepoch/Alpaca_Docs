---
updatedAt: 2026-10-01T16:01:01.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Create a Signed Agreement

Create a signed agreement for a party.

Use this endpoint to record party-level agreements after party creation (for example
`certifications_and_resolutions_statement` when it was not included on `POST /v1/parties`),
or to record per-account agreements that require an `account_id`.
Party-level agreements cannot be added via `PATCH /v1/parties/{id}` — use this endpoint instead.

See [Business Trading Accounts — Party-Level Agreements](https://docs.alpaca.markets/us/docs/business-trading-accounts#party-level-agreements)
for the party-first onboarding flow.


# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "CreateAccountAgreementRequest": {
        "additionalProperties": false,
        "description": "Request to create a per-account agreement. Per-account agreements are tied to a\nspecific trading account and require an `account_id`.\n",
        "properties": {
          "account_id": {
            "description": "The account associated with this agreement. Required for per-account agreements.",
            "example": "d7e8f9a0-b1c2-3d4e-5f67-890123456789",
            "format": "uuid",
            "type": "string"
          },
          "agreement": {
            "$ref": "#/components/schemas/PerAccountAgreementType"
          },
          "ip_address": {
            "description": "The IP address from which the agreement was signed",
            "example": "192.168.1.100",
            "type": "string"
          },
          "party_id": {
            "description": "The party signing the agreement",
            "example": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
            "format": "uuid",
            "type": "string"
          },
          "revision": {
            "description": "Optional agreement revision in format `XX.YYYY.MM`.\nIf omitted, the active revision from the agreements reference table is used.\n",
            "example": "19.2024.01",
            "type": "string"
          },
          "signed_at": {
            "description": "The timestamp when the agreement was signed",
            "example": "2024-01-15T11:00:00Z",
            "format": "date-time",
            "type": "string"
          },
          "signer_party_id": {
            "description": "Required for legal entity parties. Must reference a natural person party\nthat is an authorized signer of the legal entity.\n",
            "example": "550e8400-e29b-41d4-a716-446655440003",
            "format": "uuid",
            "type": "string"
          }
        },
        "required": [
          "party_id",
          "agreement",
          "signed_at",
          "ip_address",
          "account_id"
        ],
        "title": "CreateAccountAgreementRequest",
        "type": "object"
      },
      "CreateAgreementRequest": {
        "description": "Request to create a signed agreement for a party.\n\nThis is a sum type with two variants:\n- `CreatePartyAgreementRequest`: for per-party agreements (no `account_id`)\n- `CreateAccountAgreementRequest`: for per-account agreements (`account_id` required)\n\nThe correct variant is determined by the agreement type and presence of `account_id`.\n",
        "oneOf": [
          {
            "$ref": "#/components/schemas/CreatePartyAgreementRequest"
          },
          {
            "$ref": "#/components/schemas/CreateAccountAgreementRequest"
          }
        ],
        "title": "CreateAgreementRequest"
      },
      "CreatePartyAgreementRequest": {
        "additionalProperties": false,
        "description": "Request to create a per-party agreement. Per-party agreements are signed at the\nparty level and do not require an `account_id`. The `account_id` field is not allowed.\n",
        "properties": {
          "agreement": {
            "$ref": "#/components/schemas/PartyAgreementType"
          },
          "ip_address": {
            "description": "The IP address from which the agreement was signed",
            "example": "10.0.0.50",
            "type": "string"
          },
          "party_id": {
            "description": "The party signing the agreement",
            "example": "e4d3c2b1-a098-7654-3210-fedcba987654",
            "format": "uuid",
            "type": "string"
          },
          "revision": {
            "description": "Optional agreement revision in format `XX.YYYY.MM`.\nIf omitted, the active revision from the agreements reference table is used.\nNot supported for `nasdaq_agreement`, `nyse_agreement`, or `oauth_api_agreement`;\nsending `revision` for these types returns `400`, and the response omits it.\n",
            "example": "01.2024.02",
            "type": "string"
          },
          "signed_at": {
            "description": "The timestamp when the agreement was signed",
            "example": "2024-08-18T14:00:00Z",
            "format": "date-time",
            "type": "string"
          },
          "signer_party_id": {
            "description": "Required for legal entity parties. Must reference a natural person party\nthat is an authorized signer of the legal entity.\n",
            "example": "b5c7e1a2-3d4f-4e5a-8b6c-9d0e1f2a3b4c",
            "format": "uuid",
            "type": "string"
          }
        },
        "required": [
          "party_id",
          "agreement",
          "signed_at",
          "ip_address"
        ],
        "title": "CreatePartyAgreementRequest",
        "type": "object"
      },
      "PartyAgreementType": {
        "description": "Per-party agreement types. These agreements are signed at the party level\nand do not require an `account_id`.\n",
        "enum": [
          "margin_agreement",
          "certifications_and_resolutions_statement",
          "nasdaq_agreement",
          "nyse_agreement",
          "oauth_api_agreement",
          "opra_agreement",
          "trusted_contact_consent",
          "custodian_customer_agreement"
        ],
        "example": "certifications_and_resolutions_statement",
        "title": "PartyAgreementType",
        "type": "string"
      },
      "PartyErrorResponse": {
        "additionalProperties": false,
        "description": "Error response returned by party, agreement, document, and verification endpoints.",
        "properties": {
          "error": {
            "description": "Machine-readable error code",
            "enum": [
              "invalid_request",
              "not_found",
              "unauthorized",
              "forbidden",
              "internal_error",
              "party_not_found",
              "invalid_party_id",
              "email_in_use",
              "rate_limited"
            ],
            "example": "invalid_request",
            "type": "string"
          },
          "error_description": {
            "description": "Human-readable error description",
            "example": "Validation failed",
            "type": "string"
          },
          "fields": {
            "description": "List of invalid request fields, if any",
            "example": [
              {
                "error": "must be an authorized signer of the party",
                "name": "signer_party_id"
              }
            ],
            "items": {
              "properties": {
                "error": {
                  "description": "Error message associated with the field",
                  "example": "must be an authorized signer of the party",
                  "type": "string"
                },
                "name": {
                  "description": "Name of the invalid request field",
                  "example": "signer_party_id",
                  "type": "string"
                }
              },
              "required": [
                "name"
              ],
              "type": "object"
            },
            "type": "array"
          }
        },
        "required": [
          "error"
        ],
        "title": "PartyErrorResponse",
        "type": "object"
      },
      "PerAccountAgreementType": {
        "description": "Per-account agreement types. These agreements are tied to a specific trading\naccount and require an `account_id`.\n",
        "enum": [
          "account_agreement",
          "customer_agreement",
          "options_agreement",
          "master_securities_lending_agreement",
          "crypto_agreement",
          "dvp_customer_agreement",
          "etc_agreement",
          "joint_account_agreement"
        ],
        "example": "customer_agreement",
        "title": "PerAccountAgreementType",
        "type": "string"
      },
      "SignedAgreement": {
        "additionalProperties": false,
        "description": "A signed agreement between a party and Alpaca, as returned by\n`POST /v1/agreements`. Includes both per-party and per-account agreements.\n",
        "properties": {
          "account_id": {
            "description": "The account associated with this agreement. Present for per-account agreements\nsuch as `customer_agreement`, `account_agreement`, `options_agreement`,\n`master_securities_lending_agreement`, `crypto_agreement`,\n`dvp_customer_agreement`, `etc_agreement`, and `joint_account_agreement`.\n",
            "example": "d7e8f9a0-b1c2-3d4e-5f67-890123456789",
            "format": "uuid",
            "type": "string"
          },
          "agreement": {
            "$ref": "#/components/schemas/SignedAgreementType"
          },
          "ip_address": {
            "description": "The IP address from which the agreement was signed",
            "example": "10.0.0.50",
            "type": "string"
          },
          "party_id": {
            "description": "The party that signed the agreement",
            "example": "e4d3c2b1-a098-7654-3210-fedcba987654",
            "format": "uuid",
            "type": "string"
          },
          "revision": {
            "description": "The agreement revision. The format is `XX.YYYY.MM` where XX is an incrementing\nrevision number, YYYY is the year and MM is the month. If the revision is not\nspecified in the request, the active revision will be used, which will align\nwith the [Alpaca Documents Library](https://alpaca.markets/disclosures).\nOmitted for agreement types that do not support revisions\n(`nasdaq_agreement`, `nyse_agreement`, `oauth_api_agreement`).\n",
            "example": "01.2024.02",
            "type": "string"
          },
          "signed_at": {
            "description": "The timestamp when the agreement was signed",
            "example": "2024-08-18T14:00:00Z",
            "format": "date-time",
            "type": "string"
          },
          "signer_party_id": {
            "description": "The party ID of the authorized signer who signed on behalf of a legal entity.\nRequired for legal entity parties.\n",
            "example": "b5c7e1a2-3d4f-4e5a-8b6c-9d0e1f2a3b4c",
            "format": "uuid",
            "type": "string"
          }
        },
        "required": [
          "party_id",
          "agreement",
          "signed_at",
          "ip_address"
        ],
        "title": "SignedAgreement",
        "type": "object"
      },
      "SignedAgreementType": {
        "description": "The type of agreement that was signed. Union of per-party and per-account\nagreement types returned by `POST /v1/agreements`.\n\nPer-party agreements (no `account_id`):\n- margin_agreement\n- certifications_and_resolutions_statement (legal entities only)\n- nasdaq_agreement\n- nyse_agreement\n- oauth_api_agreement\n- opra_agreement\n- trusted_contact_consent\n- custodian_customer_agreement\n\nPer-account agreements (`account_id` present):\n- account_agreement\n- customer_agreement\n- options_agreement\n- master_securities_lending_agreement\n- crypto_agreement\n- dvp_customer_agreement\n- etc_agreement\n- joint_account_agreement\n",
        "enum": [
          "margin_agreement",
          "certifications_and_resolutions_statement",
          "nasdaq_agreement",
          "nyse_agreement",
          "oauth_api_agreement",
          "opra_agreement",
          "trusted_contact_consent",
          "custodian_customer_agreement",
          "account_agreement",
          "customer_agreement",
          "options_agreement",
          "master_securities_lending_agreement",
          "crypto_agreement",
          "dvp_customer_agreement",
          "etc_agreement",
          "joint_account_agreement"
        ],
        "example": "certifications_and_resolutions_statement",
        "title": "SignedAgreementType",
        "type": "string"
      }
    },
    "securitySchemes": {
      "BasicAuth": {
        "scheme": "basic",
        "type": "http"
      }
    }
  },
  "info": {
    "contact": {
      "email": "support@alpaca.markets",
      "name": "Alpaca Support",
      "url": "https://alpaca.markets/support"
    },
    "description": "Open brokerage accounts, enable stock, options and crypto trading. Manage the ongoing user experience and brokerage customer lifecycle with the Alpaca Broker API",
    "termsOfService": "https://s3.amazonaws.com/files.alpaca.markets/disclosures/library/TermsAndConditions.pdf",
    "title": "Broker API",
    "version": "1.1.1"
  },
  "openapi": "3.1.2",
  "paths": {
    "/v1/agreements": {
      "post": {
        "description": "Create a signed agreement for a party.\n\nUse this endpoint to record party-level agreements after party creation (for example\n`certifications_and_resolutions_statement` when it was not included on `POST /v1/parties`),\nor to record per-account agreements that require an `account_id`.\nParty-level agreements cannot be added via `PATCH /v1/parties/{id}` — use this endpoint instead.\n\nSee [Business Trading Accounts — Party-Level Agreements](https://docs.alpaca.markets/us/docs/business-trading-accounts#party-level-agreements)\nfor the party-first onboarding flow.\n",
        "operationId": "createAgreement",
        "requestBody": {
          "content": {
            "application/json": {
              "examples": {
                "perAccountLegalEntity": {
                  "summary": "Per-account agreement for a legal entity",
                  "value": {
                    "account_id": "d7e8f9a0-b1c2-3d4e-5f67-890123456789",
                    "agreement": "options_agreement",
                    "ip_address": "10.0.0.50",
                    "party_id": "550e8400-e29b-41d4-a716-446655440000",
                    "signed_at": "2024-08-18T14:05:00Z",
                    "signer_party_id": "550e8400-e29b-41d4-a716-446655440003"
                  }
                },
                "perAccountNaturalPerson": {
                  "summary": "Per-account agreement for a natural person",
                  "value": {
                    "account_id": "d7e8f9a0-b1c2-3d4e-5f67-890123456789",
                    "agreement": "customer_agreement",
                    "ip_address": "192.168.1.100",
                    "party_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                    "signed_at": "2024-01-15T11:00:00Z"
                  }
                },
                "perPartyLegalEntity": {
                  "summary": "Certifications and resolutions for a legal entity",
                  "value": {
                    "agreement": "certifications_and_resolutions_statement",
                    "ip_address": "10.0.0.50",
                    "party_id": "e4d3c2b1-a098-7654-3210-fedcba987654",
                    "signed_at": "2024-08-18T14:00:00Z",
                    "signer_party_id": "b5c7e1a2-3d4f-4e5a-8b6c-9d0e1f2a3b4c"
                  }
                },
                "perPartyNaturalPerson": {
                  "summary": "Per-party agreement for a natural person",
                  "value": {
                    "agreement": "margin_agreement",
                    "ip_address": "192.168.1.100",
                    "party_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                    "revision": "19.2024.01",
                    "signed_at": "2024-01-15T10:30:00Z"
                  }
                }
              },
              "schema": {
                "$ref": "#/components/schemas/CreateAgreementRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "examples": {
                  "perAccountNaturalPerson": {
                    "summary": "Per-account agreement created",
                    "value": {
                      "account_id": "d7e8f9a0-b1c2-3d4e-5f67-890123456789",
                      "agreement": "customer_agreement",
                      "ip_address": "192.168.1.100",
                      "party_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                      "revision": "19.2024.01",
                      "signed_at": "2024-01-15T11:00:00Z"
                    }
                  },
                  "perPartyLegalEntity": {
                    "summary": "Certifications and resolutions created",
                    "value": {
                      "agreement": "certifications_and_resolutions_statement",
                      "ip_address": "10.0.0.50",
                      "party_id": "e4d3c2b1-a098-7654-3210-fedcba987654",
                      "revision": "01.2024.02",
                      "signed_at": "2024-08-18T14:00:00Z",
                      "signer_party_id": "b5c7e1a2-3d4f-4e5a-8b6c-9d0e1f2a3b4c"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/SignedAgreement"
                }
              }
            },
            "description": "Agreement created successfully"
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "invalidRequest": {
                    "summary": "Validation failed",
                    "value": {
                      "error": "invalid_request",
                      "error_description": "Validation failed",
                      "fields": [
                        {
                          "name": "signer_party_id"
                        }
                      ]
                    }
                  },
                  "partyNotFound": {
                    "summary": "Party not found",
                    "value": {
                      "error": "party_not_found",
                      "error_description": "Party not found"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/PartyErrorResponse"
                }
              }
            },
            "description": "Invalid request. Common causes include an unknown party_id (party_not_found),\nmissing required fields (including `party_id`), an invalid agreement type for\nthe party, a missing `account_id` for a per-account agreement, or an invalid\n`signer_party_id` for a legal entity.\n"
          },
          "403": {
            "content": {
              "application/json": {
                "examples": {
                  "forbidden": {
                    "summary": "Party belongs to another correspondent",
                    "value": {
                      "error": "forbidden",
                      "error_description": "Access to party is forbidden"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/PartyErrorResponse"
                }
              }
            },
            "description": "The party does not belong to the authenticated correspondent."
          }
        },
        "summary": "Create a Signed Agreement",
        "tags": [
          "Agreements"
        ]
      }
    }
  },
  "security": [
    {
      "BasicAuth": []
    }
  ],
  "servers": [
    {
      "description": "Sandbox endpoint",
      "url": "https://broker-api.sandbox.alpaca.markets"
    },
    {
      "description": "Production endpoint",
      "url": "https://broker-api.alpaca.markets"
    }
  ],
  "tags": [
    {
      "name": "Agreements"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false
  }
}
```