

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogQueryItemsForItemOptions(UniversalBaseModel):
    """
    The query filter to return the items containing the specified item option IDs.
    """

    item_option_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A set of `CatalogItemOption` IDs to be used to find associated
    `CatalogItem`s. All Items that contain all of the given Item Options (in any order)
    will be returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
