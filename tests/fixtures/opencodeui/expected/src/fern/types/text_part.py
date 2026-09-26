

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .text_part_time import TextPartTime


class TextPart(UniversalBaseModel):
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    text: str
    synthetic: typing.Optional[bool] = None
    ignored: typing.Optional[bool] = None
    time: typing.Optional[TextPartTime] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
