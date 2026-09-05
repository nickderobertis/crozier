

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_pagination import ApiPagination
from .endpoint_post_users_searches_data_item import EndpointPostUsersSearchesDataItem


class EndpointPostUsersSearches(UniversalBaseModel):
    data: typing.Optional[typing.List[EndpointPostUsersSearchesDataItem]] = None
    pagination: typing.Optional[ApiPagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
