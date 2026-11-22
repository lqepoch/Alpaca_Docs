---
updatedAt: 2026-11-17T12:48:12.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Latest quotes

The latest quotes endpoint provides the latest best bid and ask prices for the given symbols.


# OpenAPI definition

```json
{
  "components": {
    "headers": {
      "ratelimit_limit": {
        "description": "Request limit per minute.",
        "example": 100,
        "schema": {
          "type": "integer"
        }
      },
      "ratelimit_remaining": {
        "description": "Request limit per minute remaining.",
        "example": 90,
        "schema": {
          "type": "integer"
        }
      },
      "ratelimit_reset": {
        "description": "The UNIX epoch when the remaining quota changes.",
        "example": 1674044551,
        "schema": {
          "type": "integer"
        }
      }
    },
    "parameters": {
      "stock_v3_latest_feed": {
        "description": "The source feed of the data. All feeds require a subscription.\n - `euroctp`: EuroCTP, the official EU consolidated tape, covering trades from all EU trading venues\n - `xetr`: Xetra, the electronic trading venue of the Frankfurt Stock Exchange (Deutsche Börse)\n - `xhkg`: Hong Kong Stock Exchange (HKEX)\n - `xlon`: London Stock Exchange (LSE)\n - `xsau`: Saudi Exchange (Tadawul)\n",
        "example": "xetr",
        "in": "path",
        "name": "feed",
        "required": true,
        "schema": {
          "$ref": "#/components/schemas/stock_v3_latest_feed"
        }
      },
      "stock_v3_symbols": {
        "description": "A comma-separated list of symbols with a limit of 1000.\nEach symbol must be in `TICKER:MIC` format, where MIC is the ISO 10383 defined code of the symbol's primary market.\nThe market must be one the feed covers, e.g. `XETR` on `xetr`; `euroctp` accepts any market.\n",
        "example": "BMW:XETR,SAP:XETR",
        "in": "query",
        "name": "symbols",
        "required": true,
        "schema": {
          "type": "string"
        }
      }
    },
    "responses": {
      "400": {
        "description": "One of the request parameters is invalid. See the returned message for details.\n",
        "headers": {
          "X-RateLimit-Limit": {
            "$ref": "#/components/headers/ratelimit_limit"
          },
          "X-RateLimit-Remaining": {
            "$ref": "#/components/headers/ratelimit_remaining"
          },
          "X-RateLimit-Reset": {
            "$ref": "#/components/headers/ratelimit_reset"
          }
        }
      },
      "401": {
        "description": "Authentication headers are missing or invalid. Make sure you authenticate your request with a valid API key.\n"
      },
      "403": {
        "description": "The requested resource is forbidden, for example because the subscription does not cover the requested data.\n"
      },
      "404": {
        "description": "The requested resource was not found, for example because the requested feed does not exist.\n"
      },
      "429": {
        "description": "Too many requests. You hit the rate limit. Use the X-RateLimit-... response headers to make sure you're under the rate limit.\n",
        "headers": {
          "X-RateLimit-Limit": {
            "$ref": "#/components/headers/ratelimit_limit"
          },
          "X-RateLimit-Remaining": {
            "$ref": "#/components/headers/ratelimit_remaining"
          },
          "X-RateLimit-Reset": {
            "$ref": "#/components/headers/ratelimit_reset"
          }
        }
      },
      "500": {
        "description": "Internal server error. We recommend retrying these later. If the issue persists, please contact us on [Slack](https://alpaca.markets/slack) or on the [Community Forum](https://forum.alpaca.markets/).\n"
      }
    },
    "schemas": {
      "stock_v3_latest_feed": {
        "enum": [
          "euroctp",
          "xetr",
          "xhkg",
          "xlon",
          "xsau"
        ],
        "type": "string"
      },
      "stock_v3_latest_quotes_resp": {
        "properties": {
          "quotes": {
            "additionalProperties": {
              "$ref": "#/components/schemas/stock_v3_quote"
            },
            "description": "The latest quotes keyed by symbol (`TICKER:MIC`).",
            "type": "object"
          }
        },
        "required": [
          "quotes"
        ],
        "type": "object"
      },
      "stock_v3_quote": {
        "description": "The best bid and offer (BBO) for the symbol.\n",
        "examples": [
          {
            "ap": "57.84",
            "as": "260",
            "bp": "57.82",
            "bs": "520",
            "t": "2026-09-24T13:30:00.041325568Z"
          }
        ],
        "properties": {
          "ap": {
            "description": "Best ask price, in the native quotation currency.",
            "format": "decimal",
            "type": "string"
          },
          "as": {
            "description": "Number of shares available at the best ask price.",
            "format": "decimal",
            "type": "string"
          },
          "bp": {
            "description": "Best bid price, in the native quotation currency.",
            "format": "decimal",
            "type": "string"
          },
          "bs": {
            "description": "Number of shares available at the best bid price.",
            "format": "decimal",
            "type": "string"
          },
          "t": {
            "$ref": "#/components/schemas/timestamp"
          }
        },
        "required": [
          "t",
          "bp",
          "bs",
          "ap",
          "as"
        ],
        "type": "object"
      },
      "timestamp": {
        "description": "Timestamp in RFC-3339 format with nanosecond precision.",
        "format": "date-time",
        "type": "string"
      }
    },
    "securitySchemes": {
      "BasicAuth": {
        "scheme": "basic",
        "type": "http"
      },
      "apiKey": {
        "in": "header",
        "name": "APCA-API-KEY-ID",
        "type": "apiKey"
      },
      "apiSecret": {
        "in": "header",
        "name": "APCA-API-SECRET-KEY",
        "type": "apiKey"
      }
    }
  },
  "info": {
    "contact": {
      "email": "support@alpaca.markets",
      "name": "Alpaca Support",
      "url": "https://alpaca.markets/support"
    },
    "description": "Access real-time and historical market data for US equities, options, crypto, and foreign exchange data through the Alpaca REST and WebSocket APIs. There are APIs for Stock Pricing, Option Pricing, Crypto Pricing, Forex, Logos, Fixed income, Corporate Actions, Screener, and News.\n",
    "license": {
      "name": "Creative Commons Attribution Share Alike 4.0 International",
      "url": "https://spdx.org/licenses/CC-BY-SA-4.0.html"
    },
    "termsOfService": "https://s3.amazonaws.com/files.alpaca.markets/disclosures/library/TermsAndConditions.pdf",
    "title": "Market Data API",
    "version": "1.1"
  },
  "openapi": "3.1.2",
  "paths": {
    "/v3/stocks/{feed}/latest/quotes": {
      "get": {
        "description": "The latest quotes endpoint provides the latest best bid and ask prices for the given symbols.\n",
        "operationId": "StockV3LatestQuotes",
        "parameters": [
          {
            "$ref": "#/components/parameters/stock_v3_latest_feed"
          },
          {
            "$ref": "#/components/parameters/stock_v3_symbols"
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "xlon": {
                    "summary": "VOD:XLON on the xlon feed after the close of 2026-11-13",
                    "value": {
                      "quotes": {
                        "VOD:XLON": {
                          "ap": "120",
                          "as": "55563",
                          "bp": "114.2",
                          "bs": "4000",
                          "t": "2026-11-13T17:30:00.12296Z"
                        }
                      }
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/stock_v3_latest_quotes_resp"
                }
              }
            },
            "description": "OK",
            "headers": {
              "X-RateLimit-Limit": {
                "$ref": "#/components/headers/ratelimit_limit"
              },
              "X-RateLimit-Remaining": {
                "$ref": "#/components/headers/ratelimit_remaining"
              },
              "X-RateLimit-Reset": {
                "$ref": "#/components/headers/ratelimit_reset"
              }
            }
          },
          "400": {
            "$ref": "#/components/responses/400"
          },
          "401": {
            "$ref": "#/components/responses/401"
          },
          "403": {
            "$ref": "#/components/responses/403"
          },
          "404": {
            "$ref": "#/components/responses/404"
          },
          "429": {
            "$ref": "#/components/responses/429"
          },
          "500": {
            "$ref": "#/components/responses/500"
          }
        },
        "security": [
          {
            "apiKey": [],
            "apiSecret": []
          },
          {
            "BasicAuth": []
          }
        ],
        "summary": "Latest quotes",
        "tags": [
          "Stock v3"
        ]
      }
    }
  },
  "servers": [
    {
      "description": "Production",
      "url": "https://data.alpaca.markets"
    },
    {
      "description": "Sandbox",
      "url": "https://data.sandbox.alpaca.markets"
    }
  ],
  "tags": [
    {
      "description": "Endpoints for global stocks.",
      "name": "Stock v3"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false,
    "apply-tag-changes": true
  }
}
```