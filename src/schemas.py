from pydantic import BaseModel, Field, PositiveFloat, computed_field


class CapacityCompany(BaseModel):
    name: str
    units: list["CapacityMarketUnit"]


class CapacityMarketUnit(BaseModel):
    cmu_id: str
    name: str
    capacity: float = Field(gt=0)
    min_acceptable_price: float = Field(default=0, ge=0)

    def model_post_init(self, __context) -> None:
        if "min_acceptable_price" not in self.model_fields_set:
            self.min_acceptable_price = self.calculate_initial_min_price()

    def calculate_initial_min_price(self) -> float:
        # TODO: replace with real logic
        # Despina to provide table of type (renewable/gas etc. and missing money)
        return 10.0

    def should_exit(self, current_auction_price: float) -> bool:

        return current_auction_price <= self.min_acceptable_price


class CapacityBuyer(BaseModel):
    name: str = "System Operator"
    target_capacity: PositiveFloat = Field(
        description="Capacity the buyer wants to procure, GW."
    )
    net_CONE: PositiveFloat = Field(description="Net cost of new entry.")

    @computed_field
    @property
    def price_cap(self) -> float:
        return 1.5 * self.net_CONE

    def demand_capacity(self, price_current: float) -> float:

        if price_current > self.price_cap:
            raise ValueError("Current price cannot exceed the auction cap.")

        if price_current < 0:
            raise ValueError("Current price cannot be negative.")

        if price_current > self.net_CONE:
            demand = (self.target_capacity - 1.5) + 1.5 * (
                price_current - self.price_cap
            ) / (self.net_CONE - self.price_cap)
        else:
            demand = self.target_capacity + 1.5 * (1 - price_current / self.net_CONE)

        return demand


class AuctionRound(BaseModel):
    round_number: int
    price: float
    active_capacity_mw: float
    exited_capacity_mw: float
    spare_capacity_mw: float
