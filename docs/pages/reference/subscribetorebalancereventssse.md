---
updatedAt: 2026-10-02T09:07:54.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Subscribe to Rebalancer Events (SSE)

The Events API provides event push as well as historical queries via SSE (server sent events).

This stream is correspondent-scoped and v2-only. A subscriber receives rebalancer events for their own correspondent. Every `event_id` is a ULID.

You can listen to portfolio status changes, portfolio run creation, and portfolio run status changes.

Historical events are streamed immediately if queried, and updates are pushed as events occur.

Query Params Rules:
- `since` required if `until` specified
- `since_id` required if `until_id` specified
- `since` and `since_id` can't be used at the same time
- `until` and `until_id` can't be used at the same time

Behavior:
- if `since` or `since_id` not specified this will not return any historic data
- if `until` or `until_id` reached stream will end (status 200)
- the `Last-Event-Id` request header, when present, is used as `since_id` and takes precedence over the `since_id` query parameter. Combining it with `since` returns an error, the same as sending `since` and `since_id` together.
- `since` and `until` select events by the time encoded in `event_id` (when the event was emitted), not by `at`. To resume reliably, use `since_id` or `Last-Event-Id`.

---

**Event types**

`event_type` selects the payload:

- `portfolio.status_changed` carries the portfolio snapshot. Weights and rebalance conditions are included. `symbol` is always present on a weight and is `null` for cash.
- `run.created` and `run.status_changed` both carry the full run snapshot: `id`, `account_id`, `portfolio_id`, `type`, `initiated_from`, `status`, `reason`, `created_at`, `updated_at`, `completed_at`, and `canceled_at`. `weights`, `orders`, `failed_orders`, and `skipped_orders` are omitted; read them from `GET /v1/rebalancing/runs/{run_id}`.
- Run `status` on this stream is `QUEUED`, `IN_PROGRESS`, `CANCELED`, `ERROR`, `TIMEOUT`, `COMPLETED_ADJUSTED`, or `COMPLETED_SUCCESS`. `CANCELED_MID_RUN` is not sent.

`correspondent` is not included in the event JSON.

---

Note for people using the clients generated from this OAS spec. Currently OAS-3 doesn't have full support for representing SSE style responses from an API, so if you are using a generated client and don't specify a `since` and `until` there is a good chance the generated clients will hang waiting for the response to end.

If you require the streaming capabilities we recommend not using the generated clients for this specific usecase until the OAS-3 standards come to a consensus on how to represent this correctly in OAS-3.


# OpenAPI definition

