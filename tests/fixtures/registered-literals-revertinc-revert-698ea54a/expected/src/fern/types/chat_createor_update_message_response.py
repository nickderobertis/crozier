

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .common_message import CommonMessage
from .common_response_status import CommonResponseStatus


class ChatCreateorUpdateMessageResponse(UniversalBaseModel):
    status: CommonResponseStatus
    result: CommonMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
