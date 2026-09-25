

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok53(UniversalBaseModel):
    id: str
    test_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="testDescription"), pydantic.Field(alias="testDescription")
    ]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
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
    ordering_provider: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderingProvider"), pydantic.Field(alias="orderingProvider")
    ]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    order_date: typing_extensions.Annotated[str, FieldMetadata(alias="orderDate"), pydantic.Field(alias="orderDate")]
    order_date_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderDateTimezone"), pydantic.Field(alias="orderDateTimezone")
    ]
    sign_off_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffDate"), pydantic.Field(alias="signOffDate")
    ]
    sign_off_person: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffPerson"), pydantic.Field(alias="signOffPerson")
    ]
    test_status: typing_extensions.Annotated[str, FieldMetadata(alias="testStatus"), pydantic.Field(alias="testStatus")]
    nextgen_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="nextgenStatus"), pydantic.Field(alias="nextgenStatus")
    ]
    lab_id: typing_extensions.Annotated[str, FieldMetadata(alias="labId"), pydantic.Field(alias="labId")]
    signoff_comments_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="signoffCommentsIndicator"), pydantic.Field(alias="signoffCommentsIndicator")
    ]
    documents_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="documentsIndicator"), pydantic.Field(alias="documentsIndicator")
    ]
    order_control: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderControl"), pydantic.Field(alias="orderControl")
    ]
    order_priority: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderPriority"), pydantic.Field(alias="orderPriority")
    ]
    time_entered: typing_extensions.Annotated[
        str, FieldMetadata(alias="timeEntered"), pydantic.Field(alias="timeEntered")
    ]
    specimen_action_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="specimenActionCode"), pydantic.Field(alias="specimenActionCode")
    ]
    billing_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="billingType"), pydantic.Field(alias="billingType")
    ]
    clinical_information: typing_extensions.Annotated[
        str, FieldMetadata(alias="clinicalInformation"), pydantic.Field(alias="clinicalInformation")
    ]
    cancel_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="cancelReason"), pydantic.Field(alias="cancelReason")
    ]
    intrf_message: typing_extensions.Annotated[
        str, FieldMetadata(alias="intrfMessage"), pydantic.Field(alias="intrfMessage")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    provider_display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="providerDisplayName"), pydantic.Field(alias="providerDisplayName")
    ]
    location_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="locationName"), pydantic.Field(alias="locationName")
    ]
    address_line1: typing_extensions.Annotated[
        str, FieldMetadata(alias="addressLine1"), pydantic.Field(alias="addressLine1")
    ]
    address_line2: typing_extensions.Annotated[
        str, FieldMetadata(alias="addressLine2"), pydantic.Field(alias="addressLine2")
    ]
    city: str
    state: str
    zip: str
    phone: str
    fax: str
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    middle_initial: typing_extensions.Annotated[
        str, FieldMetadata(alias="middleInitial"), pydantic.Field(alias="middleInitial")
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
    general_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="generalComment"), pydantic.Field(alias="generalComment")
    ]
    order_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderComment"), pydantic.Field(alias="orderComment")
    ]
    patient_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientComment"), pydantic.Field(alias="patientComment")
    ]
    is_ordered_else_where: typing_extensions.Annotated[
        str, FieldMetadata(alias="isOrderedElseWhere"), pydantic.Field(alias="isOrderedElseWhere")
    ]
    is_completed: typing_extensions.Annotated[
        str, FieldMetadata(alias="isCompleted"), pydantic.Field(alias="isCompleted")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
