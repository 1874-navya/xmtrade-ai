from datetime import datetime, timezone

def audit_event(event_type: str, details: dict) -> dict:
    return {"event_type": event_type, "timestamp": datetime.now(timezone.utc).isoformat(), "details": details, "execution_mode": "PAPER_ONLY"}
