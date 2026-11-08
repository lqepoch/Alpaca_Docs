---
updatedAt: 2026-11-04T20:30:26.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Anthropic Trading Availability and FAQs

Anthropic has filed to go public and is expected to list as soon as Monday, November 16, 2026, although no date has been officially set or confirmed by the firm. There is strong partner interest, so this page provides consistent answers for partners. Two points up front:

* Alpaca is not expecting to receive an IPO allocation for Anthropic. Direct IPO purchase is not available to customers on Alpaca powered platforms.
* Anthropic trading is separate from Alpaca's US IPO product. Participation is through the secondary market once the stock begins trading.

### When does Anthropic start trading?

Anthropic is expected to begin trading as soon as Monday, November 16, 2026, but no official date has been set for the IPO. Alpaca will have the symbol configured and ready to accept orders at 5:00 AM ET on listing day. We will update this page if timing changes.

### What is Anthropic's ticker symbol?

Anthropic will trade under the ticker `ANT` on Nasdaq.

### Can customers buy Anthropic at the IPO price?

No. Direct IPO purchase is not available. Customers on Alpaca-powered platforms can participate in the secondary market once Anthropic begins trading.

# Pre-open trading window

### When will the symbol appear in the assets API?

Alpaca will configure the symbol before the open on listing day. Once configured, the asset is visible in `/v2/assets` and ready to accept pre-open limit orders.

### Can customers place orders before Anthropic starts trading?

Yes. As soon as the symbol is configured, customers can queue whole-share limit orders. These orders will not be executable until the first exchange print at the opening cross. Note: orders with limit prices outside a reasonable range will be rejected by our venues.

### What order types are supported in the pre-open window?

Only limit orders are accepted during the pre-open window. Market orders will be rejected. Both `DAY` and `GTC` time-in-force values are supported. Only whole-share orders are accepted in this window. Fractional and notional orders are not available until after the opening cross.

### How do I confirm the asset is live and fully tradeable?

Check for all three: `asset_class` equals `us_equity`, `status` equals `active`, and `tradable` equals `true`. Note that `tradable = true` is also set during the pre-open window, so relying on `tradable` alone is not sufficient.

# First day of trading

### Are fractional shares available on day 1?

Yes, fractional trading is planned for day 1. At the opening cross, only whole-share orders will start trading for the symbol. Fractional availability will begin 5 minutes after the stock opens rather than exactly at the opening cross, similar to other fractional providers.

### Are market orders supported on day 1?

Market orders are rejected during the pre-open window. After the opening cross, market orders become available.

### Why might the stock not start trading right at market open?

On the day of the IPO, `ANT` will not start trading at market open. Most symbols start trading between 10:00 AM ET and 12:00 PM ET on the day of their IPO. This is because new listings go through a price discovery process before trading begins. Market makers collect buy and sell orders to determine an opening price and minimize the opening imbalance, which can delay the first trade. The price discovery process can take anywhere from a couple of minutes to a couple of hours.

### Can customers buy Anthropic on margin?

No. Margin is not available for newly public securities for the first 30 days after the IPO. This is a standard regulatory requirement.

### Is short selling allowed?

No. Short selling is not permitted at launch. This is standard practice for newly listed securities.

# Extended and overnight sessions

### Will extended hours and overnight trading be available?

We expect to offer extended hours and overnight sessions for Anthropic, including the overnight session from 8:00 PM ET to 4:00 AM ET, subject to market availability and applicable restrictions. If anything changes, we will update this page accordingly. When these sessions are enabled, fractional and notional orders are also supported across them.

### Are all order types supported during extended hours?

No. During extended hours sessions only certain order types are supported:

* Whole-share, fractional-share, and notional-dollar orders are supported.
* Orders must be submitted as limit orders with a specified limit price. Market orders and other unsupported types are rejected.
* Time-in-force must be `DAY` or `GTC`. Any other value is rejected.

# Trading halts and volatility

### Should I expect trading halts?

