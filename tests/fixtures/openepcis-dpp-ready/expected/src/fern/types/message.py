

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_type_enum import MessageTypeEnum
from .timestamp import Timestamp


class Message(UniversalBaseModel):
    """
    A result message (EN 18222 Table 13).
    """

    message_type: typing_extensions.Annotated[
        MessageTypeEnum, FieldMetadata(alias="messageType"), pydantic.Field(alias="messageType")
    ]
    text: str = pydantic.Field()
    """
    The message text.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Technology-dependent status or error code.
    """

    correlation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="correlationId"),
        pydantic.Field(alias="correlationId", description="Identifier relating messages across systems."),
    ] = None
    """
    Identifier relating messages across systems.
    """

    timestamp: typing.Optional[Timestamp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
