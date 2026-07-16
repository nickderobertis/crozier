

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Statistics(UniversalBaseModel):
    active_devices: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activeDevices")] = None
    active_users: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activeUsers")] = None
    capture_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="captureTime")] = (
        pydantic.Field(default=None)
    )
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    messages_received: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="messagesReceived")] = None
    messages_stored: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="messagesStored")] = None
    requests: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
