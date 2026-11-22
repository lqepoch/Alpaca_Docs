---
updatedAt: 2026-04-20T20:39:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Get An Account by ID

You can query a specific account that you submitted to Alpaca by passing into the query the account_id associated with the account you're retrieving.


# OpenAPI definition

````json
{
  "components": {
    "parameters": {
      "AccountID": {
        "description": "Account identifier.",
        "in": "path",
        "name": "account_id",
        "required": true,
        "schema": {
          "format": "uuid",
          "type": "string"
        }
      }
    },
    "schemas": {
      "AccountCashInterestProgram": {
        "properties": {
          "apr_tier_name": {
            "description": "The unique name of the APR tier for a specific program",
            "example": "gold",
            "type": "string"
          },
          "status": {
            "description": "The status of the account within a cash interest program. One of:\n- **ACTIVE**\nThe account is enrolled and eligible for idle cash to be swept at the end of day (EOD).\n- **INACTIVE**\nThe account is not enrolled due to it either not being eligible (e.g. the updated Alpaca Customer Agreement has not been signed), an APR tier needs to be assigned, or they have been unenrolled.\n- **PENDING_CHANGE**\nAn enrollment, APR Tier change, or unenrollment is in progress\n",
            "example": "ACTIVE",
            "type": "string"
          }
        },
        "type": "object"
      },
      "AccountCashInterestResponse": {
        "description": "The configuration and status of the account's USD cash interest program\n",
        "properties": {
          "USD": {
            "$ref": "#/components/schemas/AccountCashInterestProgram"
          }
        },
        "type": "object"
      },
      "AccountConfigurations": {
        "description": "Represents additional configuration settings for an account",
        "properties": {
          "disable_overnight_trading": {
            "description": "If true, overnight trading is disabled.",
            "type": "boolean"
          },
          "fractional_trading": {
            "description": "If true, account is able to participate in fractional trading",
            "type": "boolean"
          },
          "max_margin_multiplier": {
            "description": "Can be \"1\" or \"2\"",
            "type": "string"
          },
          "max_options_trading_level": {
            "description": "The desired maximum options trading level. 0=disabled, 1=Covered Call/Cash-Secured Put, 2=Long Call/Put, 3=Spreads/Straddles.",
            "enum": [
              0,
              1,
              2,
              3
            ],
            "type": "integer"
          },
          "no_shorting": {
            "description": "If true, account becomes long-only mode.",
            "type": "boolean"
          },
          "ptp_no_exception_entry": {
            "description": "If set to true then Alpaca will accept orders for PTP symbols with no exception. Default is false.",
            "type": "boolean"
          },
          "suspend_trade": {
            "description": "If true, new orders are blocked.",
            "type": "boolean"
          },
          "trade_confirm_email": {
            "description": "all or none. If none, emails for order fills are not sent.",
            "enum": [
              "all",
              "none"
            ],
            "type": "string"
          }
        },
        "title": "AccountConfigurations",
        "type": "object"
      },
      "AccountDRIPResponse": {
        "description": "This feature is available in sandbox for beta partners only.\n\nThe account's dividend reinvestment (DRIP) setting.\nThis field is returned only when DRIP was turned on for the account at least once.\n",
        "example": {
          "equities_dividend_reinvestments": true
        },
        "properties": {
          "equities_dividend_reinvestments": {
            "description": "If true, Alpaca reinvests eligible cash dividends on US equities in the same security.",
            "example": true,
            "type": "boolean"
          }
        },
        "required": [
          "equities_dividend_reinvestments"
        ],
        "type": "object"
      },
      "AccountExtended": {
        "description": "Represents an account with all data available. If your api response is missing some of these fields, there is a good chance you are using a route that returns `Account` instances instead of these.",
        "examples": [
          {
            "account_number": "601842165",
            "account_type": "trading",
            "agreements": [
              {
                "agreement": "margin_agreement",
                "ip_address": "127.0.0.1",
                "revision": "16.2021.05",
                "signed_at": "2022-01-21T21:25:26.579487214Z"
              },
              {
                "agreement": "customer_agreement",
                "ip_address": "127.0.0.1",
                "revision": "22.2024.08",
                "signed_at": "2022-01-21T21:25:26.579487214Z"
              }
            ],
            "beneficiaries": [
              {
                "date_of_birth": "1970-01-01",
                "family_name": "Smith",
                "given_name": "John",
                "middle_name": "P",
                "relationship": "spouse",
                "share_pct": "100",
                "tax_id": "xxx-xx-xxxx",
                "tax_id_type": "USA_SSN",
                "type": "primary"
              }
            ],
            "contact": {
              "city": "San Mateo",
              "country": "USA",
              "email_address": "strange_elbakyan_97324509@example.com",
              "phone_number": "614-555-0697",
              "postal_code": "94401",
              "state": "CA",
              "street_address": [
                "20 N San Mateo Dr"
              ]
            },
            "created_at": "2022-01-21T21:25:26.583576Z",
            "crypto_status": "INACTIVE",
            "currency": "USD",
            "disclosures": {
              "immediate_family_exposed": false,
              "is_affiliated_exchange_or_finra": false,
              "is_control_person": false,
              "is_discretionary": false,
              "is_politically_exposed": false
            },
            "documents": [
              {
                "content": "https://example.com/documents/identity-verification.jpg",
                "created_at": "2022-01-21T21:25:28.184231Z",
                "document_sub_type": "passport",
                "document_type": "identity_verification",
                "id": "d5af1585-6c60-494d-9ea5-c5df62704229"
              }
            ],
            "id": "3dcb795c-3ccc-402a-abb9-07e26a1b1326",
            "identity": {
              "country_of_birth": "USA",
              "country_of_citizenship": "USA",
              "country_of_tax_residence": "USA",
              "date_of_birth": "1970-01-01",
              "family_name": "Elbakyan",
              "funding_source": [
                "employment_income"
              ],
              "given_name": "Strange",
              "tax_id_type": "USA_SSN"
            },
            "last_equity": "40645.13",
            "primary_account_holder_id": null,
            "status": "ACTIVE",
            "trusted_contact": {
              "email_address": "strange_elbakyan_97324509@example.com",
              "family_name": "Doe",
              "given_name": "Jane"
            }
          }
        ],
        "properties": {
          "account_name": {
            "type": "string"
          },
          "account_number": {
            "type": [
              "string",
              "null"
            ]
          },
          "account_sub_type": {
            "$ref": "#/components/schemas/AccountSubType"
          },
          "account_type": {
            "$ref": "#/components/schemas/AccountType"
          },
          "agreements": {
            "items": {
              "$ref": "#/components/schemas/Agreement"
            },
            "type": "array"
          },
          "allow_instant_ach": {
            "description": "Determines whether the account is enabled for Instant ACH by the partner.",
            "type": "boolean"
          },
          "beneficiaries": {
            "items": {
              "$ref": "#/components/schemas/Beneficiary"
            },
            "type": "array"
          },
          "cash_interest": {
            "$ref": "#/components/schemas/AccountCashInterestResponse"
          },
          "contact": {
            "$ref": "#/components/schemas/Contact"
          },
          "created_at": {
            "format": "date-time",
            "type": "string"
          },
          "crypto_status": {
            "$ref": "#/components/schemas/AccountStatus"
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "custodial_account_type": {
            "$ref": "#/components/schemas/CustodialAccountType"
          },
          "disclosures": {
            "$ref": "#/components/schemas/Disclosures"
          },
          "documents": {
            "description": "The documents associated with the primary owner of the account",
            "items": {
              "$ref": "#/components/schemas/OwnerDocument"
            },
            "type": "array"
          },
          "drip": {
            "$ref": "#/components/schemas/AccountDRIPResponse"
          },
          "enabled_assets": {
            "items": {
              "$ref": "#/components/schemas/EnabledAssetClass"
            },
            "type": "array"
          },
          "fpsl": {
            "$ref": "#/components/schemas/AccountFPSLResponse"
          },
          "id": {
            "format": "uuid",
            "type": "string"
          },
          "identity": {
            "$ref": "#/components/schemas/Identity"
          },
          "instant_ach_blocked": {
            "description": "Indicates whether the account is blocked for Instant ACH by Alpaca. Defaults to false when the partner creates the account. If the partner has set allow_instant_ach to true but instant_ach_blocked is true, then the account is blocked for Instant ACH irrespective of the fact that the partner has it enabled.",
            "type": "boolean"
          },
          "investment_objective": {
            "description": "The user's investment objective. This field should be used instead of the deprecated `investment_objective` under identity.\n",
            "enum": [
              "generate_income",
              "preserve_wealth",
              "market_speculation",
              "growth",
              "balance_preserve_wealth_with_growth"
            ],
            "type": "string"
          },
          "investment_time_horizon": {
            "description": "The expected period of time the user plan to invest to achieve his/her financial goal(s). This field should be used instead of the deprecated `investment_time_horizon` under identity.\n",
            "enum": [
              "less_than_1_year",
              "1_to_2_years",
              "3_to_5_years",
              "6_to_10_years",
              "more_than_10_years"
            ],
            "type": "string"
          },
          "kyc_results": {
            "$ref": "#/components/schemas/KYCResults"
          },
          "last_equity": {
            "format": "decimal",
            "type": "string"
          },
          "liquidity_needs": {
            "description": "The user's ability to quickly and easily convert to cash all or a portion of the investments in this account without experiencing significant loss in value. This field should be used instead of the deprecated `liquidity_needs` under identity.\n",
            "enum": [
              "very_important",
              "important",
              "somewhat_important",
              "does_not_matter"
            ],
            "type": "string"
          },
          "minor_identity": {
            "$ref": "#/components/schemas/CustodialAccountMinorIdentity"
          },
          "primary_account_holder_id": {
            "description": "UUID of the account's primary holder when available; otherwise `null`.",
            "format": "uuid",
            "type": [
              "string",
              "null"
            ]
          },
          "risk_tolerance": {
            "description": "The user's investment risk tolerance. This field should be used instead of the deprecated `risk_tolerance` under identity.\n",
            "enum": [
              "conservative",
              "moderate",
              "significant_risk"
            ],
            "type": "string"
          },
          "status": {
            "$ref": "#/components/schemas/AccountStatus"
          },
          "trading_configurations": {
            "$ref": "#/components/schemas/AccountConfigurations"
          },
          "trusted_contact": {
            "$ref": "#/components/schemas/TrustedContact"
          },
          "usd": {
            "description": "values in USD. This is returned for LCT (non-USD) accounts only.",
            "properties": {
              "last_equity": {
                "example": "123.45",
                "format": "decimal",
                "type": "string"
              }
            },
            "type": "object"
          }
        },
        "required": [
          "id",
          "account_number",
          "status",
          "currency",
          "last_equity",
          "created_at",
          "account_type"
        ],
        "type": "object"
      },
      "AccountFPSLItem": {
        "properties": {
          "status": {
            "description": "The status of the account for this FPSL market. One of:\n- **ACTIVE**\nThe account is successfully enrolled for FPSL for this market.\n- **INACTIVE**\nThe account is not enrolled for FPSL for this market due to it either not being eligible, an FPSL tier has not been assigned, or it has been unenrolled.\n",
            "example": "ACTIVE",
            "type": "string"
          },
          "tier_id": {
            "description": "The id of the FPSL tier for this market",
            "example": "61e69015-8549-4bfd-b9c3-01e75843f47d",
            "format": "uuid",
            "type": "string"
          }
        },
        "type": "object"
      },
      "AccountFPSLResponse": {
        "description": "The account's Fully Paid Securities Lending (FPSL) configuration.\nThis is only returned for accounts that have FPSL enabled.\n",
        "properties": {
          "US": {
            "$ref": "#/components/schemas/AccountFPSLItem"
          }
        },
        "type": "object"
      },
      "AccountStatus": {
        "description": "Designates the current status of this account\n\nPossible Values:\n- **INACTIVE**\nAccount not set to trade given asset.\n- **PAPER_ONLY**\nThe account is limited to paper trading.\n- **ONBOARDING**\nAn application is expected for this user, but has not been submitted yet.\n- **SUBMITTED**\nThe application has been submitted and is being processed.\n- **SUBMISSION_FAILED**\nUsed to display if failure on submission\n- **ACTION_REQUIRED**\nThe application requires manual action.\n- **ACCOUNT_UPDATED**\nUsed to display when Account has been modified by user\n- **APPROVAL_PENDING**\nInitial value. The application approval process is in progress.\n- **APPROVED**\nThe account application has been approved, and waiting to be ACTIVE\n- **REJECTED**\nThe account application is rejected for some reason\n- **ACTIVE**\nThe account is fully active. Trading and funding are processed under this status.\n- **ACCOUNT_CLOSED**\nThe account is closed.\n",
        "enum": [
          "INACTIVE",
          "PAPER_ONLY",
          "ONBOARDING",
          "SUBMITTED",
          "SUBMISSION_FAILED",
          "ACTION_REQUIRED",
          "ACCOUNT_UPDATED",
          "APPROVAL_PENDING",
          "APPROVED",
          "REJECTED",
          "ACTIVE",
          "ACCOUNT_CLOSED"
        ],
        "example": "ACTIVE",
        "type": "string"
      },
      "AccountSubType": {
        "description": "IRA Account only\n\nPossible values are:\n\n- traditional\n- roth",
        "enum": [
          "traditional",
          "roth"
        ],
        "example": "traditional",
        "title": "AccountSubType",
        "type": "string"
      },
      "AccountType": {
        "description": "The account type returned for the account.",
        "enum": [
          "trading",
          "custodial",
          "donor_advised",
          "ira",
          "trust",
          "omnibus_non_disclosed",
          "omnibus_sub",
          "hsa",
          "joint"
        ],
        "example": "trading",
        "title": "AccountType",
        "type": "string"
      },
      "Agreement": {
        "properties": {
          "agreement": {
            "$ref": "#/components/schemas/AgreementType"
          },
          "ip_address": {
            "description": "The ip_address the signed agreements were sent from by the user.",
            "example": "185.13.21.99",
            "format": "ipv4",
            "type": "string"
          },
          "revision": {
            "description": "The agreement revision.\nThe format is XX.YYYY.MM where XX is an incrementing revision number, YYYY is the year and MM is the month.\nIf the revision is not specified in a POST or PATCH request, the active revision will be used, which will align with the [Alpaca Documents Library](https://alpaca.markets/disclosures).\n",
            "type": "string"
          },
          "signed_at": {
            "description": "The timestamp the agreement was signed.",
            "example": "2019-09-11T18:09:33Z",
            "format": "date-time",
            "type": "string"
          }
        },
        "required": [
          "agreement",
          "signed_at",
          "ip_address"
        ],
        "type": "object"
      },
      "AgreementType": {
        "description": "The type of agreement the customer signed.",
        "enum": [
          "margin_agreement",
          "account_agreement",
          "customer_agreement",
          "crypto_agreement",
          "options_agreement",
          "custodian_customer_agreement",
          "trusted_contact_consent",
          "master_securities_lending_agreement",
          "certifications_and_resolutions_statement",
          "joint_account_agreement",
          "foreign_markets_addendum"
        ],
        "example": "customer_agreement",
        "title": "AgreementType",
        "type": "string",
        "x-enumDescriptions": {
          "account_agreement": "Alpaca Account Agreement",
          "certifications_and_resolutions_statement": "Alpaca Certifications and Resolutions Statement",
          "crypto_agreement": "Alpaca Crypto Agreement",
          "custodian_customer_agreement": "Alpaca Custodial Customer Agreement (deprecated; use customer_agreement)",
          "customer_agreement": "Alpaca Customer Agreement",
          "foreign_markets_addendum": "Alpaca Foreign Markets / Global Equities Addendum",
          "joint_account_agreement": "Alpaca Joint Account Agreement",
          "margin_agreement": "Alpaca Margin Agreement",
          "master_securities_lending_agreement": "Alpaca Master Securities Lending Agreement",
          "options_agreement": "Alpaca Options Agreement",
          "trusted_contact_consent": "Alpaca Trusted Contact Consent"
        }
      },
      "Beneficiary": {
        "description": "Beneficiary of an IRA account. The same shape is used on account create, account update, and account responses.\n",
        "example": {
          "date_of_birth": "1970-01-01",
          "family_name": "Doe",
          "given_name": "Jane",
          "middle_name": null,
          "relationship": "spouse",
          "share_pct": "100",
          "tax_id": "xxx-xx-xxxx",
          "tax_id_type": "USA_SSN",
          "type": "primary"
        },
        "properties": {
          "date_of_birth": {
            "description": "Date of birth in YYYY-MM-DD format. It cannot be in the future.",
            "example": "1970-01-01",
            "format": "date",
            "type": "string"
          },
          "family_name": {
            "description": "Beneficiary family name.",
            "example": "Doe",
            "minLength": 1,
            "type": "string"
          },
          "given_name": {
            "description": "Beneficiary given name.",
            "example": "Jane",
            "minLength": 1,
            "type": "string"
          },
          "middle_name": {
            "description": "Beneficiary middle name. Omit this field or send null when the beneficiary has no middle name. An empty string is rejected. Account responses always include the field and use null when it is unset.\n",
            "example": "P",
            "minLength": 1,
            "type": [
              "string",
              "null"
            ]
          },
          "relationship": {
            "description": "Relationship of the beneficiary to the account holder.",
            "enum": [
              "spouse",
              "other"
            ],
            "example": "spouse",
            "type": "string"
          },
          "share_pct": {
            "description": "Share of the account allocated to this beneficiary, as a decimal string. The value must be greater than 0 and at most 100, with at most two decimal places.\n",
            "example": "100",
            "format": "decimal",
            "type": "string"
          },
          "tax_id": {
            "description": "Beneficiary tax identifier. Create and update requests require a USA SSN. Account responses always return the masked value `xxx-xx-xxxx`.\n",
            "example": "xxx-xx-xxxx",
            "minLength": 1,
            "type": "string"
          },
          "tax_id_type": {
            "description": "Tax identifier type.",
            "enum": [
              "USA_SSN"
            ],
            "example": "USA_SSN",
            "type": "string"
          },
          "type": {
            "description": "Whether this beneficiary is primary or contingent. An account with beneficiaries needs at least one primary beneficiary. The `share_pct` values of all primary beneficiaries must add up to 100, and the `share_pct` values of all contingent beneficiaries, if any, must also add up to 100.\n",
            "enum": [
              "primary",
              "contingent"
            ],
            "example": "primary",
            "type": "string"
          }
        },
        "required": [
          "given_name",
          "family_name",
          "date_of_birth",
          "tax_id",
          "tax_id_type",
          "relationship",
          "type",
          "share_pct"
        ],
        "type": "object"
      },
      "Contact": {
        "description": "Contact is the model for the account owner contact information.\n",
        "properties": {
          "city": {
            "example": "San Mateo",
            "type": "string"
          },
          "country": {
            "description": "country code in ISO 3166-1 alpha-3 format, representing the country the person/entity resides in.",
            "example": "USA",
            "type": "string"
          },
          "email_address": {
            "example": "john.doe@example.com",
            "format": "email",
            "type": "string"
          },
          "phone_number": {
            "description": "Phone number should include the country code, format: \"+15555555555\"",
            "example": "+15556667788",
            "type": [
              "string",
              "null"
            ]
          },
          "postal_code": {
            "example": "94401",
            "type": "string"
          },
          "state": {
            "description": "Required if the country or country_of_tax_residence (in the identity model below) is 'USA'.",
            "example": "CA",
            "type": "string"
          },
          "street_address": {
            "description": "The user's street address. If multiple lines in address, pass in as additional array elements. Maximum of 3 objects in array",
            "items": {
              "$ref": "#/components/schemas/StreetAddress"
            },
            "type": "array"
          },
          "unit": {
            "description": "The specific apartment number if applicable",
            "type": "string"
          }
        },
        "required": [
          "email_address",
          "street_address",
          "city"
        ],
        "type": "object"
      },
      "Currency": {
        "description": "\"USD\" // US Dollar\n\"JPY\" // Japanese Yen\n\"EUR\" // Euro\n\"CAD\" // Canadian Dollar\n\"GBP\" // British Pound Sterling\n\"CHF\" // Swiss Franc\n\"TRY\" // Turkish Lira\n\"AUD\" // Australian Dollar\n\"CZK\" // Czech Koruna\n\"SEK\" // Swedish Krona\n\"DKK\" // Danish Krone\n\"SGD\" // Singapore Dollar\n\"HKD\" // Hong Kong Dollar\n\"HUF\" // Hungarian Forint\n\"NZD\" // New Zealand Dollar\n\"NOK\" // Norwegian Krone\n\"PLN\" // Poland Złoty",
        "example": "USD",
        "title": "Currency",
        "type": "string"
      },
      "CustodialAccountMinorIdentity": {
        "description": "Represents Identity information for a minor that an account of type \"custodial\" is for",
        "properties": {
          "country_of_birth": {
            "type": "string"
          },
          "country_of_citizenship": {
            "type": "string"
          },
          "country_of_tax_residence": {
            "type": "string"
          },
          "date_of_birth": {
            "format": "date",
            "type": "string"
          },
          "email": {
            "format": "email",
            "type": "string"
          },
          "family_name": {
            "type": "string"
          },
          "given_name": {
            "type": "string"
          },
          "state": {
            "type": "string"
          },
          "tax_id": {
            "type": "string"
          },
          "tax_id_type": {
            "$ref": "#/components/schemas/TaxIdType"
          }
        },
        "required": [
          "given_name",
          "family_name",
          "date_of_birth",
          "tax_id_type",
          "country_of_tax_residence",
          "state",
          "email"
        ],
        "type": "object"
      },
      "CustodialAccountType": {
        "description": "Represents the type of custodial account based on the state where the beneficiary resides.\nThis value is returned only when the `country_of_tax_residence` is `USA`. For other countries, this property is not included in the response.\n\n**Possible Return Values**\n\n`CustodianTypeUTMA` - Indicates that the custodial account is governed by the Uniform Transfers to Minors Act.\n`CustodianTypeUGMA` - Indicates that the custodial account is governed by the Uniform Gifts to Minors Act.",
        "title": "CustodialAccountType",
        "type": "string"
      },
      "DisclosureContextAnnotation": {
        "properties": {
          "company_city": {
            "description": "Required for FINRA affiliations and controlled firms.",
            "type": "string"
          },
          "company_compliance_email": {
            "description": "Required for FINRA affiliations and controlled firms.",
            "type": "string"
          },
          "company_country": {
            "description": "Required for FINRA affiliations and controlled firms.",
            "type": "string"
          },
          "company_name": {
            "description": "Required for FINRA affiliations and controlled firms.",
            "type": "string"
          },
          "company_state": {
            "description": "Required if and only if `company_country` is `USA`.",
            "type": "string"
          },
          "company_street_address": {
            "description": "Required for FINRA affiliations and controlled firms.",
            "type": "string"
          },
          "context_type": {
            "description": "Specifies the type of disclosure annotation. Valid types are FINRA affiliations, for users affiliated with or employed by a FINRA member firm, a Stock Exchange Member, FINRA, Registered Investment Advisor, or a Municipal Securities Broker/Dealer; Company control relationships, for senior executives, and 10% or greater shareholders, of a publicly traded company; and immediate family members of politically exposed individuals.",
            "enum": [
              "CONTROLLED_FIRM",
              "IMMEDIATE_FAMILY_EXPOSED",
              "AFFILIATE_FIRM"
            ],
            "type": "string"
          },
          "family_name": {
            "description": "Required for immediate family members of politically exposed persons.",
            "type": "string"
          },
          "given_name": {
            "description": "Required for immediate family members of politically exposed persons.",
            "type": "string"
          }
        },
        "required": [
          "context_type"
        ],
        "title": "DisclosureContextAnnotation",
        "type": "object"
      },
      "Disclosures": {
        "description": "Disclosures fields denote if the account owner falls under\neach category defined by FINRA rule. The client has to ask\nquestions for the end user and the values should reflect\ntheir answers.\nIf one of the answers is true (yes), the account goes into\nACTION_REQUIRED status.\n",
        "example": {
          "immediate_family_exposed": false,
          "is_affiliated_exchange_or_finra": false,
          "is_control_person": false,
          "is_politically_exposed": false
        },
        "properties": {
          "context": {
            "description": "Array of annotations describing the rationale for marking `is_control_person`, `is_affiliated_exchange_or_finra`, and/or `immediate_family_exposed` as true",
            "items": {
              "$ref": "#/components/schemas/DisclosureContextAnnotation"
            },
            "type": [
              "array",
              "null"
            ]
          },
          "employer_address": {
            "description": "The employer's address if the user is employed.",
            "type": "string"
          },
          "employer_name": {
            "description": "The name of the employer if the user is employed.",
            "type": "string"
          },
          "employment_position": {
            "description": "The user's position if they are employed.",
            "type": "string"
          },
          "employment_sector": {
            "description": "The industry sector of employment.\nIf the `employment_status` is `unemployed` or `student`, set this property to `not_employed`.\nIf the `employment_status` is `retired`, set this to `self_employed`.\n",
            "enum": [
              "agriculture",
              "business_management",
              "computers_and_it",
              "construction",
              "education",
              "finance",
              "government",
              "healthcare",
              "hospitality",
              "manufacturing",
              "marketing",
              "media",
              "other",
              "science",
              "self_employed",
              "transportation",
              "not_employed"
            ],
            "type": "string"
          },
          "employment_status": {
            "description": "One of the following: `employed`, `unemployed`, `retired`, or `student`.",
            "enum": [
              "unemployed",
              "employed",
              "student",
              "retired"
            ],
            "type": "string"
          },
          "immediate_family_exposed": {
            "description": "If your user's immediate family member (sibling, husband/wife, child, parent) is either politically exposed or holds a control position.",
            "type": "boolean"
          },
          "is_affiliated_exchange_or_finra": {
            "description": "Whether user is affiliated with any exchanges or FINRA.",
            "type": "boolean"
          },
          "is_control_person": {
            "description": "Whether user holds a controlling position in a publicly traded company, member of the board of directors or has policy making abilities in a publicly traded company.",
            "type": "boolean"
          },
          "is_politically_exposed": {
            "description": "Whether the user is politically exposed.",
            "type": "boolean"
          }
        },
        "required": [
          "is_control_person",
          "is_affiliated_exchange_or_finra",
          "is_politically_exposed",
          "immediate_family_exposed"
        ],
        "type": "object"
      },
      "EnabledAssetClass": {
        "description": "An asset class that can be enabled on a brokerage account, i.e. a value that may appear in an account's `enabled_assets`. This differs from `AssetClass` (which also covers order and asset metadata) by excluding `ipo`, which is not an enable-able asset.",
        "enum": [
          "us_equity",
          "us_option",
          "crypto"
        ],
        "type": "string"
      },
      "Identification": {
        "description": "An identity document or identifier of the account owner. Responses return only `type`.",
        "example": {
          "issued_country": "GBR",
          "number": "5493001KJTIIGC8Y1R12",
          "type": "LEI"
        },
        "properties": {
          "expiry_date": {
            "description": "The expiry date in \"YYYY-MM-DD\" format. It must be later than today (UTC) and no earlier than `issued_date`.",
            "example": "2030-01-01",
            "format": "date",
            "type": "string",
            "writeOnly": true
          },
          "issued_country": {
            "description": "Required on write. [ISO 3166-1 alpha-3](https://www.iso.org/iso-3166-country-codes.html) code of the issuing country.\n",
            "example": "GBR",
            "type": "string",
            "writeOnly": true
          },
          "issued_date": {
            "description": "The issue date in \"YYYY-MM-DD\" format. It can't be later than today (UTC).",
            "example": "2020-01-01",
            "format": "date",
            "type": "string",
            "writeOnly": true
          },
          "number": {
            "description": "Required on write. The identification number. An `LEI` number is 20 characters long and must pass the ISO 17442 check digits, or the request fails with 422. Lowercase letters are accepted and stored in uppercase.\n",
            "example": "5493001KJTIIGC8Y1R12",
            "type": "string",
            "writeOnly": true
          },
          "type": {
            "description": "The identification type, for example `passport`, `national_id` or `LEI`. `LEI` is uppercase.",
            "example": "LEI",
            "type": "string"
          }
        },
        "required": [
          "type"
        ],
        "type": "object"
      },
      "Identity": {
        "description": "Identity is the model to provide account owner's identity information.\n",
        "example": {
          "country_of_birth": "AUS",
          "country_of_citizenship": "AUS",
          "country_of_tax_residence": "USA",
          "date_of_birth": "1990-01-01",
          "family_name": "Doe",
          "funding_source": [
            "employment_income"
          ],
          "given_name": "John",
          "tax_id": "666-55-4321",
          "tax_id_type": "USA_SSN"
        },
        "properties": {
          "annual_income_max": {
            "description": "The upper bound of the user's annual income.",
            "example": "100000",
            "format": "decimal",
            "type": "string"
          },
          "annual_income_min": {
            "description": "The lower bound of the user's annual income.",
            "example": "50000",
            "format": "decimal",
            "type": "string"
          },
          "country_of_birth": {
            "description": "[ISO 3166-1 alpha-3](https://www.iso.org/iso-3166-country-codes.html).\n",
            "example": "USA",
            "type": "string"
          },
          "country_of_citizenship": {
            "description": "[ISO 3166-1 alpha-3](https://www.iso.org/iso-3166-country-codes.html).\n",
            "example": "USA",
            "type": "string"
          },
          "country_of_tax_residence": {
            "description": "[ISO 3166-1 alpha-3](https://www.iso.org/iso-3166-country-codes.html).\n",
            "example": "USA",
            "type": "string"
          },
          "date_of_birth": {
            "description": "The date of birth in \"YYYY-MM-DD\" format.",
            "example": "1990-01-01",
            "format": "date",
            "type": "string"
          },
          "date_of_departure_from_usa": {
            "description": "Required if `visa_type` = B1 or B2",
            "format": "date",
            "type": "string"
          },
          "family_name": {
            "description": "The last name (surname) of the user.",
            "example": "Doe",
            "type": "string"
          },
          "funding_source": {
            "description": "Can be one or more of the following: `employment_income`, `investments`, `inheritance`, `business_income`, `savings`, `family`.",
            "items": {
              "enum": [
                "employment_income",
                "investments",
                "inheritance",
                "business_income",
                "savings",
                "family"
              ],
              "type": "string"
            },
            "type": "array"
          },
          "given_name": {
            "description": "The first/given name of the user.",
            "example": "John",
            "type": "string"
          },
          "identifications": {
            "description": "Identity documents and identifiers other than the tax ID, such as a passport or an LEI. On update, the array replaces every stored identification except the tax ID, which only `tax_id` and `tax_id_type` change.\n\nAccount responses include this field only for natural persons, and each entry has only `type`. Responses also list the tax ID as an entry typed with its tax ID type, for example `USA_SSN`, or `NOT_SPECIFIED` when the type is unknown. Omit that entry on update.\n",
            "items": {
              "$ref": "#/components/schemas/Identification"
            },
            "type": "array"
          },
          "investment_experience_with_options": {
            "description": "The user's level of expertise and familiarity with investing in Options.\n",
            "enum": [
              "none",
              "1_to_5_years",
              "over_5_years"
            ],
            "type": "string"
          },
          "investment_experience_with_stocks": {
            "description": "The user's level of expertise and familiarity with investing in US Equities.\n",
            "enum": [
              "none",
              "1_to_5_years",
              "over_5_years"
            ],
            "type": "string"
          },
          "investment_objective": {
            "deprecated": true,
            "description": "The user's investment objective. This field is deprecated. Please use the top level `investment_objective` field.\n",
            "enum": [
              "generate_income",
              "preserve_wealth",
              "market_speculation",
              "growth",
              "balance_preserve_wealth_with_growth"
            ],
            "type": "string"
          },
          "investment_time_horizon": {
            "deprecated": true,
            "description": "The expected period of time the user plan to invest to achieve his/her financial goal(s). This field is deprecated. Please use the top level `investment_time_horizon` field.\n",
            "enum": [
              "less_than_1_year",
              "1_to_2_years",
              "3_to_5_years",
              "6_to_10_years",
              "more_than_10_years"
            ],
            "type": "string"
          },
          "liquid_net_worth_max": {
            "description": "The upper bound of the user's liquid net worth.",
            "example": "500000",
            "format": "decimal",
            "type": "string"
          },
          "liquid_net_worth_min": {
            "description": "The lower bound of the user's liquid net worth.",
            "example": "100000",
            "format": "decimal",
            "type": "string"
          },
          "liquidity_needs": {
            "deprecated": true,
            "description": "The user's ability to quickly and easily convert all or part of their investments in this account to cash without significant loss in value. This field is deprecated. Please use the top level `liquidity_needs` field.\n",
            "enum": [
              "very_important",
              "important",
              "somewhat_important",
              "does_not_matter"
            ],
            "type": "string"
          },
          "marital_status": {
            "description": "The marital status of the user.\n",
            "enum": [
              "SINGLE",
              "MARRIED",
              "DIVORCED",
              "WIDOWED"
            ],
            "type": "string"
          },
          "middle_name": {
            "description": "The middle name of the user.",
            "type": "string"
          },
          "number_of_dependents": {
            "description": "The number of dependents the user has.\n",
            "type": "integer"
          },
          "permanent_resident": {
            "description": "Only used to collect permanent residence status in the USA.",
            "type": "boolean"
          },
          "risk_tolerance": {
            "deprecated": true,
            "description": "The user's investment risk tolerance. This field is deprecated. Please use the top level `risk_tolerance` field.\n",
            "enum": [
              "conservative",
              "moderate",
              "significant_risk"
            ],
            "type": "string"
          },
          "tax_id": {
            "description": "If this is provided, `tax_id_type` is required.",
            "example": "666-55-4321",
            "type": "string"
          },
          "tax_id_type": {
            "description": "Required on write when `tax_id` is set. May be `null` on read when unset or for sparse identity on OmniSub / omnibus-non-disclosed accounts.\n\nAn LEI is not a tax ID: a request with `tax_id_type` set to `LEI`, in any case, fails with 422. Send the LEI in `identifications` and the national tax ID in `tax_id`.\n",
            "oneOf": [
              {
                "$ref": "#/components/schemas/TaxIdType"
              },
              {
                "type": "null"
              }
            ]
          },
          "total_net_worth_max": {
            "description": "The upper bound of the user's total net worth.",
            "example": "1000000",
            "format": "decimal",
            "type": "string"
          },
          "total_net_worth_min": {
            "description": "The lower bound of the user's total net worth.",
            "example": "100000",
            "format": "decimal",
            "type": "string"
          },
          "visa_expiration_date": {
            "description": "Required if `visa_type` is set.",
            "format": "date",
            "type": "string"
          },
          "visa_type": {
            "description": "Only used to collect visa types for users residing in the USA.",
            "type": "string"
          }
        },
        "required": [
          "given_name",
          "family_name",
          "date_of_birth",
          "country_of_tax_residence",
          "funding_source"
        ],
        "type": "object"
      },
      "KYCResultType": {
        "description": "A KYC reason identifier used as a property name in `KYCResultTypeSet`. The set is extensible, so integrations must tolerate and preserve unrecognized values.",
        "examples": [
          "IDENTITY_VERIFICATION",
          "compromised_document"
        ],
        "title": "KYCResultType",
        "type": "string"
      },
      "KYCResultTypeSet": {
        "additionalProperties": {
          "maxProperties": 0,
          "type": "object"
        },
        "description": "A nullable set of KYC reason identifiers represented as property names with empty object values. See `KYCResults` for documented identifiers and interpretation guidance.",
        "examples": [
          null,
          {},
          {
            "IDENTITY_VERIFICATION": {},
            "WATCHLIST_HIT": {}
          }
        ],
        "propertyNames": {
          "$ref": "#/components/schemas/KYCResultType"
        },
        "title": "KYCResultTypeSet",
        "type": [
          "object",
          "null"
        ]
      },
      "KYCResults": {
        "description": "Holds information about the result of KYC.\n\n`accept`, `indeterminate`, and `reject` are nullable sets represented as objects. Each property name is a KYC reason identifier, and every property value is always an empty object (`{}`) carrying no nested data. For example:\n\n```json\n{\n  \"IDENTITY_VERIFICATION\": {},\n  \"WATCHLIST_HIT\": {}\n}\n```\n\nInterpret each reason together with its enclosing result category and `additional_information`.\n\nDocumented reason identifiers:\n- `IDENTITY_VERIFICATION`: A government-issued identity document is required to verify the account owner's identity.\n- `TAX_IDENTIFICATION`: A tax identification document is required to verify the account owner's tax identification number.\n- `ADDRESS_VERIFICATION`: Additional documentation, such as a government-issued ID or statement, may be required to verify the account owner's residential address.\n- `DATE_OF_BIRTH`: A government-issued identity document is required to verify the account owner's date of birth.\n- `SELFIE_VERIFICATION`: A live selfie of the account owner is required to verify identity.\n- `PEP`: The account owner disclosed politically exposed person status, and additional information may be required.\n- `FAMILY_MEMBER_PEP`: The account owner disclosed that an immediate family member is politically exposed, and additional information may be required.\n- `CONTROL_PERSON`: Additional company information may be required because the account owner disclosed a control position.\n- `AFFILIATED`: Additional firm information may be required because the account owner disclosed an affiliation with FINRA or an exchange.\n- `VISA_TYPE_OTHER`: The account owner's visa type and expiration date may be required because the submitted visa type was \"other.\"\n- `W8BEN_CORRECTION`: A new W-8BEN with corrected identifying information is required.\n- `COUNTRY_NOT_SUPPORTED`: The account owner's country of tax residence or legal residence is not supported for this account.\n- `WATCHLIST_HIT`: Watchlist screening returned a result that requires further review; no action is needed from the account owner unless separately requested.\n- `OTHER`: See `additional_information` for a custom message describing what is required from the account owner.\n- `OTHER_PARTNER`: See `additional_information` for a custom message intended for the Broker API partner.\n- `CITIZENSHIP_COUNTRY_NOT_SUPPORTED`: The account owner's country of citizenship is not supported for this account.\n- `DIFFERING_COUNTRY`: A submitted identity document was issued by a country different from the account owner's country of tax residence.\n- `WL_PEP_SCREENING`: Watchlist screening returned a result related to possible political exposure.\n- `WL_LEGAL_REGULATORY_WARNING`: Watchlist screening returned a legal or regulatory warning result.\n- `UNDER_MINIMUM_AGE`: The account owner does not meet the minimum age requirement for this account.\n- `PEP_FOREIGN`: The account owner disclosed foreign politically exposed person status, and additional information may be required.\n- `FAMILY_MEMBER_PEP_FOREIGN`: The account owner disclosed that an immediate family member has foreign politically exposed person status, and additional information may be required.\n- `DISCRETIONARY`: The account is designated for discretionary trading by a registered investment adviser and requires review.\n- `HIO`: Additional information and a declaration form may be required because the account owner disclosed being the head of an international organization.\n- `INTERNAL_CHECK`: A non-specific account-opening check contributed to the KYC outcome; no more specific reason is available.\n- `compromised_document`: The identity document check indicated that the document may be compromised.\n- `data_comparison`: Data extracted from the identity document did not pass comparison checks and requires review.\n- `image_integrity`: A document or selfie image did not pass image-integrity checks and requires review.\n\nThe set of reason identifiers is extensible, so integrations must tolerate and preserve unrecognized values.\n",
        "properties": {
          "accept": {
            "$ref": "#/components/schemas/KYCResultTypeSet"
          },
          "additional_information": {
            "description": "Used to display a custom message.",
            "type": "string"
          },
          "indeterminate": {
            "$ref": "#/components/schemas/KYCResultTypeSet"
          },
          "reject": {
            "$ref": "#/components/schemas/KYCResultTypeSet"
          },
          "summary": {
            "description": "Either `pass` or `fail`. Used to indicate if KYC has completed and passed or not. This field is used for internal purposes only.",
            "type": "string"
          }
        },
        "type": [
          "object",
          "null"
        ]
      },
      "OwnerDocument": {
        "description": "A document associated with an owner of the account",
        "example": {
          "created_at": "2019-09-30T23:55:31.185998Z",
          "document_sub_type": "passport",
          "document_type": "identity_verification",
          "id": "0d18ae51-3c94-4511-b209-101e1666416b",
          "mime_type": "image/jpeg"
        },
        "properties": {
          "created_at": {
            "format": "date-time",
            "type": "string"
          },
          "document_sub_type": {
            "description": "The sub-type of the document. This is a free-form property.",
            "type": "string"
          },
          "document_type": {
            "$ref": "#/components/schemas/OwnerDocumentType"
          },
          "id": {
            "format": "uuid",
            "type": "string"
          },
          "mime_type": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "document_type",
          "created_at"
        ],
        "type": "object"
      },
      "OwnerDocumentType": {
        "description": "The type of the owner document",
        "enum": [
          "account_approval_letter",
          "address_verification",
          "cip_result",
          "company_formation",
          "date_of_birth_verification",
          "entity_operating_document",
          "entity_registration",
          "hio_declaration_form",
          "identity_verification",
          "limited_trading_authorization",
          "pep_declaration_form",
          "tax_id_verification",
          "w8ben",
          "w9"
        ],
        "example": "identity_verification",
        "type": "string"
      },
      "StreetAddress": {
        "example": "20 N San Mateo Dr",
        "type": "string"
      },
      "TaxIdType": {
        "description": "The type of the tax ID or other government-issued identification number.\n\nEach country-specific type is meant for accounts whose `country_of_tax_residence` is the country it is named after, and some are also meant for that country's associated jurisdictions, such as its territories. For correspondents with strict tax ID validation, the type must match `country_of_tax_residence` and be supported in the account's booking center, so a listed type can still be rejected when the account is validated. The \"for individuals\" and \"for entities\" notes describe who each type is typically issued to, and aren't checked when the account is validated.\n\nPossible values are:\n\n- **USA_SSN**: USA SSN (Social Security Number), for individuals\n- **USA_EIN**: USA EIN (Employer Identification Number), for entities\n- **USA_ITIN**: USA ITIN (Individual Taxpayer Identification Number), for individuals\n- **USA_TIN**: USA TIN (Taxpayer Identification Number), for entities\n- **ABW_PN**: Aruba Persoonsnummer (Aruba TIN), for individuals and entities\n- **AGO_NIF**: Angola NIF (Número de Identificação Fiscal), for individuals and entities\n- **ALB_NIPT**: Albania NIPT (Numri i Identifikimit të Personit të Tatueshëm), for individuals and entities\n- **AND_NRT**: Andorra NRT (Número de Registre Tributari), for individuals and entities\n- **ARE_EID**: UAE Emirates ID, for individuals\n- **ARE_TRN**: UAE TRN (Tax Registration Number), for entities\n- **ARG_AG_CUIT**: Legacy value for an Argentina CUIT. Use `ARG_AR_CUIT` instead.\n- **ARG_AR_CUIT**: Argentina CUIT (Clave Única de Identificación Tributaria), for individuals and entities\n- **ARM_SSN**: Armenia SSN (Social Security Number), for individuals\n- **ARM_TIN**: Armenia TIN (Tax Identification Number), for entities\n- **AUS_ABN**: Australia ABN (Australian business number), for entities\n- **AUS_TFN**: Australia TFN (Tax File Number), for individuals and entities\n- **AUT_UID**: Austria UID-Nummer (VAT Identification Number), for entities\n- **AUT_VNR**: Austria Versicherungsnummer (Social Insurance Number), for individuals\n- **AZE_FIN**: Azerbaijan FIN (Fərdi İdentifikasiya Nömrəsi), for individuals\n- **AZE_VOEN**: Azerbaijan VÖEN (Tax Identification Number), for entities\n- **BEL_BCE**: Belgium BCE/KBO (Enterprise Number), for entities\n- **BEL_NN**: Belgium NN (Numéro National / Rijksregisternummer), for individuals\n- **BEN_IFU**: Benin IFU (Identifiant Fiscal Unique), for individuals and entities\n- **BFA_IFU**: Burkina Faso IFU (Identifiant Financier Unique), for individuals and entities\n- **BGD_TIN**: Bangladesh TIN (Tax Identification Number), for individuals and entities\n- **BGR_EGN**: Bulgaria EGN (Edinen Grazhdanski Nomer), for individuals\n- **BGR_EIK**: Bulgaria EIK/BULSTAT (Entity Identification Code), for entities\n- **BHR_CPR**: Bahrain CPR (Central Population Registry), for individuals\n- **BIH_JMBG**: Bosnia and Herzegovina JMBG (Jedinstveni Matični Broj Građana), for individuals\n- **BLR_ID**: Belarus Personal Identification Number, for individuals\n- **BLR_UNP**: Belarus UNP (Uchyotny Nomer Platelshchika), for entities\n- **BLZ_TIN**: Belize TIN (Tax Identification Number), for individuals and entities\n- **BOL_NIT**: Bolivia NIT (Número de Identificación Tributaria), for individuals and entities\n- **BRA_CNPJ**: Brazil CNPJ (Cadastro Nacional da Pessoa Jurídica), for entities\n- **BRA_CPF**: Brazil CPF (Cadastro de Pessoas Físicas), for individuals\n- **BRB_TIN**: Barbados TIN (Tax Identification Number), for individuals and entities\n- **BTN_TPN**: Bhutan TPN (Taxpayer Number), for individuals and entities\n- **BWA_TIN**: Botswana TIN (Tax Identification Number), for individuals and entities\n- **CAN_BN**: Canada BN (Business Number), for entities\n- **CAN_SIN**: Canada SIN (Social Insurance Number), for individuals\n- **CHE_AHV**: Switzerland AHV/AVS (Social Insurance Number), for individuals\n- **CHE_UID**: Switzerland UID (Unternehmens-Identifikationsnummer), for entities\n- **CHL_RUT**: Chile RUT (Rol Único Tributario), for individuals and entities\n- **CHN_RID**: China Resident Identity Card Number (居民身份证号码), for individuals\n- **CHN_USCC**: China USCC (Unified Social Credit Code / 统一社会信用代码), for entities\n- **CIV_NCC**: Côte d'Ivoire NCC (Numéro de Compte Contribuable), for individuals and entities\n- **CMR_NIU**: Cameroon NIU (Numéro d'Identifiant Unique), for individuals and entities\n- **COK_RMD**: Cook Islands RMD Number (Revenue Management Division), for individuals and entities\n- **COL_CC**: Colombia CC (Cédula de Ciudadanía), for individuals\n- **COL_CE**: Colombia CE (Cédula de Extranjería), for individuals\n- **COL_NIT**: Colombia NIT (Número de Identificación Tributaria), for individuals and entities\n- **COL_NUIP**: Colombia NUIP (Número Único de Identificación Personal), for individuals\n- **COL_PPT**: Colombia PPT (Permiso por Protección Temporal), for individuals\n- **CPV_NIF**: Cabo Verde NIF (Número de Identificação Fiscal), for individuals and entities\n- **CRI_CJ**: Costa Rica Cédula Jurídica (Legal Entity ID), for entities\n- **CRI_DIMEX**: Costa Rica DIMEX (Documento de Identificación Migratorio para Extranjeros), for individuals\n- **CRI_NITE**: Costa Rica NITE (Número de Identificación Tributaria Especial), for individuals and entities\n- **CRI_PIN**: Costa Rica Personal Identification Number (PIN), for individuals\n- **CUW_CRIB**: Curaçao CRIB (Centraal Registratie Informatie Belastingplichtige), for individuals and entities\n- **CYP_TIC**: Cyprus TIC (Tax Identification Code), for individuals and entities\n- **CZE_TIN**: Czech Republic TIN (Tax Identification Number), for individuals and entities\n- **DEU_TAX_ID**: Germany Tax ID (Identifikationsnummer), for individuals\n- **DEU_UST_ID**: Germany USt-IdNr (Umsatzsteuer-Identifikationsnummer), for entities\n- **DNK_CPR**: Denmark CPR-nummer (Det Centrale Personregister), for individuals\n- **DNK_CVR**: Denmark CVR-nummer (Det Centrale Virksomhedsregister), for entities\n- **DOM_CED**: Dominican Republic Cédula de Identidad y Electoral, for individuals\n- **DOM_RNC**: Dominican Republic RNC (Registro Nacional del Contribuyente), for entities\n- **DZA_NIF**: Algeria NIF (Numéro d'Identification Fiscale), for individuals and entities\n- **ECU_RUC**: Ecuador RUC (Registro Unico de Contribuyentes), for individuals and entities\n- **EGY_NID**: Egypt National ID Number, for individuals\n- **EGY_TRN**: Egypt Tax Registration Number, for entities\n- **ESP_DNI**: Spain DNI (Documento Nacional de Identidad), for individuals\n- **ESP_NIE**: Spain NIE (Número de Identidad de Extranjero), for individuals\n- **ESP_NIF**: Spain NIF (Número de Identificación Fiscal), for individuals and entities\n- **EST_IK**: Estonia Isikukood (Personal Identification Code), for individuals\n- **EST_RC**: Estonia Registrikood (Registry Code), for entities\n- **ETH_TIN**: Ethiopia TIN (Tax Identification Number), for individuals and entities\n- **FIN_HETU**: Finland HETU (Henkilötunnus), for individuals\n- **FIN_YTU**: Finland Y-tunnus (Business ID), for entities\n- **FJI_TIN**: Fiji TIN (Tax Identification Number), for individuals and entities\n- **FRA_SIREN**: France SIREN (Business tax ID), for entities\n- **FRA_SPI**: France SPI (Reference tax number), for individuals\n- **GAB_NIF**: Gabon NIF (Numéro d'Identification Fiscale), for individuals and entities\n- **GBR_CRN**: UK CRN (Companies House Registration Number), for entities\n- **GBR_NINO**: UK NINO (National Insurance Number), for individuals\n- **GBR_UTR**: UK UTR (Unique Taxpayer Reference), for individuals and entities\n- **GEO_PID**: Georgia Personal Identification Number, for individuals\n- **GEO_TIN**: Georgia TIN (Tax Identification Number), for entities\n- **GHA_TIN**: Ghana TIN (Tax Identification Number), for individuals and entities\n- **GRC_AFM**: Greece AFM (Arithmos Forologikou Mitroou), for individuals and entities\n- **GTM_NIT**: Guatemala NIT (Número de Identificación Tributaria), for individuals and entities\n- **HKG_BRN**: Hong Kong BRN (Business Registration Number), for entities\n- **HKG_HKID**: Hong Kong HKID (Hong Kong Identity Card), for individuals\n- **HND_RTN**: Honduras RTN (Registro Tributario Nacional), for individuals and entities\n- **HRV_OIB**: Croatia OIB (Osobni Identifikacijski Broj), for individuals\n- **HTI_NIF**: Haiti NIF (Numéro d'Identification Fiscale), for individuals and entities\n- **HUN_ENT**: Hungary Adószám (Entity Tax Number), for entities\n- **HUN_TIN**: Hungary TIN (Tax Identification Number), for individuals\n- **IDN_KTP**: Indonesia KTP (Indonesian Identity Card), for individuals\n- **IDN_NWPW**: Indonesia NPWP (Nomor Pokok Wajib Pajak), for individuals and entities. The code is spelled `IDN_NWPW`, not `IDN_NPWP`.\n- **IND_GSTIN**: India GSTIN (Goods and Services Tax Identification Number), for entities\n- **IND_PAN**: India PAN (Permanent Account Number), for individuals\n- **IRL_CRO**: Ireland CRO (Companies Registration Office Number), for entities\n- **IRL_PPS**: Ireland PPS (Personal Public Service Number), for individuals\n- **IRN_NID**: Iran National ID (Kode Melli), for individuals\n- **ISL_KT**: Iceland Kennitala (National Identification Number), for individuals\n- **ISR_CORP**: Israel Company Number (Mispar Chevra), for entities\n- **ISR_TAX_ID**: Israel Tax ID (Teudat Zehut), for individuals\n- **ITA_PIVA**: Italy Partita IVA (VAT Number), for entities\n- **ITA_TAX_ID**: Italy Tax ID (Codice fiscale), for individuals\n- **JAM_TRN**: Jamaica TRN (Taxpayer Registration Number), for individuals and entities\n- **JOR_NID**: Jordan National ID Number, for individuals\n- **JPN_CORP**: Japan Corporate Number (法人番号), for entities\n- **JPN_TAX_ID**: Japan Tax ID (kojin bango), for individuals\n- **KAZ_BIN**: Kazakhstan BIN (Business Identification Number), for entities\n- **KAZ_IIN**: Kazakhstan IIN (Individual Identification Number), for individuals\n- **KEN_KRA_PIN**: Kenya KRA PIN (Kenya Revenue Authority PIN), for individuals and entities\n- **KGZ_INN**: Kyrgyzstan INN (Individual Tax Number), for individuals\n- **KHM_NID**: Cambodia National ID Number, for individuals\n- **KOR_BRN**: South Korea BRN (Business Registration Number), for entities\n- **KOR_RRN**: South Korea RRN (Resident Registration Number), for individuals\n- **KWT_CID**: Kuwait Civil ID Number, for individuals\n- **LBN_TIN**: Lebanon TIN (Tax Identification Number), for individuals and entities\n- **LKA_NIC**: Sri Lanka NIC (National Identity Card), for individuals\n- **LKA_TIN**: Sri Lanka TIN (Tax Identification Number), for entities\n- **LTU_AK**: Lithuania Asmens Kodas (Personal Code), for individuals\n- **LTU_JAK**: Lithuania Juridinio Asmens Kodas (Legal Entity Code), for entities\n- **LUX_NIN**: Luxembourg Matricule (National Identification Number), for individuals\n- **LUX_TVA**: Luxembourg Numéro TVA (VAT Number), for entities\n- **LVA_PK**: Latvia Personas Kods (Personal Code), for individuals\n- **LVA_REG**: Latvia Reģistrācijas Numurs (Registration Number), for entities\n- **MAC_TIN**: Macao Taxpayer Number, for individuals and entities\n- **MAR_CIN**: Morocco CIN (Carte d'Identité Nationale), for individuals\n- **MAR_ICE**: Morocco ICE (Identifiant Commun de l'Entreprise), for entities\n- **MDA_IDNO**: Moldova IDNO (State Identification Number of Entity), for entities\n- **MDA_IDNP**: Moldova IDNP (Personal Identification Number), for individuals\n- **MEX_CURP**: Mexico CURP (Clave Única de Registro de Población), for individuals\n- **MEX_RFC**: Mexico RFC (Registro Federal de Contribuyentes), for individuals and entities\n- **MKD_EDB**: North Macedonia EDB (Unique Tax Number), for entities\n- **MKD_EMBG**: North Macedonia EMBG (Unique Master Citizen Number), for individuals\n- **MLI_NIF**: Mali NIF (Numéro d'Identification Fiscale), for individuals and entities\n- **MLT_ID**: Malta Identity Card Number, for individuals\n- **MLT_VAT**: Malta VAT Number, for entities\n- **MNE_JMBG**: Montenegro Unique Master Citizen Number, for individuals\n- **MNE_PIB**: Montenegro PIB (Tax Identification Number), for entities\n- **MNG_RD**: Mongolia Register Number, for individuals\n- **MOZ_NUIT**: Mozambique NUIT (Tax Identification Number), for individuals and entities\n- **MUS_NID**: Mauritius National Identity Card Number, for individuals\n- **MUS_TAN_ENT**: Mauritius TAN (Entity Tax Account Number), for entities\n- **MUS_TAN_IND**: Mauritius TAN (Individual Tax Account Number), for individuals\n- **MWI_TPIN**: Malawi TPIN (Taxpayer Identification Number), for individuals and entities\n- **MYS_MYKAD**: Malaysia MyKad (National Registration Identity Card), for individuals\n- **MYS_ROC**: Malaysia ROC (Companies Commission Registration Number), for entities\n- **NAM_TIN**: Namibia TIN (Tax Identification Number), for individuals and entities\n- **NGA_NIN**: Nigeria NIN (National Identification Number), for individuals\n- **NGA_TIN**: Nigeria TIN (Tax Identification Number), for entities\n- **NIC_RUC**: Nicaragua RUC (Registro Unico de Contribuyentes), for individuals and entities\n- **NLD_BTW**: Netherlands Btw-identificatienummer (btw-id), for entities\n- **NLD_KVK**: Netherlands KVK (Kamer van Koophandel), for entities\n- **NLD_OBN**: Netherlands Omzetbelastingnummer (ob-nummer), for entities\n- **NLD_TIN**: Netherlands BSN (Burgerservicenummer), for individuals\n- **NOR_FNR**: Norway Fødselsnummer (National Identity Number), for individuals\n- **NOR_ORG**: Norway Organisasjonsnummer (Organisation Number), for entities\n- **NPL_PAN**: Nepal PAN (Permanent Account Number), for individuals and entities\n- **NZL_IRD**: New Zealand IRD Number (Inland Revenue Department), for individuals and entities\n- **NZL_NZBN**: New Zealand NZBN (New Zealand Business Number), for entities\n- **OMN_CID**: Oman Civil ID Number, for individuals\n- **PAK_NIC**: Pakistan NIC (National Identity Card), for individuals\n- **PAK_NTN**: Pakistan NTN (National Tax Number), for individuals and entities\n- **PAN_RUC**: Panama RUC (Registro Unico de Contribuyentes), for individuals and entities\n- **PER_RUC**: Peru RUC (Registro Unico de Contribuyentes), for individuals and entities\n- **PHL_TIN**: Philippines TIN (Tax Identification Number), for individuals and entities\n- **POL_NIP**: Poland NIP (Numer Identyfikacji Podatkowej), for entities\n- **POL_PESEL**: Poland PESEL (Polish National Identification Number), for individuals\n- **PRT_NIF**: Portugal NIF (Número de Identificação Fiscal), for individuals and entities\n- **PRY_RUC**: Paraguay RUC (Registro Unico de Contribuyentes), for individuals and entities\n- **QAT_QID**: Qatar QID (Qatar Identity Number), for individuals\n- **ROU_CNP**: Romania CNP (Cod Numeric Personal), for individuals\n- **ROU_CUI**: Romania CUI (Cod Unic de Înregistrare), for entities\n- **RUS_INN_ENT**: Russia INN (Entity Tax Number), for entities\n- **RUS_INN_IND**: Russia INN (Individual Tax Number), for individuals\n- **RWA_TIN**: Rwanda TIN (Tax Identification Number), for individuals and entities\n- **SAU_TIN**: Saudi Arabia TIN (Tax Identification Number), for individuals and entities\n- **SAU_VAT**: Saudi Arabia VAT Registration Number, for entities\n- **SEN_NINEA**: Senegal NINEA (Numéro d'Identification Nationale des Entreprises), for entities\n- **SGP_ASGD**: Singapore ASGD, for individuals\n- **SGP_FIN**: Singapore FIN, for individuals\n- **SGP_ITR**: Singapore ITR, for individuals and entities\n- **SGP_NRIC**: Singapore NRIC, for individuals\n- **SGP_UEN**: Singapore UEN (Unique Entity Number), for entities\n- **SLV_NIT**: El Salvador NIT (Número de Identificación Tributaria), for individuals and entities\n- **SRB_JMBG**: Serbia JMBG (Unique Master Citizen Number), for individuals\n- **SRB_PIB**: Serbia PIB (Tax Identification Number), for entities\n- **SVK_ICO**: Slovakia IČO (Identification Number of Organisation), for entities\n- **SVK_TIN**: Slovakia TIN (Tax Identification Number), for individuals\n- **SVN_DAS**: Slovenia Davčna Številka (Tax Number), for individuals and entities\n- **SVN_MS**: Slovenia Matična Številka (Registration Number), for entities\n- **SWE_ORG**: Sweden Organisationsnummer (Organisation Number), for entities\n- **SWE_TAX_ID**: Sweden Tax ID (Personnummer), for individuals\n- **SWZ_TIN**: Eswatini TIN (Tax Identification Number), for individuals and entities\n- **SXM_CRIB**: Sint Maarten CRIB (Centraal Registratie Informatie Belastingplichtige), for individuals and entities\n- **SYR_TIN**: Syria TIN (Tax Identification Number), for individuals and entities\n- **THA_NID**: Thailand National ID Card Number (เลขประจำตัวประชาชน), for individuals\n- **THA_TIN**: Thailand Tax ID (เลขประจำตัวผู้เสียภาษี), for entities\n- **TJK_TIN**: Tajikistan TIN (Tax Identification Number), for individuals and entities\n- **TTO_BIR**: Trinidad and Tobago BIR (Board of Inland Revenue File Number), for individuals and entities\n- **TUN_CIN**: Tunisia CIN (Carte d'Identité Nationale), for individuals\n- **TUN_MF**: Tunisia Matricule Fiscal (Tax Identification Number), for entities\n- **TUR_TIN**: Turkey TIN (Tax Identification Number), for individuals and entities\n- **TWN_GUI**: Taiwan GUI (Unified Business Number / 統一編號), for entities\n- **TWN_NID**: Taiwan National ID Number (身分證字號), for individuals\n- **TZA_TIN**: Tanzania TIN (Tax Identification Number), for individuals and entities\n- **UGA_TIN**: Uganda TIN (Tax Identification Number), for individuals and entities\n- **UKR_EDRPOU**: Ukraine EDRPOU (Entity Identification Code), for entities\n- **UKR_RNTRC**: Ukraine RNTRC (Individual Tax Number), for individuals\n- **URY_CI**: Uruguay CI (Cédula de Identidad), for individuals\n- **URY_RUT**: Uruguay RUT (Rol Único Tributario), for entities\n- **UZB_INN**: Uzbekistan INN (Entity Tax Number), for entities\n- **UZB_PINFL**: Uzbekistan PINFL (Personal Identification Number), for individuals\n- **VEN_RIF**: Venezuela RIF (Registro de Información Fiscal), for individuals and entities\n- **VNM_MST_BRN**: Vietnam MST Branch (Mã số thuế đơn vị phụ thuộc), for entities\n- **VNM_MST_CORP**: Vietnam MST Enterprise (Mã số thuế doanh nghiệp), for individuals and entities\n- **VNM_MST_PIN**: Vietnam PIN (Personal identification number / Số định danh cá nhân), for individuals\n- **WSM_TIN**: Samoa TIN (Tax Identification Number), for individuals and entities\n- **XXK_PID**: Kosovo Personal Identification Number, for individuals\n- **ZAF_CRN**: South Africa Company Registration Number, for entities\n- **ZAF_ID**: South African ID Number, for individuals\n- **ZMB_TPIN**: Zambia TPIN (Taxpayer Identification Number), for individuals and entities\n- **ZWE_TIN**: Zimbabwe TIN (Tax Identification Number), for individuals and entities\n- **NATIONAL_ID**: National ID number, if a tax ID number is not available\n- **PASSPORT**: Passport number, if a tax ID number is not available\n- **PERMANENT_RESIDENT**: Permanent resident number, if a tax ID number is not available\n- **DRIVER_LICENSE**: Driver's license number, if a tax ID number is not available\n- **OTHER_GOV_ID**: Other government issued identifier, if a tax ID number is not available\n- **NOT_SPECIFIED**: Other Tax IDs",
        "enum": [
          "USA_SSN",
          "USA_EIN",
          "USA_ITIN",
          "USA_TIN",
          "ABW_PN",
          "AGO_NIF",
          "ALB_NIPT",
          "AND_NRT",
          "ARE_EID",
          "ARE_TRN",
          "ARG_AG_CUIT",
          "ARG_AR_CUIT",
          "ARM_SSN",
          "ARM_TIN",
          "AUS_ABN",
          "AUS_TFN",
          "AUT_UID",
          "AUT_VNR",
          "AZE_FIN",
          "AZE_VOEN",
          "BEL_BCE",
          "BEL_NN",
          "BEN_IFU",
          "BFA_IFU",
          "BGD_TIN",
          "BGR_EGN",
          "BGR_EIK",
          "BHR_CPR",
          "BIH_JMBG",
          "BLR_ID",
          "BLR_UNP",
          "BLZ_TIN",
          "BOL_NIT",
          "BRA_CNPJ",
          "BRA_CPF",
          "BRB_TIN",
          "BTN_TPN",
          "BWA_TIN",
          "CAN_BN",
          "CAN_SIN",
          "CHE_AHV",
          "CHE_UID",
          "CHL_RUT",
          "CHN_RID",
          "CHN_USCC",
          "CIV_NCC",
          "CMR_NIU",
          "COK_RMD",
          "COL_CC",
          "COL_CE",
          "COL_NIT",
          "COL_NUIP",
          "COL_PPT",
          "CPV_NIF",
          "CRI_CJ",
          "CRI_DIMEX",
          "CRI_NITE",
          "CRI_PIN",
          "CUW_CRIB",
          "CYP_TIC",
          "CZE_TIN",
          "DEU_TAX_ID",
          "DEU_UST_ID",
          "DNK_CPR",
          "DNK_CVR",
          "DOM_CED",
          "DOM_RNC",
          "DZA_NIF",
          "ECU_RUC",
          "EGY_NID",
          "EGY_TRN",
          "ESP_DNI",
          "ESP_NIE",
          "ESP_NIF",
          "EST_IK",
          "EST_RC",
          "ETH_TIN",
          "FIN_HETU",
          "FIN_YTU",
          "FJI_TIN",
          "FRA_SIREN",
          "FRA_SPI",
          "GAB_NIF",
          "GBR_CRN",
          "GBR_NINO",
          "GBR_UTR",
          "GEO_PID",
          "GEO_TIN",
          "GHA_TIN",
          "GRC_AFM",
          "GTM_NIT",
          "HKG_BRN",
          "HKG_HKID",
          "HND_RTN",
          "HRV_OIB",
          "HTI_NIF",
          "HUN_ENT",
          "HUN_TIN",
          "IDN_KTP",
          "IDN_NWPW",
          "IND_GSTIN",
          "IND_PAN",
          "IRL_CRO",
          "IRL_PPS",
          "IRN_NID",
          "ISL_KT",
          "ISR_CORP",
          "ISR_TAX_ID",
          "ITA_PIVA",
          "ITA_TAX_ID",
          "JAM_TRN",
          "JOR_NID",
          "JPN_CORP",
          "JPN_TAX_ID",
          "KAZ_BIN",
          "KAZ_IIN",
          "KEN_KRA_PIN",
          "KGZ_INN",
          "KHM_NID",
          "KOR_BRN",
          "KOR_RRN",
          "KWT_CID",
          "LBN_TIN",
          "LKA_NIC",
          "LKA_TIN",
          "LTU_AK",
          "LTU_JAK",
          "LUX_NIN",
          "LUX_TVA",
          "LVA_PK",
          "LVA_REG",
          "MAC_TIN",
          "MAR_CIN",
          "MAR_ICE",
          "MDA_IDNO",
          "MDA_IDNP",
          "MEX_CURP",
          "MEX_RFC",
          "MKD_EDB",
          "MKD_EMBG",
          "MLI_NIF",
          "MLT_ID",
          "MLT_VAT",
          "MNE_JMBG",
          "MNE_PIB",
          "MNG_RD",
          "MOZ_NUIT",
          "MUS_NID",
          "MUS_TAN_ENT",
          "MUS_TAN_IND",
          "MWI_TPIN",
          "MYS_MYKAD",
          "MYS_ROC",
          "NAM_TIN",
          "NGA_NIN",
          "NGA_TIN",
          "NIC_RUC",
          "NLD_BTW",
          "NLD_KVK",
          "NLD_OBN",
          "NLD_TIN",
          "NOR_FNR",
          "NOR_ORG",
          "NPL_PAN",
          "NZL_IRD",
          "NZL_NZBN",
          "OMN_CID",
          "PAK_NIC",
          "PAK_NTN",
          "PAN_RUC",
          "PER_RUC",
          "PHL_TIN",
          "POL_NIP",
          "POL_PESEL",
          "PRT_NIF",
          "PRY_RUC",
          "QAT_QID",
          "ROU_CNP",
          "ROU_CUI",
          "RUS_INN_ENT",
          "RUS_INN_IND",
          "RWA_TIN",
          "SAU_TIN",
          "SAU_VAT",
          "SEN_NINEA",
          "SGP_ASGD",
          "SGP_FIN",
          "SGP_ITR",
          "SGP_NRIC",
          "SGP_UEN",
          "SLV_NIT",
          "SRB_JMBG",
          "SRB_PIB",
          "SVK_ICO",
          "SVK_TIN",
          "SVN_DAS",
          "SVN_MS",
          "SWE_ORG",
          "SWE_TAX_ID",
          "SWZ_TIN",
          "SXM_CRIB",
          "SYR_TIN",
          "THA_NID",
          "THA_TIN",
          "TJK_TIN",
          "TTO_BIR",
          "TUN_CIN",
          "TUN_MF",
          "TUR_TIN",
          "TWN_GUI",
          "TWN_NID",
          "TZA_TIN",
          "UGA_TIN",
          "UKR_EDRPOU",
          "UKR_RNTRC",
          "URY_CI",
          "URY_RUT",
          "UZB_INN",
          "UZB_PINFL",
          "VEN_RIF",
          "VNM_MST_BRN",
          "VNM_MST_CORP",
          "VNM_MST_PIN",
          "WSM_TIN",
          "XXK_PID",
          "ZAF_CRN",
          "ZAF_ID",
          "ZMB_TPIN",
          "ZWE_TIN",
          "NATIONAL_ID",
          "PASSPORT",
          "PERMANENT_RESIDENT",
          "DRIVER_LICENSE",
          "OTHER_GOV_ID",
          "NOT_SPECIFIED"
        ],
        "example": "USA_SSN",
        "title": "TaxIdType",
        "type": "string"
      },
      "TrustedContact": {
        "anyOf": [
          {
            "required": [
              "email_address"
            ]
          },
          {
            "required": [
              "phone_number"
            ]
          },
          {
            "required": [
              "street_address"
            ]
          }
        ],
        "dependentRequired": {
          "street_address": [
            "city",
            "state",
            "postal_code",
            "country"
          ]
        },
        "description": "This model input is optional. However, the client should make a reasonable effort to obtain the trusted contact information. See [FINRA Notice 17-11](https://www.finra.org/sites/default/files/Regulatory-Notice-17-11.pdf) for more details.\n\nAt least one of the following is required:\n- `email_address`\n- `phone_number`\n- `street_address`\n",
        "example": {
          "email_address": "jane.doe@example.com",
          "family_name": "Doe",
          "given_name": "Jane"
        },
        "properties": {
          "city": {
            "description": "Required if `street_address` is set.",
            "type": "string"
          },
          "country": {
            "description": "The country in [ISO 3166-1 alpha-3](https://www.iso.org/iso-3166-country-codes.html) format. Required if `street_address` is set.",
            "type": "string"
          },
          "email_address": {
            "description": "At least one of `email_address`, `phone_number`, or `street_address` is required.",
            "example": "jane.doe@example.com",
            "format": "email",
            "type": "string"
          },
          "family_name": {
            "example": "Doe",
            "type": "string"
          },
          "given_name": {
            "example": "Jane",
            "type": "string"
          },
          "phone_number": {
            "description": "At least one of `email_address`, `phone_number`, or `street_address` is required.",
            "type": "string"
          },
          "postal_code": {
            "description": "Required if `street_address` is set.",
            "type": "string"
          },
          "state": {
            "description": "Required if `street_address` is set.",
            "type": "string"
          },
          "street_address": {
            "description": "At least one of `email_address`, `phone_number`, or `street_address` is required.",
            "items": {
              "type": "string"
            },
            "type": "array"
          }
        },
        "required": [
          "given_name",
          "family_name"
        ],
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
    "/v1/accounts/{account_id}": {
      "get": {
        "description": "You can query a specific account that you submitted to Alpaca by passing into the query the account_id associated with the account you're retrieving.\n",
        "operationId": "getAccount",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AccountExtended"
                }
              }
            },
            "description": "Will return an AccountExtended if an account with account_id exists, otherwise will throw an error."
          }
        },
        "summary": "Get An Account by ID",
        "tags": [
          "Accounts"
        ]
      },
      "parameters": [
        {
          "$ref": "#/components/parameters/AccountID"
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
      "name": "Accounts"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false,
    "apply-tag-changes": true
  }
}
````