---
updatedAt: 2026-11-17T18:34:44.000Z
agentTools:
  siteIndex: https://docs.alpaca.markets/llms.txt
  projectIndex: https://docs.alpaca.markets/us/llms.txt
---

# NMS Exchanges 23/5 Overnight (Dec 6, 2026)

### What is changing on Dec 6?

#### <br />What is 23/5 vs today’s overnight trading?

Prior to December 6th, overnight equities were traded in Alternative Trading Systems (ATS) only; Blue Ocean ATS, Bruce ATS, and  Moon ATS.

On December 6, five National Market System (NMS) exchanges will join the overnight sessions: NASDAQ, CBOE EDGX, NYSE ARCA, MEMX and 24X.

For NMS exchanges to operate overnight, the industry must update the Securities Information Processors (SIPs), Trade Reporting Facilities (TRFs), Depository Trust & Clearing Corporation / National Securities Clearing Corporation (DTCC/NSCC), and Consolidated Audit Trail (CAT) infrastructure that supports U.S. equity trading.

#### What are the industry infrastructure changes?

* **SIP**: Operating hours extend overnight so NMS exchange quotes/trades, static overnight LULD bands, and symbol/halt reference data can disseminate during the night session.
* **TRF**: Reporting windows extend (roughly Sunday 9:00 PM – Friday 8:00 PM ET, with the daily 8:00–9:00 PM pause) and trade date shifts to an 8:00 PM–8:00 PM definition so overnight OTC/NMS prints can be reported in near real time.
* **DTCC/NSCC**: Clearing aligns to a near-continuous 24×5 model, including overnight/session and clearing-date handling so overnight trades can clear on the correct business date.
* **CAT**: Trade-date and related reporting rules move to the 8:00 PM–8:00 PM day so overnight activity is attributed to the correct CAT trade date starting Dec 6, 2026.

#### What are the NMS trading hours after Dec 6?

* Overnight / Night session: 8:00 pm to 4:00 am ET
* NMS Overnight coverage: 9pm to 4am ET
* Day block (early, core and late): 4:00 am to 8:00 pm ET
* NMS Maintenance Pause: 8:00 pm to 9:00 pm ET

#### What markets are trading overnight?

* Daily NMS maintenance pause: 8:00 PM to 9:00 PM ET
  * NMS exchanges are closed for trading
  * Overnight ATSs remain open and are the only venues available
* Overnight session: 8:00 PM to 4:00 AM ET
  * NMS exchanges will be halted during the first hour while overnight ATSs are available for trading. Starting 9pm ET all venues will be eligible to receive orders.

***

### Partner API & Integration

#### Do partners need API or workflow changes for Dec 6?

We do not expect partner-side API or workflow changes. Continue using existing overnight / extended hours order instructions. No new fields, TIF values, or breaking parameter changes are expected.

#### Will existing overnight / extended-hours orders automatically participate after go-live?

Yes. Same order instructions and lifecycle. Session handling and venue selection stay on Alpaca’s stack. Partners do not choose ATS vs exchange via the API.

#### Will TIF / DAY / GTC semantics change?

No partner-facing changes expected. Same overnight TIF behavior as today (limit-only overnight; DAY/GTC semantics per current overnight docs).

#### Do partners need to do anything for SIP, TRF, DTCC/NSCC, or CAT for Dec 6 23/5?

No. Those are Alpaca and industry-infrastructure obligations. Alpaca is handling the SIP, TRF, DTCC/NSCC, and CAT readiness work for 23/5.

Partners do not need to integrate, test, or report against those systems for go-live.

***

### Routing & execution

#### Who decides where overnight orders execute (ATS vs NMS)?

Alpaca routes overnight orders to our overnight execution venues (i.e., market makers). A market maker may fill principally or route to an eligible ATS or NMS destination for best available price in that window. Partners do not choose a specific overnight market.

#### What happens during the 8:00–9:00 PM maintenance pause?

Exchanges are paused. Overnight trading continues via ATS-eligible destinations.

#### Can I see what NMS or ATS market the order traded in?

Overnight orders are sent to our overnight execution venues, which may fill principally or route to an NMS exchange or ATS for best available price. Partners typically see the routing venue (which execution partner handled the order), not a full breakdown of the underlying NMS vs ATS market on every fill.<br />

***

### Market Data

#### Is there changes for market data feeds?

Yes at the industry/Alpaca layer; no partner integration rewrite is expected for the APIs.<br />The SIP extends into overnight hours once NMS exchanges go live (9:00 PM – 4:00 AM ET). SIP also carries overnight reference data (e.g., static LULD bands, halt/status messaging).

#### Will Alpaca support an aggregated Market Data feed (combining both NMS Exchanges and the overnight ATS)?

Not for the Dec 6 launch. Overnight NMS and ATS market data will remain available as separate feeds. Partners who need a combined view can aggregate those feeds on their side.&#x20;

However, Alpaca does intend to release combined historical bar data, returning 24/5 bar data for our customers’ charting applications. We do not yet have a delivery date but we will update our partners when this is ready.<br />

***

### Corporate Action

#### Is there changes on Corporation Action Handling?

No. Corporate action and overnight halt handling does not change for partners.

Overnight orders continue to route through our existing overnight execution venues. Symbols undergoing certain corporate actions may be halted overnight, the same as today. No partner API or workflow changes are required for Dec 6.

***

The content of this article is for general informational purposes only and does not constitute investment advice or a recommendation to buy or sell any security.
Extended Hours trading has unique risks and is different than trading in the main trading session, for more information please review our [Alpaca Extended Hours & Overnight Trading Risk Disclosure](https://files.alpaca.markets/disclosures/library/ExtHrsOvernightRisk.pdf).
Securities brokerage services are provided by Alpaca Securities LLC (dba "Alpaca Clearing"), member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.

This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities is not registered or licensed, as applicable.