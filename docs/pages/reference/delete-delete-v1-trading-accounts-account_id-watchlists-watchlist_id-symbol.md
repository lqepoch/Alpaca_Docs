---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Remove a Symbol from a Watchlist

Delete one entry for an asset by symbol name

# OpenAPI definition

```json
{
  "components": {
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
    "/v1/trading/accounts/{account_id}/watchlists/{watchlist_id}/{symbol}": {
      "delete": {
        "description": "Delete one entry for an asset by symbol name",
        "operationId": "delete-DELETE-v1-trading-accounts-account_id-watchlists-watchlist_id-symbol",
        "responses": {
          "200": {
            "description": "OK"
          },
          "404": {
            "description": "The requested watchlist is not found"
          }
        },
        "summary": "Remove a Symbol from a Watchlist",
        "tags": [
          "Watchlist"
        ]
      },
      "parameters": [
        {
          "description": "Account identifier.",
          "in": "path",
          "name": "account_id",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "description": "The Watchlist ID",
          "in": "path",
          "name": "watchlist_id",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "description": "The symbol ",
          "in": "path",
          "name": "symbol",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
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
      "name": "Watchlist"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false
  }
}
```