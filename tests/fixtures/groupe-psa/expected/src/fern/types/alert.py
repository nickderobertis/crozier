

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .alert_end_position import AlertEndPosition
from .alert_links import AlertLinks
from .alert_msg_enum import AlertMsgEnum
from .alert_severity import AlertSeverity
from .alert_start_position import AlertStartPosition
from .created_at_field import CreatedAtField
from .updated_at_field import UpdatedAtField
from .vin import Vin


class Alert(CreatedAtField, UpdatedAtField):
    links: typing_extensions.Annotated[AlertLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    id: str
    vin: Vin
    active: bool
    type: AlertMsgEnum
    severity: typing.Optional[AlertSeverity] = pydantic.Field(default=None)
    """
    Alert severity level.
    
    |Severity|Description|
    |:---|:---|
    |Information|Better to fix but it is operating accurately.|
    |Warning|Should fix it asap.|
    |Critical|Starting prohibited without repair.|
    """

    started_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ]
    end_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endAt"), pydantic.Field(alias="endAt")
    ] = None
    start_position: typing_extensions.Annotated[
        typing.Optional[AlertStartPosition], FieldMetadata(alias="startPosition"), pydantic.Field(alias="startPosition")
    ] = None
    end_position: typing_extensions.Annotated[
        typing.Optional[AlertEndPosition], FieldMetadata(alias="endPosition"), pydantic.Field(alias="endPosition")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
