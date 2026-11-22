---
updatedAt: 2026-11-10T17:13:10.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Anthropic Trading Availability and FAQs

Trading API FAQs for the upcoming Antrhopic (ANT) IPO. 

# Overview

Anthropic has filed to go public and a listing is planned for the coming days or weeks, although no date has been officially set or confirmed by the firm. This page provides consistent answers for Trading API clients.

Two points up front:

* Alpaca is not expecting to receive an IPO allocation for Anthropic. Direct IPO purchase is not available through the Trading API.
* Anthropic trading is separate from Alpaca's US IPO product. Participation is through the secondary market once the stock begins trading.

# When does Anthropic start trading?

Anthropic is expected to begin trading in the next several days, but no official date has been set for the IPO. Alpaca will have the symbol configured and ready to accept orders at 5am ET on listing day. We will update this page if timing changes.

# **What is Anthropic's ticker symbol?**

Anthropic will trade under the ticker ANT on Nasdaq.

# **Can I buy Anthropic at the IPO price?**

No. Direct IPO purchase is not available. You can participate in the secondary market once Anthropic begins trading.

# **When will the symbol appear in the assets API?**

Alpaca will configure the symbol before the open on listing day. Once configured, the asset is visible in `/v2/assets` and ready to accept pre-open limit orders.

# **Can I place orders before Anthropic starts trading?**

Yes. As soon as the symbol is configured, you can submit whole share limit orders. These orders will not be executable until the first exchange print at the opening cross. Note: orders with limit prices outside a reasonable range will be rejected by our venues.

# **What order types are supported in the pre-open window?**

During the pre-open window, only whole-share limit orders with `DAY` or `GTC` time-in-force are accepted. All other order types - including market, fractional, and notional orders - will be rejected and will not become available until after the opening cross.

# **How do I confirm the asset is live and fully tradeable?**

Check for all three: `asset_class = us_equity` AND `status = active` AND `tradable = true`. Note that `tradable = true` is also set during the pre-open window so relying on `tradable` alone is not sufficient.

# **Are fractional and notional orders available on day 1?**

Yes, fractional and notional trading are planned for day 1. During the pre-open window, only whole-share limit orders with `DAY` or `GTC` time-in-force are accepted. Fractional and notional availability will begin 5 minutes after the stock opens rather than exactly at the opening cross, similar to other fractional providers.

# **Are market orders supported on day 1?**

Market orders are rejected during the pre-open window. After the opening cross, market orders become available.

# **Why might the stock not start trading right at market open?**

Most symbols will begin trading during the market session on the day of the IPO. This is because new listings go through a price discovery process before trading begins. Market makers collect buy and sell orders to determine an opening price and minimize the opening imbalance, which can delay the first trade. The price discovery process can take anywhere from a couple minutes to a couple hours.

# **Can I buy Anthropic on margin?**

No. Margin is not available for newly public securities for the first 30 days after the IPO.

# **Is short selling allowed?**

No. Short selling is not permitted at launch. This is standard practice for newly listed securities.

# **Will paper trading be supported?**

Yes. Users will be able to trade ANT via their paper account(s).

# **Will extended hours and overnight trading be available?**

We expect to offer extended hours and overnight sessions for Anthropic, including the overnight session from 8:00 PM ET to 4:00 AM ET, subject to market availability and applicable restrictions. If anything changes, we will update this page accordingly. When these sessions are enabled, fractional and notional orders are also supported across them.

# **What order types are available during extended hours?**

During extended hours sessions, the following are available:

* Limit orders for whole shares, fractional shares, and notional dollar amounts
* Time in force of `DAY` or `GTC`.

The following are not available and will be rejected:

* Market orders
* Stop orders
* Stop-limit orders
* Trailing stop orders
* Any time in force other than `DAY` or `GTC`.

# **How do LULD rules apply?**

