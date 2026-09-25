

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok57(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    order_type: typing_extensions.Annotated[str, FieldMetadata(alias="orderType"), pydantic.Field(alias="orderType")]
    is_future_order: typing_extensions.Annotated[
        str, FieldMetadata(alias="isFutureOrder"), pydantic.Field(alias="isFutureOrder")
    ]
    schedule_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="scheduleType"), pydantic.Field(alias="scheduleType")
    ]
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")]
    end_date: typing_extensions.Annotated[str, FieldMetadata(alias="endDate"), pydantic.Field(alias="endDate")]
    interval: str
    timespan: str
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    next_due_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="nextDueDate"), pydantic.Field(alias="nextDueDate")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    is_auto_releasable: typing_extensions.Annotated[
        str, FieldMetadata(alias="isAutoReleasable"), pydantic.Field(alias="isAutoReleasable")
    ]
    max_occurrence: typing_extensions.Annotated[
        str, FieldMetadata(alias="maxOccurrence"), pydantic.Field(alias="maxOccurrence")
    ]
    stop_date: typing_extensions.Annotated[str, FieldMetadata(alias="stopDate"), pydantic.Field(alias="stopDate")]
    stop_reason: typing_extensions.Annotated[str, FieldMetadata(alias="stopReason"), pydantic.Field(alias="stopReason")]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
