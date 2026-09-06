

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_redirects_response_pagination import ListRedirectsResponsePagination
from .list_redirects_response_redirects_item import ListRedirectsResponseRedirectsItem


class ListRedirectsResponse(UniversalBaseModel):
    """
    Site redirects response
    """

    redirects: typing.Optional[typing.List[ListRedirectsResponseRedirectsItem]] = pydantic.Field(default=None)
    """
    List of redirects for a given site
    """

    pagination: typing.Optional[ListRedirectsResponsePagination] = pydantic.Field(default=None)
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
