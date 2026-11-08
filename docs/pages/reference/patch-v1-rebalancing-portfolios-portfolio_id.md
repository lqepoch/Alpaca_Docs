---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Update Portfolio by ID

Updates a portfolio. If weights or conditions are changed, all subscribed accounts will be evaluated for rebalancing at the next opportunity (normal market hours). If a cooldown is active on the portfolio, the rebalancing will occur after the cooldown expired.

# OpenAPI definition

```json
{
  "components": {
    "examples": {
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
      "rebalancing_calendar_day_not_mmdd": {
        "description": "Use that format and try again. Message template: calendar conditions day must be in MM-DD format: {time_parse_error}",
        "summary": "An annual calendar condition has a day that is not in MM-DD format",
        "value": {
          "code": 40010001,
          "message": "calendar conditions day must be in MM-DD format: parsing time \"13-40\" as \"01-02\": month out of range"
        }
      },
      "rebalancing_calendar_day_not_number": {
        "description": "Use a day from 1 to 31 and try again. Message template: calendar conditions day must be a number: {parse_error}",
        "summary": "A monthly or quarterly calendar condition has a day that is not a number",
        "value": {
          "code": 40010001,
          "message": "calendar conditions day must be a number: strconv.Atoi: parsing \"abc\": invalid syntax"
        }
      },
      "rebalancing_calendar_day_out_of_range": {
        "description": "Use a day in that range and try again.",
        "summary": "A monthly or quarterly calendar condition has a day outside 1 to 31",
        "value": {
          "code": 40010001,
          "message": "calendar conditions must have a valid day between 1 and 31 inclusive"
        }
      },
      "rebalancing_calendar_day_required": {
        "description": "Set the day and try again.",
        "summary": "A calendar rebalance condition is missing its day",
        "value": {
          "code": 40010001,
          "message": "calendar conditions must have day specified"
        }
      },
      "rebalancing_calendar_subtype_invalid": {
        "description": "Use `weekly`, `monthly`, `quarterly`, or `annually`.",
        "summary": "A calendar rebalance condition has a missing or unsupported subtype",
        "value": {
          "code": 40010001,
          "message": "calendar conditions must have sub_type: weekly, monthly, annually, quarterly"
        }
      },
      "rebalancing_calendar_weekday_invalid": {
        "description": "Use monday, tuesday, wednesday, thursday, or friday.",
        "summary": "A weekly calendar condition has a day that is not a weekday name",
        "value": {
          "code": 40010001,
          "message": "calendar conditions must have day: [monday tuesday wednesday thursday friday]"
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
      "rebalancing_condition_percent_not_decimal": {
        "description": "Send a numeric percent and try again. Message template: rebalance_conditions[{index}].percent: {parse_error}",
        "summary": "The percent on the rebalance condition named in the message is not a valid decimal",
        "value": {
          "code": 40010001,
          "message": "rebalance_conditions[0].percent: can't convert not-a-number to decimal"
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
      "rebalancing_drift_percent_not_decimal": {
        "description": "Send a numeric percent and try again. Message template: drift_band conditions percent must be a decimal: {parse_error}",
        "summary": "A drift band percent is not a valid decimal number",
        "value": {
          "code": 40010001,
          "message": "drift_band conditions percent must be a decimal: can't convert not-a-number to decimal"
        }
      },
      "rebalancing_drift_percent_not_positive": {
        "description": "Use a percent greater than zero and try again.",
        "summary": "A drift band condition has a negative percent",
        "value": {
          "code": 40010001,
          "message": "drift_band conditions must have positive percent"
        }
      },
      "rebalancing_drift_percent_precision": {
        "description": "Round it to two decimal places and try again.",
        "summary": "A drift band percent has more than two decimal places",
        "value": {
          "code": 40010001,
          "message": "drift_band conditions only support percent up to two 2 decimal places"
        }
      },
      "rebalancing_drift_percent_required": {
        "description": "Set the percent and try again.",
        "summary": "A drift band condition is missing its percent",
        "value": {
          "code": 40010001,
          "message": "drift_band conditions must have percent specified"
        }
      },
      "rebalancing_drift_subtype_invalid": {
        "description": "Use `absolute` or `relative`.",
        "summary": "A drift band condition has a missing or unsupported subtype",
        "value": {
          "code": 40010001,
          "message": "drift_band conditions must have sub_type absolute or relative"
        }
      },
      "rebalancing_duplicate_absolute_drift": {
        "description": "Remove the extra one and try again.",
        "summary": "Only one absolute drift band condition is allowed",
        "value": {
          "code": 40010001,
          "message": "you can only have one absolute drift_band type rebalance condition"
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
      "rebalancing_duplicate_calendar_condition": {
        "description": "Remove the extra one and try again.",
        "summary": "Only one calendar rebalance condition is allowed",
        "value": {
          "code": 40010001,
          "message": "you can only have one calendar type rebalance condition"
        }
      },
      "rebalancing_duplicate_on_update_condition": {
        "description": "Remove the extra `on_portfolio_update` condition and try again.",
        "summary": "Only one on portfolio update condition is allowed",
        "value": {
          "code": 40010001,
          "message": "you can only have one on_portfolio_update type rebalance condition"
        }
      },
      "rebalancing_duplicate_relative_drift": {
        "description": "Remove the extra one and try again.",
        "summary": "Only one relative drift band condition is allowed",
        "value": {
          "code": 40010001,
          "message": "you can only have one relative drift_band type rebalance condition"
        }
      },
      "rebalancing_empty_portfolio_update": {
        "description": "Send at least one of `name`, `description`, `cooldown_days`, `weights`, or `rebalance_conditions`.",
        "summary": "The update did not include any fields to change",
        "value": {
          "code": 40010001,
          "message": "update request must contain at least one of the following fields: name, description, cooldown_days, weights, rebalance_conditions"
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
      "rebalancing_on_update_day_forbidden": {
        "description": "Remove `day` from the `on_portfolio_update` condition and try again.",
        "summary": "An on portfolio update condition cannot include a day",
        "value": {
          "code": 40010001,
          "message": "on_portfolio_update conditions cannot have day specified"
        }
      },
      "rebalancing_on_update_percent_forbidden": {
        "description": "Remove `percent` from the `on_portfolio_update` condition and try again.",
        "summary": "An on portfolio update condition cannot include a percent",
        "value": {
          "code": 40010001,
          "message": "on_portfolio_update conditions cannot have percent specified"
        }
      },
      "rebalancing_on_update_subtype_forbidden": {
        "description": "Remove `sub_type` from the `on_portfolio_update` condition and try again.",
        "summary": "An on portfolio update condition cannot include a subtype",
        "value": {
          "code": 40010001,
          "message": "on_portfolio_update conditions cannot have sub_type specified"
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
      "RebalancingConditions": {
        "properties": {
          "day": {
            "description": "Used to specify the rebalancing day for conditions of type = calendar. Only permitted and required for type = calendar. In scenarios when the specified day aligns to a non-trading day, the rebalance will be triggered on the preceding trading day. For type= annually, the value must be passed in MM-DD format. If 02-29 is specified and the current year is not a leap year, the rebalance will occur on the trading day preceding 2/29. For type= quarterly and monthly the value must be an integer between 1 and 31 inclusive. This represents the day of month. For quarterly, rebalancing will trigger on this day in January, March, June, and December. If the specified day is non-existent for the month then the rebalancing will trigger on the preceding trading day. For type = weekly, permitted values are Monday, Tuesday, Wednesday, Thursday, Friday.",
            "type": "string"
          },
          "percent": {
            "description": "Must be a positive value, up to two decimal places. Only permitted and required for type = drift_band. This is the max allowable drift percent from any target weight (+/-)",
            "type": "string"
          },
          "sub_type": {
            "description": "For type = drift_band: absolute or relative. For type = calendar: weekly,monthly, quarterly or annually. For type = on_portfolio_update: there is no subtype",
            "type": "string"
          },
          "type": {
            "description": "Possible values of drift_band, calendar or on_portfolio_update",
            "type": "string"
          }
        },
        "title": "RebalancingConditions",
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
      ],
      "patch": {
        "description": "Updates a portfolio. If weights or conditions are changed, all subscribed accounts will be evaluated for rebalancing at the next opportunity (normal market hours). If a cooldown is active on the portfolio, the rebalancing will occur after the cooldown expired.",
        "operationId": "patch-v1-rebalancing-portfolios-portfolio_id",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "cooldown_days": {
                    "description": "Used to update portfolio cooldown days.",
                    "type": "integer"
                  },
                  "description": {
                    "description": "Used to update portfolio description.",
                    "type": "string"
                  },
                  "name": {
                    "description": "Used to update portfolio name.",
                    "type": "string"
                  },
                  "rebalancing_conditions": {
                    "description": "Used to update portfolio conditions.",
                    "items": {
                      "$ref": "#/components/schemas/RebalancingConditions"
                    },
                    "type": "array"
                  },
                  "weights": {
                    "description": "Used to update portfolio weights.",
                    "items": {
                      "$ref": "#/components/schemas/PortfolioWeightRequest"
                    },
                    "type": "array"
                  }
                },
                "required": [
                  "cooldown_days"
                ],
                "type": "object"
              }
            }
          }
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Portfolio"
                }
              }
            },
            "description": "The updated portfolio"
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
                  "asset_not_found": {
                    "$ref": "#/components/examples/rebalancing_asset_not_found"
                  },
                  "asset_not_fractionable": {
                    "$ref": "#/components/examples/rebalancing_asset_not_fractionable"
                  },
                  "asset_symbol_required": {
                    "$ref": "#/components/examples/rebalancing_asset_symbol_required"
                  },
                  "calendar_day_not_mmdd": {
                    "$ref": "#/components/examples/rebalancing_calendar_day_not_mmdd"
                  },
                  "calendar_day_not_number": {
                    "$ref": "#/components/examples/rebalancing_calendar_day_not_number"
                  },
                  "calendar_day_out_of_range": {
                    "$ref": "#/components/examples/rebalancing_calendar_day_out_of_range"
                  },
                  "calendar_day_required": {
                    "$ref": "#/components/examples/rebalancing_calendar_day_required"
                  },
                  "calendar_subtype_invalid": {
                    "$ref": "#/components/examples/rebalancing_calendar_subtype_invalid"
                  },
                  "calendar_weekday_invalid": {
                    "$ref": "#/components/examples/rebalancing_calendar_weekday_invalid"
                  },
                  "cash_weight_percent_empty": {
                    "$ref": "#/components/examples/rebalancing_cash_weight_percent_empty"
                  },
                  "condition_percent_not_decimal": {
                    "$ref": "#/components/examples/rebalancing_condition_percent_not_decimal"
                  },
                  "crypto_asset": {
                    "$ref": "#/components/examples/rebalancing_crypto_asset"
                  },
                  "drift_percent_not_decimal": {
                    "$ref": "#/components/examples/rebalancing_drift_percent_not_decimal"
                  },
                  "drift_percent_not_positive": {
                    "$ref": "#/components/examples/rebalancing_drift_percent_not_positive"
                  },
                  "drift_percent_precision": {
                    "$ref": "#/components/examples/rebalancing_drift_percent_precision"
                  },
                  "drift_percent_required": {
                    "$ref": "#/components/examples/rebalancing_drift_percent_required"
                  },
                  "drift_subtype_invalid": {
                    "$ref": "#/components/examples/rebalancing_drift_subtype_invalid"
                  },
                  "duplicate_absolute_drift": {
                    "$ref": "#/components/examples/rebalancing_duplicate_absolute_drift"
                  },
                  "duplicate_asset": {
                    "$ref": "#/components/examples/rebalancing_duplicate_asset"
                  },
                  "duplicate_calendar_condition": {
                    "$ref": "#/components/examples/rebalancing_duplicate_calendar_condition"
                  },
                  "duplicate_on_update_condition": {
                    "$ref": "#/components/examples/rebalancing_duplicate_on_update_condition"
                  },
                  "duplicate_relative_drift": {
                    "$ref": "#/components/examples/rebalancing_duplicate_relative_drift"
                  },
                  "empty_portfolio_update": {
                    "$ref": "#/components/examples/rebalancing_empty_portfolio_update"
                  },
                  "invalid_portfolio_id": {
                    "$ref": "#/components/examples/rebalancing_invalid_portfolio_id"
                  },
                  "invalid_request": {
                    "$ref": "#/components/examples/rebalancing_invalid_request"
                  },
                  "nested_portfolio_weights": {
                    "$ref": "#/components/examples/rebalancing_nested_portfolio_weights"
                  },
                  "on_update_day_forbidden": {
                    "$ref": "#/components/examples/rebalancing_on_update_day_forbidden"
                  },
                  "on_update_percent_forbidden": {
                    "$ref": "#/components/examples/rebalancing_on_update_percent_forbidden"
                  },
                  "on_update_subtype_forbidden": {
                    "$ref": "#/components/examples/rebalancing_on_update_subtype_forbidden"
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
            "description": "Something went wrong on our side while handling the request. Retry with backoff. If it keeps happening, contact support."
          }
        },
        "summary": "Update Portfolio by ID",
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