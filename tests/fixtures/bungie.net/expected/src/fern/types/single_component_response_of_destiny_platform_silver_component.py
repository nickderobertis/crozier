

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_components_inventory_destiny_platform_silver_component import (
    DestinyComponentsInventoryDestinyPlatformSilverComponent,
)


class SingleComponentResponseOfDestinyPlatformSilverComponent(UniversalBaseModel):
    data: typing.Optional[DestinyComponentsInventoryDestinyPlatformSilverComponent] = None
    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, this component is disabled.
    """

    privacy: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
