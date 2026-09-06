

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_pages_response_pages_item import ListPagesResponsePagesItem
from .list_pages_response_pagination import ListPagesResponsePagination


class ListPagesResponse(UniversalBaseModel):
    """
    The Page object
    """

    pages: typing.Optional[typing.List[ListPagesResponsePagesItem]] = None
    pagination: typing.Optional[ListPagesResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
