

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class OrderLineItemModifier(UniversalBaseModel):
    """
    A [CatalogModifier](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifier).
    """

    base_price_money: typing.Optional[Money] = None
    catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The catalog object ID referencing [CatalogModifier](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifier).
    """

    catalog_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the catalog object that this modifier references.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the item modifier.
    """

    total_price_money: typing.Optional[Money] = None
    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the modifier only within this order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
