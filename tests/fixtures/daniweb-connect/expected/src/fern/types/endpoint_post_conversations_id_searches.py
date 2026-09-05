

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .api_pagination import ApiPagination
from .endpoint_post_conversations_id_searches_data_item import EndpointPostConversationsIdSearchesDataItem


class EndpointPostConversationsIdSearches(UniversalBaseModel):
    data: typing.Optional[typing.List[EndpointPostConversationsIdSearchesDataItem]] = None
    pagination: typing.Optional[ApiPagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EndpointPostConversationsIdSearches)
