---
updatedAt: 2026-11-03T12:19:10.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Data Validations

# Data Validations

Data validation applies to requests via the account creation (`POST /v1/accounts`) and update (`PATCH /v1/accounts/:account_id`) endpoints. A validation check on user information submitted via these endpoints will return a **422 error** if the information submitted does not meet our validation criteria. (In some flows a **400** with code `40010001` may be returned instead.) Partners integrating with Broker API (including KYC and correspondent flows) should ensure their systems comply with all criteria below.

***

## Validation Criteria

The validation criteria include the following:

### Name and Address Romanization

* `given_name`, `middle_name`, `family_name`, `street_address`, `unit`, `city`, `state`, `postal_code`, `email_address`, and `tax_id` are all required to be provided in Latin characters. The accepted input for these fields will be limited to **ASCII character range 32–126**.
* We have introduced the following fields to continue accepting name and address information in its original script if desired: `local_given_name`, `local_middle_name`, `local_family_name`, `local_street_address`, `local_unit`, `local_city`, and `local_state`.

### Given Name

* `given_name` (`identity.given_name`) is now required for all users.

### Tax ID Number Validation

* `tax_id` (`identity.tax_id`) is required for securities accounts. All values must meet the general rules below. When a country-specific `tax_id_type` is submitted, the value must also match that type's format.
* If the tax ID type is `USA_SSN` or `USA_ITIN`, then the following must be met:
  * No values having an Area Number (first three digits) of 000 nor 666.
  * No values having a Group Number (middle two digits) of 00.
  * No values having a Serial Number (last four digits) of 0000.
  * No values all of the same digit such as 000-00-0000, 111-11-1111, 333-33-3333, 666-66-6666, 999-99-9999, nor all increasing or decreasing characters (e.g. 123-45-6789 or 987-65-4321).
  * Values must be exactly 9 characters in length after dashes have been stripped.
* All tax ID types will undergo the following validation:
  * The length must be greater than 1 character (e.g. submitting 0 as a tax ID will not be permitted).
  * No values all of the same digit, nor all increasing or decreasing characters as above.
  * Max length of 40 characters.
  * Only letters, digits, dashes (denoted by ASCII char 45), periods, and plus (+) signs will be permitted.
  * Value must contain digits (e.g. submitting `TIN_NOT_ISSUED` or `xxx-xxx-xxxx` will not be permitted).
* Country-specific format validation:
  * When a supported country-specific `tax_id_type` is submitted, Alpaca validates `tax_id` against the format defined for that type.
  * Supported types and their formats are available via `GET /v1/country-info` for each country of tax residence.
  * Validation failures return 422 Unprocessable Entity.
  * Examples:

| Country                           | Correct Type | Expected format               |
| --------------------------------- | ------------ | ----------------------------- |
| Nigeria                           | `NGA_TIN`    | Country-specific TIN format   |
| United Arab Emirates (individual) | `ARE_EID`    | 784-XXXX-XXXXXXX-X            |
| United Arab Emirates (entity)     | `ARE_TRN`    | 15-digit TRN beginning with 1 |
| Brazil (individual)               | `BRA_CPF`    | XXX.XXX.XXX-XX                |
| Brazil (entity)                   | `BRA_CNPJ`   | XX.XXX.XXX/XXXX-XX            |

* As a general reminder to our partners that onboard users in regions where tax ID numbers are not issued, there is still a requirement for a unique identifier to be submitted for those users. The identifier should be either a national identity card number, passport number, permanent resident number, driver's license number, etc. We have introduced the following `tax_id_type` values to support these classifications: `NATIONAL_ID`, `PASSPORT`, `PERMANENT_RESIDENT`, `DRIVER_LICENSE`, `OTHER_GOV_ID`.

### Tax ID Type Selection

The `tax_id_type` submitted must correspond to the tax ID number provided.

**Use country-specific types where available. When Alpaca supports a country-specific tax ID type for the user's country of tax residence, that type must be used.**

**Generic types such as `NATIONAL_ID`, `PASSPORT`, `PERMANENT_RESIDENT`, `DRIVER_LICENSE`, and `OTHER_GOV_ID` are valid only in regions where country-specific tax ID is not available. This includes foreign-born residents and countries that do not issue tax identification to every person. `NOT_SPECIFIED` will no longer be accepted as a tax ID type.**

