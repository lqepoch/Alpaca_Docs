---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Inactivate Portfolio By ID

Archives a portfolio (soft delete). Only permitted when the portfolio has no active subscriptions. Archived portfolios are hidden from the default list response and cannot be used for new subscriptions.

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
      "rebalancing_invalid_portfolio_id": {
        "description": "Check `portfolio_id` and try again.",
        "summary": "The portfolio ID in the path is not a valid UUID",
        "value": {
          "code": 40010001,
          "message": "invalid portfolio_id"
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
      "rebalancing_nested_portfolio_weights": {
        "description": "Contact support.",
        "summary": "This portfolio includes a nested portfolio weight, which cannot be updated or deleted through this API",
        "value": {
          "code": 40010001,
          "message": "publishing portfolio status changed: portfolio contains nested portfolio weights that cannot be represented in a rebalancer event"
        }
      },
      "rebalancing_portfolio_already_inactive": {
        "description": "The portfolio is already inactive, so no further action is needed.",
        "summary": "The portfolio is already inactive, so there is nothing to delete",
        "value": {
          "code": 40010001,
          "message": "nothing to delete"
        }
      },
      "rebalancing_portfolio_has_subscriptions": {
        "description": "Unsubscribe those accounts first.",
        "summary": "Accounts are still subscribed to this portfolio, so it cannot be deleted",
        "value": {
          "code": 40010001,
          "message": "there are active subscriptions to this portfolio"
        }
      },
      "rebalancing_portfolio_not_found": {
        "description": "Check the portfolio ID and try again.",
        "summary": "No portfolio with this ID exists for your correspondent",
        "value": {
          "code": 40410000,
          "message": "portfolio not found"
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
    "/v1/rebalancing/portfolios/{portfolio_id}": {
      "delete": {
        "description": "Archives a portfolio (soft delete). Only permitted when the portfolio has no active subscriptions. Archived portfolios are hidden from the default list response and cannot be used for new subscriptions.",
        "operationId": "delete-v1-rebalancing-portfolios-portfolio_id",
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
                  "portfolio_not_found": {
                    "$ref": "#/components/examples/rebalancing_portfolio_not_found"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "No portfolio with this ID exists for your correspondent. Check the portfolio ID and try again."
          },
          "422": {
            "content": {
              "application/json": {
                "examples": {
                  "invalid_portfolio_id": {
                    "$ref": "#/components/examples/rebalancing_invalid_portfolio_id"
                  },
                  "invalid_request": {
                    "$ref": "#/components/examples/rebalancing_invalid_request"
                  },
                  "nested_portfolio_weights": {
                    "$ref": "#/components/examples/rebalancing_nested_portfolio_weights"
                  },
                  "portfolio_already_inactive": {
                    "$ref": "#/components/examples/rebalancing_portfolio_already_inactive"
                  },
                  "portfolio_has_subscriptions": {
                    "$ref": "#/components/examples/rebalancing_portfolio_has_subscriptions"
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
        "summary": "Inactivate Portfolio By ID",
        "tags": [
          "Rebalancing"
        ]
      },
      "parameters": [
        {
          "description": "The Portfolio ID",
          "in": "path",
          "name": "portfolio_id",
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