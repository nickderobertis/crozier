

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bot_summary import BotSummary


class ManagedBotResponse(UniversalBaseModel):
    bot: BotSummary
    channel_id: typing_extensions.Annotated[str, FieldMetadata(alias="channelId"), pydantic.Field(alias="channelId")]
    setup_pending: typing_extensions.Annotated[
        bool, FieldMetadata(alias="setupPending"), pydantic.Field(alias="setupPending")
    ]
    message: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
