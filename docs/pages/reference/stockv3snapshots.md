---
updatedAt: 2026-11-17T12:48:12.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Snapshots

The snapshot endpoint provides the latest trade, latest quote, minute bar, daily bar, and previous daily bar for each requested symbol.

Bars are not adjusted after splits or dividends. Symbol mapping is also not supported: in case of a name change the symbol active at the time must be used. Trades, bars, and snapshots may include prints that were later corrected or cancelled. Corrections and cancel/error events are not applied.


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
      "stock_v3_bar": {
        "description": "OHLC aggregate of trades in an interval.\nBars are not adjusted after splits or dividends. Symbol mapping is also not supported: in case of a name change the symbol active at the time must be used.\nBars may include prints that were later corrected or cancelled. Corrections and cancel/error events are not applied.\n",
        "examples": [
          {
            "c": "57.88",
            "h": "60.08",
            "l": "57.88",
            "n": "14950",
            "o": "59.92",
            "t": "2026-09-22T22:00:00Z",
            "v": "2540940",
            "vw": "58.365"
          }
        ],
        "properties": {
          "c": {
            "description": "Price of the last trade in the bar, in the native quotation currency.",
            "format": "decimal",
            "type": "string"
          },
          "h": {
            "description": "Highest trade price in the bar, in the native quotation currency.",
            "format": "decimal",
            "type": "string"
          },
          "l": {
            "description": "Lowest trade price in the bar, in the native quotation currency.",
            "format": "decimal",
            "type": "string"
          },
          "n": {
            "description": "Number of trades in the bar.",
            "format": "int64",
            "type": "string"
          },
          "o": {
            "description": "Price of the first trade in the bar, in the native quotation currency.",
            "format": "decimal",
            "type": "string"
          },
          "t": {
            "$ref": "#/components/schemas/timestamp"
          },
          "v": {
            "description": "Number of shares traded in the bar.",
            "format": "decimal",
            "type": "string"
          },
          "vw": {
            "description": "Volume-weighted average price of the trades in the bar, in the native quotation currency.",
            "format": "decimal",
            "type": "string"
          }
        },
        "required": [
          "t",
          "o",
          "h",
          "l",
          "c",
          "v",
          "n",
          "vw"
        ],
        "type": "object"
      },
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
      "stock_v3_snapshot": {
        "description": "The latest trade, latest quote, minute bar, current daily bar, and previous daily bar for one symbol.\nBars are not adjusted after splits or dividends. Symbol mapping is also not supported: in case of a name change the symbol active at the time must be used.\nTrades and bars may include prints that were later corrected or cancelled. Corrections and cancel/error events are not applied.\n",
        "properties": {
          "daily_bar": {
            "$ref": "#/components/schemas/stock_v3_bar"
          },
          "latest_quote": {
            "$ref": "#/components/schemas/stock_v3_quote"
          },
          "latest_trade": {
            "$ref": "#/components/schemas/stock_v3_trade"
          },
          "minute_bar": {
            "$ref": "#/components/schemas/stock_v3_bar"
          },
          "prev_daily_bar": {
            "$ref": "#/components/schemas/stock_v3_bar"
          }
        },
        "type": "object"
      },
      "stock_v3_snapshots_resp": {
        "properties": {
          "snapshots": {
            "additionalProperties": {
              "$ref": "#/components/schemas/stock_v3_snapshot"
            },
            "description": "Snapshots keyed by symbol (`TICKER:MIC`).",
            "type": "object"
          }
        },
        "required": [
          "snapshots"
        ],
        "type": "object"
      },
      "stock_v3_trade": {
        "description": "A trade print published by an execution venue.\nTrades may include prints that were later corrected or cancelled. Corrections and cancel/error events are not applied.\n",
        "examples": [
          {
            "i": "1",
            "m": "XETR",
            "p": "57.84",
            "s": "120",
            "t": "2026-09-24T13:30:00.086175744Z"
          },
          {
            "m": "CEUX",
            "p": "57.84",
            "s": "45",
            "t": "2026-09-24T13:30:01.244839680Z"
          }
        ],
        "properties": {
          "i": {
            "description": "Trade ID. Omitted when the venue does not publish one.",
            "type": "string"
          },
          "m": {
            "description": "MIC of the execution venue that published the print. It can differ from the listing MIC in the symbol.",
            "type": "string"
          },
          "p": {
            "description": "Trade price, in the native quotation currency.",
            "format": "decimal",
            "type": "string"
          },
          "s": {
            "description": "Number of shares traded.",
            "format": "decimal",
            "type": "string"
          },
          "t": {
            "$ref": "#/components/schemas/timestamp"
          }
        },
        "required": [
          "t",
          "m",
          "p",
          "s"
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
    "/v3/stocks/{feed}/snapshots": {
      "get": {
        "description": "The snapshot endpoint provides the latest trade, latest quote, minute bar, daily bar, and previous daily bar for each requested symbol.\n\nBars are not adjusted after splits or dividends. Symbol mapping is also not supported: in case of a name change the symbol active at the time must be used. Trades, bars, and snapshots may include prints that were later corrected or cancelled. Corrections and cancel/error events are not applied.\n",
        "operationId": "StockV3Snapshots",
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
                  "euroctp": {
                    "summary": "BMW:XETR on the euroctp feed after the close of 2026-11-13",
                    "value": {
                      "snapshots": {
                        "BMW:XETR": {
                          "daily_bar": {
                            "c": "57.92",
                            "h": "57.98",
                            "l": "56.7",
                            "n": "12829",
                            "o": "57.08",
                            "t": "2026-11-12T23:00:00Z",
                            "v": "2044549",
                            "vw": "57.541271"
                          },
                          "latest_quote": {
                            "ap": "59.2",
                            "as": "150",
                            "bp": "55.84",
                            "bs": "300",
                            "t": "2026-11-13T18:48:19.89115Z"
                          },
                          "latest_trade": {
                            "m": "SINT",
                            "p": "57.92",
                            "s": "87",
                            "t": "2026-11-13T21:58:07.933045226Z"
                          },
                          "minute_bar": {
                            "c": "57.92",
                            "h": "57.92",
                            "l": "57.92",
                            "n": "1",
                            "o": "57.92",
                            "t": "2026-11-13T21:58:00Z",
                            "v": "87",
                            "vw": "57.92"
                          },
                          "prev_daily_bar": {
                            "c": "56.76",
                            "h": "58.8",
                            "l": "56.76",
                            "n": "15403",
                            "o": "58.32",
                            "t": "2026-11-11T23:00:00Z",
                            "v": "4858215",
                            "vw": "57.939011"
                          }
                        }
                      }
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/stock_v3_snapshots_resp"
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
        "summary": "Snapshots",
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