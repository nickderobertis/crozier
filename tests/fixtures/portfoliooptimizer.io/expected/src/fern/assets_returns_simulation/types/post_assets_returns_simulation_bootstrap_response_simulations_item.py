

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_assets_returns_simulation_bootstrap_response_simulations_item_assets_item import (
    PostAssetsReturnsSimulationBootstrapResponseSimulationsItemAssetsItem,
)


class PostAssetsReturnsSimulationBootstrapResponseSimulationsItem(UniversalBaseModel):
    assets: typing.List[PostAssetsReturnsSimulationBootstrapResponseSimulationsItemAssetsItem] = pydantic.Field()
    """
    assets[i] is the data for the i-th asset
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
