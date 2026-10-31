

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemTotalsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total ID.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total name.
    """

    value: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
