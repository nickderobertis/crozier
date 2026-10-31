

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sparkplug_name import SparkplugName
from .uuid_list import UuidList


class Session(UniversalBaseModel):
    """
    A record describing a single device session (the period between a BIRTH and a DEATH or reBIRTH). If finish is not present the session has not yet ended.
    """

    group_id: typing_extensions.Annotated[
        SparkplugName, FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ]
    node_id: typing_extensions.Annotated[SparkplugName, FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId")]
    device_id: typing_extensions.Annotated[
        typing.Optional[SparkplugName], FieldMetadata(alias="deviceId"), pydantic.Field(alias="deviceId")
    ] = None
    start: dt.datetime
    finish: typing.Optional[dt.datetime] = None
    death: typing.Optional[bool] = None
    schemas: typing.Optional[UuidList] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
