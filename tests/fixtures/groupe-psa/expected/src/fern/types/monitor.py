

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .monitor_id import MonitorId
from .monitor_links import MonitorLinks
from .monitor_parameter import MonitorParameter
from .monitor_status import MonitorStatus


class Monitor(UniversalBaseModel):
    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Date when the resource has been created."),
    ]
    """
    Date when the resource has been created.
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    links: typing_extensions.Annotated[MonitorLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    monitor_id: typing_extensions.Annotated[
        MonitorId, FieldMetadata(alias="monitorId"), pydantic.Field(alias="monitorId")
    ]
    monitor: MonitorParameter
    status: MonitorStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
