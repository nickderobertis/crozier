

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MessageOut(UniversalBaseModel):
    channels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of free-form identifiers that endpoints can filter by
    """

    event_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="eventId"),
        pydantic.Field(alias="eventId", description="Optional unique identifier for the message"),
    ] = None
    """
    Optional unique identifier for the message
    """

    event_type: typing_extensions.Annotated[str, FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")]
    id: str
    payload: typing.Dict[str, typing.Any]
    timestamp: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
