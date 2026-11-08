---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Cancel Run by ID

Cancels a run so it does not start, or is not retried. Only a run in QUEUED or IN_PROGRESS can be canceled. A run in any other status is rejected. Canceling does not stop a run that is already placing orders: those orders are not canceled, and the run's final status can replace CANCELED.

# OpenAPI definition

```json
{
  "components": {
    "examples": {
      "rebalancing_insufficient_permission": {
        "description": "Use credentials with the required permission and try again.",
        "summary": "These credentials are not allowed to call this endpoint, or rebalancing is not enabled for the correspondent",
        "value": {
          "code": 40310000,
          "message": "insufficient permission"
        }
      },
      "rebalancing_internal_server_error": {
        "description": "If it keeps happening, contact support.",
        "summary": "Something went wrong on our side",
        "value": {
          "code": 50010000,
          "message": "internal server error occurred"
        }
      },
      "rebalancing_invalid_request": {
        "description": "Retry it. If it keeps happening, contact support.",
        "summary": "A valid client IP address could not be read from the request",
        "value": {
          "code": 40010001,
          "message": "invalid request"
        }
      },
      "rebalancing_invalid_run_id": {
        "description": "Check `run_id` and try again.",
        "summary": "The run ID in the path is not a valid UUID",
        "value": {
          "code": 40010001,
          "message": "invalid run_id"
        }
      },
      "rebalancing_run_cannot_be_canceled": {
        "description": "Only a run in `QUEUED` or `IN_PROGRESS` can be canceled.",
        "summary": "This run cannot be canceled because it is not queued or in progress",
        "value": {
          "code": 42210000,
          "message": "run cannot be canceled"
        }
      },
      "rebalancing_run_not_found": {
        "description": "Check the run ID and try again.",
        "summary": "No rebalance run with this ID exists for your correspondent",
        "value": {
          "code": 40410000,
          "message": "rebalance run not found"
        }
      },
      "rebalancing_unauthorized": {
        "description": "Send a valid API key ID and secret, or a Broker Dashboard session, and try again.",
        "summary": "The request is not authenticated",
        "value": {
          "code": 40110000,
          "message": "request is not authorized"
        }
      },
      "rebalancing_unexpected_error": {
        "description": "If it keeps happening, contact support.",
        "summary": "Something went wrong on our side while handling the request",
        "value": {
          "error": "Internal Server Error",
          "message": "An unexpected error occurred"
        }
      }
    },
    "schemas": {
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
      "UnexpectedError": {
        "description": "Returned when request handling stops unexpectedly. This body has no numeric code.",
        "properties": {
          "error": {
            "type": "string"
          },
          "message": {
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ],
        "title": "UnexpectedError",
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
    "/v1/rebalancing/runs/{run_id}": {
      "delete": {
        "description": "Cancels a run so it does not start, or is not retried. Only a run in QUEUED or IN_PROGRESS can be canceled. A run in any other status is rejected. Canceling does not stop a run that is already placing orders: those orders are not canceled, and the run's final status can replace CANCELED.",
        "operationId": "delete-v1-rebalancing-runs-run_id",
        "responses": {
          "204": {
            "description": "No Content"
          },
          "401": {
            "content": {
              "application/json": {
                "examples": {
                  "unauthorized": {
                    "$ref": "#/components/examples/rebalancing_unauthorized"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "The request is not authenticated. Send a valid API key ID and secret, or a Broker Dashboard session, and try again."
          },
          "403": {
            "content": {
              "application/json": {
                "examples": {
                  "insufficient_permission": {
                    "$ref": "#/components/examples/rebalancing_insufficient_permission"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "These credentials are not allowed to call this endpoint, or rebalancing is not enabled for the correspondent. Use credentials with the required permission and try again."
          },
          "404": {
            "content": {
              "application/json": {
                "examples": {
                  "run_not_found": {
                    "$ref": "#/components/examples/rebalancing_run_not_found"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "No rebalance run with this ID exists for your correspondent. Check the run ID and try again."
          },
          "422": {
            "content": {
              "application/json": {
                "examples": {
                  "invalid_request": {
                    "$ref": "#/components/examples/rebalancing_invalid_request"
                  },
                  "invalid_run_id": {
                    "$ref": "#/components/examples/rebalancing_invalid_run_id"
                  },
                  "run_cannot_be_canceled": {
                    "$ref": "#/components/examples/rebalancing_run_cannot_be_canceled"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "The request failed validation or cannot be completed in its current state. The message describes the reason."
          },
          "500": {
            "content": {
              "application/json": {
                "examples": {
                  "internal_server_error": {
                    "$ref": "#/components/examples/rebalancing_internal_server_error"
                  },
                  "unexpected_error": {
                    "$ref": "#/components/examples/rebalancing_unexpected_error"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "$ref": "#/components/schemas/Error"
                    },
                    {
                      "$ref": "#/components/schemas/UnexpectedError"
                    }
                  ]
                }
              }
            },
            "description": "Something went wrong on our side while handling the request. Retry with backoff. If it keeps happening, contact support."
          }
        },
        "summary": "Cancel Run by ID",
        "tags": [
          "Rebalancing"
        ]
      },
      "parameters": [
        {
          "description": "the id of the portfolio run",
          "in": "path",
          "name": "run_id",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
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
      "name": "Rebalancing"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false
  }
}
```