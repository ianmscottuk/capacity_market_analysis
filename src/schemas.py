from pydantic import BaseModel, Field


class CapacityMarketUnit(BaseModel):
    cmu_id: str
    name: str
    parent_company: str
    capacity_mw: float = Field(gt=0)
    min_acceptable_price: float = Field(ge=0)
    is_price_taker: bool

    def can_exit_at_price(
        self, current_auction_price: float, price_taker_threshold: float
    ) -> bool:
        return current_auction_price <= self.min_acceptable_price
