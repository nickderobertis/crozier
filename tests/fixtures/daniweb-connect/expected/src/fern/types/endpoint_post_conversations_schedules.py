

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .api_pagination import ApiPagination
from .endpoint_post_conversations_schedules_data_item import EndpointPostConversationsSchedulesDataItem


class EndpointPostConversationsSchedules(UniversalBaseModel):
    data: typing.Optional[typing.List[EndpointPostConversationsSchedulesDataItem]] = None
    pagination: typing.Optional[ApiPagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EndpointPostConversationsSchedules)
