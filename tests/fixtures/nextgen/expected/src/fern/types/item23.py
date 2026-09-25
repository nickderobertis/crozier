

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item23(UniversalBaseModel):
    id: str
    test_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="testDescription"), pydantic.Field(alias="testDescription")
    ]
    test_status: typing_extensions.Annotated[str, FieldMetadata(alias="testStatus"), pydantic.Field(alias="testStatus")]
    nextgen_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="nextgenStatus"), pydantic.Field(alias="nextgenStatus")
    ]
    lab_id: typing_extensions.Annotated[str, FieldMetadata(alias="labId"), pydantic.Field(alias="labId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    ufo_number: typing_extensions.Annotated[str, FieldMetadata(alias="ufoNumber"), pydantic.Field(alias="ufoNumber")]
    generated_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="generatedBy"), pydantic.Field(alias="generatedBy")
    ]
    order_type: typing_extensions.Annotated[str, FieldMetadata(alias="orderType"), pydantic.Field(alias="orderType")]
    test_location: typing_extensions.Annotated[
        str, FieldMetadata(alias="testLocation"), pydantic.Field(alias="testLocation")
    ]
    order_control: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderControl"), pydantic.Field(alias="orderControl")
    ]
    order_priority: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderPriority"), pydantic.Field(alias="orderPriority")
    ]
    ordering_provider: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderingProvider"), pydantic.Field(alias="orderingProvider")
    ]
    order_date: typing_extensions.Annotated[str, FieldMetadata(alias="orderDate"), pydantic.Field(alias="orderDate")]
    order_date_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderDateTimezone"), pydantic.Field(alias="orderDateTimezone")
    ]
    sign_off_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffDate"), pydantic.Field(alias="signOffDate")
    ]
    intrf_message: typing_extensions.Annotated[
        str, FieldMetadata(alias="intrfMessage"), pydantic.Field(alias="intrfMessage")
    ]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    sign_off_person: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffPerson"), pydantic.Field(alias="signOffPerson")
    ]
    is_future_order: typing_extensions.Annotated[
        str, FieldMetadata(alias="isFutureOrder"), pydantic.Field(alias="isFutureOrder")
    ]
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")]
    next_due_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="nextDueDate"), pydantic.Field(alias="nextDueDate")
    ]
    expected_result_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="expectedResultDate"), pydantic.Field(alias="expectedResultDate")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
