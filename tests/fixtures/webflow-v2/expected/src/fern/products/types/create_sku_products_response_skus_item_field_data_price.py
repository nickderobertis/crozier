

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateSkuProductsResponseSkusItemFieldDataPrice(UniversalBaseModel):
    """
    price of SKU
    """

    value: typing.Optional[float] = pydantic.Field(default=None)
    """
    Price of SKU
    """

    unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency of Item
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency of Item (alternative representation)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
