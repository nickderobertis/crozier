

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_response import BaseResponse
from .sms_inbox_response_messages_item import SmsInboxResponseMessagesItem


class SmsInboxResponse(BaseResponse):
    messages: typing.Optional[typing.List[SmsInboxResponseMessagesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
