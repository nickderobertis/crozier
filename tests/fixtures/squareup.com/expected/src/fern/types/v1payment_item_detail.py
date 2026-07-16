

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1PaymentItemDetail(UniversalBaseModel):
    """
    V1PaymentItemDetail
    """

    category_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the item's merchant-defined category, if any.
    """

    item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the item purchased, if any.
    """

    item_variation_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the item variation purchased, if any.
    """

    sku: typing.Optional[str] = pydantic.Field(default=None)
    """
     The item's merchant-defined SKU, if any.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
