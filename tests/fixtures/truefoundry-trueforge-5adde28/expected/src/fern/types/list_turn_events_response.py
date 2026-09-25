

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_event import SessionEvent
from .token_pagination import TokenPagination


class ListTurnEventsResponse(UniversalBaseModel):
    data: typing.List[SessionEvent]
    pagination: TokenPagination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
