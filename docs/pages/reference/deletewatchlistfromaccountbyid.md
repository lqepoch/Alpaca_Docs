---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Remove a Watchlist

Irrevocably delete a watchlist.

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
    "/v1/trading/accounts/{account_id}/watchlists/{watchlist_id}": {
      "delete": {
        "description": "Irrevocably delete a watchlist.",
        "operationId": "deleteWatchlistFromAccountById",
        "responses": {
          "200": {
            "description": "Watchlist deleted."
          }
        },
        "summary": "Remove a Watchlist",
        "tags": [
          "Watchlist"
        ]
      },
      "parameters": [
        {
          "description": "Unique identifier of an account",
          "in": "path",
          "name": "account_id",
          "required": true,
          "schema": {
            "format": "uuid",
            "type": "string"
          }
        },
        {
          "description": "Unique identifier of a watchlist",
          "in": "path",
          "name": "watchlist_id",
          "required": true,
          "schema": {
            "format": "uuid",
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