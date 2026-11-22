---
updatedAt: 2026-10-29T14:05:59.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# Historical News Data

Query historical news articles over REST. Articles can come from one or more news feeds, and the source field shows which feed each one came from. For parameters and response fields, see the [API reference](https://docs.alpaca.markets/us/reference/news-3).

# Use cases

Historical news fits into both customer-facing apps built on the Broker API and trading strategies built on the Trading API. The endpoint filters articles by symbol and time range, pages through results, and can include or omit full article content.

1. **News widgets**<br />Add a news feed to a web or mobile app so end users see what is moving the symbols they hold or watch. Each article includes a `headline`, a `url` to the original story, and the related `symbols`, and most include a `summary`. Many articles also come with `images` in `thumb`, `small`, and `large` sizes, so the same feed works in a compact list or a full card layout.
2. **Sentiment analysis**<br />Build a labeled dataset from past headlines, summaries, and content, and train models that score the sentiment of new articles. Because every article carries its `created_at` time and related symbols, sentiment can be correlated with price data to show the effect news had on a stock.
3. **Backtesting news-driven strategies**<br />Replay past news alongside historical market data to test how a strategy would have reacted to announcements, earnings coverage, or analyst rating changes before risking capital.
4. **Real-time trading on news**<br />Once a strategy works on historical data, switch to [real-time news over WebSocket](https://docs.alpaca.markets/us/docs/streaming-real-time-news) to receive articles as they are published and let trading algorithms act on them immediately.