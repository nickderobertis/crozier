

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delete_redirects_response_pagination import DeleteRedirectsResponsePagination
from .delete_redirects_response_redirects_item import DeleteRedirectsResponseRedirectsItem


class DeleteRedirectsResponse(UniversalBaseModel):
    """
    Site redirects response
    """

    redirects: typing.Optional[typing.List[DeleteRedirectsResponseRedirectsItem]] = pydantic.Field(default=None)
    """
    List of redirects for a given site
    """

    pagination: typing.Optional[DeleteRedirectsResponsePagination] = pydantic.Field(default=None)
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
