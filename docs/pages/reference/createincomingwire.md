---
updatedAt: 2026-11-09T17:57:00.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Simulate an Incoming Wire Transfer

Simulate an incoming wire transfer to fund one of your accounts, without a real sending bank.

This endpoint is **only available in the sandbox environment**. Calling it in production returns `403`. In production, incoming wires are sent by the customer's bank and cannot be created through the API.

Identify the destination account by including an FFC (For Further Credit) string `FFC <correspondent>-<account_number>` in `wire_instructions`, where `<correspondent>` is your 4-character correspondent code and `<account_number>` is the account's 9-character account number.

`currency` defaults to `USD` and must match the account's base currency. Supported currencies are `AUD`, `CAD`, `CHF`, `EUR`, `GBP`, `JPY`, `NZD`, `SGD`, `TRY`, and `USD`.

The wire is created with status `QUEUED` and processed asynchronously on the next worker run.

# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "CreateSimulatedIncomingWireRequest": {
        "description": "Request body for simulating an incoming wire transfer in the sandbox environment.\n\n`currency` defaults to `USD` when omitted and must match the base currency of the destination account. Supported currencies are `AUD`, `CAD`, `CHF`, `EUR`, `GBP`, `JPY`, `NZD`, `SGD`, `TRY`, and `USD`. Other currencies are rejected with `422`.",
        "properties": {
          "amount": {
            "description": "Amount of the incoming wire. Must be greater than 0.",
            "example": "1000.00",
            "format": "decimal",
            "type": "string"
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "delay_until": {
            "description": "Accepted and returned in the response, but not currently used. The wire is processed on the next worker run regardless of this value.",
            "example": "2026-11-10T14:00:00Z",
            "format": "date-time",
            "type": [
              "string",
              "null"
            ]
          },
          "wire_instructions": {
            "description": "Must contain an FFC (For Further Credit) string identifying the destination account, in the form `FFC <correspondent>-<account_number>`. The hyphen can also be a space or omitted. Text before or after the FFC string is ignored.\n\n`<correspondent>` must be your 4-character correspondent code, and `<account_number>` must be the 9-character account number of one of your accounts. Only the first 9 characters after the correspondent code are read as the account number.",
            "example": "FFC TEST-123456789",
            "pattern": "FFC [0-9A-Za-z]{4}[-\\s]?[0-9A-Za-z]{9}",
            "type": "string"
          }
        },
        "required": [
          "amount",
          "wire_instructions"
        ],
        "title": "CreateSimulatedIncomingWireRequest",
        "type": "object"
      },
      "Currency": {
        "description": "\"USD\" // US Dollar\n\"JPY\" // Japanese Yen\n\"EUR\" // Euro\n\"CAD\" // Canadian Dollar\n\"GBP\" // British Pound Sterling\n\"CHF\" // Swiss Franc\n\"TRY\" // Turkish Lira\n\"AUD\" // Australian Dollar\n\"CZK\" // Czech Koruna\n\"SEK\" // Swedish Krona\n\"DKK\" // Danish Krone\n\"SGD\" // Singapore Dollar\n\"HKD\" // Hong Kong Dollar\n\"HUF\" // Hungarian Forint\n\"NZD\" // New Zealand Dollar\n\"NOK\" // Norwegian Krone\n\"PLN\" // Poland Złoty",
        "example": "USD",
        "title": "Currency",
        "type": "string"
      },
      "Error": {
        "properties": {
          "code": {
            "description": "Alpaca error code, such as `40310000`. Usually the HTTP status code followed by a five-digit suffix. Several errors can share the same code, so check `message` for the specific reason.",
            "type": "number"
          },
          "message": {
            "description": "Human-readable reason for the rejection.",
            "type": "string"
          }
        },
        "required": [
          "code",
          "message"
        ],
        "title": "Error",
        "type": "object"
      },
      "SimulatedIncomingWire": {
        "description": "A simulated incoming wire transfer created with `POST /v1/testing/incoming_wires`.\n\nAvailable in the sandbox environment only.",
        "properties": {
          "account_number": {
            "description": "Account number of the destination account.",
            "example": "123456789",
            "type": "string"
          },
          "amount": {
            "description": "Amount of the incoming wire.",
            "example": "1000",
            "format": "decimal",
            "type": "string"
          },
          "batch_processed_at": {
            "description": "Not currently populated. Always returns the zero time `0001-01-01T00:00:00Z`.",
            "example": "0001-01-01T00:00:00Z",
            "format": "date-time",
            "type": "string"
          },
          "correspondent": {
            "description": "Your 4-character correspondent code.",
            "example": "TEST",
            "type": "string"
          },
          "create_at": {
            "description": "Timestamp when the incoming wire was created.",
            "example": "2026-11-09T17:45:12.123456Z",
            "format": "date-time",
            "type": "string"
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "delay_until": {
            "description": "The `delay_until` value from the request, or `null` if none was sent. Not used to delay processing.",
            "example": null,
            "format": "date-time",
            "type": [
              "string",
              "null"
            ]
          },
          "id": {
            "description": "The incoming wire ID.",
            "example": "0b6c4a9e-2f4d-4b8a-9c1e-7f3d2a1b5c6d",
            "format": "uuid",
            "type": "string"
          },
          "status": {
            "$ref": "#/components/schemas/TransferStatus"
          },
          "wire_instructions": {
            "description": "The `wire_instructions` value from the request.",
            "example": "FFC TEST-123456789",
            "type": "string"
          }
        },
        "required": [
          "id",
          "amount",
          "create_at",
          "batch_processed_at",
          "wire_instructions",
          "status",
          "delay_until",
          "account_number",
          "correspondent",
          "currency"
        ],
        "title": "SimulatedIncomingWire",
        "type": "object"
      },
      "TransferStatus": {
        "description": "- **QUEUED**\nTransfer is in queue to be processed.\n- **APPROVAL_PENDING**\nTransfer is pending approval.\n- **PENDING**\nTransfer is pending processing.\n- **SENT_TO_CLEARING**\nTransfer is being processed by the clearing firm.\n- **REJECTED**\nTransfer is rejected.\n- **CANCELED**\nClient initiated transfer cancellation.\n- **APPROVED**\nTransfer is approved.\n- **COMPLETE**\nTransfer is completed.\n- **RETURNED**\nThe bank issued an ACH return for the transfer.\n",
        "enum": [
          "QUEUED",
          "APPROVAL_PENDING",
          "PENDING",
          "SENT_TO_CLEARING",
          "REJECTED",
          "CANCELED",
          "APPROVED",
          "COMPLETE",
          "RETURNED"
        ],
        "example": "QUEUED",
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
    "/v1/testing/incoming_wires": {
      "post": {
        "description": "Simulate an incoming wire transfer to fund one of your accounts, without a real sending bank.\n\nThis endpoint is **only available in the sandbox environment**. Calling it in production returns `403`. In production, incoming wires are sent by the customer's bank and cannot be created through the API.\n\nIdentify the destination account by including an FFC (For Further Credit) string `FFC <correspondent>-<account_number>` in `wire_instructions`, where `<correspondent>` is your 4-character correspondent code and `<account_number>` is the account's 9-character account number.\n\n`currency` defaults to `USD` and must match the account's base currency. Supported currencies are `AUD`, `CAD`, `CHF`, `EUR`, `GBP`, `JPY`, `NZD`, `SGD`, `TRY`, and `USD`.\n\nThe wire is created with status `QUEUED` and processed asynchronously on the next worker run.",
        "operationId": "createIncomingWire",
        "requestBody": {
          "content": {
            "application/json": {
              "examples": {
                "eur": {
                  "summary": "EUR incoming wire to a EUR account",
                  "value": {
                    "amount": "250.50",
                    "currency": "EUR",
                    "wire_instructions": "FFC TEST-987654321"
                  }
                },
                "usd": {
                  "summary": "USD incoming wire",
                  "value": {
                    "amount": "1000.00",
                    "wire_instructions": "FFC TEST-123456789"
                  }
                }
              },
              "schema": {
                "$ref": "#/components/schemas/CreateSimulatedIncomingWireRequest"
              }
            }
          },
          "description": "The amount, currency, and destination account of the simulated incoming wire.",
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "queued": {
                    "summary": "Newly created incoming wire",
                    "value": {
                      "account_number": "123456789",
                      "amount": "1000",
                      "batch_processed_at": "0001-01-01T00:00:00Z",
                      "correspondent": "TEST",
                      "create_at": "2026-11-09T17:45:12.123456Z",
                      "currency": "USD",
                      "delay_until": null,
                      "id": "0b6c4a9e-2f4d-4b8a-9c1e-7f3d2a1b5c6d",
                      "status": "QUEUED",
                      "wire_instructions": "FFC TEST-123456789"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/SimulatedIncomingWire"
                }
              }
            },
            "description": "The simulated incoming wire was created."
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "malformedBody": {
                    "summary": "Malformed request body",
                    "value": {
                      "code": 40010000,
                      "message": "request body format is invalid"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "The request body is malformed, for example invalid JSON."
          },
          "403": {
            "content": {
              "application/json": {
                "examples": {
                  "production": {
                    "summary": "Called in production",
                    "value": {
                      "code": 40310000,
                      "message": "testing incoming wires is only available to sandbox environments"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "The endpoint was called in production. It is only available in the sandbox environment."
          },
          "404": {
            "content": {
              "application/json": {
                "examples": {
                  "accountNotFound": {
                    "summary": "Unknown account number",
                    "value": {
                      "code": 40410000,
                      "message": "account number 123456789 does not exist"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "No account with the account number in `wire_instructions` exists for your correspondent."
          },
          "422": {
            "content": {
              "application/json": {
                "examples": {
                  "invalidWireInstructions": {
                    "summary": "Wire instructions without an FFC string",
                    "value": {
                      "code": 40010001,
                      "message": "invalid wire instructions: must be in format FFC TEST-987654321"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "The request was rejected by validation. Common reasons include:\n\n- `invalid wire instructions: must be in format FFC TEST-987654321`: `wire_instructions` does not contain an FFC string.\n- `invalid correspondent used in wire instructions`: the correspondent in `wire_instructions` is not yours.\n- `currency does not match account's base currency`: `currency`, or the `USD` default, differs from the account's base currency.\n- `please contact support. currency is not supported for incoming_wire: <currency>`: `currency` is not a supported incoming wire currency.\n- `currency is not a valid currency`: `currency` is not a recognized currency code.\n- `amount should be greater than or equal to zero`: `amount` is 0 or negative. The amount must be greater than 0.\n"
          },
          "default": {
            "content": {
              "application/json": {
                "examples": {
                  "internalError": {
                    "summary": "Internal server error",
                    "value": {
                      "code": 50010000,
                      "message": "internal server error occurred"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "Unexpected error."
          }
        },
        "summary": "Simulate an Incoming Wire Transfer",
        "tags": [
          "Funding"
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
      "name": "Funding"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false,
    "apply-tag-changes": true
  }
}
```