

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogCategory(UniversalBaseModel):
    """
    A category to which a `CatalogItem` instance belongs.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The category name. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
