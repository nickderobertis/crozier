

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Item(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    String with the SKU ID in VTEX’s catalog.
    """

    price: int = pydantic.Field()
    """
    Integer with the SKU’s unit price. If the value is `USD110.50`, convert it to the format → `11050`.
    """

    quantity: int = pydantic.Field()
    """
    Integer with the quantity of the SKU present in the order. The value should be greater than zero.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
