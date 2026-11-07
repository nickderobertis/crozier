

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChangeLogEntry(UniversalBaseModel):
    """
    A changelog entry
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id of the changelog entry
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The message as template or rendered as plain text
    """

    message_properties: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="messageProperties"),
        pydantic.Field(
            alias="messageProperties",
            description="The values of the properties in the message. May be nested as object with a value field ",
        ),
    ] = None
    """
    The values of the properties in the message. May be nested as object with a value field 
    """

    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UTC unix timestamp when this change occurred
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
