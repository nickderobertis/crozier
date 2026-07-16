

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogItemOptionValueForItemVariation(UniversalBaseModel):
    """
    A `CatalogItemOptionValue` links an item variation to an item option as
    an item option value. For example, a t-shirt item may offer a color option and
    a size option. An item option value would represent each variation of t-shirt:
    For example, "Color:Red, Size:Small" or "Color:Blue, Size:Medium".
    """

    item_option_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id of an item option.
    """

    item_option_value_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id of the selected value for the item option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
