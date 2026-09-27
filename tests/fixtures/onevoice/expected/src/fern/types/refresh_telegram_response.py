

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .refresh_telegram_response_linked_group_status import RefreshTelegramResponseLinkedGroupStatus


class RefreshTelegramResponse(UniversalBaseModel):
    linked_chat_id: int
    linked_group_status: RefreshTelegramResponseLinkedGroupStatus
    channel_title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
