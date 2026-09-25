from typing import TypedDict


class Order(TypedDict):
    order_id: str
    status: str
    promised_eta: str
    current_eta: str | None
    estimated_delay_minutes: int | None
    restaurant_status: str
    driver_status: str
    support_opened: bool
    previous_intervention: str | None
