---
updatedAt: 2026-05-18T08:35:05.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Read FPSL Loans Analytics for an Account

Returns aggregated FPSL interest and loan-activity counts for one account over a date range. Use this for "earned so far this month" customer UIs and for supervisory spot-checks against your internal accrual model.

The `{account_id}` path parameter accepts a account UUID (aggregation for that account).

# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "FPSLAnalyticsLoansResponse": {
        "description": "Aggregated FPSL interest and loan-activity counts for one account over a date range.\n",
        "properties": {
          "account_number": {
            "description": "Account's number at Alpaca",
            "example": "286873545",
            "type": "string"
          },
          "in_progress_lending_activities": {
            "description": "The number of FPSL lending activities currently in progress for the account.",
            "example": 2,
            "format": "int64",
            "type": "integer"
          },
          "interest": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FPSLInterest"
              }
            ],
            "description": "The accumulated interest totals for all loans in the date range.\nTotals may be adjusted retroactively at any time until interests are finalized for the month.\n",
            "example": {
              "customer": "8.61",
              "partner": "11.55"
            }
          },
          "total_lending_activities": {
            "description": "The total number of FPSL lending activities for the account within the specified date range.",
            "example": 7,
            "format": "int64",
            "type": "integer"
          }
        },
        "required": [
          "account_number",
          "interest",
          "total_lending_activities",
          "in_progress_lending_activities"
        ],
        "type": "object"
      },
      "FPSLError": {
        "description": "FPSL API error response",
        "properties": {
          "message": {
            "example": "Internal Server Error",
            "type": "string"
          }
        },
        "type": "object"
      },
      "FPSLInterest": {
        "description": "FPSL interest split between the customer and the partner.\nInterest may be adjusted retroactively at any time until interests are finalized for the month.\n",
        "properties": {
          "customer": {
            "description": "The interest accrued by the customer.",
            "example": "1.23",
            "format": "decimal",
            "type": "string"
          },
          "partner": {
            "description": "The interest accrued by the partner.",
            "example": "1.65",
            "format": "decimal",
            "type": "string"
          }
        },
        "required": [
          "customer",
          "partner"
        ],
        "type": "object"
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
    "/v1/fpsl/analytics/{account_id}/loans": {
      "get": {
        "description": "Returns aggregated FPSL interest and loan-activity counts for one account over a date range. Use this for \"earned so far this month\" customer UIs and for supervisory spot-checks against your internal accrual model.\n\nThe `{account_id}` path parameter accepts a account UUID (aggregation for that account).",
        "operationId": "get-v1-fpsl-analytics-account-loans",
        "parameters": [
          {
            "description": "The account identifier (account UUID).",
            "in": "path",
            "name": "account_id",
            "required": true,
            "schema": {
              "format": "uuid",
              "type": "string"
            }
          },
          {
            "description": "Filter loans after or on this start date (inclusive). Defaults to the first day of the current month, New York timezone.",
            "in": "query",
            "name": "start",
            "required": false,
            "schema": {
              "format": "date",
              "type": "string"
            }
          },
          {
            "description": "Filter loans before this end date (exclusive). Defaults to the day after the current date, New York timezone.",
            "in": "query",
            "name": "end",
            "required": false,
            "schema": {
              "format": "date",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FPSLAnalyticsLoansResponse"
                }
              }
            },
            "description": "Returns the aggregated FPSL loan analytics for the account."
          },
          "400": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FPSLError"
                }
              }
            },
            "description": "One of the request parameters is invalid. See the returned message for details."
          },
          "401": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FPSLError"
                }
              }
            },
            "description": "Authentication headers are missing or invalid. Make sure you authenticate your request with a valid API key."
          },
          "403": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FPSLError"
                }
              }
            },
            "description": "User has no access to a resource."
          },
          "500": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FPSLError"
                }
              }
            },
            "description": "Internal server error. We recommend retrying these later. If the issue persists, please contact us on Slack or on the Community Forum."
          }
        },
        "summary": "Read FPSL Loans Analytics for an Account",
        "tags": [
          "FPSL Program"
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
      "name": "FPSL Program"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false,
    "apply-tag-changes": true
  }
}
```