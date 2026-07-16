

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_portfolio_simulation_rebalancing_fixed_weight_response_portfolios_item import (
    PostPortfolioSimulationRebalancingFixedWeightResponsePortfoliosItem,
)


class PostPortfolioSimulationRebalancingFixedWeightResponse(UniversalBaseModel):
    portfolios: typing.List[PostPortfolioSimulationRebalancingFixedWeightResponsePortfoliosItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
