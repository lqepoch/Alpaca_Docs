---
updatedAt: 2026-11-05T14:18:37.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Portfolios

A portfolio is a reusable investment model that you define and manage.

# Weights

Weights describe what assets an account should hold and how they should be allocated. All portfolio weights must sum to 100%. You may have an asset weight or a cash weight. All asset weights must be:

* Fractionable and tradable US equities.

*Crypto, fixed income, and non-US equities are not supported in portfolio weights.*

# Portfolio status

A portfolio can enter a `needs_adjustment` status when an asset in the portfolio becomes unusable (for example, if a symbol is delisted, is marked non-tradable, or is no longer fractionable).

<Callout icon="💡" theme="info">
  ### Tip

  [Monitor portfolio statuses via SSEs](/us/reference/subscribetorebalancereventssse) and correct portfolios that enter the `needs_adjustment` status.
</Callout>

When this happens:

* The portfolio status changes to `needs_adjustment`.
* Queued runs for that portfolio are cancelled.
* The evaluator stops queuing new runs until you fix the model.

To recover: update the portfolio (e.g. replace the affected symbol) to return the portfolio back to `active`.

# Rebalance conditions

Rebalance conditions control when a full rebalance runs. If any configured condition is met and the cooldown period has elapsed, a full rebalance is queued. You may configure up to four condition types:

| Type                    | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| `drift_band` (absolute) | Rebalance when any position drifts beyond a fixed percentage-point band. |
| `drift_band` (relative) | Rebalance when drift exceeds a percentage of the target weight.          |
| `calendar`              | Rebalance on a schedule.                                                 |
| `on_portfolio_update`   | Rebalance when you change portfolio weights or assets are added/removed. |

If no conditions are configured, automatic full rebalances will not be triggered by the evaluator. The portfolio will only fully rebalance on the initial subscription to the portfolio and when a manual run is triggered.

## Drift band

Drift is measured by comparing each weight's current allocation (as a percentage of account equity) to its target.

**Absolute**: fires when `|CurrentAllocation% − TargetAllocation%| > Threshold`.

Example: target 35%, threshold 5% → rebalance if the position falls below 30% or rises above 40%.

**Relative**: fires when `|CurrentAllocation% −TargetAllocation%| > Threshold% × Target%`.

Example: target 35%, threshold 10% → band is 3.5 percentage points (10% of 35%) → rebalance below 31.5% or above 38.5%.

## Calendar

Schedule-based rebalancing on US market trading days:

| Sub-type    | `day` format                  | Behaviour                                                                     |
| ----------- | ----------------------------- | ----------------------------------------------------------------------------- |
| `weekly`    | Day name `monday` - `friday`) | Fires on that weekday when the market is open.                                |
| `monthly`   | Day of the month `1` - `31`)  | Fires on that day, or the prior trading day if it falls on a holiday/weekend. |
| `quarterly` | Day of the month `1` - `31`)  | Fires in March, June, September, and December.                                |
| `annually`  | MM-DD (e.g. `07-01`)          | Fires once per year on that date, adjusted for non-trading days.              |

## On portfolio update

Fires when:

* You update the portfolio's weights since the account's last full rebalance, or
* An asset in the portfolio was added or removed relative to the account's current positions.

This helps ensure model changes propagate to subscribed accounts.

# Cooldown period

After a full rebalance completes, the account enters a cooldown period. During this period, drift and calendar conditions are ignored. Portfolio updates will still trigger a rebalance during this period.

Invest cash runs will not trigger a cooldown period and invest cash runs will continue to happen during the cooldown period.

You can configure how many days (calendar time, not trading days) an account stays in cooldown by setting `cooldown_days` on the subscription.

You can calculate if an account is currently in cooldown by looking at the `last_rebalanced_at` attribute on a subscription. This attribute is only set when a full rebalance reaches any terminal state. Invest-cash runs do not update this timestamp.

<br />

<br />

<br />

***

*Any symbols or examples shown are for demonstration purposes only and do not constitute investment advice or a recommendation to buy or sell any security.*