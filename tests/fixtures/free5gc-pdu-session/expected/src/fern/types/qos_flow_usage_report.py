

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QosFlowUsageReport(UniversalBaseModel):
    qfi: int
    start_time_stamp: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="startTimeStamp"), pydantic.Field(alias="startTimeStamp")
    ]
    end_time_stamp: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="endTimeStamp"), pydantic.Field(alias="endTimeStamp")
    ]
    downlink_volume: typing_extensions.Annotated[
        int, FieldMetadata(alias="downlinkVolume"), pydantic.Field(alias="downlinkVolume")
    ]
    uplink_volume: typing_extensions.Annotated[
        int, FieldMetadata(alias="uplinkVolume"), pydantic.Field(alias="uplinkVolume")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
