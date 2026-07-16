

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class CatalogModifier(UniversalBaseModel):
    """
    A modifier applicable to items at the time of sale.
    """

    modifier_list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the `CatalogModifierList` associated with this modifier.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The modifier name.  This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points.
    """

    ordinal: typing.Optional[int] = pydantic.Field(default=None)
    """
    Determines where this `CatalogModifier` appears in the `CatalogModifierList`.
    """

    price_money: typing.Optional[Money] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
