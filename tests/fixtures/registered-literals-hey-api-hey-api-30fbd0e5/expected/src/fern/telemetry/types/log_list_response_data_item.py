

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .log_list_response_data_item_attributes_item import LogListResponseDataItemAttributesItem
from .log_list_response_data_item_body import LogListResponseDataItemBody


class LogListResponseDataItem(UniversalBaseModel):
    time_unix_nano: typing_extensions.Annotated[
        str, FieldMetadata(alias="timeUnixNano"), pydantic.Field(alias="timeUnixNano")
    ]
    body: LogListResponseDataItemBody
    trace_id: typing_extensions.Annotated[str, FieldMetadata(alias="traceId"), pydantic.Field(alias="traceId")]
    attributes: typing.List[LogListResponseDataItemAttributesItem]
    severity_text: typing_extensions.Annotated[
        str, FieldMetadata(alias="severityText"), pydantic.Field(alias="severityText")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
