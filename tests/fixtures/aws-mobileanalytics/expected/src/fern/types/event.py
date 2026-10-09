

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .double import Double
from .event_session import EventSession
from .string0to1000chars import String0To1000Chars


class Event(UniversalBaseModel):
    """
    A JSON object representing a batch of unique event occurrences in your app.
    """

    event_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="eventType"),
        pydantic.Field(
            alias="eventType",
            description="A name signifying an event that occurred in your app. This is used for grouping and aggregating like events together for reporting purposes.",
        ),
    ]
    """
    A name signifying an event that occurred in your app. This is used for grouping and aggregating like events together for reporting purposes.
    """

    timestamp: str = pydantic.Field()
    """
    The time the event occurred in ISO 8601 standard date time format. For example, 2014-06-30T19:07:47.885Z
    """

    session: typing.Optional[EventSession] = pydantic.Field(default=None)
    """
    The session the event occured within. 
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the event.
    """

    attributes: typing.Optional[typing.Dict[str, String0To1000Chars]] = pydantic.Field(default=None)
    """
    <p>A collection of key-value pairs that give additional context to the event. The key-value pairs are specified by the developer.</p> <p>This collection can be empty or the attribute object can be omitted.</p>
    """

    metrics: typing.Optional[typing.Dict[str, Double]] = pydantic.Field(default=None)
    """
    <p>A collection of key-value pairs that gives additional, measurable context to the event. The key-value pairs are specified by the developer.</p> <p>This collection can be empty or the attribute object can be omitted.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
