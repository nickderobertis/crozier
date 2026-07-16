

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogQueryText(UniversalBaseModel):
    """
    The query filter to return the search result whose searchable attribute values contain all of the specified keywords or tokens, independent of the token order or case.
    """

    keywords: typing.List[str] = pydantic.Field()
    """
    A list of 1, 2, or 3 search keywords. Keywords with fewer than 3 characters are ignored.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
