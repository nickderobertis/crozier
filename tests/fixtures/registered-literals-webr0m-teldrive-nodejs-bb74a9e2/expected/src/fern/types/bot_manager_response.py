

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bot_manager_response_pending_item import BotManagerResponsePendingItem
from .bot_summary import BotSummary


class BotManagerResponse(UniversalBaseModel):
    configured: bool
    supported: typing.Optional[bool] = None
    bot: typing.Optional[BotSummary] = None
    pending: typing.List[BotManagerResponsePendingItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
