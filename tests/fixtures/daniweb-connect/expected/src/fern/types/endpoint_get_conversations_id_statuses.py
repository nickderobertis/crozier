

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_get_conversations_id_statuses_data_item import EndpointGetConversationsIdStatusesDataItem


class EndpointGetConversationsIdStatuses(UniversalBaseModel):
    data: typing.Optional[typing.List[EndpointGetConversationsIdStatusesDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EndpointGetConversationsIdStatuses)
