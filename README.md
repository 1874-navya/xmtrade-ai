# XMTrade AI

Paper-only, gold-focused intraday research assistant.

## V1 configuration
- Gold symbol: auto-discover in the optional MT5 read-only adapter; verify broker contract specifications.
- Primary timeframe: M15; H1 confirmation; M5/H4 context.
- Maximum planned risk: 0.5% per simulated trade.
- Starting paper balance: USD 1,000.
- News analysis: enabled; provider adapter must be configured.
- Primary data: independent historical-data provider.
- Execution: simulated only.

## Safety boundary
This repository intentionally has no broker login, deposit, withdrawal, or live-order implementation. Do not add MT5 `order_send` or expose broker trading methods to agents. The MT5 adapter, when implemented, must remain read-only. Missing, stale, or invalid data must result in NO_TRADE.

For users in India, verify the exact contracting entity, product and applicable permissions with a qualified compliance professional before any real account integration, funding or trading. RBI's Alert List includes XM / xm.com, but that does not establish whether a separately branded XMTrading account is the same legal entity; absence from the list is not proof of authorisation.

## Quick start
Python 3.11+:
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
uvicorn app.api.main:app --reload
pytest
```
API docs: http://127.0.0.1:8000/docs

## CSV data contract
Put one file per symbol/timeframe in `data/`, e.g. `GOLD_M15.csv`, with columns:
`timestamp,open,high,low,close,volume`.
Timestamps must be UTC. The CSV adapter is a development source; no live feed or licensed provider is bundled.

## Roadmap
1. Integrate and validate an independent historical-data provider.
2. Add provider-specific bid/ask, spread and instrument metadata.
3. Add a reliable news/calendar source with publisher and retrieval timestamps.
4. Add LangGraph agents as evidence summarizers/reviewers; keep calculations deterministic.
5. Improve paper fills with spread, slippage, commissions, swaps and conservative intrabar resolution.
6. Add walk-forward backtesting, dashboard performance views and MLflow/AgentOps tracing.

This is an engineering scaffold and unvalidated research hypothesis, not financial advice or a claim of profitability.
