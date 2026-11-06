def assess_paper_risk(equity_usd: float, requested_risk_pct: float, ceiling_pct: float = 0.5):
    if equity_usd <= 0:
        return {"approved": False, "max_loss_usd": 0.0, "reason": "Equity must be positive."}
    if requested_risk_pct <= 0 or requested_risk_pct > ceiling_pct or ceiling_pct > 0.5:
        return {"approved": False, "max_loss_usd": 0.0, "reason": "Risk exceeds v1 ceiling."}
    return {
        "approved": True,
        "max_loss_usd": round(equity_usd * requested_risk_pct / 100, 2),
        "reason": "Within paper risk policy.",
    }
