---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Create Run

Creates a rebalance run.

Omit `weights` or provide an empty array to create a subscription-driven run using the account's active subscription. Provide a non-empty `weights` array to create a manual one-off run. A manual run is rejected if the account already has an active subscription.

The determination of a run's orders and the execution of a run take place during normal market hours. Runs can be initiated outside normal market hours but remain `QUEUED` until normal market hours.

Only one run in a non-terminal status is allowed at any time.

# OpenAPI definition

```json
{
  "components": {
    "examples": {
      "rebalancing_account_not_found_for_id": {
        "description": "Check the account ID and try again. Message template: account not found for {account_id}",
        "summary": "No account with the ID in the message exists for your correspondent",
        "value": {
          "code": 40410000,
          "message": "account not found for bf2b0f93-f296-4276-a9cf-288586cf4fb7"
        }
      },
      "rebalancing_account_not_funded": {
        "description": "Fund the account and try again.",
        "summary": "The account has no equity to rebalance",
        "value": {
          "code": 42210000,
          "message": "account is not funded"
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
      "rebalancing_amount_not_decimal": {
        "description": "Send a numeric amount and try again. Message template: amount must be a decimal: {parse_error}",
        "summary": "The amount is not a valid decimal number",
        "value": {
          "code": 40010001,
          "message": "amount must be a decimal: can't convert not-a-number to decimal"
        }
      },
      "rebalancing_asset_not_found": {
        "description": "Check the symbol in the message and try again. Message template: could not find asset {symbol}",
        "summary": "A symbol in the weights is not a known asset",
        "value": {
          "code": 40010001,
          "message": "could not find asset ZZZZ"
        }
      },
      "rebalancing_asset_not_fractionable": {
        "description": "Choose a fractionable asset and try again. Message template: only assets which are fractionable are allowed. {symbol} is not fractionable",
        "summary": "The asset named in the message cannot be traded in fractional quantity, so it cannot be used in a portfolio",
        "value": {
          "code": 40010001,
          "message": "only assets which are fractionable are allowed. BRK.A is not fractionable"
        }
      },
      "rebalancing_asset_symbol_required": {
        "description": "Set the symbol and try again.",
        "summary": "A weight of type asset is missing its symbol",
        "value": {
          "code": 40010001,
          "message": "asset symbol must be specified with type asset"
        }
      },
      "rebalancing_cash_weight_percent_empty": {
        "description": "Set a numeric percent and try again. Message template: weights[{index}].percent: {parse_error}",
        "summary": "A cash weight has an empty percent",
        "value": {
          "code": 40010001,
          "message": "weights[0].percent: can't convert  to decimal"
        }
      },
      "rebalancing_correspondent_not_found": {
        "description": "Check the API key and try again.",
        "summary": "The correspondent for these credentials could not be found",
        "value": {
          "code": 40410000,
          "message": "correspondent not found"
        }
      },
      "rebalancing_crypto_asset": {
        "description": "Remove the symbol named in the message and try again. Message template: crypto assets are not allowed: {symbol}",
        "summary": "Cryptocurrency cannot be used in a portfolio",
        "value": {
          "code": 40010001,
          "message": "crypto assets are not allowed: BTC/USD"
        }
      },
      "rebalancing_duplicate_asset": {
        "description": "The message names the symbol. Include each symbol only once and try again. Message template: duplicate assets are not allowed. {symbol} is duplicated",
        "summary": "The same symbol appears more than once in the weights",
        "value": {
          "code": 40010001,
          "message": "duplicate assets are not allowed. AAPL is duplicated"
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
      "rebalancing_manual_run_with_subscription": {
        "description": "Unsubscribe first, or omit the weights and run against the subscription.",
        "summary": "This account already has a subscription, so a manual run with its own weights cannot be created",
        "value": {
          "code": 40010001,
          "message": "cannot create manual rebalance run with active subscription"
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
      "rebalancing_partial_liquidation_unsupported": {
        "description": "Use a supported run type and try again.",
        "summary": "Partial liquidation runs are not supported",
        "value": {
          "code": 40010001,
          "message": "partial_liquidation is currently not supported"
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
      "rebalancing_subscription_required": {
        "description": "Subscribe the account, or send weights for a one-off run.",
        "summary": "This account is not subscribed to a portfolio, and the request did not include weights",
        "value": {
          "code": 40410000,
          "message": "no subscription for account"
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
      },
      "rebalancing_weight_percent_not_decimal": {
        "description": "Send a numeric percent and try again. Message template: percent must be a decimal: {parse_error}",
        "summary": "A weight percent is not a valid decimal number",
        "value": {
          "code": 40010001,
          "message": "percent must be a decimal: can't convert not-a-number to decimal"
        }
      },
      "rebalancing_weight_percent_not_positive": {
        "description": "Increase it and try again.",
        "summary": "A weight percent must be greater than zero",
        "value": {
          "code": 40010001,
          "message": "percent must be greater than zero"
        }
      },
      "rebalancing_weights_must_sum_to_100": {
        "description": "The message includes the current total. Adjust the weights and try again. Message template: portfolio weights must add up to 100. Total is currently: {total}",
        "summary": "The weight percents must add up to exactly 100",
        "value": {
          "code": 40010001,
          "message": "portfolio weights must add up to 100. Total is currently: 90"
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
      "PortfolioWeightAssetEntry": {
        "allOf": [
          {
            "$ref": "#/components/schemas/PortfolioWeightRequestBase"
          },
          {
            "properties": {
              "symbol": {
                "type": "string"
              },
              "type": {
                "enum": [
                  "asset"
                ],
                "type": "string"
              }
            },
            "required": [
              "type",
              "symbol"
            ],
            "type": "object"
          }
        ],
        "description": "An asset weight. `symbol` is required.",
        "title": "PortfolioWeightAssetEntry"
      },
      "PortfolioWeightCashEntry": {
        "allOf": [
          {
            "$ref": "#/components/schemas/PortfolioWeightRequestBase"
          },
          {
            "properties": {
              "type": {
                "enum": [
                  "cash"
                ],
                "type": "string"
              }
            },
            "required": [
              "type"
            ],
            "type": "object"
          }
        ],
        "description": "A cash weight. `symbol` is optional and may be null.",
        "title": "PortfolioWeightCashEntry"
      },
      "PortfolioWeightRequest": {
        "description": "Weight entry in a portfolio create or update request, selected by `type`.",
        "discriminator": {
          "mapping": {
            "asset": "#/components/schemas/PortfolioWeightAssetEntry",
            "cash": "#/components/schemas/PortfolioWeightCashEntry"
          },
          "propertyName": "type"
        },
        "oneOf": [
          {
            "$ref": "#/components/schemas/PortfolioWeightCashEntry"
          },
          {
            "$ref": "#/components/schemas/PortfolioWeightAssetEntry"
          }
        ],
        "title": "PortfolioWeightRequest"
      },
      "PortfolioWeightRequestBase": {
        "description": "Shared fields for a portfolio weight in a create or update request.",
        "properties": {
          "percent": {
            "description": "Percentage allocated to this weight. Values must be greater than zero, and all supplied weights must total exactly 100.",
            "example": "50",
            "format": "decimal",
            "type": "string"
          },
          "symbol": {
            "description": "Asset symbol. Required and non-null when `type` is `asset`.",
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
          "percent"
        ],
        "title": "PortfolioWeightRequestBase",
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
    "/v1/rebalancing/runs": {
      "post": {
        "description": "Creates a rebalance run.\n\nOmit `weights` or provide an empty array to create a subscription-driven run using the account's active subscription. Provide a non-empty `weights` array to create a manual one-off run. A manual run is rejected if the account already has an active subscription.\n\nThe determination of a run's orders and the execution of a run take place during normal market hours. Runs can be initiated outside normal market hours but remain `QUEUED` until normal market hours.\n\nOnly one run in a non-terminal status is allowed at any time.",
        "operationId": "post-v1-rebalancing-runs",
        "requestBody": {
          "content": {
            "application/json": {
              "examples": {
                "manualRun": {
                  "summary": "Manual one-off rebalance run",
                  "value": {
                    "account_id": "bf2b0f93-f296-4276-a9cf-288586cf4fb7",
                    "type": "full_rebalance",
                    "weights": [
                      {
                        "percent": "35",
                        "symbol": "AAPL",
                        "type": "asset"
                      },
                      {
                        "percent": "20",
                        "symbol": "TSLA",
                        "type": "asset"
                      },
                      {
                        "percent": "45",
                        "symbol": "SPY",
                        "type": "asset"
                      }
                    ]
                  }
                },
                "subscriptionRun": {
                  "summary": "Subscription-driven rebalance run",
                  "value": {
                    "account_id": "bf2b0f93-f296-4276-a9cf-288586cf4fb7",
                    "type": "full_rebalance"
                  }
                }
              },
              "schema": {
                "properties": {
                  "account_id": {
                    "description": "The account to create the run for.",
                    "format": "uuid",
                    "type": "string"
                  },
                  "amount": {
                    "description": "Optional decimal amount used by the run. JSON strings and numbers are accepted.",
                    "type": [
                      "string",
                      "number",
                      "null"
                    ]
                  },
                  "type": {
                    "description": "The kind of rebalance run to create.",
                    "enum": [
                      "full_rebalance",
                      "invest_cash"
                    ],
                    "type": "string"
                  },
                  "weights": {
                    "description": "Asset allocation weights. Omit this field or provide an empty array to use the account's active subscription. Provide a non-empty array to create a manual one-off run. A manual run is rejected if the account already has an active subscription.",
                    "items": {
                      "$ref": "#/components/schemas/PortfolioWeightRequest"
                    },
                    "type": "array"
                  }
                },
                "required": [
                  "account_id",
                  "type"
                ],
                "type": "object"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
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
                  "account_not_found_for_id": {
                    "$ref": "#/components/examples/rebalancing_account_not_found_for_id"
                  },
                  "correspondent_not_found": {
                    "$ref": "#/components/examples/rebalancing_correspondent_not_found"
                  },
                  "portfolio_not_found": {
                    "$ref": "#/components/examples/rebalancing_portfolio_not_found"
                  },
                  "subscription_required": {
                    "$ref": "#/components/examples/rebalancing_subscription_required"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            },
            "description": "The resource does not exist or is not visible to this correspondent."
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
                  "account_not_funded": {
                    "$ref": "#/components/examples/rebalancing_account_not_funded"
                  },
                  "active_run_exists": {
                    "$ref": "#/components/examples/rebalancing_active_run_exists"
                  },
                  "amount_not_decimal": {
                    "$ref": "#/components/examples/rebalancing_amount_not_decimal"
                  },
                  "asset_not_found": {
                    "$ref": "#/components/examples/rebalancing_asset_not_found"
                  },
                  "asset_not_fractionable": {
                    "$ref": "#/components/examples/rebalancing_asset_not_fractionable"
                  },
                  "asset_symbol_required": {
                    "$ref": "#/components/examples/rebalancing_asset_symbol_required"
                  },
                  "cash_weight_percent_empty": {
                    "$ref": "#/components/examples/rebalancing_cash_weight_percent_empty"
                  },
                  "crypto_asset": {
                    "$ref": "#/components/examples/rebalancing_crypto_asset"
                  },
                  "duplicate_asset": {
                    "$ref": "#/components/examples/rebalancing_duplicate_asset"
                  },
                  "invalid_request": {
                    "$ref": "#/components/examples/rebalancing_invalid_request"
                  },
                  "manual_run_with_subscription": {
                    "$ref": "#/components/examples/rebalancing_manual_run_with_subscription"
                  },
                  "partial_liquidation_unsupported": {
                    "$ref": "#/components/examples/rebalancing_partial_liquidation_unsupported"
                  },
                  "schema_validation_failed": {
                    "$ref": "#/components/examples/rebalancing_schema_validation_failed"
                  },
                  "weight_percent_not_decimal": {
                    "$ref": "#/components/examples/rebalancing_weight_percent_not_decimal"
                  },
                  "weight_percent_not_positive": {
                    "$ref": "#/components/examples/rebalancing_weight_percent_not_positive"
                  },
                  "weights_must_sum_to_100": {
                    "$ref": "#/components/examples/rebalancing_weights_must_sum_to_100"
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
            "description": "Something went wrong on our side while handling the request. Check whether the run was created before retrying, because this request is not idempotent. If it keeps happening, contact support."
          }
        },
        "summary": "Create Run",
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