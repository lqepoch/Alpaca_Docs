---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Subscribe to Admin Action Events (SSE)

The Events API provides event push as well as historical queries via SSE (server sent events).

This endpoint streams events related to administrative actions performed by our systems.

Historical events are streamed immediately if queried, and updates are pushed as events occur.

Query Params Rules:
- `since` required if `until` specified
- `since_id` required if `until_id` specified
- `since` and `since_id` can't be used at the same time
Behavior:
- if `since` or `since_id` not specified this will not return any historic data
- if `until` or `until_id` reached stream will end (status 200)

---

Warning: Currently OAS-3 doesn't have full support for representing SSE style responses from an API.

In case the client code is generated from this OAS spec, don't specify a `since` and `until` there is a good chance the generated clients will hang forever waiting for the response to end.

If you require the streaming capabilities we recommend not using the generated clients for this specific endpoint until the OAS-3 standards come to a consensus on how to represent this behavior in OAS-3.

---

###  Comment messages
According to the SSE specification, any line that starts with a colon is a comment which does not contain data.  It is typically a free text that does not follow any data schema. A few examples mentioned below for comment messages.

#####  Slow client

The server sends a comment when the client is not consuming messages fast enough. Example: `: you are reading too slowly, dropped 10000 messages`

##### Internal server error

An error message is sent as a comment when the server closes the connection on an internal server error (only sent by the v2 and v2beta1 endpoints). Example: `: internal server error`

---

**Event Types**

- **LegacyNote:** Old free text based admin notes
- **Liquidation:** Event for a position liquidation which initialized by an admin
- **TransactionCancel:** Event for a manually cancelled transaction
- **AcatsStatus:** Event for a status change of an ACATS transfer (`type: acats_status_admin_event`, `category: acats`). Only sent to correspondents with ACATS API access.

# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "AdminActionAcatsStatus": {
        "allOf": [
          {
            "$ref": "#/components/schemas/AdminActionEventGeneral"
          },
          {
            "properties": {
              "context": {
                "description": "Variable schema type which depends on the type",
                "properties": {
                  "acats_id": {
                    "description": "The ID of the ACATS transfer",
                    "format": "uuid",
                    "type": "string"
                  },
                  "status_details": {
                    "$ref": "#/components/schemas/AdminActionAcatsStatusDetails"
                  },
                  "transfer_identifier": {
                    "description": "The ACATS control number (identifier) from the DTCC system. Empty until the transfer has been submitted to and acknowledged by DTCC, for example while the transfer is `PENDING`.",
                    "type": "string"
                  }
                },
                "required": [
                  "acats_id",
                  "transfer_identifier",
                  "status_details"
                ],
                "type": "object"
              },
              "type": {
                "description": "ACATS status discriminator value.",
                "enum": [
                  "acats_status_admin_event"
                ],
                "type": "string"
              }
            },
            "required": [
              "context"
            ],
            "title": "AdminActionContextAcatsStatus",
            "type": "object"
          }
        ],
        "description": "Represents structure of an AcatsStatus type AdminAction.\n\nSent for ACATS transfers on accounts of correspondents with ACATS API access, whenever the transfer changes state: when the transfer is created (`PENDING`), when it is approved and submitted to DTCC (`IN_PROGRESS`), on each subsequent DTCC status change, and when it is `REJECTED` or `SETTLED`. Sent for both incoming and outgoing transfers, including transfers not initiated through the ACATS API.\n\nThe same status may be delivered more than once for a transfer. Use `context.acats_id` to correlate events with the transfer returned by the ACATS endpoints.\n",
        "example": {
          "at": "2026-09-29T14:03:12.123456Z",
          "belongs_to_id_reference": "dfb80abb-7f52-35bd-b820-cad7e3edafec",
          "belongs_to_kind": "account",
          "category": "acats",
          "context": {
            "acats_id": "635e4b4a-baea-4b4d-a47e-406f3a9c6667",
            "status_details": {
              "broker_name": "Example Brokerage Inc.",
              "broker_number": "0001",
              "dtcc_reject_reason": "ACCOUNT_TITLE_MISMATCH",
              "dtcc_status": "REJECT",
              "rejection_message": "The account title does not match the account at the contra broker.",
              "transfer_direction": "INCOMING",
              "transfer_status": "REJECTED",
              "transfer_type": "FULL"
            },
            "transfer_identifier": "20262720012345"
          },
          "correspondent": "LPCA",
          "created_by_id_reference": "acats",
          "created_by_kind": "service",
          "event_id": "01K6BJ3Z8Q4W2X5V7N9R0T1Y3M",
          "note": "",
          "type": "acats_status_admin_event",
          "visibility": "external"
        }
      },
      "AdminActionAcatsStatusDetails": {
        "description": "Status details of the ACATS transfer at the time of the event.",
        "properties": {
          "broker_name": {
            "description": "Name of the contra broker. Omitted if not available.",
            "type": "string"
          },
          "broker_number": {
            "description": "DTCC participant number of the contra broker. Omitted if not available.",
            "type": "string"
          },
          "dtcc_reject_reason": {
            "description": "Rejection reason, as returned by DTCC. Omitted if the transfer has not been rejected by DTCC. Uses the same values as `rejection_details.rejection_reason` on the ACATS transfer; DTCC system rejections may carry additional DTCC system reject reason codes, so treat unknown values as a generic rejection. May already be present on an `IN_PROGRESS` event, before the transfer is marked `REJECTED`.",
            "example": "ACCOUNT_TITLE_MISMATCH",
            "type": "string"
          },
          "dtcc_status": {
            "description": "Transfer status as tracked by DTCC. Omitted until DTCC reports a status for the transfer. Usually one of the values of `status.dtcc_status` on the ACATS transfer; other values may appear, for example in sandbox, so treat unknown values as an intermediate status.",
            "example": "REVIEW",
            "type": "string"
          },
          "rejection_message": {
            "description": "Human readable message regarding the reason for the rejection. Omitted if not available.",
            "type": "string"
          },
          "transfer_direction": {
            "$ref": "#/components/schemas/AdminActionAcatsTransferDirection"
          },
          "transfer_status": {
            "description": "Transfer status as tracked by Alpaca. Usually one of `PENDING`, `IN_PROGRESS`, `REJECTED` or `SETTLED`, matching `status.transfer_status` on the ACATS transfer. Other values may appear in some cases, so treat unknown values as still in progress and use the ACATS endpoints for the current state.",
            "example": "IN_PROGRESS",
            "type": "string"
          },
          "transfer_type": {
            "$ref": "#/components/schemas/AdminActionAcatsTransferType"
          }
        },
        "required": [
          "transfer_status",
          "transfer_type",
          "transfer_direction"
        ],
        "type": "object"
      },
      "AdminActionAcatsTransferDirection": {
        "description": "Direction of the ACATS transfer. `UNSPECIFIED` is sent when the direction is not known; use the ACATS endpoints to get the transfer direction.",
        "enum": [
          "INCOMING",
          "OUTGOING",
          "UNSPECIFIED"
        ],
        "type": "string"
      },
      "AdminActionAcatsTransferType": {
        "description": "Type of the ACATS transfer. Note this is a simplified classification and differs from the DTCC transfer type code (`FUL`, `PTR`, ...) returned as `transfer_type` by the ACATS endpoints. `UNSPECIFIED` is sent when the type is not known or does not map to one of the other values; use the ACATS endpoints to get the DTCC transfer type.",
        "enum": [
          "FULL",
          "PARTIAL",
          "RCR",
          "UNSPECIFIED"
        ],
        "type": "string"
      },
      "AdminActionBelongsTo": {
        "description": "Represents structure of an Identifier for all AdminAction type",
        "properties": {
          "id_reference": {
            "type": "string"
          },
          "kind": {
            "$ref": "#/components/schemas/AdminActionBelongsToKind"
          }
        },
        "title": "AdminActionBelongsTo",
        "type": "object"
      },
      "AdminActionBelongsToKind": {
        "enum": [
          "account",
          "owner",
          "correspondent"
        ]
      },
      "AdminActionCategory": {
        "description": "Category of the Admin Action",
        "enum": [
          "accounts",
          "order",
          "other",
          "acats"
        ]
      },
      "AdminActionCreatedBy": {
        "description": "Represents structure of an Creator's Identifier for all AdminAction type\n",
        "properties": {
          "id_reference": {
            "type": "string"
          },
          "kind": {
            "$ref": "#/components/schemas/AdminActionCreatedByKind"
          }
        },
        "title": "AdminActionCreatedBy",
        "type": "object"
      },
      "AdminActionCreatedByKind": {
        "enum": [
          "admin",
          "service"
        ]
      },
      "AdminActionEventGeneral": {
        "description": "Represents general fields for all AdminAction type",
        "properties": {
          "at": {
            "description": "Timestamp of event",
            "format": "date-time",
            "type": "string"
          },
          "belongs_to": {
            "allOf": [
              {
                "deprecated": true,
                "description": "**Deprecation notice:**\nNever sent by the stream. Use belongs_to_kind and belongs_to_id_reference instead.\n\nSince: 2026-09-30\nSunset: 2027-01-13\n\n---\n\nDeprecated. Not sent by the stream; use `belongs_to_kind` and `belongs_to_id_reference` instead.",
                "x-deprecation": {
                  "reason": "Never sent by the stream. Use belongs_to_kind and belongs_to_id_reference instead.",
                  "since": "2026-09-30",
                  "sunset": "2027-01-13"
                }
              },
              {
                "$ref": "#/components/schemas/AdminActionBelongsTo"
              }
            ]
          },
          "belongs_to_id_reference": {
            "description": "The ID of the entity that this event belongs to",
            "type": "string"
          },
          "belongs_to_kind": {
            "$ref": "#/components/schemas/AdminActionBelongsToKind"
          },
          "category": {
            "$ref": "#/components/schemas/AdminActionCategory"
          },
          "correspondent": {
            "description": "Related correspondent",
            "type": "string"
          },
          "created_by": {
            "allOf": [
              {
                "deprecated": true,
                "description": "**Deprecation notice:**\nNever sent by the stream. Use created_by_kind and created_by_id_reference instead.\n\nSince: 2026-09-30\nSunset: 2027-01-13\n\n---\n\nDeprecated. Not sent by the stream; use `created_by_kind` and `created_by_id_reference` instead.",
                "x-deprecation": {
                  "reason": "Never sent by the stream. Use created_by_kind and created_by_id_reference instead.",
                  "since": "2026-09-30",
                  "sunset": "2027-01-13"
                }
              },
              {
                "$ref": "#/components/schemas/AdminActionCreatedBy"
              }
            ]
          },
          "created_by_id_reference": {
            "description": "The ID of the entity that created this event",
            "type": "string"
          },
          "created_by_kind": {
            "$ref": "#/components/schemas/AdminActionCreatedByKind"
          },
          "event_id": {
            "description": "Lexically sortable, monotonically increasing character array",
            "format": "ulid",
            "type": "string"
          },
          "note": {
            "description": "Free text form description of the admin action",
            "type": "string"
          },
          "replaces_event_id": {
            "description": "Id of the replaced event (optional)",
            "format": "ulid",
            "type": "string"
          },
          "type": {
            "$ref": "#/components/schemas/AdminActionType"
          },
          "visibility": {
            "$ref": "#/components/schemas/AdminActionVisibility"
          }
        },
        "required": [
          "event_id",
          "at",
          "belongs_to_kind",
          "belongs_to_id_reference",
          "created_by_kind",
          "created_by_id_reference",
          "type",
          "category",
          "visibility",
          "note",
          "correspondent"
        ],
        "title": "AdminActionEvent",
        "type": "object"
      },
      "AdminActionLegacyNote": {
        "allOf": [
          {
            "$ref": "#/components/schemas/AdminActionEventGeneral"
          },
          {
            "properties": {
              "context": {
                "description": "Variable schema type which depends on the type",
                "type": "object"
              },
              "type": {
                "description": "Admin note discriminator value. Sent as `note_admin_event`; `legacy_note_admin_event` is accepted for older events.",
                "enum": [
                  "note_admin_event",
                  "legacy_note_admin_event"
                ],
                "type": "string"
              }
            },
            "required": [
              "context"
            ],
            "title": "AdminActionContextLegacyNote",
            "type": "object"
          }
        ],
        "description": "Represents structure of a LegacyNote type AdminAction",
        "examples": [
          {
            "at": "2023-03-06T16:38:01Z",
            "belongs_to_id_reference": "0bbf1dd7-4235-4eca-8b1a-0db63572c735",
            "belongs_to_kind": "account",
            "category": "other",
            "context": {},
            "correspondent": "LPCA",
            "created_by_id_reference": "19455a3c-595f-457f-97b3-64a2b5aeae96",
            "created_by_kind": "admin",
            "event_id": "01GTVS4FVS2KJDTPYH2WM6NAXF",
            "note": "Performed action: Positions split AMZN (long): 1.011266402\n",
            "type": "note_admin_event",
            "visibility": "internal"
          }
        ]
      },
      "AdminActionLiquidation": {
        "allOf": [
          {
            "$ref": "#/components/schemas/AdminActionEventGeneral"
          },
          {
            "properties": {
              "context": {
                "description": "Variable schema type which depends on the type",
                "properties": {
                  "available_qty": {
                    "format": "decimal",
                    "type": "string"
                  },
                  "error": {
                    "type": "string"
                  },
                  "reason": {
                    "type": "string"
                  },
                  "requested_qty": {
                    "format": "decimal",
                    "type": "string"
                  },
                  "symbol": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "type": {
                "description": "Liquidation discriminator value.",
                "enum": [
                  "liquidation_admin_event"
                ],
                "type": "string"
              }
            },
            "required": [
              "context"
            ],
            "title": "AdminActionContextLiquidation",
            "type": "object"
          }
        ],
        "description": "Represents structure of a Liquidation type AdminAction",
        "examples": [
          {
            "at": "2023-03-06T16:38:01Z",
            "belongs_to_id_reference": "0bbf1dd7-4235-4eca-8b1a-0db63572c735",
            "belongs_to_kind": "account",
            "category": "accounts",
            "context": {
              "available_qty": "0.0001",
              "error": "",
              "reason": "Liquidation due to real time risk",
              "requested_qty": "0.0001",
              "symbol": "TSLA"
            },
            "correspondent": "LPCA",
            "created_by_id_reference": "19455a3c-595f-457f-97b3-64a2b5aeae96",
            "created_by_kind": "admin",
            "event_id": "01GTVS4FVS2KJDTPYH2WM6NAXF",
            "note": "Performed action: Position liquidated: Asset: TSLA, Quantity: 0.0001, Reason: Liquidation due to real time risk\n",
            "type": "liquidation_admin_event",
            "visibility": "external"
          }
        ]
      },
      "AdminActionTransactionCancel": {
        "allOf": [
          {
            "$ref": "#/components/schemas/AdminActionEventGeneral"
          },
          {
            "properties": {
              "context": {
                "description": "Variable schema type which depends on the type",
                "properties": {
                  "entry_type": {
                    "type": "string"
                  },
                  "external_id": {
                    "type": "string"
                  },
                  "transaction_id": {
                    "format": "uuid",
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "type": {
                "description": "Transaction cancel discriminator value.",
                "enum": [
                  "transaction_cancel_admin_event"
                ],
                "type": "string"
              }
            },
            "required": [
              "context"
            ],
            "title": "AdminActionContextTransactionCancel",
            "type": "object"
          }
        ],
        "description": "Represents structure of a TransactionCancel type AdminAction",
        "examples": [
          {
            "at": "2023-03-06T16:38:01Z",
            "belongs_to_id_reference": "0bbf1dd7-4235-4eca-8b1a-0db63572c735",
            "belongs_to_kind": "account",
            "category": "accounts",
            "context": {
              "entry_type": "JNLC",
              "external_id": "d5eede2c-1c08-45df-9800-87ad5eefc11f",
              "transaction_id": "fdf18af2-142b-409e-8aad-d1731e276af0"
            },
            "correspondent": "LPCA",
            "created_by_id_reference": "19455a3c-595f-457f-97b3-64a2b5aeae96",
            "created_by_kind": "admin",
            "event_id": "01GTVS4FVS2KJDTPYH2WM6NAXF",
            "note": "\"Transaction fdf18af2-142b-409e-8aad-d1731e276af0 cancelled for LPCA-12345678\n",
            "type": "transaction_cancel_admin_event",
            "visibility": "external"
          }
        ]
      },
      "AdminActionType": {
        "description": "Type of the Admin Action",
        "enum": [
          "liquidation_admin_event",
          "legacy_note_admin_event",
          "note_admin_event",
          "transaction_cancel_admin_event",
          "acats_status_admin_event"
        ]
      },
      "AdminActionVisibility": {
        "description": "Visibility of the Admin Action",
        "enum": [
          "internal",
          "external",
          "correspondent_only"
        ]
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
    "/v2/events/admin-actions": {
      "get": {
        "description": "The Events API provides event push as well as historical queries via SSE (server sent events).\n\nThis endpoint streams events related to administrative actions performed by our systems.\n\nHistorical events are streamed immediately if queried, and updates are pushed as events occur.\n\nQuery Params Rules:\n- `since` required if `until` specified\n- `since_id` required if `until_id` specified\n- `since` and `since_id` can't be used at the same time\nBehavior:\n- if `since` or `since_id` not specified this will not return any historic data\n- if `until` or `until_id` reached stream will end (status 200)\n\n---\n\nWarning: Currently OAS-3 doesn't have full support for representing SSE style responses from an API.\n\nIn case the client code is generated from this OAS spec, don't specify a `since` and `until` there is a good chance the generated clients will hang forever waiting for the response to end.\n\nIf you require the streaming capabilities we recommend not using the generated clients for this specific endpoint until the OAS-3 standards come to a consensus on how to represent this behavior in OAS-3.\n\n---\n\n###  Comment messages\nAccording to the SSE specification, any line that starts with a colon is a comment which does not contain data.  It is typically a free text that does not follow any data schema. A few examples mentioned below for comment messages.\n\n#####  Slow client\n\nThe server sends a comment when the client is not consuming messages fast enough. Example: `: you are reading too slowly, dropped 10000 messages`\n\n##### Internal server error\n\nAn error message is sent as a comment when the server closes the connection on an internal server error (only sent by the v2 and v2beta1 endpoints). Example: `: internal server error`\n\n---\n\n**Event Types**\n\n- **LegacyNote:** Old free text based admin notes\n- **Liquidation:** Event for a position liquidation which initialized by an admin\n- **TransactionCancel:** Event for a manually cancelled transaction\n- **AcatsStatus:** Event for a status change of an ACATS transfer (`type: acats_status_admin_event`, `category: acats`). Only sent to correspondents with ACATS API access.",
        "operationId": "subscribeToAdminActionSSE",
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
            "in": "query",
            "name": "since_id",
            "schema": {
              "format": "ulid",
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "until_id",
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
                "schema": {
                  "items": {
                    "discriminator": {
                      "mapping": {
                        "acats_status_admin_event": "#/components/schemas/AdminActionAcatsStatus",
                        "legacy_note_admin_event": "#/components/schemas/AdminActionLegacyNote",
                        "liquidation_admin_event": "#/components/schemas/AdminActionLiquidation",
                        "note_admin_event": "#/components/schemas/AdminActionLegacyNote",
                        "transaction_cancel_admin_event": "#/components/schemas/AdminActionTransactionCancel"
                      },
                      "propertyName": "type"
                    },
                    "oneOf": [
                      {
                        "$ref": "#/components/schemas/AdminActionLegacyNote"
                      },
                      {
                        "$ref": "#/components/schemas/AdminActionLiquidation"
                      },
                      {
                        "$ref": "#/components/schemas/AdminActionTransactionCancel"
                      },
                      {
                        "$ref": "#/components/schemas/AdminActionAcatsStatus"
                      }
                    ]
                  },
                  "type": "array"
                }
              }
            },
            "description": "Connected. Events will now start streaming as long as you keep the connection open."
          }
        },
        "summary": "Subscribe to Admin Action Events (SSE)",
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