Standard Limit Up Limit Down (LULD) rules apply to ANT as they do to all NMS stocks. Alpaca surfaces LULD-related market events via the standard API event stream.

# **What happens to open orders during a halt?**

Open orders are held in a pending state during a halt and are not automatically canceled. When trading resumes, orders remain active and eligible to fill at the prevailing price subject to your specified limit price.

# **Is indicative or reference price data available before it opens?**

Generally, indicative pricing is not available through normal data providers unless you subscribe to professional feeds that provide order book imbalances. For retail traders, the best sources will be public financial news outlets.

# **When does the live price feed go active?**

Price data is available from the first trade on secondary trading. There is no intentional delay though normal data propagation latency applies.

# **Are there additional risks when trading a newly listed IPO stock?**

Yes. Risks may include higher volatility, limited public operating history, rapid price movements, reduced analyst coverage initially and wider bid ask spreads.

# **When will options on ANT be available?**

Based on exchange listing criteria, ANT is expected to clear the size threshold and qualify for an accelerated options listing schedule.

Under that track, options typically begin trading about 2 business days after the equity IPO day (vs. \~4 business days for a standard new listing).

Anthropic equity is expected to begin secondary trading in the next several days. On that basis, ANT options are expected to begin trading about 2 business days after the equity IPO day, subject to OCC and options-exchange listing schedules.

Alpaca will support trading of listed ANT options once they are available on the exchanges.

Final dates will be confirmed when OCC / the options exchanges publish the listing notice.

# When will ANT option contracts appear in the Trading API?

Contracts become available through Alpaca’s options endpoints once they are listed and loaded into our systems - typically early on the options listing day. Do not hard-code a clock time.

Poll `/v2/options/contracts` (filter by underlying ANT) rather than assuming contracts exist the night before.<br />Limit orders may be accepted once contracts are live.

Quotes and marketable liquidity are generally available once the regular session opens (9:30 AM ET).

# **When can I place options orders?**

Order placement is expected during the regular trading session (9:30 AM – 4:00 PM ET) on the options listing day, consistent with standard equity-options handling. Exact availability depends on exchange listing and contract load timing that morning.

# **Do you support options trading during extended hours for ANT?**

No. Alpaca does not support options trading during extended hours, including for ANT options. Options orders may only be placed during regular market hours.

**Options orders are subject to:**

`time_in_force` must be `DAY` or `GTC`

# Which option expirations will be available at launch?

Initial contract availability is determined by the options exchanges and OCC. Alpaca supports the expirations that are listed and available for trading. To see what is live, poll `/v2/options/contracts` for underlying ANT.

# Will Alpaca support ANT options on day one of listing?

Yes. Once ANT options are listed and trading on the exchanges, Alpaca intends to support them the same day for Trading API accounts that are already approved for options trading.

# **Disclosures**

Investments in initial public offerings ("IPOs") involve significant risks and are not suitable for all investors. IPO securities have no prior public trading history, and the offering price may not reflect the market price following the offering. The market price of IPO securities may be volatile, and investors may lose part or all of their investment.

Information regarding an IPO issuer may be limited, and the issuer may have a limited operating history or may not be profitable. There can be no assurance that an active or liquid trading market will develop.

This material is provided for informational purposes only and does not constitute an offer to sell or a solicitation of an offer to buy securities. Any offer will be made solely by means of a prospectus filed with the U.S. Securities and Exchange Commission. Investors should carefully review the prospectus, including the risk factors described therein, before investing.

Fractional share trading allows a customer to buy and sell fractional share quantities and dollar amounts of certain securities. Fractional share trading presents unique risks and is subject to particular limitations that you should be aware of before engaging in such activity. See Alpaca Customer Agreement at <https://alpaca.markets/disclosures> for more details.

Extended Hours trading has unique risks and is different than trading in the main trading session. For more information, you can review our Alpaca Extended Hours and Overnight Trading Risk Disclosure.