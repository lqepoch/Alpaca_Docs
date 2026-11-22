---
updatedAt: 2026-09-23T09:33:08.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Best Practices & FAQ

# Best Practices

1. **Set a reasonable cooldown**: this prevents excessive trading when markets are volatile. Thirty-one days is a common starting point.
2. **Combine drift and calendar triggers carefully**: any single met condition triggers a rebalance. Use thresholds that match your product's trading philosophy.
3. **Monitor portfolios that need adjustments**: act quickly when securities in your models become ineligible.
4. **Add a small cash buffer**: It's best to keep a small cash buffer in your portfolios to absorb market movements during rebalances. Twenty-five bps is a good starting point.
5. **Handle&#x20;**`COMPLETED_ADJUSTED` **rebalance runs**: partial rebalances can happen. Review failed orders and skipped orders on each run and decide whether to continue, retry, or notify the customer.
6. **Unsubscribe before portfolio changes at scale**: if retiring a model, unsubscribe accounts first, then archive the portfolio.
7. **Validate before subscribing**: check for open orders and crypto positions in your onboarding flow to avoid API errors.

# FAQ

**Can one account subscribe to multiple portfolios?**<br />The rebalancer supports exactly one account subscribed to one portfolio at a time. However, you can offer multiple portfolios by using sub-accounts.&#x20;

**How often can an account rebalance?**<br />At most one run per trading day from automatic evaluation, plus any manual runs you trigger. Full rebalances are also limited by the portfolio's cooldown days.

**What happens if I deposit cash between rebalances?**
If invest cash is enabled and conditions are met, excess cash may be invested automatically. Otherwise, cash stays until a full rebalance is triggered.

**Do rebalances trade during extended hours?**<br />No, runs execute from 11:30 ET to 15:30 ET.

**What happens on market early close days?**<br />The runner execution window will be from 11:30 ET to 12:45 ET.

**How long does it take for a deposit to be invested?**<br />Invest cash runs are queued by the evaluator. This means that if an investor deposits funds at 14:00 ET; the funds might not be invested until the next trading day.

**How can I withdraw funds from a managed account?**

1. [Unsubscribe the account](/us/reference/delete-v1-rebalancing-subscriptions-subscription_id) from the their portfolio.
2. [Execute a manual run](/us/reference/post-v1-rebalancing-runs) with revised weights that frees up the desired amount of cash.
3. After the trade settles withdraw the funds.
4. [Resubscribe the account](/us/reference/post-v1-rebalancing-subscriptions) to the portfolio.

**What assets can I include?**<br />Tradable, fractionable US equities. Crypto and fixed income are not supported.

**Can I rebalance an account that is not subscribed to a portfolio?**<br />Yes, you can [create a manual rebalance](/us/reference/post-v1-rebalancing-runs) for a one-off rebalance with weights entered at the time of the API call.

<br />

<br />

<br />

***

*Any symbols or examples shown are for demonstration purposes only and do not constitute investment advice or a recommendation to buy or sell any security.*