Individual versus legal entity accounts. Individual accounts must use individual tax ID types such as `USA_SSN`, `BRA_CPF`, and `ARE_EID`. Legal entity accounts must use entity tax ID types such as `USA_EIN`, `BRA_CNPJ`, and `ARE_TRN`.

### Retrieving Supported Tax ID Types

Call `GET /v1/country-info` and use the returned ID types for each country to determine:

* Which `tax_id_type` values are valid for that country
* The pattern each type expects
* An example value that matches the pattern. You can display this to customers for reference.

Implement client-side validation from these patterns so users receive immediate feedback before submission.

### `street_address` Validation

* No values consisting of only digits.
* Length must be greater than 1 character.
* A validation has been introduced to the `street_address` (`contact.street_address`) field to prevent the submission of US Post Office Boxes (PO Boxes) for a residential address. This validation is case-insensitive and detects keywords indicative of a PO Box, including: PO Box, Post Office Box, P.O. Box, and Box #. If a prohibited value is detected, the request will be blocked, returning a **422 error** with the specific message: `"street_address cannot be a P.O. Box"`. This validation applies to requests via the `POST /v1/accounts` and `PATCH /v1/accounts/:account_id` endpoints, and partners should ensure their systems are prepared to handle this validation error.

### Postal Code Validation

* **Overall maximum length:** 12 characters for `postal_code` (`contact.postal_code`) and `local_postal_code` (`contact.local_postal_code`).
* If country of tax residence = USA:
  * The `postal_code` attribute will be required upon account creation.
  * No values less than 5 characters in length and the first 5 characters must only contain digits.
  * No values greater than 10 digits.
* United Kingdom: `postal_code` must match UK postcode format (e.g. SW4 6EH). Invalid format will return an error.
* Canada: `postal_code` must match Canadian postcode format (e.g. A1A 1A1). Invalid format will return an error.

### `date_of_birth` Validation

* No values greater than or less than 10 characters in length. Values for `date_of_birth` (`identity.date_of_birth`) must be in **YYYY-MM-DD** format.

### Email Address

* Email addresses (`contact.email_address`), after aliases are removed, are restricted to a maximum of **60 characters** in length. Alpaca defines an alias as all characters after a + sign and before the @ sign. The stored value is also subject to a **100 character** database limit.

### State Validation

* For all countries:
  * The max length for `state` (`contact.state`) should not be greater than 50 characters.
  * `state` cannot consist of only digits. It can be alphanumeric.
* If country of tax residence = USA:
  * `state` will be limited to either the 2 letter abbreviation code for the state or the complete name of the state as defined in our documentation.

### City

* The `city` (`contact.city`) attribute cannot consist of only digits. It can be alphanumeric. Length must be between 2 and 50 characters (individuals), or 2 and 100 characters (legal entities).

### Whitespace Validation

* The following validation will be applied to the `given_name`, `middle_name`, `family_name`, `street_address`, `unit`, `city`, `state`, `postal_code`, `email_address`, `tax_id_type`, and `tax_id` fields on the Accounts API (i.e. `identity.given_name`, `identity.middle_name`, `identity.family_name`, `contact.street_address`, `contact.unit`, `contact.city`, `contact.state`, `contact.postal_code`, `contact.email_address`, `identity.tax_id_type`, `identity.tax_id`):
  * The space character, denoted by ASCII character 32, will be the only whitespace character we accept.
  * Leading and trailing spaces present in the string will return a 422 error.
* Additionally, we may clean up existing accounts in our system that contain invalid whitespace characters. We will follow up directly with the affected partners and share the complete list of accounts and data points that we will be updating.

***

## Field Length Limits (Additional Constraints)

In addition to the criteria above, the following **maximum character lengths** are enforced. Exceeding them returns an error (e.g. *"\<field> must not be longer than \<N>"* or *"unit/apt # too long, must be less than 20 characters"*).

Fields use `object.field` notation: `contact` (address, email, phone), `identity` (name, tax, citizenship, visa), `disclosures` (employment, affiliation). `referral_source` is at account/owner level.

