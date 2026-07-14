

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaginationProperties(UniversalBaseModel):
    """
    Properties for common pagination handling to be included in any wrapping object that needs pagination elements
    """

    next_page: typing.Optional[str] = pydantic.Field(default=None)
    """
    True if additional pages exist (page + 1) or False if this is the last page
    """

    page: typing.Optional[str] = pydantic.Field(default=None)
    """
    The page number returned (should match the requested page query string param)
    """

    returned_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of items sent in this response
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
