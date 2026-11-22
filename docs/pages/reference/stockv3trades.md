---
updatedAt: 2026-11-17T12:48:12.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Historical trades

The historical trades API provides trade data for a list of symbols between the specified times.

The trades of each symbol are sorted by timestamp. The order of symbols is not guaranteed. A page can contain one symbol when that symbol fills `page_size`. Continue with `next_page_token`.


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
      "page_token": {
        "description": "The pagination token from which to continue. The value to pass here is returned in specific requests when more data is available, usually because of a response result limit.\n",
        "in": "query",
        "name": "page_token",
        "schema": {
          "type": "string"
        }
      },
      "stock_v3_end": {
        "description": "The inclusive end of the interval. A data point is returned when `start <= t <= end`. Format: RFC-3339 or YYYY-MM-DD.\nA date means the end of that day in the market's time zone.\nDefaults to the current time if not specified.\n",
        "examples": {
          "RFC-3339 nanosecond": {
            "summary": "RFC-3339 date-time with nanosecond accuracy",
            "value": "2026-09-24T01:02:03.123456789Z"
          },
          "RFC-3339 second": {
            "summary": "RFC-3339 date-time with second accuracy",
            "value": "2026-09-24T00:00:00Z"
          },
          "RFC-3339 with timezone": {
            "summary": "RFC-3339 date-time with time zone",
            "value": "2026-09-24T09:30:00-04:00"
          },
          "date": {
            "summary": "Date",
            "value": "2026-09-24"
          }
        },
        "in": "query",
        "name": "end",
        "required": false,
        "schema": {
          "anyOf": [
            {
              "format": "date-time",
              "type": "string"
            },
            {
              "format": "date",
              "type": "string"
            }
          ]
        }
      },
      "stock_v3_historical_feed": {
        "description": "The source feed of the data. All feeds require a subscription.\n - `euroctp`: EuroCTP, the official EU consolidated tape, covering trades from all EU trading venues\n - `xetr`: Xetra, the electronic trading venue of the Frankfurt Stock Exchange (Deutsche Börse)\n - `xhkg`: Hong Kong Stock Exchange (HKEX)\n - `xlon`: London Stock Exchange (LSE)\n - `xsau`: Saudi Exchange (Tadawul)\n",
        "example": "xetr",
        "in": "path",
        "name": "feed",
        "required": true,
        "schema": {
          "$ref": "#/components/schemas/stock_v3_historical_feed"
        }
      },
      "stock_v3_page_size": {
        "description": "The maximum number of data points to return in the response page.\nThe page_size applies to the total number of data points across all symbols, not per symbol.\nThe API may return fewer, even if more data points exist in the requested interval.\nAlways check `next_page_token` for more pages.\n",
        "in": "query",
        "name": "page_size",
        "required": false,
        "schema": {
          "default": 1000,
          "maximum": 10000,
          "minimum": 1,
          "type": "integer"
        }
      },
      "stock_v3_sort": {
        "description": "Sort the data points of each symbol by timestamp in ascending or descending order.",
        "in": "query",
        "name": "sort",
        "schema": {
          "allOf": [
            {
              "$ref": "#/components/schemas/sort"
            },
            {
              "type": "string"
            }
          ]
        }
      },
      "stock_v3_start": {
        "description": "The inclusive start of the interval. Format: RFC-3339 or YYYY-MM-DD.\nA date means the start of that day in the market's time zone.\n",
        "examples": {
          "RFC-3339 nanosecond": {
            "summary": "RFC-3339 date-time with nanosecond accuracy",
            "value": "2026-09-23T01:02:03.123456789Z"
          },
          "RFC-3339 second": {
            "summary": "RFC-3339 date-time with second accuracy",
            "value": "2026-09-23T00:00:00Z"
          },
          "RFC-3339 with timezone": {
            "summary": "RFC-3339 date-time with time zone",
            "value": "2026-09-23T09:30:00-04:00"
          },
          "date": {
            "summary": "Date",
            "value": "2026-09-23"
          }
        },
        "in": "query",
        "name": "start",
        "required": true,
        "schema": {
          "anyOf": [
            {
              "format": "date-time",
              "type": "string"
            },
            {
              "format": "date",
              "type": "string"
            }
          ]
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
      "next_page_token": {
        "description": "Pagination token for the next page.",
        "type": [
          "string",
          "null"
        ]
      },
      "sort": {
        "default": "asc",
        "description": "Sort data in ascending or descending order.",
        "enum": [
          "asc",
          "desc"
        ],
        "type": "string"
      },
      "stock_v3_historical_feed": {
        "enum": [
          "euroctp",
          "xetr",
          "xhkg",
          "xlon",
          "xsau"
        ],
        "type": "string"
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
      "stock_v3_trades_resp": {
        "properties": {
          "next_page_token": {
            "$ref": "#/components/schemas/next_page_token"
          },
          "trades": {
            "additionalProperties": {
              "items": {
                "$ref": "#/components/schemas/stock_v3_trade"
              },
              "type": "array"
            },
            "description": "Trades keyed by symbol (`TICKER:MIC`).",
            "type": "object"
          }
        },
        "required": [
          "trades",
          "next_page_token"
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
    "/v3/stocks/{feed}/trades": {
      "get": {
        "description": "The historical trades API provides trade data for a list of symbols between the specified times.\n\nThe trades of each symbol are sorted by timestamp. The order of symbols is not guaranteed. A page can contain one symbol when that symbol fills `page_size`. Continue with `next_page_token`.\n",
        "operationId": "StockV3Trades",
        "parameters": [
          {
            "$ref": "#/components/parameters/stock_v3_historical_feed"
          },
          {
            "$ref": "#/components/parameters/stock_v3_symbols"
          },
          {
            "$ref": "#/components/parameters/stock_v3_start"
          },
          {
            "$ref": "#/components/parameters/stock_v3_end"
          },
          {
            "$ref": "#/components/parameters/stock_v3_sort"
          },
          {
            "$ref": "#/components/parameters/stock_v3_page_size"
          },
          {
            "$ref": "#/components/parameters/page_token"
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "euroctp": {
                    "summary": "BMW:XETR trades from several venues on the euroctp feed",
                    "value": {
                      "next_page_token": "dHJhZGVzfEJNVzpYRVRSfDE3OTQ0OTAyNDgxNjYwNDg4MzJ8RVJGUXww",
                      "trades": {
                        "BMW:XETR": [
                          {
                            "m": "XGAT",
                            "p": "57.14",
                            "s": "400",
                            "t": "2026-11-12T13:30:41.54608138Z"
                          },
                          {
                            "m": "CEUX",
                            "p": "57.14",
                            "s": "10",
                            "t": "2026-11-12T13:30:43.05075Z"
                          },
                          {
                            "m": "CEUX",
                            "p": "57.14",
                            "s": "11",
                            "t": "2026-11-12T13:30:43.05077Z"
                          },
                          {
                            "m": "TQEX",
                            "p": "57.16",
                            "s": "287",
                            "t": "2026-11-12T13:30:44.37277Z"
                          },
                          {
                            "m": "XETA",
                            "p": "57.16",
                            "s": "449",
                            "t": "2026-11-12T13:30:48.16554Z"
                          }
                        ]
                      }
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/stock_v3_trades_resp"
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
        "summary": "Historical trades",
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