

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stream_info import StreamInfo


class GlobalAlert(UniversalBaseModel):
    alert_html: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="AlertHtml"), pydantic.Field(alias="AlertHtml")
    ] = None
    alert_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="AlertKey"), pydantic.Field(alias="AlertKey")
    ] = None
    alert_level: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="AlertLevel"), pydantic.Field(alias="AlertLevel")
    ] = None
    alert_link: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="AlertLink"), pydantic.Field(alias="AlertLink")
    ] = None
    alert_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="AlertTimestamp"), pydantic.Field(alias="AlertTimestamp")
    ] = None
    alert_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="AlertType"), pydantic.Field(alias="AlertType")
    ] = None
    stream_info: typing_extensions.Annotated[
        typing.Optional[StreamInfo], FieldMetadata(alias="StreamInfo"), pydantic.Field(alias="StreamInfo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
