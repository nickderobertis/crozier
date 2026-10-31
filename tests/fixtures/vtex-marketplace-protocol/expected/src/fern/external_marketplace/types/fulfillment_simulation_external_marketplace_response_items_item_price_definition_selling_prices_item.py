

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinitionSellingPricesItem(UniversalBaseModel):
    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    Rounding quantity, meaning how many items are rounded to this value.
    """

    value: typing.Optional[int] = pydantic.Field(default=None)
    """
    Value in cents for that specific rounding.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
