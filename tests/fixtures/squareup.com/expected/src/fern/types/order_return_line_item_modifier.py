

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class OrderReturnLineItemModifier(UniversalBaseModel):
    """
    A line item modifier being returned.
    """

    base_price_money: typing.Optional[Money] = None
    catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The catalog object ID referencing [CatalogModifier](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifier).
    """

    catalog_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the catalog object that this line item modifier references.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the item modifier.
    """

    source_modifier_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The modifier `uid` from the order's line item that contains the
    original sale of this line item modifier.
    """

    total_price_money: typing.Optional[Money] = None
    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the return modifier only within this order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
