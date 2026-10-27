

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChatViewpoint(UniversalBaseModel):
    is_hidden: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")
    ] = None
    last_message_read_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastMessageReadDateTime"),
        pydantic.Field(alias="lastMessageReadDateTime"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
