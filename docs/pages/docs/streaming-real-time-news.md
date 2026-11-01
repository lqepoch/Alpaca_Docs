---
updatedAt: 2026-10-29T14:06:25.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Real-time News

Stream news articles in real time over WebSocket. For connecting, authenticating, and handling messages, see [real-time market data streaming](https://docs.alpaca.markets/us/docs/streaming-market-data).

# URL

The URL for the news stream is

```
wss://stream.data.alpaca.markets/v1beta1/news
```

Sandbox URL:

```
wss://stream.data.sandbox.alpaca.markets/v1beta1/news
```

# Channels

## News

### Schema

| Attribute    | Type            | Notes                                                                                        |
| :----------- | :-------------- | :------------------------------------------------------------------------------------------- |
| `T`          | `string`        | Type of message (`n` for news)                                                               |
| `id`         | `int`           | News article ID                                                                              |
| `headline`   | `string`        | Headline or title of the article                                                             |
| `summary`    | `string`        | Summary text for article (may be first sentence of content, may be empty)                    |
| `author`     | `string`        | Original author of news article (may be empty)                                               |
| `created_at` | `string`        | Date article was created in [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) format |
| `updated_at` | `string`        | Date article was updated in [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) format |
| `content`    | `string`        | Content of news article (might contain HTML, may be empty)                                   |
| `url`        | `string`        | URL of article (if applicable)                                                               |
| `symbols`    | `array<string>` | List of related or mentioned symbols                                                         |
| `source`     | `string`        | Source from which the news originated                                                        |

### Example

```shell
$ websocat \
    -H="APCA-API-KEY-ID: ${APCA_API_KEY_ID}" \
    -H="APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
    "wss://stream.data.alpaca.markets/v1beta1/news"
[{"T":"success","msg":"connected"}]
[{"T":"success","msg":"authenticated"}]
{"action":"subscribe","news":["*"]}
[{"T":"subscription","news":["*"]}]
```

Each message arrives as a single line. Formatted for readability:

```json
[
    {
        "T": "n",
        "id": 100536145,
        "headline": "Analysts Adjust Price Targets for SpaceX Following Q3 Results",
        "summary": "Financial institutions including UBS and Wells Fargo have updated their price targets for SpaceX following the company's third-quarter earnings report.",
        "author": "",
        "created_at": "2026-10-21T15:02:10Z",
        "updated_at": "2026-10-21T15:02:10Z",
        "url": "https://www.moomoo.com/stock/SPCX-US/news?chain_id=Name1K9-3FXPhg.1lcj000&global_content=%7B%22promote_id%22%3A13764,%22sub_promote_id%22%3A64,%22f%22%3A%22www.moomoo.com%2Fcommunity%2Fprofile%2F105275796%2Fpost%2Fall%22%7D",
        "content": "Following the release of SpaceX's third-quarter 2026 financial results, several analysts have updated their outlook on the company. UBS maintained a Buy rating while raising its price target to $230 from $210. Additionally, Wells Fargo maintained an Overweight rating and increased its price target to $274 from $214. These adjustments reflect analyst reactions to the company's reported revenue growth and strategic focus on artificial intelligence.",
        "symbols": ["SPCX"],
        "source": "fiscal.ai"
    },
    {
        "T": "n",
        "id": 62429279,
        "headline": "This Week in TSLA: Roadster's Flying Debut, Cybercab Speeding in School Zones, SpaceX Merger and More",
        "summary": "This week, Tesla unveiled its flying Roadster, faced Cybercab questions and merger speculation with SpaceX.",
        "author": "Badar Shaikh",
        "created_at": "2026-10-18T12:51:02Z",
        "updated_at": "2026-10-18T12:51:02Z",
        "url": "https://www.benzinga.com/markets/tech/26/10/62429279/this-week-in-tsla-roadsters-flying-debut-cybercab-speeding-in-school-zones-spacex-merger-and-more",
        "content": "<p>It was yet another eventful week for <strong>Tesla Inc</strong> (NASDAQ:TSLA) and CEO <strong>Elon Musk</strong> amid the Roadster's high-flying debut, questions about a possible SpaceX merger and more.</p>",
        "symbols": ["SPCX", "TSLA"],
        "source": "benzinga"
    }
]
```