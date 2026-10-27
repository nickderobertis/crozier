

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chat_message_reactions_item_user import ChatMessageReactionsItemUser


class ChatMessageReactionsItem(UniversalBaseModel):
    reaction_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="reactionType"), pydantic.Field(alias="reactionType")
    ] = None
    created_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdDateTime"), pydantic.Field(alias="createdDateTime")
    ] = None
    user: typing.Optional[ChatMessageReactionsItemUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
