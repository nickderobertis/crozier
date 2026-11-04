

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaginationMetadata(UniversalBaseModel):
    """
    Metadata about a paginated response
    """

    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    Current page number
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of items per page
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of items
    """

    total_pages: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of pages
    """

    has_next: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether there is a next page
    """

    has_previous: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether there is a previous page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
