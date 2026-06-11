from pydantic import BaseModel, Field, PositiveFloat


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


class CapacityBuyer(BaseModel):
    name: str = "System Operator"
    target_capacity_mw: PositiveFloat = Field(
        description="Capacity the buyer wants to procure."
    )
    price_cap_per_kw_year: PositiveFloat = Field(description="Maximum auction price.")

    def spare_capacity(self, active_capacity_mw: float) -> float:
        return active_capacity_mw - self.target_capacity_mw


class AuctionRound(BaseModel):
    round_number: int
    price_cap: float
    price_floor: float
    active_capacity_mw: float
    exited_capacity_mw: float
