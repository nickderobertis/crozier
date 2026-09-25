

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok70(UniversalBaseModel):
    id: str
    fdb_name: typing_extensions.Annotated[str, FieldMetadata(alias="fdbName"), pydantic.Field(alias="fdbName")]
    medication_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="medicationName"), pydantic.Field(alias="medicationName")
    ]
    generic_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="genericName"), pydantic.Field(alias="genericName")
    ]
    brand_name: typing_extensions.Annotated[str, FieldMetadata(alias="brandName"), pydantic.Field(alias="brandName")]
    dose: str
    dose_form: typing_extensions.Annotated[str, FieldMetadata(alias="doseForm"), pydantic.Field(alias="doseForm")]
    ndc_id: typing_extensions.Annotated[str, FieldMetadata(alias="ndcId"), pydantic.Field(alias="ndcId")]
    gcn: str
    route: str
    hicl_sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="hiclSequenceNumber"), pydantic.Field(alias="hiclSequenceNumber")
    ]
    gcn_sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="gcnSequenceNumber"), pydantic.Field(alias="gcnSequenceNumber")
    ]
    dea_class_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="deaClassCode"), pydantic.Field(alias="deaClassCode")
    ]
    medication_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="medicationId"), pydantic.Field(alias="medicationId")
    ]
    is_available: typing_extensions.Annotated[
        str, FieldMetadata(alias="isAvailable"), pydantic.Field(alias="isAvailable")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    modify_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimezone"), pydantic.Field(alias="modifyTimestampTimezone")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    encounter_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterProviderId"), pydantic.Field(alias="encounterProviderId")
    ]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    encounter_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestampTimezone"), pydantic.Field(alias="encounterTimestampTimezone")
    ]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    practice_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="practiceName"), pydantic.Field(alias="practiceName")
    ]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    enterprise_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseName"), pydantic.Field(alias="enterpriseName")
    ]
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")]
    original_start_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="originalStartDate"), pydantic.Field(alias="originalStartDate")
    ]
    stop_date: typing_extensions.Annotated[str, FieldMetadata(alias="stopDate"), pydantic.Field(alias="stopDate")]
    sig_codes: typing_extensions.Annotated[str, FieldMetadata(alias="sigCodes"), pydantic.Field(alias="sigCodes")]
    rx_quantity: typing_extensions.Annotated[str, FieldMetadata(alias="rxQuantity"), pydantic.Field(alias="rxQuantity")]
    rx_refills: typing_extensions.Annotated[str, FieldMetadata(alias="rxRefills"), pydantic.Field(alias="rxRefills")]
    is_generic_allowed: typing_extensions.Annotated[
        str, FieldMetadata(alias="isGenericAllowed"), pydantic.Field(alias="isGenericAllowed")
    ]
    is_sample: typing_extensions.Annotated[str, FieldMetadata(alias="isSample"), pydantic.Field(alias="isSample")]
    dispense_as_written: typing_extensions.Annotated[
        str, FieldMetadata(alias="dispenseAsWritten"), pydantic.Field(alias="dispenseAsWritten")
    ]
    org_refills: typing_extensions.Annotated[str, FieldMetadata(alias="orgRefills"), pydantic.Field(alias="orgRefills")]
    last_refill_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastRefillDate"), pydantic.Field(alias="lastRefillDate")
    ]
    sig_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="sigDescription"), pydantic.Field(alias="sigDescription")
    ]
    is_prescribed_elsewhere: typing_extensions.Annotated[
        str, FieldMetadata(alias="isPrescribedElsewhere"), pydantic.Field(alias="isPrescribedElsewhere")
    ]
    rx_units: typing_extensions.Annotated[str, FieldMetadata(alias="rxUnits"), pydantic.Field(alias="rxUnits")]
    rx_comment: typing_extensions.Annotated[str, FieldMetadata(alias="rxComment"), pydantic.Field(alias="rxComment")]
    rx_special_instruction: typing_extensions.Annotated[
        str, FieldMetadata(alias="rxSpecialInstruction"), pydantic.Field(alias="rxSpecialInstruction")
    ]
    print_spanish_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="printSpanishIndicator"), pydantic.Field(alias="printSpanishIndicator")
    ]
    is_generic_selected: typing_extensions.Annotated[
        str, FieldMetadata(alias="isGenericSelected"), pydantic.Field(alias="isGenericSelected")
    ]
    diagnosis_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCode"), pydantic.Field(alias="diagnosisCode")
    ]
    secondary_diagnosis_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryDiagnosisCode"), pydantic.Field(alias="secondaryDiagnosisCode")
    ]
    tertiary_diagnosis_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="tertiaryDiagnosisCode"), pydantic.Field(alias="tertiaryDiagnosisCode")
    ]
    representative_ndc_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="representativeNdcIndicator"), pydantic.Field(alias="representativeNdcIndicator")
    ]
    prn_reason: typing_extensions.Annotated[str, FieldMetadata(alias="prnReason"), pydantic.Field(alias="prnReason")]
    formulary_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="formularyId"), pydantic.Field(alias="formularyId")
    ]
    formula_override_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="formulaOverrideCode"), pydantic.Field(alias="formulaOverrideCode")
    ]
    formula_override_text: typing_extensions.Annotated[
        str, FieldMetadata(alias="formulaOverrideText"), pydantic.Field(alias="formulaOverrideText")
    ]
    original_rx_ndc: typing_extensions.Annotated[
        str, FieldMetadata(alias="originalRxNdc"), pydantic.Field(alias="originalRxNdc")
    ]
    formula_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="formulaStatus"), pydantic.Field(alias="formulaStatus")
    ]
    audit_mask: typing_extensions.Annotated[str, FieldMetadata(alias="auditMask"), pydantic.Field(alias="auditMask")]
    audit_id: typing_extensions.Annotated[str, FieldMetadata(alias="auditId"), pydantic.Field(alias="auditId")]
    send_audit_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sendAuditId"), pydantic.Field(alias="sendAuditId")
    ]
    last_audit_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastAuditType"), pydantic.Field(alias="lastAuditType")
    ]
    lot_number: typing_extensions.Annotated[str, FieldMetadata(alias="lotNumber"), pydantic.Field(alias="lotNumber")]
    expiration_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="expirationDate"), pydantic.Field(alias="expirationDate")
    ]
    is_prn: typing_extensions.Annotated[str, FieldMetadata(alias="isPrn"), pydantic.Field(alias="isPrn")]
    renew_parent_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="renewParentId"), pydantic.Field(alias="renewParentId")
    ]
    rx_unit_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="rxUnitCode"), pydantic.Field(alias="rxUnitCode")
    ]
    old_id: typing_extensions.Annotated[str, FieldMetadata(alias="oldId"), pydantic.Field(alias="oldId")]
    rx_renew_note: typing_extensions.Annotated[
        str, FieldMetadata(alias="rxRenewNote"), pydantic.Field(alias="rxRenewNote")
    ]
    fdb_dosage_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="FdbDosageId"), pydantic.Field(alias="FdbDosageId")
    ]
    refill_limit: typing_extensions.Annotated[
        str, FieldMetadata(alias="refillLimit"), pydantic.Field(alias="refillLimit")
    ]
    refill_limit_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="refillLimitDate"), pydantic.Field(alias="refillLimitDate")
    ]
    prescribed_elsewhere_location: typing_extensions.Annotated[
        str, FieldMetadata(alias="prescribedElsewhereLocation"), pydantic.Field(alias="prescribedElsewhereLocation")
    ]
    prior_authorization_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="priorAuthorizationIndicator"), pydantic.Field(alias="priorAuthorizationIndicator")
    ]
    prior_authorization_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="priorAuthorizationId"), pydantic.Field(alias="priorAuthorizationId")
    ]
    prior_authorization_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="priorAuthorizationDate"), pydantic.Field(alias="priorAuthorizationDate")
    ]
    privacy_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="privacyIndicator"), pydantic.Field(alias="privacyIndicator")
    ]
    refills_remaining: typing_extensions.Annotated[
        str, FieldMetadata(alias="refillsRemaining"), pydantic.Field(alias="refillsRemaining")
    ]
    custom_dosage_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="customDosageId"), pydantic.Field(alias="customDosageId")
    ]
    is_auto_calculated: typing_extensions.Annotated[
        str, FieldMetadata(alias="isAutoCalculated"), pydantic.Field(alias="isAutoCalculated")
    ]
    pbm_id: typing_extensions.Annotated[str, FieldMetadata(alias="pbmId"), pydantic.Field(alias="pbmId")]
    formulary_detail_data: typing_extensions.Annotated[
        str, FieldMetadata(alias="formularyDetailData"), pydantic.Field(alias="formularyDetailData")
    ]
    formulary_summary_data: typing_extensions.Annotated[
        str, FieldMetadata(alias="formularySummaryData"), pydantic.Field(alias="formularySummaryData")
    ]
    source_product_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceProductId"), pydantic.Field(alias="sourceProductId")
    ]
    supervising_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="supervisingProviderId"), pydantic.Field(alias="supervisingProviderId")
    ]
    ineffective_medication_indicator: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ineffectiveMedicationIndicator"),
        pydantic.Field(alias="ineffectiveMedicationIndicator"),
    ]
    ped_order_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="pedOrderId"), pydantic.Field(alias="pedOrderId")
    ]
    e_coupon_note: typing_extensions.Annotated[
        str, FieldMetadata(alias="eCouponNote"), pydantic.Field(alias="eCouponNote")
    ]
    e_coupon_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="eCouponUrl"), pydantic.Field(alias="eCouponUrl")
    ]
    audit_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="auditTimestamp"), pydantic.Field(alias="auditTimestamp")
    ]
    is_erx_disabled_by_state: typing_extensions.Annotated[
        str, FieldMetadata(alias="isErxDisabledByState"), pydantic.Field(alias="isErxDisabledByState")
    ]
    is_fax_disabled_by_state: typing_extensions.Annotated[
        str, FieldMetadata(alias="isFaxDisabledByState"), pydantic.Field(alias="isFaxDisabledByState")
    ]
    is_hidden: typing_extensions.Annotated[str, FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")]
    is_supply: typing_extensions.Annotated[str, FieldMetadata(alias="isSupply"), pydantic.Field(alias="isSupply")]
    rx_norm_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="rxNormCode"), pydantic.Field(alias="rxNormCode")
    ]
    status: str
    rx_fill_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="rxFillIndicator"), pydantic.Field(alias="rxFillIndicator")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
