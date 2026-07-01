from pydantic import BaseModel, Field, PositiveFloat, computed_field


class CapacityMarketUnit(BaseModel):
    cmu_id: str
    name: str
    parent_company: str
    capacity_mw: float = Field(gt=0)
    is_price_taker: bool

    min_acceptable_price: float = Field(default=0, ge=0)

    def model_post_init(self, __context) -> None:
        if "min_acceptable_price" not in self.model_fields_set:
            self.min_acceptable_price = self.calculate_initial_min_price()

    def calculate_initial_min_price(self) -> float:
        # TODO: replace with real logic
        # Despina to provide table of type (renewable/gas etc. and missing money)
        return 10.0

    def exit_at_price(self, current_auction_price: float) -> bool:
        return current_auction_price <= self.min_acceptable_price


class CapacityBuyer(BaseModel):
    name: str = "System Operator"
    target_capacity_mw: PositiveFloat = Field(
        description="Capacity the buyer wants to procure."
    )
    net_CONE: PositiveFloat = Field(description="Net cost of new entry.")

    @computed_field
    @property
    def price_cap_per_kw_year(self) -> float:
        return 1.5 * self.net_CONE

    def spare_capacity(self, active_capacity_mw: float) -> float:
        return active_capacity_mw - self.target_capacity_mw


class AuctionRound(BaseModel):
    round_number: int
    price: float
    active_capacity_mw: float
    exited_capacity_mw: float
    spare_capacity_mw: float