```json
{
  "components": {
    "examples": {
      "RebalancerEventPortfolioStatusChanged": {
        "summary": "Portfolio status changed",
        "value": {
          "at": "2026-10-05T14:30:00.123456Z",
          "event_id": "01K6Q6ZJ7M2X3T0E4B9N8RCW5D",
          "event_type": "portfolio.status_changed",
          "portfolio": {
            "cooldown_days": 7,
            "created_at": "2026-09-01T12:00:00Z",
            "description": "60/40 with a cash sleeve",
            "id": "2d49d00e-ab1c-4014-89d8-70c5f64df2fc",
            "name": "Balanced",
            "rebalance_conditions": [
              {
                "percent": "5",
                "sub_type": "absolute",
                "type": "drift_band"
              },
              {
                "day": "15",
                "sub_type": "monthly",
                "type": "calendar"
              }
            ],
            "status": "active",
            "updated_at": "2026-10-05T14:30:00.123456Z",
            "weights": [
              {
                "percent": "60",
                "symbol": "SPY",
                "type": "asset"
              },
              {
                "percent": "40",
                "symbol": null,
                "type": "cash"
              }
            ]
          }
        }
      },
      "RebalancerEventRunCreated": {
        "summary": "Portfolio run created",
        "value": {
          "at": "2026-10-05T14:31:00Z",
          "event_id": "01K6Q70B3D8H5S2V9F1G6KTMXE",
          "event_type": "run.created",
          "run": {
            "account_id": "6221407b-32b2-3e6b-a7fe-cd79e1b68ba3",
            "canceled_at": null,
            "completed_at": null,
            "created_at": "2026-10-05T14:31:00Z",
            "id": "bdc8e56f-cd91-448d-bb46-a4593cde2f95",
            "initiated_from": "system",
            "portfolio_id": "2d49d00e-ab1c-4014-89d8-70c5f64df2fc",
            "reason": null,
            "status": "QUEUED",
            "type": "full_rebalance",
            "updated_at": "2026-10-05T14:31:00Z"
          }
        }
      },
      "RebalancerEventRunStatusChanged": {
        "summary": "Portfolio run status changed",
        "value": {
          "at": "2026-10-05T14:33:12Z",
          "event_id": "01K6Q74R9W2C7N4J0P3Y5HQZAB",
          "event_type": "run.status_changed",
          "run": {
            "account_id": "6221407b-32b2-3e6b-a7fe-cd79e1b68ba3",
            "canceled_at": null,
            "completed_at": "2026-10-05T14:33:12Z",
            "created_at": "2026-10-05T14:31:00Z",
            "id": "bdc8e56f-cd91-448d-bb46-a4593cde2f95",
            "initiated_from": "system",
            "portfolio_id": "2d49d00e-ab1c-4014-89d8-70c5f64df2fc",
            "reason": null,
            "status": "COMPLETED_SUCCESS",
            "type": "full_rebalance",
            "updated_at": "2026-10-05T14:33:12Z"
          }
        }
      }
    },
    "schemas": {
      "PortfolioRunInitiator": {
        "description": "Who created the run: `system` for runs Alpaca creates (scheduled rebalancing and subscription creation), `api` for runs created with `POST /v1/rebalancing/runs`, or `dashboard` for runs created by a user in the Broker API dashboard.",
        "enum": [
          "system",
          "api",
          "dashboard"
        ],
        "title": "PortfolioRunInitiator",
        "type": "string"
      },
      "PortfolioRunType": {
        "description": "full_rebalance, partial_liquidation, or invest_cash. partial_liquidation is emitted when a run has that type. Creating one through the REST API is rejected today.",
        "enum": [
          "full_rebalance",
          "partial_liquidation",
          "invest_cash"
        ],
        "title": "PortfolioRunType",
        "type": "string"
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
      "RebalancerEvent": {
        "description": "A correspondent-scoped rebalancer event delivered on `GET /v2/events/rebalancer`.\n\n`event_type` is one of `portfolio.status_changed`, `run.created`, or `run.status_changed`.\n",
        "discriminator": {
          "mapping": {
            "portfolio.status_changed": "#/components/schemas/RebalancerPortfolioStatusChangedEvent",
            "run.created": "#/components/schemas/RebalancerRunCreatedEvent",
            "run.status_changed": "#/components/schemas/RebalancerRunStatusChangedEvent"
          },
          "propertyName": "event_type"
        },
        "oneOf": [
          {
            "$ref": "#/components/schemas/RebalancerPortfolioStatusChangedEvent"
          },
          {
            "$ref": "#/components/schemas/RebalancerRunCreatedEvent"
          },
          {
            "$ref": "#/components/schemas/RebalancerRunStatusChangedEvent"
          }
        ],
        "title": "RebalancerEvent"
      },
      "RebalancerEventPortfolio": {
        "description": "Portfolio snapshot carried on `portfolio.status_changed`, including weights and rebalance conditions.",
        "properties": {
          "cooldown_days": {
            "type": "integer"
          },
          "created_at": {
            "format": "date-time",
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "id": {
            "format": "uuid",
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "rebalance_conditions": {
            "items": {
              "$ref": "#/components/schemas/RebalancerEventRebalanceCondition"
            },
            "type": "array"
          },
          "status": {
            "enum": [
              "active",
              "inactive",
              "needs_adjustment"
            ],
            "type": "string"
          },
          "updated_at": {
            "format": "date-time",
            "type": "string"
          },
          "weights": {
            "items": {
              "$ref": "#/components/schemas/PortfolioWeights"
            },
            "type": "array"
          }
        },
        "required": [
          "id",
          "name",
          "status",
          "description",
          "weights",
          "cooldown_days",
          "rebalance_conditions",
          "created_at",
          "updated_at"
        ],
        "title": "RebalancerEventPortfolio",
        "type": "object"
      },
      "RebalancerEventRebalanceCondition": {
        "description": "Rebalance condition on a `portfolio.status_changed` event. Empty `sub_type`, `percent`, and `day` are omitted.",
        "properties": {
          "day": {
            "description": "Calendar day. A lowercase weekday name (`monday` through `friday`) for `weekly`, a day of the month (`1` to `31`) for `monthly` and `quarterly`, and `MM-DD` for `annually`. Omitted when empty.",
            "type": "string"
          },
          "percent": {
            "description": "Decimal string. Present for drift_band conditions. Omitted when empty.",
            "type": "string"
          },
          "sub_type": {
            "description": "Omitted when the producer sends no subtype.",
            "enum": [
              "absolute",
              "relative",
              "weekly",
              "monthly",
              "quarterly",
              "annually"
            ],
            "type": "string"
          },
          "type": {
            "enum": [
              "drift_band",
              "calendar",
              "on_portfolio_update"
            ],
            "type": "string"
          }
        },
        "required": [
          "type"
        ],
        "title": "RebalancerEventRebalanceCondition",
        "type": "object"
      },
      "RebalancerEventRun": {
        "description": "Full run snapshot sent on `run.created` and `run.status_changed`. Order lists are omitted; read them from `GET /v1/rebalancing/runs/{run_id}`.",
        "properties": {
          "account_id": {
            "format": "uuid",
            "type": "string"
          },
          "canceled_at": {
            "format": "date-time",
            "type": [
              "string",
              "null"
            ]
          },
          "completed_at": {
            "format": "date-time",
            "type": [
              "string",
              "null"
            ]
          },
          "created_at": {
            "format": "date-time",
            "type": "string"
          },
          "id": {
            "format": "uuid",
            "type": "string"
          },
          "initiated_from": {
            "$ref": "#/components/schemas/PortfolioRunInitiator"
          },
          "portfolio_id": {
            "format": "uuid",
            "type": "string"
          },
          "reason": {
            "type": [
              "string",
              "null"
            ]
          },
          "status": {
            "description": "Run status delivered on the rebalancer stream. `CANCELED_MID_RUN` is a REST portfolio-run status and is not sent on this stream.",
            "enum": [
              "QUEUED",
              "IN_PROGRESS",
              "CANCELED",
              "ERROR",
              "TIMEOUT",
              "COMPLETED_ADJUSTED",
              "COMPLETED_SUCCESS"
            ],
            "type": "string"
          },
          "type": {
            "$ref": "#/components/schemas/PortfolioRunType"
          },
          "updated_at": {
            "format": "date-time",
            "type": "string"
          }
        },
        "required": [
          "id",
          "account_id",
          "portfolio_id",
          "type",
          "initiated_from",
          "status",
          "reason",
          "created_at",
          "updated_at",
          "completed_at",
          "canceled_at"
        ],
        "title": "RebalancerEventRun",
        "type": "object"
      },
      "RebalancerPortfolioStatusChangedEvent": {
        "description": "Emitted when a portfolio status changes. `at` is the business time of the transition.",
        "properties": {
          "at": {
            "description": "Business time of the portfolio status transition.",
            "format": "date-time",
            "type": "string"
          },
          "event_id": {
            "format": "ulid",
            "type": "string"
          },
          "event_type": {
            "enum": [
              "portfolio.status_changed"
            ],
            "type": "string"
          },
          "portfolio": {
            "$ref": "#/components/schemas/RebalancerEventPortfolio"
          }
        },
        "required": [
          "event_id",
          "at",
          "event_type",
          "portfolio"
        ],
        "title": "RebalancerPortfolioStatusChangedEvent",
        "type": "object"
      },
      "RebalancerRunCreatedEvent": {
        "description": "Emitted when a portfolio run is created. `run` is the full run snapshot, without order lists.",
        "properties": {
          "at": {
            "description": "Business time of the run creation.",
            "format": "date-time",
            "type": "string"
          },
          "event_id": {
            "format": "ulid",
            "type": "string"
          },
          "event_type": {
            "enum": [
              "run.created"
            ],
            "type": "string"
          },
          "run": {
            "$ref": "#/components/schemas/RebalancerEventRun"
          }
        },
        "required": [
          "event_id",
          "at",
          "event_type",
          "run"
        ],
        "title": "RebalancerRunCreatedEvent",
        "type": "object"
      },
      "RebalancerRunStatusChangedEvent": {
        "description": "Emitted when a portfolio run status changes. `run` is the same full snapshot sent on `run.created`.",
        "properties": {
          "at": {
            "description": "Business time of the run status transition.",
            "format": "date-time",
            "type": "string"
          },
          "event_id": {
            "format": "ulid",
            "type": "string"
          },
          "event_type": {
            "enum": [
              "run.status_changed"
            ],
            "type": "string"
          },
          "run": {
            "$ref": "#/components/schemas/RebalancerEventRun"
          }
        },
        "required": [
          "event_id",
          "at",
          "event_type",
          "run"
        ],
        "title": "RebalancerRunStatusChangedEvent",
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
    "/v2/events/rebalancer": {
      "get": {
        "description": "The Events API provides event push as well as historical queries via SSE (server sent events).\n\nThis stream is correspondent-scoped and v2-only. A subscriber receives rebalancer events for their own correspondent. Every `event_id` is a ULID.\n\nYou can listen to portfolio status changes, portfolio run creation, and portfolio run status changes.\n\nHistorical events are streamed immediately if queried, and updates are pushed as events occur.\n\nQuery Params Rules:\n- `since` required if `until` specified\n- `since_id` required if `until_id` specified\n- `since` and `since_id` can't be used at the same time\n- `until` and `until_id` can't be used at the same time\n\nBehavior:\n- if `since` or `since_id` not specified this will not return any historic data\n- if `until` or `until_id` reached stream will end (status 200)\n- the `Last-Event-Id` request header, when present, is used as `since_id` and takes precedence over the `since_id` query parameter. Combining it with `since` returns an error, the same as sending `since` and `since_id` together.\n- `since` and `until` select events by the time encoded in `event_id` (when the event was emitted), not by `at`. To resume reliably, use `since_id` or `Last-Event-Id`.\n\n---\n\n**Event types**\n\n`event_type` selects the payload:\n\n- `portfolio.status_changed` carries the portfolio snapshot. Weights and rebalance conditions are included. `symbol` is always present on a weight and is `null` for cash.\n- `run.created` and `run.status_changed` both carry the full run snapshot: `id`, `account_id`, `portfolio_id`, `type`, `initiated_from`, `status`, `reason`, `created_at`, `updated_at`, `completed_at`, and `canceled_at`. `weights`, `orders`, `failed_orders`, and `skipped_orders` are omitted; read them from `GET /v1/rebalancing/runs/{run_id}`.\n- Run `status` on this stream is `QUEUED`, `IN_PROGRESS`, `CANCELED`, `ERROR`, `TIMEOUT`, `COMPLETED_ADJUSTED`, or `COMPLETED_SUCCESS`. `CANCELED_MID_RUN` is not sent.\n\n`correspondent` is not included in the event JSON.\n\n---\n\nNote for people using the clients generated from this OAS spec. Currently OAS-3 doesn't have full support for representing SSE style responses from an API, so if you are using a generated client and don't specify a `since` and `until` there is a good chance the generated clients will hang waiting for the response to end.\n\nIf you require the streaming capabilities we recommend not using the generated clients for this specific usecase until the OAS-3 standards come to a consensus on how to represent this correctly in OAS-3.\n",
        "operationId": "subscribeToRebalancerEventsSSE",
        "parameters": [
          {
            "description": "Format: RFC3339 or YYYY-MM-DD",
            "in": "query",
            "name": "since",
            "schema": {
              "format": "date-time",
              "type": "string"
            }
          },
          {
            "description": "Format: RFC3339 or YYYY-MM-DD",
            "in": "query",
            "name": "until",
            "schema": {
              "format": "date-time",
              "type": "string"
            }
          },
          {
            "description": "ULID `event_id` to resume the stream from. The first event returned will be the one immediately after `since_id`.",
            "in": "query",
            "name": "since_id",
            "schema": {
              "format": "ulid",
              "type": "string"
            }
          },
          {
            "description": "ULID `event_id` at which the stream will end (inclusive). Useful for backfills.",
            "in": "query",
            "name": "until_id",
            "schema": {
              "format": "ulid",
              "type": "string"
            }
          },
          {
            "description": "Used as `since_id`, taking precedence over the `since_id` query parameter. Can't be combined with `since`.",
            "in": "header",
            "name": "Last-Event-Id",
            "schema": {
              "format": "ulid",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "text/event-stream": {
                "examples": {
                  "PortfolioStatusChanged": {
                    "$ref": "#/components/examples/RebalancerEventPortfolioStatusChanged"
                  },
                  "RunCreated": {
                    "$ref": "#/components/examples/RebalancerEventRunCreated"
                  },
                  "RunStatusChanged": {
                    "$ref": "#/components/examples/RebalancerEventRunStatusChanged"
                  }
                },
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/RebalancerEvent"
                  },
                  "type": "array"
                }
              }
            },
            "description": "Connected. Events will now start streaming as long as you keep the connection open."
          }
        },
        "summary": "Subscribe to Rebalancer Events (SSE)",
        "tags": [
          "Events"
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
      "name": "Events"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false
  }
}
```