---
updatedAt: 2026-09-23T09:32:51.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Rebalance Runs

A rebalance run is a single execution attempt for one account against one portfolio's target weights. Each run is tied to one account and one portfolio.

# Run types

## <br />Full rebalance

Brings the account as close as possible to the target portfolio. The runner may buy and sell equities and adjust cash. This is the default run type for subscriptions and most automatic triggers.

*Example: An account has target portfolio weights of 80% VTI and 20% AGG with a 5% absolute drift rebalance condition. Overtime, with market movements VTI drifts to 86% of the portfolio and AGG now makes up 14% of your portfolio. To correct this, the rebalancer sells a portion of your VTI shares to raise cash, and uses that cash to buy more AGG shares, bringing the account as close as possible back to your strict 80/20 target.*

## Invest cash

A lighter-weight run that buys only. It invests excess cash above the portfolio's target cash allocation in an attempt to bring the portfolio back into weights without selling existing positions.

Invest cash runs are considered only when:

* A full rebalance is not due.
* The account has completed at least one prior full rebalance.
* Invest cash is enabled for your correspondent (contact your account representative to configure).
* Excess cash exceeds your configured minimum threshold.
* You can also trigger an invest-cash run manually via the API.

Excess cash is calculated as: `trade_cash − target_cash_allocation − estimated_REG/TAF_fees`.

*Example: An account has target portfolio weights of 80% VTI and 20% AGG with a 5% absolute drift rebalance condition. The account has a $1,000 balance with 83% in VTI and 17% in AGG. The user makes a deposit of $1,000. The rebalancer will create an order for $230 of AGG and $770 of VTI.*

# Run lifecycle

Runs move through the following statuses:

| Status               | Terminal? | Description                                                                 |
| -------------------- | --------- | --------------------------------------------------------------------------- |
| `QUEUED`             | No        | Run created; waiting for the execution window.                              |
| `IN_PROGRESS`        | No        | Runner claimed the run and is placing orders.                               |
| `COMPLETED_SUCCESS`  | Yes       | All orders filled with no warnings.                                         |
| `COMPLETED_ADJUSTED` | Yes       | Run finished with partial fills, skipped orders, or other non-fatal issues. |
| `CANCELED`           | Yes       | Canceled via API while queued or in progress.                               |
| `ERROR`              | Yes       | Fatal failure (e.g. planning error, order submission failure).              |
| `TIMEOUT`            | Yes       | Execution exceeded the allowed time budget.                                 |

*An account may have at most one non-terminal run at a time, and at most one run per trading day from automatic evaluation.*

# Run triggers

A rebalance run can be triggered in two ways:

## Automatically

When an account is subscribed to a portfolio, the rebalancer monitors it on trading days and queues a run when the portfolio's rebalance conditions are met (for example, drift beyond a threshold or a scheduled date). A funded account also receives an initial full rebalance at subscribe time. Automatic runs are initiated by the system and will only run at a maximum of once a day.

## Manually

You can [queue a run at any time via the API](/us/reference/post-v1-rebalancing-runs). Use this for on-demand rebalances, one-off allocations with custom weights, or when you want to act immediately without waiting for the next evaluation cycle. Manual runs are initiated by the API and you can create multiple manual runs in a day.

*In both cases, the run follows the same lifecycle: it is queued, executed during runner hours, and completes with a terminal status. An account may have at most one non-terminal run at a time.*

# Run eligibility

Accounts must meet these requirements to subscribe to a portfolio or run rebalances:

| Requirement                            | Description                                                                                                                                           |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| USD accounts                           | Non-USD accounts are not supported.                                                                                                                   |
| Funded                                 | Account equity must be greater than zero to execute a run.                                                                                            |
| Tradable                               | Account must not be blocked from trading (eg: a recent ACH return can block an account from trading).                                                 |
| $1 order minimum per asset             | Each asset order must be at least $1 or the asset will be skipped during a rebalance.                                                                 |
| $10 minimum balance (invest cash only) | For invest cash runs, there must be a minimum cash balance of $10 (this number is configurable; ask your Alpaca representative for more information). |
| Not liquidation-only                   | Accounts restricted to liquidation cannot rebalance.                                                                                                  |
| No crypto positions                    | Active crypto holdings block rebalance runs.                                                                                                          |

<br />

<br />

<br />

***

*Any symbols or examples shown are for demonstration purposes only and do not constitute investment advice or a recommendation to buy or sell any security.*