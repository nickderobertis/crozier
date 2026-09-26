

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_message_model import UserMessageModel
from .user_message_summary import UserMessageSummary
from .user_message_time import UserMessageTime


class UserMessage(UniversalBaseModel):
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    time: UserMessageTime
    summary: typing.Optional[UserMessageSummary] = None
    agent: str
    model: UserMessageModel
    system: typing.Optional[str] = None
    tools: typing.Optional[typing.Dict[str, bool]] = None
    variant: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
