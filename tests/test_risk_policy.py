from app.risk.policy import assess_paper_risk

def test_default_risk_limit():
    result = assess_paper_risk(1000, 0.5)
    assert result["approved"] is True
    assert result["max_loss_usd"] == 5.0

def test_risk_above_ceiling_rejected():
    assert assess_paper_risk(1000, 0.6)["approved"] is False

def test_nonpositive_equity_rejected():
    assert assess_paper_risk(0, 0.5)["approved"] is False
