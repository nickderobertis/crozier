

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdProceduresProcedureIdRequest(UniversalBaseModel):
    service_item_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceItemId"), pydantic.Field(alias="serviceItemId")
    ]
    service_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceDate"), pydantic.Field(alias="serviceDate")
    ]
    start_time: typing_extensions.Annotated[str, FieldMetadata(alias="startTime"), pydantic.Field(alias="startTime")]
    stop_time: typing_extensions.Annotated[str, FieldMetadata(alias="stopTime"), pydantic.Field(alias="stopTime")]
    amount: str
    place_of_service: typing_extensions.Annotated[
        str, FieldMetadata(alias="placeOfService"), pydantic.Field(alias="placeOfService")
    ]
    units: str
    rx_on_file_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="rxOnFileIndicator"), pydantic.Field(alias="rxOnFileIndicator")
    ]
    suppress_billing_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="suppressBillingIndicator"), pydantic.Field(alias="suppressBillingIndicator")
    ]
    national_drug_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="nationalDrugCode"), pydantic.Field(alias="nationalDrugCode")
    ]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    tooth: str
    surface: str
    quadrant: str
    patient_diagnosis_id1: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId1"), pydantic.Field(alias="patientDiagnosisId1")
    ]
    patient_diagnosis_id2: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId2"), pydantic.Field(alias="patientDiagnosisId2")
    ]
    patient_diagnosis_id3: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId3"), pydantic.Field(alias="patientDiagnosisId3")
    ]
    patient_diagnosis_id4: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId4"), pydantic.Field(alias="patientDiagnosisId4")
    ]
    patient_diagnosis_id5: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId5"), pydantic.Field(alias="patientDiagnosisId5")
    ]
    patient_diagnosis_id6: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId6"), pydantic.Field(alias="patientDiagnosisId6")
    ]
    patient_diagnosis_id7: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId7"), pydantic.Field(alias="patientDiagnosisId7")
    ]
    patient_diagnosis_id8: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId8"), pydantic.Field(alias="patientDiagnosisId8")
    ]
    patient_diagnosis_id9: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId9"), pydantic.Field(alias="patientDiagnosisId9")
    ]
    patient_diagnosis_id10: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId10"), pydantic.Field(alias="patientDiagnosisId10")
    ]
    patient_diagnosis_id11: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId11"), pydantic.Field(alias="patientDiagnosisId11")
    ]
    patient_diagnosis_id12: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientDiagnosisId12"), pydantic.Field(alias="patientDiagnosisId12")
    ]
    modifier_id1: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifierId1"), pydantic.Field(alias="modifierId1")
    ]
    modifier_id2: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifierId2"), pydantic.Field(alias="modifierId2")
    ]
    modifier_id3: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifierId3"), pydantic.Field(alias="modifierId3")
    ]
    modifier_id4: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifierId4"), pydantic.Field(alias="modifierId4")
    ]
    note: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
