

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .trace_list_response_data_item_attributes_item import TraceListResponseDataItemAttributesItem
from .trace_list_response_data_item_status import TraceListResponseDataItemStatus


class TraceListResponseDataItem(UniversalBaseModel):
    trace_id: typing_extensions.Annotated[str, FieldMetadata(alias="traceId"), pydantic.Field(alias="traceId")]
    name: str
    start_time_unix_nano: typing_extensions.Annotated[
        str, FieldMetadata(alias="startTimeUnixNano"), pydantic.Field(alias="startTimeUnixNano")
    ]
    end_time_unix_nano: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="endTimeUnixNano"),
        pydantic.Field(alias="endTimeUnixNano", description="0 if trace is unfinished"),
    ]
    """
    0 if trace is unfinished
    """

    attributes: typing.List[TraceListResponseDataItemAttributesItem]
    status: TraceListResponseDataItemStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
