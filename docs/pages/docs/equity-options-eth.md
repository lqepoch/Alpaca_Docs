---
updatedAt: 2026-11-18T17:35:42.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Equity Options Extended Hours  

### What is Equity Options Extended Hours?

Equity Options Extended Hours (ETH) adds two new additional sessions:

* ***\[New]*&#x20;**&#x4D;orning Session “Global Trading Hours, GTH” (7:30-9:25am ET)
* Regular Trading Hours (9:30-4:00pm ET)
* ***\[New]*** After Hours Session “Curb” (4:00-4:15pm ET)

### **Which symbols will you support for Equity Options ETH?**

Symbol eligibility is determined by the OCC, US Options Exchanges, and our Venue partners. The symbol list is reviewed semi-annually. The criteria for eligibility for Morning and After Hours sessions are:

1. The option class has an average daily volume of 150,000 contracts or higher,
2. The underlying equity to the option has a $50 billion or higher market capitalization, and
3. The underlying equity to the option has an average daily trading volume of 10 million shares or higher.

Partners and users can use the attribute flag `has_options_extended_hours` to filter symbols that are eligible using: `GET /v1/assets?status=active&attributes=has_options_extended_hours`&#x20;

The initial launch includes 29 securities and is subject to change (access the current list via `GET / v1/assets`):

* Stock (24) : AAPL, AMD, AMZN, AVGO, BABA, BAC, F, GOOG, GOOGL, HOOD, INTC, META, MRVL, MSFT, MU, NFLX, NOK, NVDA, ORCL, PFE, PLTR, SNDK, TSLA, TSM
* ETF (5): ETFs: SPY, QQQ, IWM, GLD, XLF

### How do I enable Equity Options ETH?

Broker API Partner Enablement

* Contact your CSM to enable Equity Options ETH at the correspondent level.

Order Entry (sample POST to place an order below)

* `Extended_hours=true`: The flag indicates the order is eligible to participate in all 3 sessions - Morning Session, Regular Trading, and After Hours Sessions.
* `extended_hours=false`(or not present): The order will only participate in Regular Trading Hours hours.

<Accordion title="Sample Request for single leg option order with extended hours " icon="fa-info-circle">
  ```json
  {
   "symbol": "AAPL261113C00250000",
   "qty": "1",
   "side": "buy",
   "type": "limit",
   "time_in_force": "day",
   "limit_price": "1.25",
   "extended_hours": true
  }

  ```
</Accordion>

<Accordion title="Sample request for a multi-leg option order with extended hours" icon="fa-info-circle">
  ```json
  {
   "order_class": "mleg",
   "qty": "1",
   "type": "limit",
   "time_in_force": "day",
   "limit_price": "0.50",
   "extended_hours": true,
   "legs": [
     {
       "symbol": "AAPL261113C00250000",
       "side": "buy",
       "ratio_qty": "1",
       "position_intent": "buy_to_open"
     },
     {
       "symbol": "AAPL261113C00260000",
       "side": "sell",
       "ratio_qty": "1",
       "position_intent": "sell_to_open"
     }
   ]
  }


  ```
</Accordion>

<br />

### What happens if I set `extended_hours=true` on a non-designated symbol?

Alpaca rejects the order.

### Can I amend or replace an order to change extended\_hours?

No. Changing `extended_hours` from `true` to `false` or `false` to `true` via amend/replace is not supported. Cancel the order and submit a new one with the desired session eligibility.

### What is the difference between Late Close and Extended Hours trading for the five designated ETFs (SPY, QQQ, IWM, GLD, XLF)?

* The five designated ETFs (SPY, QQQ, IWM, GLD, and XLF) have a regular trading session from 9:30 a.m. to 4:15 p.m. ET, meaning the 4:00–4:15 p.m. period is considered part of regular trading hours, not extended hours.
* Enabling Extended Hours trading for these ETFs provides access to the additional morning trading session from 7:30 a.m. to 9:25 a.m. ET.

