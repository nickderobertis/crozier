

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EventSession(UniversalBaseModel):
    """
    The session the event occured within.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the session
    """

    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    The duration of the session.
    """

    start_timestamp: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startTimestamp"),
        pydantic.Field(
            alias="startTimestamp",
            description="The time the event started in ISO 8601 standard date time format. For example, 2014-06-30T19:07:47.885Z",
        ),
    ] = None
    """
    The time the event started in ISO 8601 standard date time format. For example, 2014-06-30T19:07:47.885Z
    """

    stop_timestamp: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="stopTimestamp"),
        pydantic.Field(
            alias="stopTimestamp",
            description="The time the event terminated in ISO 8601 standard date time format. For example, 2014-06-30T19:07:47.885Z",
        ),
    ] = None
    """
    The time the event terminated in ISO 8601 standard date time format. For example, 2014-06-30T19:07:47.885Z
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
