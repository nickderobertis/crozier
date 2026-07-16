

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogQueryItemVariationsForItemOptionValues(UniversalBaseModel):
    """
    The query filter to return the item variations containing the specified item option value IDs.
    """

    item_option_value_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A set of `CatalogItemOptionValue` IDs to be used to find associated
    `CatalogItemVariation`s. All ItemVariations that contain all of the given
    Item Option Values (in any order) will be returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
