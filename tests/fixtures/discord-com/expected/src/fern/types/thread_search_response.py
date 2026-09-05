

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_response import MessageResponse
from .thread_member_response import ThreadMemberResponse
from .thread_response import ThreadResponse


class ThreadSearchResponse(UniversalBaseModel):
    threads: typing.List[ThreadResponse]
    members: typing.List[ThreadMemberResponse]
    has_more: typing.Optional[bool] = None
    first_messages: typing.Optional[typing.List[MessageResponse]] = None
    total_results: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
