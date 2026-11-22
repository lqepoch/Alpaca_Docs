---
updatedAt: 2026-11-13T20:08:38.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Options Expiration & 0 DTE FAQ

## When do opening options orders stop on expiration day?

For stocks and most equity options: **3:15 PM ET**. For broad-based ETFs (e.g. SPY, QQQ): **3:30 PM ET**. Opening orders after the cutoff are rejected.

## What is auto-liquidation?

Auto-liquidation is Alpaca’s expiration-day risk process that closes at-risk option positions when the account does not have enough buying power or shares to support exercise or assignment. It reduces the chance of an unfunded exercise or assignment. Auto-liquidation is best efforts; the account owner remains responsible for managing expiration risk.

## When does auto-liquidation start?

Typically **3:30 PM ET** for stocks and equity options. For broad-based ETFs: **3:45 PM ET**.

## What positions are at risk of auto-liquidation?

Options with a strike price of about **0.5%** of the underlying market price (slightly ITM or OTM) when the account cannot support exercise or assignment. Although rare, this **0.5%** threshold is subject to change based on underlying market conditions.

## Can I still close an option position after the opening cutoff time?

Yes. Closing orders are still allowed. If Alpaca needs to auto-liquidate, it may cancel your working close order and send a market order.

## When is the exercise cutoff on expiration day?

After **4:00:00 PM ET**, self serve exercise requests are no longer accepted. Exercise requests can be submitted via email and completed on a best efforts basis between **4:00:00 PM ET** and **5:00:00 PM ET**

## What is a Do Not Exercise (DNE)?

A Do Not Exercise (DNE) is a request that an in-the-money long option not be auto-exercised. Placing a DNE forgoes any remaining intrinsic value.

## When should I submit a DNE?

DNE requests should be submitted before **3:00 PM ET** on expiration day. Later requests are handled on a best-efforts basis and should be submitted via email.

## How do I submit a DNE?

The preferred method is through the Do Not Exercise API endpoint: `POST /v2/positions/{symbol_or_contract_id}/do-not-exercise`. You can also request a DNE through Alpaca support; support requests are handled on a best-efforts basis. A DNE is not required for OTM options; only options that close $0.01 or more ITM are subject to automatic exercise.

## Can I DNE a short option?

No. You can only place a DNE on long options. Short option holders have the obligation to deliver if the counterparty exercises.

## What is automatic exercise?

ITM long options by ≥ $0.01 are generally exercised after the close if the account can support deliverables. Long calls and short puts need buying power to purchase 100 shares per contract; long puts and short calls need available shares (shares used for a covered call do not count as available for long puts at the same time).

## When are options auto-exercised?

Long options ITM by at least **$0.01** versus the official close are subject to automatic exercise.

## What if I do not have buying power to exercise?

You can choose to close before the sellout window, or Alpaca may auto-liquidate. If the option cannot be sold, Alpaca may place a DNE on the long contract after market close. You remain responsible for any resulting balances.

## When do exercise and assignment activity show up?

Exercise/assignment activity typically posts the same evening around 9:00pm ET. This time is subject to change depending on when we receive assignment information from the OCC.

## What happens to short options at expiration?

ITM shorts are likely assigned; OTM shorts usually expire. Assignment is not certain until the OCC confirms. Short Option positions closed before market close cannot be assigned.

## How do index options differ at expiration?

They are European-style and cash-settled (no shares). No early exercise or DNE. All multi-leg legs must share one expiration. SPXW/XSP 0DTE stop trading at 4:00 PM ET on expiration day. They generally are not in equity-style options sellout logic.

## Does Alpaca support 0DTE options?

Yes. You can open same-day expiring contracts until the opening cutoffs above.

## What happens to working opening orders at the cutoff?

Alpaca cancels opening orders on contracts expiring that day. Closing orders can remain working.

## Are there option order limits?

Yes. Up to **1,000 contracts** per order or **$50M** notional of the underlying market price.

## Why was my option liquidated on expiration?

Alpaca may liquidate expiring options if they are ITM or near the money, and the account did not have enough buying power or shares to support exercise or assignment. Auto-liquidation is best efforts; you remain responsible for managing expiration risk.

## Will far OTM options be liquidated?

Generally no. Far OTM longs are not liquidated for possible after-close moves. Near-ATM shorts can still be liquidated if assignment would leave an unsupported stock position. An OTM short option may also be liquidated if it is part of a spread and the corresponding long option is within our liquidation threshold and at risk, to avoid leaving the account with an uncovered short option.

## Does Alpaca allow exercise or assignment that would result in a short stock position?

No. Alpaca does not allow exercise or assignment that would result in a short stock position. If exercise or assignment would result in a short stock position, Alpaca may liquidate the option regardless of buying power.

## How do I identify an auto-liquidation order placed by Alpaca?

Order `source` `alpaca::auto_liquidate` indicates systematic liquidation. Additionally, sellouts by Alpaca may have `source` set to `admin`.

## How are spreads handled on expiration when both legs are ITM by more than 0.5%?

For spreads where all legs are more than 0.5% ITM, Alpaca allows exercise of the long and assignment of the short, processed simultaneously.

## How are spreads handled on expiration when both legs are OTM by more than 0.5%?

For spreads where all legs are more than 0.5% OTM, auto liquidation generally will not occur and the spread will expire worthless.

## How are spreads handled on expiration when the underlying is between the strikes, or either/both legs are within 0.5% of a strike?

For debit spreads, Alpaca liquidates the full spread. For credit spreads, if both legs are within 0.5% of a strike, Alpaca liquidates the full spread; if only the short leg is within 0.5% and the long is OTM by more than 0.5%, Alpaca liquidates the short only and allows the long leg to expire.

## Should I close options myself before the sellout window?

Yes. Closing your option positions before the sellout window is the best way to control the exit. For spreads, closing with a multi-leg order is preferred. Auto-liquidation is best efforts; the account owner remains responsible for managing expiration risk.

<br />

##### Options trading is not suitable for all investors due to its inherent high risk, which can potentially result in significant losses. Certain complex options strategies carry additional risk. Please read <Anchor target="_blank" href="https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document">Characteristics and Risks of Standardized Options</Anchor> before investing in options.