| Field                                                                                                                                                          | Max length | Notes                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contact.unit`                                                                                                                                                 | **20**     | Apartment, suite, unit number only. Do **not** put full street lines here (e.g. "2424 S 90th St Ste 100" is invalid).                                                                                                       |
| `contact.local_unit`                                                                                                                                           | 20         | Same as `contact.unit` for local script.                                                                                                                                                                                    |
| `contact.postal_code`                                                                                                                                          | 12         | Overall limit. USA-specific rules above still apply.                                                                                                                                                                        |
| `contact.local_postal_code`                                                                                                                                    | 12         |                                                                                                                                                                                                                             |
| `identity.prefix`                                                                                                                                              | 7          | Name prefix (e.g. Dr., Mr.).                                                                                                                                                                                                |
| `identity.suffix`                                                                                                                                              | 3          | Name suffix (e.g. Jr., III).                                                                                                                                                                                                |
| `identity.visa_type`                                                                                                                                           | 5          |                                                                                                                                                                                                                             |
| `identity.visa_type_other_free_text`                                                                                                                           | 50         | When `identity.visa_type` is `OTHER`.                                                                                                                                                                                       |
| `disclosures.employment_status`                                                                                                                                | 12         |                                                                                                                                                                                                                             |
| `disclosures.affiliated_firm`                                                                                                                                  | 100        | Affiliated firm name in disclosure contexts.                                                                                                                                                                                |
| `identity.country_of_tax_residence`                                                                                                                            | 3          | ISO 3166-1 alpha-3.                                                                                                                                                                                                         |
| `identity.country_of_citizenship`                                                                                                                              | 3          | ISO 3166-1 alpha-3.                                                                                                                                                                                                         |
| `identity.tax_id`                                                                                                                                              | 40         | Letters, digits, dash, period, plus; must contain digits. US SSN/ITIN: 9 digits, no invalid area, group, or serial. Country-specific types must match the pattern for the selected tax ID type. See `GET /v1/country-info`. |
| `identity.tax_id_type`                                                                                                                                         | 20         | Must match the format of the submitted tax ID. Country-specific types are required where available. Generic types remain supported only where no country-specific type is defined.                                          |
| `identity.percentage_ownership`                                                                                                                                | 5          | Decimal string (e.g. 11.25). Used for UBO/beneficiary.                                                                                                                                                                      |
| `contact.email_address`                                                                                                                                        | 100        | Stored value (database limit). See also 60-char limit after alias removal above.                                                                                                                                            |
| `identity.given_name`, `identity.family_name`, `identity.middle_name`, `identity.local_given_name`, `identity.local_family_name`, `identity.local_middle_name` | 50         | Per name component.                                                                                                                                                                                                         |
| `contact.city`                                                                                                                                                 | 50         | Individuals. 2–50 characters.                                                                                                                                                                                               |
| `contact.city` (legal entity)                                                                                                                                  | 100        | 2–100 characters.                                                                                                                                                                                                           |
| `contact.local_city`                                                                                                                                           | 50         | 2–50 characters.                                                                                                                                                                                                            |
| `referral_source`                                                                                                                                              | 128        | Account/owner level. If provided: only lowercase letters, numbers, and underscores.                                                                                                                                         |
| `contact.state`                                                                                                                                                | 50         |                                                                                                                                                                                                                             |
| `contact.mailing_postal_code`                                                                                                                                  | 12         |                                                                                                                                                                                                                             |

***

## `unit` and `local_unit` (Apartment / Suite)

* `contact.unit` and `contact.local_unit` are optional but, when provided, are limited to **20 characters**. Use these fields only for the apartment, suite, or unit designator (e.g. "Ste 100", "Apt 4B"). Do **not** put the full street line (e.g. "2424 S 90th St Ste 100") in `unit`; put the full street address in `contact.street_address` and only the unit designator in `contact.unit`. Exceeding the limit returns an error such as `"unit must not be longer than 20"` or `"unit/apt # too long, must be less than 20 characters"`.

***

## Additional Validations (Visa, Country, Legal Entities, Beneficiaries)

### Visa (Non-US Citizens / Residents)

* When `identity.visa_type` is `B1` or `B2`, `identity.country_of_tax_residence` must be USA.
* `identity.visa_type` must be one of the documented allowed values (e.g. `E1`, `E2`, `E3`, `F1`, `H1B`, `TN1`, `O1`, `J1`, `L1`, `B1`, `B2`, `DACA`, `G4`, `OTHER`).
* When `identity.visa_type` is provided and not empty, `identity.visa_expiration_date` may be required and must be in **YYYY-MM-DD** format.

### Country and Country Codes

* `contact.country`, `identity.country_of_tax_residence`, `identity.country_of_citizenship`, `identity.country_of_incorporation`, and similar country fields must be **ISO 3166-1 alpha-3** (exactly 3 characters, e.g. USA, GBR, CAN).

### Legal Entities

* `identity.legal_name` (or `entity_name`) is required. `identity.country_of_incorporation` is required; if USA, `identity.state_of_incorporation` may be required. `identity.date_of_incorporation` is required (YYYY-MM-DD). `identity.entity_type` or `identity.legal_entity_type` is required; if other, `identity.legal_entity_type_other_free_text` may be required. `identity.funding_source` is required; if it includes other, `identity.funding_source_other_free_text` may be required. `identity.type_of_business` is required; if other, `identity.type_of_business_other_free_text` may be required. `contact.country` is required for legal entity accounts.

### Disclosures (Equity Accounts)

* For equity accounts, `disclosures` are required for individuals (non–legal-entity). `disclosures.employment_status` must be one of the allowed values (e.g. `EMPLOYED`, `UNEMPLOYED`, `RETIRED`, `STUDENT`). `disclosures.employment_sector` (when provided) is validated in context of `employment_status`. Other disclosure fields (e.g. `is_control_person`, `is_politically_exposed`, `is_affiliated_exchange_or_finra`, `immediate_family_exposed`) may be required or validated per account type and product.

### Beneficiaries (e.g. IRA)

* Maximum number of beneficiaries: Sum of all beneficiaries' `share_pct` must equal 100; each value must be a positive number ≤ 100; precision typically limited (e.g. at most 2 decimal places). Each beneficiary may require `given_name`, `family_name`, `date_of_birth` (`YYYY-MM-DD`), `tax_id`, `tax_id_type` where applicable; `tax_id` is subject to the same tax ID rules (e.g. SSN/ITIN for `USA_SSN`/`USA_ITIN`).

### Error Responses

* Validation failures typically return **422 Unprocessable Entity** or **400 Bad Request** with an error code (e.g. `40010001`) and a message describing the failing rule. Partners should implement robust error handling and user-facing messages based on these responses.

***

## Summary Table (Quick Reference)

| Category                                                     | Key limits / rules                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contact.unit` / `contact.local_unit`                        | Max **20** characters; use only for apt/suite/unit.                                                                                                                                                                                                                                                        |
| `contact.postal_code`                                        | Max **12**; USA: 5–10 chars, first 5 digits; UK/Canada: format-specific.                                                                                                                                                                                                                                   |
| `identity` (names)                                           | `identity.given_name` required; `identity.family_name` required for some countries (min 2 chars USA, 1 UK); max **50** per component.                                                                                                                                                                      |
| `identity.tax_id`                                            | Chars: 0-9 A-Z a-z - . + ; length 2–40; must contain digits; SSN/ITIN: 9 digits, no 000/666/00/0000, no same/increasing/decreasing.                                                                                                                                                                        |
| `contact.street_address`                                     | Required where applicable; > 1 char; not digits-only; no PO Box (US residential).                                                                                                                                                                                                                          |
| `identity.country_of_tax_residence`, `contact.country`, etc. | ISO 3166-1 alpha-3 (**3** characters).                                                                                                                                                                                                                                                                     |
| `contact.email_address`                                      | Valid format; max **60** chars after alias removal; max **100** chars stored.                                                                                                                                                                                                                              |
| `identity` (dates)                                           | **YYYY-MM-DD** (e.g. `identity.date_of_birth`, `identity.visa_expiration_date`).                                                                                                                                                                                                                           |
| `contact.state` (USA)                                        | Required; 2-letter or full name; max 50 chars.                                                                                                                                                                                                                                                             |
| `contact.city`                                               | Not digits-only; 2–50 (or 2–100 for legal entity).                                                                                                                                                                                                                                                         |
| Whitespace                                                   | Applied to `identity.given_name`, `identity.middle_name`, `identity.family_name`, `contact.street_address`, `contact.unit`, `contact.city`, `contact.state`, `contact.postal_code`, `contact.email_address`, `identity.tax_id_type`, `identity.tax_id`. Space (ASCII 32) only; no leading/trailing spaces. |

***

*This document reflects validations applied to account creation (`POST /v1/accounts`) and account/owner updates (`PATCH /v1/accounts/:account_id` and related owner-detail patches) for Broker API, including KYC and correspondent flows. Alpaca may update these rules over time; partners should handle validation errors gracefully and refer to the latest API documentation and error messages.*