### Which sessions will my order be eligible for?

This is based on the underlying asset class and the value sent for the `extended_hours` parameter.

<Table>
  <thead>
    <tr>
      <th style={{ width: "22.1%" }}>
        Symbol Segment 
      </th>

      <th style={{ width: "21.4%" }}>
        `Extended_hours`**&#x20;is not set&#xA0;**
      </th>

      <th style={{ width: "28.6%" }}>
        `Extended_hours=false`
      </th>

      <th style={{ width: "28.1%" }}>
        `Extended_hours=true`
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **ETF Designated
        5 ETFs:** SPY, QQQ, IWM, GLD, XLF
      </td>

      <td>
        9:30 a.m.–4:15 p.m.

        \*4:00–4:15 (i.e., late close) is included in the regular trading session for ETFs
      </td>

      <td>
        9:30 a.m.–4:15 p.m.

        \*4:00–4:15 (i.e., late close) is included in the regular trading session for ETFs
      </td>

      <td>
        - **_\[New]_** Morning session: 7:30 a.m. – 9:25 a.m. ET
        - Regular Trading Session: 9:30a.m. – 4:15p.m. ET


      </td>
    </tr>

    <tr>
      <td>
        **Stock Designated
        24 stocks:&#x20;**&#x20; AAPL, AMD, AMZN, AVGO, BABA, BAC, F, GOOG, GOOGL, HOOD, INTC, META, MRVL, MSFT, MU, NFLX, NOK, NVDA, ORCL, PFE, PLTR, SNDK, TSLA, TSM
      </td>

      <td>
        9:30 a.m.–4:00 p.m.

        \*For stocks, trading ends at 4:00pm
      </td>

      <td>
        9:30 a.m.–4:00 p.m.

        \*For stocks, trading ends at 4:00pm
      </td>

      <td>
        - **_\[New]_** Morning session: 7:30 a.m. – 9:25 a.m. ET
        - Regular Trading Session: 9:30a.m. – 4:00p.m. ET
        - **_\[New]&#x20;_**&#x41;fternoon session: 4:00 p.m. – 4:15 p.m. ET
      </td>
    </tr>

    <tr>
      <td>
        **Other Stock**
      </td>

      <td>
        9:30 a.m.–4:00 p.m.
      </td>

      <td>
        9:30 a.m.–4:00 p.m.
      </td>

      <td>
        Rejected with an Error message of:<br /><br />`HTTP 422 / 42210000: asset is not eligible for global trading hours (GTH) options trading`
      </td>
    </tr>

    <tr>
      <td>
        **Other ETF with Late Close**
      </td>

      <td>
        9:30 a.m.–4:15 p.m.

        _\*(4:00–4:15 is included in the regular trading session for ETFs)_
      </td>

      <td>
        9:30 a.m.–4:15 p.m.

        _\*(4:00–4:15 is included in the regular trading session for ETFs)_
      </td>

      <td>
        Rejected with an Error message of:<br /><br />`HTTP 422 / 42210000: asset is not eligible for global trading hours (GTH) options trading`
      </td>
    </tr>

    <tr>
      <td>
        **Other ETF without Late Close**
      </td>

      <td>
        9:30 a.m.–4:00 p.m.
      </td>

      <td>
        9:30 a.m.–4:00 p.m.
      </td>

      <td>
        Rejected with an Error message of:<br /><br />`HTTP 422 / 42210000: asset is not eligible for global trading hours (GTH) options trading`
      </td>
    </tr>
  </tbody>
</Table>

### Which orders are eligible for Equity Options ETH?

For the Morning Session “GTH” (7:30-9:25am ET) and After Hours Session “Curb” (4:00-4:15pm ET)

* **Order Type:** Limits Only (Market, stop, stop-limit, trailing is rejected)
* **Time In Force:&#x20;**&#x44;ay Only (GTC is not supported at launch)
* **Option Levels:&#x20;**&#x4C;evel 1, Level 2, and Level 3 is supported
* **Multi-Leg:** Option-only Level 3 orders follow the same rules. An order with a stock leg is not supported.

