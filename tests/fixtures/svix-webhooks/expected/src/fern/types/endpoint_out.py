

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EndpointOut(UniversalBaseModel):
    channels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of message channels this endpoint listens to (omit for all)
    """

    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    description: str = pydantic.Field()
    """
    An example endpoint name
    """

    disabled: typing.Optional[bool] = None
    event_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="eventTypes"), pydantic.Field(alias="eventTypes")
    ] = None
    id: str
    metadata: typing.Dict[str, str]
    throttle_rate: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="throttleRate"),
        pydantic.Field(
            alias="throttleRate",
            description="Maximum messages per second to send to this endpoint.\n\nOutgoing messages will be throttled to this rate.",
        ),
    ] = None
    """
    Maximum messages per second to send to this endpoint.
    
    Outgoing messages will be throttled to this rate.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional unique identifier for the endpoint
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
