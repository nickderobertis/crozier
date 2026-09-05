

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_post_users_searches_data_item_relevance import EndpointPostUsersSearchesDataItemRelevance
from .user import User


class EndpointPostUsersSearchesDataItem(UniversalBaseModel):
    relevance: typing.Optional[EndpointPostUsersSearchesDataItemRelevance] = None
    user: typing.Optional[User] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