Yes. A newly listed stock like this can experience multiple trading halts on the first day due to price volatility. Standard LULD (Limit Up-Limit Down) rules apply to all NMS stocks, including newly listed ones. Alpaca surfaces halt events via the standard [API event stream](./real-time-stock-pricing-data).

### What happens to open orders during a halt?

Open orders are held in a pending state during a halt and are not automatically canceled. When trading resumes, orders remain active and eligible to fill at the prevailing price, subject to the order's specified limit price.

# Market price data

### Is indicative or reference price data available before it opens?

Generally, indicative pricing is not available through normal data providers unless the user subscribes to professional feeds that provide order book imbalances. For retail traders, the best sources will be public financial news outlets.

### When does the live price feed go active?

Price data is available from the first trade on secondary trading. There is no intentional delay, though normal data propagation latency applies.

# Additional features and risks

### Are there additional risks when trading a newly listed IPO stock?

Yes. Risks may include higher volatility, limited public operating history, rapid price movements, reduced analyst coverage initially, and wider bid-ask spreads.

# Options trading eligibility

### When will options on ANT be available?

Based on exchange listing criteria, `ANT` is expected to clear the size threshold and qualify for an accelerated options listing schedule.

Under that track, options typically begin trading about 2 business days after the equity IPO day (vs. \~4 business days for a standard new listing).

Anthropic equity is expected to begin secondary trading the week of November 16, 2026. On that basis, `ANT` options are expected to begin trading about 2 business days after the equity IPO day, subject to OCC and options-exchange listing schedules.

Alpaca will support trading of listed `ANT` options once they are available on the exchanges.

Final dates will be confirmed when OCC / the options exchanges publish the listing notice.

### When will ANT option contracts appear in Broker API?

Contracts become available through Alpaca’s options endpoints once they are listed and loaded into our systems, typically early on the options listing day. Do not hard-code a clock time.

* Poll `/v2/options/contracts` (filter by underlying `ANT`) rather than assuming contracts exist the night before.
* Limit orders may be accepted once contracts are live.
* Quotes and marketable liquidity are generally available once the regular session opens (9:30 AM ET).

### When can customers place options orders?

Order placement is expected during the regular trading session (9:30 AM – 4:00 PM ET) on the options listing day, consistent with standard equity-options handling. Exact availability depends on exchange listing and contract load timing that morning.

### Do you support options trading during extended hours for ANT?

No. Alpaca does not support options trading during extended hours, including for `ANT` options. Options orders may only be placed during regular market hours.

Options orders are subject to:

* `time_in_force` must be `day` or `gtc`

### Which option expirations will be available at launch?

Initial contract availability is determined by the options exchanges and OCC. Alpaca supports the expirations that are listed and available for trading. To see what is live, poll `/v2/options/contracts` for underlying `ANT`.

### Will Alpaca support ANT options on day one of listing?

Yes. When `ANT` options are listed and trading on the exchanges, Alpaca intends to support them the same day, with no separate partner enablement step required for correspondents already approved for options trading.

# Disclosures

Investments in initial public offerings (“IPOs”) involve significant risks and are not suitable for all investors. IPO securities have no prior public trading history, and the offering price may not reflect the market price following the offering. The market price of IPO securities may be volatile, and investors may lose part or all of their investment.

Information regarding an IPO issuer may be limited, and the issuer may have a limited operating history or may not be profitable. There can be no assurance that an active or liquid trading market will develop.

This material is provided for informational purposes only and does not constitute an offer to sell or a solicitation of an offer to buy securities. Any offer will be made solely by means of a prospectus filed with the U.S. Securities and Exchange Commission. Investors should carefully review the prospectus, including the risk factors described therein, before investing.

Fractional share trading allows a customer to buy and sell fractional share quantities and dollar amounts of certain securities. Fractional share trading presents unique risks and is subject to particular limitations that you should be aware of before engaging in such activity. See Alpaca Customer Agreement at <https://alpaca.markets/disclosures> for more details.

Extended Hours trading has unique risks and is different than trading in the main trading session. For more information please review our Alpaca Extended Hours and Overnight Trading Risk Disclosure.