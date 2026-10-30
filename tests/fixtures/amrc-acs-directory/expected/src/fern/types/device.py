

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sparkplug_name import SparkplugName
from .uuid_list import UuidList


class Device(UniversalBaseModel):
    """
    A description of a single Sparkplug device. If deviceId is present the device is a Sparkplug Device, otherwise it is an EON Node. online indicates if the device is online at the moment. lastChange indicates the last time a BIRTH or DEATH was seen. schemas is a list of all schemas used by the most recent birth certificate.
    """

    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    group_id: SparkplugName
    node_id: SparkplugName
    device_id: typing.Optional[SparkplugName] = None
    online: bool
    last_change: dt.datetime
    schemas: UuidList
    top_schema: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
