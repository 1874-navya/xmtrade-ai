from dataclasses import dataclass

@dataclass
class PaperTrade:
    symbol: str
    side: str
    entry_price: float
    quantity: float
    stop_loss: float
    take_profit: float
    status: str = "OPEN"
    exit_price: float | None = None
    pnl_usd: float | None = None

class PaperTradingEngine:
    """Simulation only; this module has no broker execution client."""
    def open_trade(self, symbol, side, entry, quantity, stop, target, risk_approved):
        if not risk_approved:
            raise PermissionError("Risk policy rejected paper trade.")
        if side not in ("BUY", "SELL"):
            raise ValueError("Side must be BUY or SELL.")
        if min(entry, quantity, stop, target) <= 0:
            raise ValueError("Prices and quantity must be positive.")
        if side == "BUY" and not stop < entry < target:
            raise ValueError("BUY requires stop < entry < target.")
        if side == "SELL" and not target < entry < stop:
            raise ValueError("SELL requires target < entry < stop.")
        return PaperTrade(symbol, side, entry, quantity, stop, target)

    def close_trade(self, trade, exit_price):
        if trade.status != "OPEN" or exit_price <= 0:
            raise ValueError("Trade must be open and exit price positive.")
        direction = 1 if trade.side == "BUY" else -1
        trade.pnl_usd = round((exit_price - trade.entry_price) * trade.quantity * direction, 2)
        trade.exit_price, trade.status = exit_price, "CLOSED"
        return trade
