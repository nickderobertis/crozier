

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendInvoiceRequestItemsItem(UniversalBaseModel):
    """ """

    id: str = pydantic.Field()
    """
    SKU ID.
    """

    price: int = pydantic.Field()
    """
    Price of the item.
    """

    quantity: int = pydantic.Field()
    """
    Quantity of items of the SKU in the cart.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
