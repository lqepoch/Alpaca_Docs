---
updatedAt: 2026-11-17T15:01:40.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Real-time Stock Data v3

The v3 stock stream provides real-time trades, quotes and bars of stocks listed outside the US over a WebSocket connection. Each feed covers one exchange or consolidated tape. For US stocks :us:, see [Real-time Stock Data](https://docs.alpaca.markets/us/docs/real-time-stock-pricing-data).

The connection, authentication and subscription flow is described in [WebSocket Stream](https://docs.alpaca.markets/us/docs/streaming-market-data). This page focuses on what differs on the v3 stock stream.

# URL

The URL for the v3 stock stream is

```
wss://stream.data.alpaca.markets/v3/stocks/{feed}
```

URL for the Broker API sandbox:

```
wss://stream.data.sandbox.alpaca.markets/v3/stocks/{feed}
```

Substitute `{feed}` with one of the following:

| Feed      | Source                                                                                 | Markets |
| :-------- | :------------------------------------------------------------------------------------- | :------ |
| `euroctp` | EuroCTP, the official EU consolidated tape, covering trades from all EU trading venues | any     |
| `xetr`    | Xetra, the electronic trading venue of the Frankfurt Stock Exchange (Deutsche Börse)   | `XETR`  |
| `xhkg`    | Hong Kong Stock Exchange (HKEX)                                                        | `XHKG`  |
| `xlon`    | London Stock Exchange (LSE)                                                            | `XLON`  |
| `xsau`    | Saudi Exchange (Tadawul)                                                               | `XSAU`  |

The feed name is lowercase. Connecting to an unknown feed fails with HTTP status 404.

<Callout icon="far fa-triangle-exclamation" theme="warn">
  ### Subscription required

  Every feed requires a subscription to that feed. Any attempt to access a feed not available for your subscription will result in an `insufficient subscription` (409) error during authentication.
</Callout>

# Symbols

Symbols are in `TICKER:MIC` format, where MIC is the [ISO 10383](https://www.iso20022.org/market-identifier-codes) code of the symbol's primary listing market, for example `SAP:XETR`, `700:XHKG` or `ENI:XMIL`. These are the same symbols the historical [Stock v3 endpoints](https://docs.alpaca.markets/us/reference/stockv3bars) use.

* The MIC must be one of the markets the feed covers (see the table above). `euroctp` accepts any market.
* Share classes are separated with a dot, e.g. `BT.A:XLON`.
* Hong Kong tickers are not zero-padded: use `700:XHKG`, not `0700:XHKG`.
* `*` subscribes to every symbol of the feed.

If a subscribe or unsubscribe message contains a symbol the feed does not accept, the whole message is rejected with error 414. The error message contains the first rejected symbol and, where possible, a suggested correct symbol:

```json
[{"T":"error","code":414,"msg":"invalid symbol for this feed: 0700:XHKG, use 700:XHKG"}]
```

# Numbers

All numeric values are sent as strings to keep their exact decimal value: prices as decimal strings (e.g. `"238.45"`), sizes, volumes and trade counts as integer strings (e.g. `"120"`). To keep prices exact, parse them with a decimal type rather than a binary floating-point type.

Prices are in the currency the symbol is traded in on its market.

# Channels

Clients can [subscribe](https://docs.alpaca.markets/us/docs/streaming-market-data#subscription) to the `trades`, `quotes`, `bars`, `updatedBars` and `dailyBars` channels. For example

```json
{"action":"subscribe","trades":["SAP:XETR"],"quotes":["SAP:XETR","BMW:XETR"],"bars":["*"]}
```

Subscribing to any other channel results in an `invalid subscribe action for this feed` (410) error.

## Trades

### Schema

| Attribute | Type   | Notes                                                                                                   |
| :-------- | :----- | :------------------------------------------------------------------------------------------------------ |
| `T`       | string | message type, always `t`                                                                                |
| `S`       | string | symbol                                                                                                  |
| `t`       | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |
| `m`       | string | MIC of the venue where the trade occurred                                                               |
| `p`       | string | trade price                                                                                             |
| `s`       | string | trade size                                                                                              |
| `i`       | string | trade ID, omitted if the venue does not publish one                                                     |

### Example

```json
{
  "T": "t",
  "S": "SAP:XETR",
  "t": "2026-11-17T09:15:42.123456789Z",
  "m": "XETR",
  "p": "238.45",
  "s": "120",
  "i": "4513276"
}
```

## Quotes

### Schema

| Attribute | Type   | Notes                                                                                                   |
| :-------- | :----- | :------------------------------------------------------------------------------------------------------ |
| `T`       | string | message type, always `q`                                                                                |
| `S`       | string | symbol                                                                                                  |
| `t`       | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision |
| `bp`      | string | bid price                                                                                               |
| `bs`      | string | bid size                                                                                                |
| `ap`      | string | ask price                                                                                               |
| `as`      | string | ask size                                                                                                |

### Example

```json
{
  "T": "q",
  "S": "BMW:XETR",
  "t": "2026-11-17T09:15:43.502114876Z",
  "bp": "84.12",
  "bs": "350",
  "ap": "84.14",
  "as": "200"
}
```

## Bars

Trade aggregates (bars) are streamed on three separate channels.

#### Minute bars (`bars`)

Minute bars are emitted right after each minute mark. They contain the trades from the previous minute.

#### Daily bars (`dailyBars`)

Daily bars are emitted right after each minute mark after the market opens. The daily bars contain all trades until the time they were emitted.

#### Updated bars (`updatedBars`)

Updated bars are emitted after each half-minute mark if a “late” trade arrived after the previous minute mark. For example, if a trade with a timestamp of `09:49:59.998` arrives right after `09:50:00`, an updated bar with `t` set to `09:49:00` containing that trade is sent shortly after `09:50:30`, possibly updating the previous bar’s closing price and volume.

### Schema

| Attribute | Type   | Description                                                                   |
| :-------- | :----- | :---------------------------------------------------------------------------- |
| `T`       | string | message type: `b`, `d` or `u`                                                 |
| `S`       | string | symbol                                                                        |
| `t`       | string | [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp |
| `o`       | string | open price                                                                    |
| `h`       | string | high price                                                                    |
| `l`       | string | low price                                                                     |
| `c`       | string | close price                                                                   |
| `v`       | string | volume                                                                        |
| `n`       | string | number of trades                                                              |
| `vw`      | string | volume-weighted average price                                                 |

### Example

```json
{
  "T": "b",
  "S": "SAP:XETR",
  "t": "2026-11-17T09:15:00Z",
  "o": "238.3",
  "h": "238.55",
  "l": "238.25",
  "c": "238.45",
  "v": "15230",
  "n": "87",
  "vw": "238.412736"
}
```

# Differences from the US stock stream

* Symbols carry their listing market (`SAP:XETR` instead of `SAP`).
* All numbers are strings.
* Trades have the venue's MIC in `m` instead of an exchange code in `x`, and have no conditions (`c`) or tape (`z`).
* Quotes have no bid and ask exchanges (`bx`, `ax`), conditions (`c`) or tape (`z`).
* There are no trade corrections, trade cancels/errors, LULDs, trading statuses or order imbalances. The subscription message has no `corrections` or `cancelErrors` lists.
* An invalid symbol returns error 414 instead of 400.

# Example

```json Shell
$ wscat -c wss://stream.data.alpaca.markets/v3/stocks/xetr
connected (press CTRL+C to quit)
< [{"T":"success","msg":"connected"}]
> {"action": "auth", "key": "*****", "secret": "*****"}
< [{"T":"success","msg":"authenticated"}]
> {"action": "subscribe", "trades": ["SAP"]}
< [{"T":"error","code":414,"msg":"invalid symbol for this feed: SAP"}]
> {"action": "subscribe", "trades": ["SAP:XETR"], "quotes": ["BMW:XETR"], "bars": ["*"]}
< [{"T":"subscription","trades":["SAP:XETR"],"quotes":["BMW:XETR"],"bars":["*"],"updatedBars":[],"dailyBars":[]}]
< [{"T":"q","S":"BMW:XETR","t":"2026-11-17T09:15:43.502114876Z","bp":"84.12","bs":"350","ap":"84.14","as":"200"}]
< [{"T":"t","S":"SAP:XETR","t":"2026-11-17T09:15:44.018273645Z","m":"XETR","p":"238.45","s":"120","i":"4513276"}]
```