

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LogTraceSpanToolCallsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tool-call identifier.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Invoked tool name.
    """

    arguments: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Arguments supplied to the tool call.
    """

    result: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Value returned by the tool call.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tool-call error message.
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="ISO 8601 tool-call start timestamp."),
    ] = None
    """
    ISO 8601 tool-call start timestamp.
    """

    end_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endTime"),
        pydantic.Field(alias="endTime", description="ISO 8601 tool-call end timestamp."),
    ] = None
    """
    ISO 8601 tool-call end timestamp.
    """

    duration: typing.Optional[float] = pydantic.Field(default=None)
    """
    Tool-call duration in milliseconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
