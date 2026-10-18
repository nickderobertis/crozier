

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .broadcast_request_message_parts_item import BroadcastRequestMessagePartsItem


class BroadcastRequestMessage(UniversalBaseModel):
    channel: str
    parts: typing.List[BroadcastRequestMessagePartsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
