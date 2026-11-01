---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Retrieve JIT Reports

Retrieves a JIT report for the requested report type and system date. By default, the report is returned inline. For large reports, use response_type=download_url to receive a temporary signed download URL.

Generated SDKs return the JSON response. To retrieve a report through an SDK, set response_type=download_url and download the file from `url`.


# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "JITReportDownloadURL": {
        "properties": {
          "expires_at": {
            "description": "Timestamp when the signed URL expires.",
            "format": "date-time",
            "type": "string"
          },
          "filename": {
            "description": "Name of the generated report file.",
            "type": "string"
          },
          "url": {
            "description": "Temporary signed URL used to download the report.",
            "format": "uri",
            "type": "string"
          }
        },
        "required": [
          "url",
          "filename",
          "expires_at"
        ],
        "type": "object"
      },
      "JITReportType": {
        "description": "Report file to retrieve. Availability depends on the correspondent's JIT configuration. The `_v2` suffix identifies a file format, not JIT generation v2.",
        "enum": [
          "detail",
          "detail_v2",
          "net_summary",
          "net_summary_v2",
          "net_payment",
          "net_payment_final",
          "gross_summary",
          "gross_summary_v2",
          "gross_payment",
          "gross_payment_final",
          "obligation",
          "obligation_v2",
          "settlement",
          "balance",
          "summary",
          "payment"
        ],
        "example": "gross_summary_v2",
        "title": "JITReportType",
        "type": "string",
        "x-enumDescriptions": {
          "balance": "CSV snapshot of settled and unsettled cash by account and currency for the report date.",
          "detail": "CSV transaction details with explicit settlement dates and legacy T+N category labels.",
          "detail_v2": "CSV transaction details with settlement dates, execution timestamps, and entry subtypes.",
          "gross_payment": "Gross payment invoice in PDF using the legacy T+N presentation.",
          "gross_payment_final": "Final gross payment invoice in PDF using the legacy T+N presentation.",
          "gross_summary": "CSV gross totals by currency in T+0/T+1/T+2 buckets.",
          "gross_summary_v2": "CSV gross totals by explicit settlement date and currency, with no T+N columns.",
          "net_payment": "Net payment invoice in PDF using the legacy T+N presentation.",
          "net_payment_final": "Final net payment invoice in PDF using the legacy T+N presentation.",
          "net_summary": "CSV signed totals by currency in T+0/T+1/T+2 buckets. Crypto uses T+0 only.",
          "net_summary_v2": "CSV signed totals by explicit settlement date and currency, with no T+N columns.",
          "obligation": "CSV individual settlement Obligations, including earlier Obligations that remain open.",
          "obligation_v2": "CSV Obligations grouped by account, settlement date, currency, and direction across report dates.",
          "payment": "Legacy alias for gross_payment.",
          "settlement": "CSV open settlement records with explicit settlement dates and external references.",
          "summary": "Legacy alias for gross_summary."
        }
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
    "/v1/transfers/jit/reports": {
      "get": {
        "description": "Retrieves a JIT report for the requested report type and system date. By default, the report is returned inline. For large reports, use response_type=download_url to receive a temporary signed download URL.\n\nGenerated SDKs return the JSON response. To retrieve a report through an SDK, set response_type=download_url and download the file from `url`.\n",
        "operationId": "get-v1-transfers-jit-reports",
        "parameters": [
          {
            "description": "The type of report you want to get.",
            "in": "query",
            "name": "report_type",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/JITReportType"
            }
          },
          {
            "description": "Date of file generation.",
            "example": "2026-10-14",
            "in": "query",
            "name": "system_date",
            "required": true,
            "schema": {
              "format": "date",
              "type": "string"
            }
          },
          {
            "description": "The asset class to retrieve for.",
            "in": "query",
            "name": "asset_class",
            "schema": {
              "enum": [
                "us_equity",
                "crypto"
              ],
              "type": "string"
            }
          },
          {
            "description": "Controls how the report is returned. Use inline to return the report content directly in the response. Use download_url to return a temporary signed URL that can be used to download the generated report. If omitted, the default value is inline.\n",
            "in": "query",
            "name": "response_type",
            "required": false,
            "schema": {
              "default": "inline",
              "enum": [
                "inline",
                "download_url"
              ],
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "download_url": {
                    "description": "Returned when response_type is download_url.",
                    "summary": "Download URL response",
                    "value": {
                      "expires_at": "2026-04-14T23:55:00Z",
                      "filename": "ALPC-2026-04-14-common_stock-detail.csv",
                      "url": "<signed_s3_url>"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/JITReportDownloadURL"
                }
              },
              "application/pdf": {
                "schema": {
                  "description": "PDF payment report file, returned as an attachment.",
                  "format": "binary",
                  "type": "string"
                }
              },
              "text/csv": {
                "schema": {
                  "description": "CSV report file, returned as an attachment.",
                  "format": "binary",
                  "type": "string"
                }
              }
            },
            "description": "The report file when response_type is inline or omitted, or a temporary download link when response_type is download_url.",
            "headers": {
              "Content-Disposition": {
                "description": "Present when the report file is returned inline. Names the file with the same value that download_url returns in `filename`.",
                "example": "attachment;filename=ALPC-2026-04-14-common_stock-detail.csv",
                "schema": {
                  "example": "attachment;filename=ALPC-2026-04-14-common_stock-detail.csv",
                  "type": "string"
                }
              }
            }
          }
        },
        "summary": "Retrieve JIT Reports",
        "tags": [
          "Funding"
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
      "name": "Funding"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false
  }
}
```