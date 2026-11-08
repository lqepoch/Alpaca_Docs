---
updatedAt: 2026-05-27T17:58:03.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# News articles

Returns the latest news articles across stocks and crypto. By default, returns the latest 10 news articles.


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
      "end": {
        "description": "The inclusive end of the interval. Format: RFC-3339 or YYYY-MM-DD.\nDefault: the current time if the user has a real-time access for the feed, otherwise 15 minutes before the current time.\n",
        "examples": {
          "RFC-3339 nanosecond": {
            "summary": "RFC-3339 date-time with nanosecond accuracy",
            "value": "2024-01-04T01:02:03.123456789Z"
          },
          "RFC-3339 second": {
            "summary": "RFC-3339 date-time with second accuracy",
            "value": "2024-01-04T00:00:00Z"
          },
          "RFC-3339 with timezone": {
            "summary": "RFC-3339 date-time with time zone",
            "value": "2024-01-04T09:30:00-04:00"
          },
          "date": {
            "summary": "Date",
            "value": "2024-01-04"
          }
        },
        "in": "query",
        "name": "end",
        "required": false,
        "schema": {
          "format": "date-time",
          "type": "string"
        }
      },
      "news_sort": {
        "description": "Sort articles by updated date.",
        "in": "query",
        "name": "sort",
        "schema": {
          "default": "desc",
          "enum": [
            "asc",
            "desc"
          ],
          "type": "string"
        }
      },
      "page_token": {
        "description": "The pagination token from which to continue. The value to pass here is returned in specific requests when more data is available, usually because of a response result limit.\n",
        "in": "query",
        "name": "page_token",
        "schema": {
          "type": "string"
        }
      },
      "start": {
        "description": "The inclusive start of the interval. Format: RFC-3339 or YYYY-MM-DD.\nDefault: the beginning of the current day, but at least 15 minutes ago if the user doesn't have real-time access for the feed.\n",
        "examples": {
          "RFC-3339 nanosecond": {
            "summary": "RFC-3339 date-time with nanosecond accuracy",
            "value": "2024-01-03T01:02:03.123456789Z"
          },
          "RFC-3339 second": {
            "summary": "RFC-3339 date-time with second accuracy",
            "value": "2024-01-03T00:00:00Z"
          },
          "RFC-3339 with timezone": {
            "summary": "RFC-3339 date-time with time zone",
            "value": "2024-01-03T09:30:00-04:00"
          },
          "date": {
            "summary": "Date",
            "value": "2024-01-03"
          }
        },
        "in": "query",
        "name": "start",
        "required": false,
        "schema": {
          "format": "date-time",
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
        "description": "The requested resource is forbidden.\n"
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
      "news": {
        "description": "Model representing a news article.",
        "properties": {
          "author": {
            "description": "Original author of news article (may be empty).",
            "type": "string"
          },
          "content": {
            "description": "Content of the news article (might contain HTML, may be empty).",
            "type": "string"
          },
          "created_at": {
            "description": "Date article was created (RFC-3339).",
            "format": "date-time",
            "type": "string"
          },
          "headline": {
            "description": "Headline or title of the article.",
            "minLength": 1,
            "type": "string"
          },
          "id": {
            "description": "News article ID.",
            "format": "int64",
            "type": "integer"
          },
          "images": {
            "description": "List of images (URLs) related to given article (may be empty).",
            "items": {
              "$ref": "#/components/schemas/news_image"
            },
            "type": "array",
            "uniqueItems": true
          },
          "source": {
            "description": "Source from which the news originated.",
            "minLength": 1,
            "type": "string"
          },
          "summary": {
            "description": "Summary text for the article (may be first sentence of content or may be empty).",
            "type": "string"
          },
          "symbols": {
            "description": "List of related or mentioned symbols.",
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "updated_at": {
            "description": "Date article was updated (RFC-3339).",
            "format": "date-time",
            "type": "string"
          },
          "url": {
            "description": "URL of article (if applicable).",
            "format": "uri",
            "type": [
              "string",
              "null"
            ]
          }
        },
        "required": [
          "id",
          "headline",
          "author",
          "created_at",
          "updated_at",
          "summary",
          "content",
          "images",
          "symbols",
          "source"
        ],
        "type": "object"
      },
      "news_image": {
        "description": "A model representing images for a news article. Simply a URL to the image along with a size parameter suggesting the display size of the image.",
        "properties": {
          "size": {
            "description": "Possible values for size are thumb, small and large.",
            "enum": [
              "thumb",
              "small",
              "large"
            ],
            "examples": [
              "thumb"
            ],
            "minLength": 1,
            "type": "string"
          },
          "url": {
            "description": "URL to image from news article.",
            "format": "uri",
            "minLength": 1,
            "type": "string"
          }
        },
        "required": [
          "size",
          "url"
        ],
        "type": "object"
      },
      "news_resp": {
        "properties": {
          "news": {
            "items": {
              "$ref": "#/components/schemas/news"
            },
            "type": "array"
          },
          "next_page_token": {
            "$ref": "#/components/schemas/next_page_token"
          }
        },
        "required": [
          "news",
          "next_page_token"
        ],
        "type": "object"
      },
      "next_page_token": {
        "description": "Pagination token for the next page.",
        "type": [
          "string",
          "null"
        ]
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
    "/v1beta1/news": {
      "get": {
        "description": "Returns the latest news articles across stocks and crypto. By default, returns the latest 10 news articles.\n",
        "operationId": "News",
        "parameters": [
          {
            "$ref": "#/components/parameters/start"
          },
          {
            "$ref": "#/components/parameters/end"
          },
          {
            "$ref": "#/components/parameters/news_sort"
          },
          {
            "description": "A comma-separated list of symbols for which to query news.",
            "in": "query",
            "name": "symbols",
            "schema": {
              "example": "AAPL,TSLA,BTCUSD",
              "type": "string"
            }
          },
          {
            "description": "Limit of news items to be returned for a result page.",
            "example": 10,
            "in": "query",
            "name": "limit",
            "schema": {
              "maximum": 50,
              "minimum": 1,
              "type": "integer"
            }
          },
          {
            "description": "Boolean indicator to include content for news articles (if available).",
            "in": "query",
            "name": "include_content",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "description": "Boolean indicator to exclude news articles that do not contain content.",
            "in": "query",
            "name": "exclude_contentless",
            "schema": {
              "type": "boolean"
            }
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
                  "news-response-example": {
                    "value": {
                      "news": [
                        {
                          "author": "",
                          "content": "Following the release of SpaceX's third-quarter 2026 financial results, several analysts have updated their outlook on the company. UBS maintained a Buy rating while raising its price target to $230 from $210. Additionally, Wells Fargo maintained an Overweight rating and increased its price target to $274 from $214. These adjustments reflect analyst reactions to the company's reported revenue growth and strategic focus on artificial intelligence.",
                          "created_at": "2026-10-21T15:02:10Z",
                          "headline": "Analysts Adjust Price Targets for SpaceX Following Q3 Results",
                          "id": 100536145,
                          "images": [],
                          "source": "fiscal.ai",
                          "summary": "Financial institutions including UBS and Wells Fargo have updated their price targets for SpaceX following the company's third-quarter earnings report.",
                          "symbols": [
                            "SPCX"
                          ],
                          "updated_at": "2026-10-21T15:02:10Z",
                          "url": "https://www.moomoo.com/stock/SPCX-US/news?chain_id=Name1K9-3FXPhg.1lcj000&global_content=%7B%22promote_id%22%3A13764,%22sub_promote_id%22%3A64,%22f%22%3A%22www.moomoo.com%2Fcommunity%2Fprofile%2F105275796%2Fpost%2Fall%22%7D"
                        },
                        {
                          "author": "Badar Shaikh",
                          "content": "<p>It was yet another eventful week for <strong>Tesla Inc</strong> (NASDAQ:TSLA) and CEO <strong>Elon Musk</strong> amid the Roadster's high-flying debut, questions about a possible SpaceX merger and more.</p>",
                          "created_at": "2026-10-18T12:51:02Z",
                          "headline": "This Week in TSLA: Roadster's Flying Debut, Cybercab Speeding in School Zones, SpaceX Merger and More",
                          "id": 62429279,
                          "images": [
                            {
                              "size": "large",
                              "url": "https://cdn.benzinga.com/files/images/story/2026/10/18/Kaunas--Lithuania-2022---April-14-Tesla-.jpg?width=2048&height=1536"
                            },
                            {
                              "size": "small",
                              "url": "https://cdn.benzinga.com/files/images/story/2026/10/18/Kaunas--Lithuania-2022---April-14-Tesla-.jpg?width=1024&height=768"
                            },
                            {
                              "size": "thumb",
                              "url": "https://cdn.benzinga.com/files/images/story/2026/10/18/Kaunas--Lithuania-2022---April-14-Tesla-.jpg?width=250&height=187"
                            }
                          ],
                          "source": "benzinga",
                          "summary": "This week, Tesla unveiled its flying Roadster, faced Cybercab questions and merger speculation with SpaceX.",
                          "symbols": [
                            "SPCX",
                            "TSLA"
                          ],
                          "updated_at": "2026-10-18T12:51:02Z",
                          "url": "https://www.benzinga.com/markets/tech/26/10/62429279/this-week-in-tsla-roadsters-flying-debut-cybercab-speeding-in-school-zones-spacex-merger-and-more"
                        }
                      ],
                      "next_page_token": "MTc5MjMyNzg2MjAwMDAwMDAwMHw2MjQyOTI3OQ=="
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/news_resp"
                }
              }
            },
            "description": "OK"
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
        "summary": "News articles",
        "tags": [
          "News"
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
      "description": "Endpoints for getting news articles about the stock market.",
      "name": "News"
    }
  ]
}
```