### What happens between 9:25-9:30am ET?

* If an order was sent earlier, and still open at 9:25:
  * The order will remain open, will not trade, and continue to rest at venues.
  * The order is eligible to trade at 9:30am ET.
  * The order can be cancelled, during the 5 minute window
* If an order is sent during 9:25-9:30:
  * The order is accepted, queued, and will not execute in the gap.
  * The order is eligible to trade at 9:30am ET.
  * The order can be cancelled, during the 5 minute window

### Why did my options order fill or remain unfilled After 4:00 p.m. ET?

Whether an options order can be executed after 4:00 p.m. ET depends on the underlying security and whether Extended Trading Hours (ETH) is enabled.

* **Designated Stocks (ETH Enabled):** Orders with `extended_hours=true` can be executed during the Curb session (4:00–4:15 p.m. ET). Only limit orders are supported.
* **Designated Stocks (Regular Hours Only):&#x20;**&#x54;rading ends at 4:00 p.m. ET. Orders without ETH enabled are not eligible for execution during the Curb session.
* **Designated ETFs:&#x20;**&#x54;he 4:00–4:15 p.m. ET period is part of the regular trading session, so orders can be executed without enabling ETH.
* **Non-Designated Securities:** Extended trading sessions (GTH and Curb) are not supported. Orders submitted with `extended_hours=true` will be rejected by Alpaca.

### If I submit an options order overnight or outside trading hours, when will It become eligible for execution?

You can submit an order for a designated options symbol outside of trading hours with `extended_hours=true`. The order will be accepted by the system and routed to the trading venue when the Morning Session opens at 7:30 a.m. ET, at which point it becomes eligible for execution.

### Why was my options order rejected during Equity Options ETH?

The following error messages have been added in preparation for support for Equity Options ETH.

* HTTP 403 / 40310000: account not allowed for global trading hours (GTH) options trading
* HTTP 422 / 42210000: asset is not eligible for global trading hours (GTH) options trading
* HTTP 422 / 42210000: leg "symbol" is not eligible for global trading hours (GTH)
* HTTP 422 / 42210000: global trading hours (GTH) options orders must be DAY limit orders
* HTTP 422 / 42210000: orders global trading hours (GTH) options orders must be limit orders
* HTTP 422 / 42210000: equity legs are allowed only with a corresponding amount of call contracts

### How do market holidays and early closures at 1:00 p.m. ET affect extended trading hours for equity options?

* Market Holidays: No trading available (No Morning Session, No Regular Trading Session, and No After Hours Session)
* Early Closures at 1:00 p.m. ET:
  * Morning Session is available
  * Regular Trading Session is available - but will terminate early
  * After Hours Session is not available

### How do expiration and liquidation work for equity options during extended trading hours?

There are no changes to the existing expiration or liquidation processes for equity options during extended trading hours

### How do 0DTE cutoffs and auto-liquidation work during extended trading hours (ETH) and the 4:00–4:15 p.m. ET session?

The cutoff times for opening or increasing 0DTE positions and the start of auto-liquidation vary depending on the underlying security. Extended Trading Hours does not change these cutoff times, but it may affect how liquidation orders are handled after 4:00 p.m. ET.

| **Security Type**     | **Open/Increase Cutoff** | **Auto-Liquidation Begins** | **Trading Ends**          |
| --------------------- | ------------------------ | --------------------------- | ------------------------- |
| Designated Stocks     | 3:15 p.m.                | 3:30 p.m.                   | 4:15 p.m. (Curb)          |
| Designated ETFs       | 3:30 p.m.                | 3:45 p.m.                   | 4:15 p.m. (Regular Hours) |
| Other Stocks          | 3:15 p.m.                | 3:30 p.m.                   | 4:00 p.m.                 |
| Other Late-Close ETFs | 3:30 p.m.                | 3:45 p.m.                   | 4:15 p.m. (Regular Hours) |

