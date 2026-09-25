def is_at_risk(order: dict) -> bool:
    """Return whether an order is operationally at risk.

    Existing business rule used by Operations:
    - only ACTIVE orders are actionable;
    - an order is at risk when estimated delay is at least 10 minutes;
    - if estimated delay is unknown, we do not classify the order as at risk.

    Keep this rule centralized. Callers should reuse it rather than duplicating it.
    """
    delay = order.get("estimated_delay_minutes")
    return (
        order.get("status") == "ACTIVE"
        and delay is not None
        and delay >= 10
    )
