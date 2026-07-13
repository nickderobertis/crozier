

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stream_info import StreamInfo


class GlobalAlert(UniversalBaseModel):
    alert_html: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="AlertHtml")] = None
    alert_key: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="AlertKey")] = None
    alert_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="AlertLevel")] = None
    alert_link: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="AlertLink")] = None
    alert_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="AlertTimestamp")
    ] = None
    alert_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="AlertType")] = None
    stream_info: typing_extensions.Annotated[typing.Optional[StreamInfo], FieldMetadata(alias="StreamInfo")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