### What happens after 4:00 p.m. ET?

* **Designated Stocks:&#x20;**&#x4C;iquidation orders during the Curb session (4:00–4:15 p.m. ET) must be limit orders with `extended_hours=true`.
* **Designated ETFs:&#x20;**&#x54;rading continues until 4:15 p.m. ET as part of the regular session. The extended-hours flag is not required.
* **Other Stocks:&#x20;**&#x54;rading ends at 4:00 p.m. ET, with no additional trading session available.
* **Other Late-Close ETFs:&#x20;**&#x54;rading continues until 4:15 p.m. ET as part of the regular session, without requiring the extended-hours flag.

### When are orders accepted vs. when can they execute?

* Alpaca will accept the orders as soon as it can.
* The orders will be routed to the venues and eligible for trading starting at 7:30am
* Orders submitted outside equity options ETH windows (for example overnight) with extended hours are accepted and queued; they are not live until the next eligible session open (Morning Session at 7:30 a.m.)

### **I sent a designated options order with extended\_hours=true and an order type/TIF that is normally acceptable during RTH (9:30–4:00). What will happens?**

If the order is not a DAY limit with `extended_hours=true`, then Alpaca will reject it.&#x20;

You must send the appropriate extended-hours flag and order type for the session/time you are trading.

### Does Equity Options ETH affect Options Approval Levels or Account Setup?

No. Existing options approval levels (Levels 1–3) remain unchanged. Extended Trading Hours (ETH) does not provide access to additional options strategies or higher approval levels. There are also no changes to account setup requirements or settlement types.

### Are multi-leg orders supported for Equity Options ETH?

Option-only multi-leg (Level 3) orders follow the same ETH rules: designated symbols only, day limit orders only when `extended_hours=true`.

### What rejection or error messages can occur for Equity Options ETH?

* HTTP 403 / 40310000: account not allowed for global trading hours (GTH) options trading

* HTTP 422 / 42210000: asset is not eligible for global trading hours (GTH) options trading

* HTTP 422 / 42210000: leg "symbol" is not eligible for global trading hours (GTH)

* HTTP 422 / 42210000: global trading hours (GTH) options orders must be DAY limit orders

* HTTP 422 / 42210000: orders global trading hours (GTH) options orders must be limit orders

* HTTP 422 / 42210000: equity legs are allowed only with a corresponding amount of call contracts

### How do fees or pricing work for Morning and After Hours sessions for Equity Options ETH?

Pricing follows existing equity options rates and no separate Equity Options ETH fees:

* Trading API: Commission-free for retail equity options
* Broker API: Existing monthly/tiered per-contract schedule
  * Contact your Sales or CSM rep for additional information.

### Will market data be available during Morning and After Hours sessions for Equity Options ETH?

Yes, Market data, including quotes and trades, will be available during both the Morning and After-Hours sessions for designated options classes and their associated option series.

### How do you test Equity Options Extended Hours?

* Broker API: Reach out to your CSM to enable it on your correspondent sandbox environment
* Trading API: Test with your paper account via Dashboard or API

### What is the go live date for Equity Options Extended Hours?

Alpaca is targeting a production go-live on Dec 4th 2026

***

The content of this article is for general informational purposes only and does not constitute investment advice or a recommendation to buy or sell any security.
Extended Hours trading has unique risks and is different than trading in the main trading session, for more information please review our [Alpaca Extended Hours & Overnight Trading Risk Disclosure.](https://files.alpaca.markets/disclosures/library/ExtHrsOvernightRisk.pdf)
Options trading is not suitable for all investors due to its inherent high risk, which can potentially result in significant losses. Certain complex options strategies carry additional risk. Please read [Characteristics and Risks of Standardized Options](https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document) before investing in options.

Securities brokerage services are provided by Alpaca Securities LLC (dba "Alpaca Clearing"), member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.

This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities is not registered or licensed, as applicable.