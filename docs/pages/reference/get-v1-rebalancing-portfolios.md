---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# List Portfolios

Lists portfolios.

When more than one query parameter is passed, only portfolios meeting all provided values will be returned (logical AND between parameter values).

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
      "rebalancing_invalid_query_parameter": {
        "description": "The message names the parameter. Correct it and try again. Message template: invalid {name}",
        "summary": "A query parameter is invalid or was sent more than once",
        "value": {
          "code": 40010001,
          "message": "invalid status"
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
            "type": "number"
          },
          "message": {
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
      "Portfolio": {
        "properties": {
          "cooldown_days": {
            "description": "Count of calendar days following a rebalance before a subscription is eligible to trigger another rebalance",
            "type": "integer"
          },
          "created_at": {
            "description": "Portfolio creation timestamp",
            "type": "string"
          },
          "description": {
            "description": "Text to describe portfolio",
            "type": "string"
          },
          "id": {
            "description": "Portfolio ID",
            "type": "string"
          },
          "name": {
            "description": "Name of portfolio",
            "type": "string"
          },
          "rebalancing_conditions": {
            "description": "Rebalancing conditions for portfolio",
            "type": "string"
          },
          "status": {
            "description": "Current status of portfolio",
            "enum": [
              "active",
              "inactive",
              "needs_adjustment"
            ],
            "type": "string"
          },
          "updated_at": {
            "description": "Portfolio updated timestamp",
            "type": "string"
          },
          "weights": {
            "description": "Weight configuration to portfolio. Sum of \"percent\" values in the weights array must be 100.00",
            "items": {
              "$ref": "#/components/schemas/PortfolioWeights"
            },
            "type": "array"
          }
        },
        "required": [
          "cooldown_days"
        ],
        "title": "Portfolio",
        "type": "object"
      },
      "PortfolioWeights": {
        "properties": {
          "percent": {
            "description": "Percentage allocated to this weight as a decimal string.",
            "type": "string"
          },
          "symbol": {
            "description": "Asset symbol. `null` for cash weights. Always present.",
            "type": [
              "string",
              "null"
            ]
          },
          "type": {
            "description": "Type of weight entry in a portfolio.",
            "enum": [
              "cash",
              "asset"
            ],
            "type": "string"
          }
        },
        "required": [
          "type",
          "symbol",
          "percent"
        ],
        "title": "PortfolioWeights",
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
    "/v1/rebalancing/portfolios": {
      "get": {
        "description": "Lists portfolios.\n\nWhen more than one query parameter is passed, only portfolios meeting all provided values will be returned (logical AND between parameter values).",
        "operationId": "get-v1-rebalancing-portfolios",
        "parameters": [
          {
            "description": "Name of portfolio",
            "in": "query",
            "name": "name",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Description of portfolio",
            "in": "query",
            "name": "description",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Symbol included in portfolio",
            "in": "query",
            "name": "symbol",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Portfolio ID",
            "in": "query",
            "name": "portfolio_id",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Portfolio Status",
            "in": "query",
            "name": "status",
            "schema": {
              "enum": [
                "active",
                "inactive",
                "needs_adjustment"
              ],
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/Portfolio"
                  },
                  "type": "array"
                }
              }
            },
            "description": "Array of Portfolios"
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
          "422": {
            "content": {
              "application/json": {
                "examples": {
                  "invalid_query_parameter": {
                    "$ref": "#/components/examples/rebalancing_invalid_query_parameter"
                  },
                  "invalid_request": {
                    "$ref": "#/components/examples/rebalancing_invalid_request"
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
        "summary": "List Portfolios",
        "tags": [
          "Rebalancing"
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
      "name": "Rebalancing"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false
  }
}
```