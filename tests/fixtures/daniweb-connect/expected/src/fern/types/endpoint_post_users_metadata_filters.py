

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_pagination import ApiPagination
from .endpoint_post_users_metadata_filters_data_item import EndpointPostUsersMetadataFiltersDataItem


class EndpointPostUsersMetadataFilters(UniversalBaseModel):
    data: typing.Optional[typing.List[EndpointPostUsersMetadataFiltersDataItem]] = None
    pagination: typing.Optional[ApiPagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
