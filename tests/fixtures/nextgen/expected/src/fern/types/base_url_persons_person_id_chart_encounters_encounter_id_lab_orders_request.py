

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdLabOrdersRequest(UniversalBaseModel):
    test_location_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="TestLocationId"), pydantic.Field(alias="TestLocationId")
    ]
    ordering_provider: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderingProvider"), pydantic.Field(alias="OrderingProvider")
    ]
    ordered_elsewhere: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderedElsewhere"), pydantic.Field(alias="OrderedElsewhere")
    ]
    copy_to_providers: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="CopyToProviders"), pydantic.Field(alias="CopyToProviders")
    ]
    payers: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="Payers"), pydantic.Field(alias="Payers")]
    general_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="GeneralComment"), pydantic.Field(alias="GeneralComment")
    ]
    order_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderComment"), pydantic.Field(alias="OrderComment")
    ]
    patient_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="PatientComment"), pydantic.Field(alias="PatientComment")
    ]
    cancel_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="CancelReason"), pydantic.Field(alias="CancelReason")
    ]
    clinical_info: typing_extensions.Annotated[
        str, FieldMetadata(alias="ClinicalInfo"), pydantic.Field(alias="ClinicalInfo")
    ]
    lab_id: typing_extensions.Annotated[str, FieldMetadata(alias="LabId"), pydantic.Field(alias="LabId")]
    generated_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="GeneratedBy"), pydantic.Field(alias="GeneratedBy")
    ]
    billing_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="BillingType"), pydantic.Field(alias="BillingType")
    ]
    order_control: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderControl"), pydantic.Field(alias="OrderControl")
    ]
    order_priority: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderPriority"), pydantic.Field(alias="OrderPriority")
    ]
    abn_code: typing_extensions.Annotated[str, FieldMetadata(alias="AbnCode"), pydantic.Field(alias="AbnCode")]
    specimen_action: typing_extensions.Annotated[
        str, FieldMetadata(alias="SpecimenAction"), pydantic.Field(alias="SpecimenAction")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
