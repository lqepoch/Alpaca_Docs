---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Create Subscription

Creates a subscription between an account and a portfolio.

# OpenAPI definition

```json
{
  "components": {
    "examples": {
      "rebalancing_account_not_found": {
        "description": "Check the account ID and try again.",
        "summary": "No account with that ID exists for your correspondent",
        "value": {
          "code": 40410000,
          "message": "account not found"
        }
      },
      "rebalancing_active_run_exists": {
        "description": "Cancel that run or wait until it finishes, then try again.",
        "summary": "The account already has a rebalance run in progress",
        "value": {
          "code": 40010001,
          "message": "there is already an active run. Please cancel previous run or wait until the run is completed"
        }
      },
      "rebalancing_crypto_position": {
        "description": "Close those positions and try again.",
        "summary": "The account holds cryptocurrency, so it cannot be subscribed to a portfolio",
        "value": {
          "code": 40010001,
          "message": "cannot create portfolio subscription when you have active position(s) in crypto"
        }
      },
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
      "rebalancing_jit_correspondent": {
        "description": "Contact support if this correspondent needs rebalancing.",
        "summary": "This correspondent uses just-in-time buying power, so rebalancing is not permitted",
        "value": {
          "code": 40310000,
          "message": "rebalancing not permitted for JIT correspondents"
        }
      },
      "rebalancing_non_usd_account": {
        "description": "This account uses another currency, so the request was rejected.",
        "summary": "Rebalancing is only available for USD accounts",
        "value": {
          "code": 40310000,
          "message": "rebalancing not permitted for Non-USD accounts"
        }
      },
      "rebalancing_open_orders": {
        "description": "Wait until those orders finish, then try again.",
        "summary": "The account has open orders, so it cannot be subscribed to a portfolio",
        "value": {
          "code": 40010001,
          "message": "cannot create portfolio subscription when you have open orders"
        }
      },
      "rebalancing_pattern_day_trader": {
        "description": "Subscribe an account that is not a pattern day trader.",
        "summary": "Pattern day trader accounts cannot be subscribed to a portfolio",
        "value": {
          "code": 40010001,
          "message": "cannot subscribe to a portfolio as a pattern day trader"
        }
      },
      "rebalancing_portfolio_unavailable": {
        "description": "Check the portfolio ID and try again.",
        "summary": "The portfolio does not exist, is not active, or does not belong to your correspondent",
        "value": {
          "code": 40010001,
          "message": "the given portfolio does not exist"
        }
      },
      "rebalancing_request_body_invalid": {
        "description": "Send a JSON body that matches the endpoint and try again.",
        "summary": "The request body is missing, is not valid JSON, or has a value of the wrong type",
        "value": {
          "code": 40010000,
          "message": "request body format is invalid"
        }
      },
      "rebalancing_schema_validation_failed": {
        "description": "Check the body against the endpoint and try again.",
        "summary": "The JSON body is missing a required field or uses a value that is not allowed",
        "value": {
          "code": 40010001,
          "message": "request parameters are invalid"
        }
      },
      "rebalancing_subscription_already_exists": {
        "description": "An account can have only one. Unsubscribe it before creating another.",
        "summary": "The account already has a subscription",
        "value": {
          "code": 42210000,
          "message": "an account can only have one active subscription"
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
      },
      "rebalancing_unsupported_media_type": {
        "description": "Set Content-Type to application/json and send the body again.",
        "summary": "The Content-Type header is not application/json",
        "value": {
          "code": 41510000,
          "message": "unsupported media type"
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
      "PortfolioSubscription": {
        "properties": {
          "account_id": {
            "description": "Account ID subscribing to portfolio",
            "type": "string"
          },
          "created_at": {
            "description": "Subscription creation timestamp",
            "format": "date-time",
            "type": "string"
          },
          "id": {
            "description": "Subscription ID",
            "type": "string"
          },
          "last_rebalanced_at": {
            "description": "Last rebalancing event for this subscription. Can be null.",
            "type": "string"
          },
          "portfolio_id": {
            "description": "Portfolio ID for subscription",
            "type": "string"
          }
        },
        "title": "PortfolioSubscription",
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
    "/v1/rebalancing/subscriptions": {
      "post": {
        "description": "Creates a subscription between an account and a portfolio.",
        "operationId": "post-v1-rebalancing-subscriptions",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "account_id": {
                    "description": "Account ID. Account must be active and the account must not have any active subscriptions already (only 1 is permitted at a time)",
                    "type": "string"
                  },
                  "portfolio_id": {
                    "description": "Portfolio ID. Portfolio must be active",
                    "type": "string"
                  }
                },
                "type": "object"
              }
            }
          },
          "description": ""
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PortfolioSubscription"
                }
              }
            },
            "description": "OK"
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "request_body_invalid": {
                    "$ref": "#/components/examples/rebalancing_request_body_invalid"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "The request body is missing, is not valid JSON, or has a value of the wrong type. Send a JSON body that matches the endpoint and try again."
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
                  },
                  "jit_correspondent": {
                    "$ref": "#/components/examples/rebalancing_jit_correspondent"
                  },
                  "non_usd_account": {
                    "$ref": "#/components/examples/rebalancing_non_usd_account"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "These credentials are not allowed to perform this action, or rebalancing is not permitted for this correspondent or account."
          },
          "404": {
            "content": {
              "application/json": {
                "examples": {
                  "account_not_found": {
                    "$ref": "#/components/examples/rebalancing_account_not_found"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "No account with that ID exists for your correspondent. Check the account ID and try again."
          },
          "415": {
            "content": {
              "application/json": {
                "examples": {
                  "unsupported_media_type": {
                    "$ref": "#/components/examples/rebalancing_unsupported_media_type"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "The Content-Type header is not application/json. Set Content-Type to application/json and send the body again."
          },
          "422": {
            "content": {
              "application/json": {
                "examples": {
                  "active_run_exists": {
                    "$ref": "#/components/examples/rebalancing_active_run_exists"
                  },
                  "crypto_position": {
                    "$ref": "#/components/examples/rebalancing_crypto_position"
                  },
                  "invalid_request": {
                    "$ref": "#/components/examples/rebalancing_invalid_request"
                  },
                  "open_orders": {
                    "$ref": "#/components/examples/rebalancing_open_orders"
                  },
                  "pattern_day_trader": {
                    "$ref": "#/components/examples/rebalancing_pattern_day_trader"
                  },
                  "portfolio_unavailable": {
                    "$ref": "#/components/examples/rebalancing_portfolio_unavailable"
                  },
                  "schema_validation_failed": {
                    "$ref": "#/components/examples/rebalancing_schema_validation_failed"
                  },
                  "subscription_already_exists": {
                    "$ref": "#/components/examples/rebalancing_subscription_already_exists"
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
            "description": "Something went wrong on our side while handling the request. Check whether the subscription was created before retrying, because this request is not idempotent. If it keeps happening, contact support."
          }
        },
        "summary": "Create Subscription",
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