

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .acknowledged_problem import AcknowledgedProblem


class BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRequest1(UniversalBaseModel):
    rx_quantity: typing_extensions.Annotated[str, FieldMetadata(alias="RxQuantity"), pydantic.Field(alias="RxQuantity")]
    rx_refills: typing_extensions.Annotated[str, FieldMetadata(alias="RxRefills"), pydantic.Field(alias="RxRefills")]
    dispense_as_written: typing_extensions.Annotated[
        str, FieldMetadata(alias="DispenseAsWritten"), pydantic.Field(alias="DispenseAsWritten")
    ]
    is_prescribed_elsewhere: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsPrescribedElsewhere"), pydantic.Field(alias="IsPrescribedElsewhere")
    ]
    privacy_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="PrivacyIndicator"), pydantic.Field(alias="PrivacyIndicator")
    ]
    prescribed_elsewhere_location: typing_extensions.Annotated[
        str, FieldMetadata(alias="PrescribedElsewhereLocation"), pydantic.Field(alias="PrescribedElsewhereLocation")
    ]
    rx_comment: typing_extensions.Annotated[str, FieldMetadata(alias="RxComment"), pydantic.Field(alias="RxComment")]
    rx_special_instruction: typing_extensions.Annotated[
        str, FieldMetadata(alias="RxSpecialInstruction"), pydantic.Field(alias="RxSpecialInstruction")
    ]
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="StartDate"), pydantic.Field(alias="StartDate")]
    stop_date: typing_extensions.Annotated[str, FieldMetadata(alias="StopDate"), pydantic.Field(alias="StopDate")]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="ProviderId"), pydantic.Field(alias="ProviderId")]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="LocationId"), pydantic.Field(alias="LocationId")]
    diagnosis_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="DiagnosisCode"), pydantic.Field(alias="DiagnosisCode")
    ]
    secondary_diagnosis_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryDiagnosisCode"), pydantic.Field(alias="SecondaryDiagnosisCode")
    ]
    tertiary_diagnosis_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="TertiaryDiagnosisCode"), pydantic.Field(alias="TertiaryDiagnosisCode")
    ]
    is_prn: typing_extensions.Annotated[str, FieldMetadata(alias="IsPrn"), pydantic.Field(alias="IsPrn")]
    prn_reason: typing_extensions.Annotated[str, FieldMetadata(alias="PrnReason"), pydantic.Field(alias="PrnReason")]
    rx_units: typing_extensions.Annotated[str, FieldMetadata(alias="RxUnits"), pydantic.Field(alias="RxUnits")]
    fdb_dosage_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="FdbDosageId"), pydantic.Field(alias="FdbDosageId")
    ]
    custom_dosage_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="CustomDosageId"), pydantic.Field(alias="CustomDosageId")
    ]
    ped_order_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="PedOrderId"), pydantic.Field(alias="PedOrderId")
    ]
    medication_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="MedicationId"), pydantic.Field(alias="MedicationId")
    ]
    is_representative_ndc: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsRepresentativeNdc"), pydantic.Field(alias="IsRepresentativeNdc")
    ]
    sig_code: typing_extensions.Annotated[str, FieldMetadata(alias="SigCode"), pydantic.Field(alias="SigCode")]
    sig_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="SigDescription"), pydantic.Field(alias="SigDescription")
    ]
    acknowledged_problems: typing_extensions.Annotated[
        typing.List[AcknowledgedProblem],
        FieldMetadata(alias="AcknowledgedProblems"),
        pydantic.Field(alias="AcknowledgedProblems"),
    ]
    supervising_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="SupervisingProviderId"), pydantic.Field(alias="SupervisingProviderId")
    ]
    prior_authorization_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="PriorAuthorizationIndicator"), pydantic.Field(alias="PriorAuthorizationIndicator")
    ]
    prior_authorization_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="PriorAuthorizationDate"), pydantic.Field(alias="PriorAuthorizationDate")
    ]
    prior_authorization_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="PriorAuthorizationId"), pydantic.Field(alias="PriorAuthorizationId")
    ]
    by_pass_dea_refill_limit_check: typing_extensions.Annotated[
        str, FieldMetadata(alias="ByPassDeaRefillLimitCheck"), pydantic.Field(alias="ByPassDeaRefillLimitCheck")
    ]
    samples_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="SamplesIndicator"), pydantic.Field(alias="SamplesIndicator")
    ]
    sample_lot_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="SampleLotNumber"), pydantic.Field(alias="SampleLotNumber")
    ]
    sample_expiration_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="SampleExpirationDate"), pydantic.Field(alias="SampleExpirationDate")
    ]
    refill_limit: typing_extensions.Annotated[
        str, FieldMetadata(alias="RefillLimit"), pydantic.Field(alias="RefillLimit")
    ]
    pbm_id: typing_extensions.Annotated[str, FieldMetadata(alias="PbmId"), pydantic.Field(alias="PbmId")]
    formulary_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="FormularyId"), pydantic.Field(alias="FormularyId")
    ]
    rx_fill_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="RxFillIndicator"), pydantic.Field(alias="RxFillIndicator")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
