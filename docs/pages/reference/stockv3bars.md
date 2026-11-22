---
updatedAt: 2026-11-17T12:48:12.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Historical bars

The historical bars API provides aggregates for a list of symbols between the specified times.

Bars are not adjusted after splits or dividends. Symbol mapping is also not supported: in case of a name change the symbol active at the time must be used. Bars may include prints that were later corrected or cancelled. Corrections and cancel/error events are not applied.

Daily, weekly and monthly bars start at midnight in the market's time zone. Weekly bars start on the market's first trading day of the week.

The bars of each symbol are sorted by timestamp. The order of symbols is not guaranteed. Continue with `next_page_token`.


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
      },
      "timeframe": {
        "description": "The timeframe represented by each bar in aggregation.\nYou can use any of the following values:\n - `[1-59]Min` or `[1-59]T`, e.g. `5Min` or `5T` creates 5-minute aggregations\n - `[1-23]Hour` or `[1-23]H`, e.g. `12Hour` or `12H` creates 12-hour aggregations\n - `1Day` or `1D` creates 1-day aggregations\n - `1Week` or `1W` creates 1-week aggregations\n - `[1,2,3,4,6,12]Month` or `[1,2,3,4,6,12]M`, e.g. `3Month` or `3M` creates 3-month aggregations\n",
        "example": "1Min",
        "in": "query",
        "name": "timeframe",
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
      "stock_v3_bars_resp": {
        "properties": {
          "bars": {
            "additionalProperties": {
              "items": {
                "$ref": "#/components/schemas/stock_v3_bar"
              },
              "type": "array"
            },
            "description": "Bars keyed by symbol (`TICKER:MIC`).",
            "type": "object"
          },
          "next_page_token": {
            "$ref": "#/components/schemas/next_page_token"
          }
        },
        "required": [
          "bars",
          "next_page_token"
        ],
        "type": "object"
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
    "/v3/stocks/{feed}/bars": {
      "get": {
        "description": "The historical bars API provides aggregates for a list of symbols between the specified times.\n\nBars are not adjusted after splits or dividends. Symbol mapping is also not supported: in case of a name change the symbol active at the time must be used. Bars may include prints that were later corrected or cancelled. Corrections and cancel/error events are not applied.\n\nDaily, weekly and monthly bars start at midnight in the market's time zone. Weekly bars start on the market's first trading day of the week.\n\nThe bars of each symbol are sorted by timestamp. The order of symbols is not guaranteed. Continue with `next_page_token`.\n",
        "operationId": "StockV3Bars",
        "parameters": [
          {
            "$ref": "#/components/parameters/stock_v3_historical_feed"
          },
          {
            "$ref": "#/components/parameters/stock_v3_symbols"
          },
          {
            "$ref": "#/components/parameters/timeframe"
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
                  "xlon": {
                    "summary": "VOD:XLON daily bars on the xlon feed, two per page",
                    "value": {
                      "bars": {
                        "VOD:XLON": [
                          {
                            "c": "116.95",
                            "h": "117.506",
                            "l": "115.6",
                            "n": "4274",
                            "o": "116.1",
                            "t": "2026-11-09T00:00:00Z",
                            "v": "41294069",
                            "vw": "116.842699"
                          },
                          {
                            "c": "116.6281",
                            "h": "119.05",
                            "l": "114.3",
                            "n": "7210",
                            "o": "117.05",
                            "t": "2026-11-10T00:00:00Z",
                            "v": "98346873",
                            "vw": "116.519345"
                          }
                        ]
                      },
                      "next_page_token": "MURheXxWT0Q6WExPTnxEfDE3OTQzNTUyMDAwMDAwMDAwMDA="
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/stock_v3_bars_resp"
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
        "summary": "Historical bars",
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