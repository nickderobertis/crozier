

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderOrderProductItemsItem(UniversalBaseModel):
    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency code representing the currency for this specific item.
    """

    item_price: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unit price for this specific item.
    """

    product_retailer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the specific product being ordered.
    """

    quantity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The quantity ordered for this specific item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
