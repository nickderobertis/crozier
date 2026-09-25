

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartLabOrdersOrderIdRequest(UniversalBaseModel):
    lab_id: typing_extensions.Annotated[str, FieldMetadata(alias="LabId"), pydantic.Field(alias="LabId")]
    test_location: typing_extensions.Annotated[
        str, FieldMetadata(alias="TestLocation"), pydantic.Field(alias="TestLocation")
    ]
    ordering_provider: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderingProvider"), pydantic.Field(alias="OrderingProvider")
    ]
    nextgen_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="NextgenStatus"), pydantic.Field(alias="NextgenStatus")
    ]
    order_control: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderControl"), pydantic.Field(alias="OrderControl")
    ]
    order_priority: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderPriority"), pydantic.Field(alias="OrderPriority")
    ]
    specimen_action_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="SpecimenActionCode"), pydantic.Field(alias="SpecimenActionCode")
    ]
    billing_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="BillingType"), pydantic.Field(alias="BillingType")
    ]
    clinical_information: typing_extensions.Annotated[
        str, FieldMetadata(alias="ClinicalInformation"), pydantic.Field(alias="ClinicalInformation")
    ]
    cancel_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="CancelReason"), pydantic.Field(alias="CancelReason")
    ]
    general_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="GeneralComment"), pydantic.Field(alias="GeneralComment")
    ]
    order_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderComment"), pydantic.Field(alias="OrderComment")
    ]
    patient_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="PatientComment"), pydantic.Field(alias="PatientComment")
    ]
    is_ordered_else_where: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsOrderedElseWhere"), pydantic.Field(alias="IsOrderedElseWhere")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
