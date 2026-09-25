

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok93(UniversalBaseModel):
    id: str
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    service_item_library_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceItemLibraryId"), pydantic.Field(alias="serviceItemLibraryId")
    ]
    service_item_group_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceItemGroupName"), pydantic.Field(alias="serviceItemGroupName")
    ]
    service_item_group_sequence_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceItemGroupSequenceNumber"),
        pydantic.Field(alias="serviceItemGroupSequenceNumber"),
    ]
    service_item_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceItemId"), pydantic.Field(alias="serviceItemId")
    ]
    service_item_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceItemDescription"), pydantic.Field(alias="serviceItemDescription")
    ]
    cpt4code: typing_extensions.Annotated[str, FieldMetadata(alias="cpt4Code"), pydantic.Field(alias="cpt4Code")]
    service_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceDate"), pydantic.Field(alias="serviceDate")
    ]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    referring_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="referringProviderId"), pydantic.Field(alias="referringProviderId")
    ]
    referring_provider_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="referringProviderName"), pydantic.Field(alias="referringProviderName")
    ]
    assisting_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="assistingProviderId"), pydantic.Field(alias="assistingProviderId")
    ]
    date_resolved: typing_extensions.Annotated[
        str, FieldMetadata(alias="dateResolved"), pydantic.Field(alias="dateResolved")
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
    diagnosis_code_id1: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId1"), pydantic.Field(alias="diagnosisCodeId1")
    ]
    diagnosis_code_library_id1: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId1"), pydantic.Field(alias="diagnosisCodeLibraryId1")
    ]
    diagnosis_code_id2: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId2"), pydantic.Field(alias="diagnosisCodeId2")
    ]
    diagnosis_code_library_id2: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId2"), pydantic.Field(alias="diagnosisCodeLibraryId2")
    ]
    diagnosis_code_id3: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId3"), pydantic.Field(alias="diagnosisCodeId3")
    ]
    diagnosis_code_library_id3: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId3"), pydantic.Field(alias="diagnosisCodeLibraryId3")
    ]
    diagnosis_code_id4: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId4"), pydantic.Field(alias="diagnosisCodeId4")
    ]
    diagnosis_code_library_id4: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId4"), pydantic.Field(alias="diagnosisCodeLibraryId4")
    ]
    place_of_service: typing_extensions.Annotated[
        str, FieldMetadata(alias="placeOfService"), pydantic.Field(alias="placeOfService")
    ]
    has_accepted_assignment: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasAcceptedAssignment"), pydantic.Field(alias="hasAcceptedAssignment")
    ]
    units: str
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    payer_id: typing_extensions.Annotated[str, FieldMetadata(alias="payerId"), pydantic.Field(alias="payerId")]
    amount: str
    is_billing_suppressed: typing_extensions.Annotated[
        str, FieldMetadata(alias="isBillingSuppressed"), pydantic.Field(alias="isBillingSuppressed")
    ]
    tooth: str
    surface: str
    quadrant: str
    note: str
    start_time: typing_extensions.Annotated[str, FieldMetadata(alias="startTime"), pydantic.Field(alias="startTime")]
    stop_time: typing_extensions.Annotated[str, FieldMetadata(alias="stopTime"), pydantic.Field(alias="stopTime")]
    total_time: typing_extensions.Annotated[str, FieldMetadata(alias="totalTime"), pydantic.Field(alias="totalTime")]
    base_unit: typing_extensions.Annotated[str, FieldMetadata(alias="baseUnit"), pydantic.Field(alias="baseUnit")]
    alternate_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="alternateCode"), pydantic.Field(alias="alternateCode")
    ]
    is_anesthesia_billing: typing_extensions.Annotated[
        str, FieldMetadata(alias="isAnesthesiaBilling"), pydantic.Field(alias="isAnesthesiaBilling")
    ]
    diagnosis_code_id5: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId5"), pydantic.Field(alias="diagnosisCodeId5")
    ]
    diagnosis_code_library_id5: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId5"), pydantic.Field(alias="diagnosisCodeLibraryId5")
    ]
    diagnosis_code_id6: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId6"), pydantic.Field(alias="diagnosisCodeId6")
    ]
    diagnosis_code_library_id6: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId6"), pydantic.Field(alias="diagnosisCodeLibraryId6")
    ]
    diagnosis_code_id7: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId7"), pydantic.Field(alias="diagnosisCodeId7")
    ]
    diagnosis_code_library_id7: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId7"), pydantic.Field(alias="diagnosisCodeLibraryId7")
    ]
    diagnosis_code_id8: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId8"), pydantic.Field(alias="diagnosisCodeId8")
    ]
    diagnosis_code_library_id8: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId8"), pydantic.Field(alias="diagnosisCodeLibraryId8")
    ]
    source_product_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceProductId"), pydantic.Field(alias="sourceProductId")
    ]
    is_rx_on_file: typing_extensions.Annotated[
        str, FieldMetadata(alias="isRxOnFile"), pydantic.Field(alias="isRxOnFile")
    ]
    national_drug_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="nationalDrugCode"), pydantic.Field(alias="nationalDrugCode")
    ]
    is_behavioral_billing: typing_extensions.Annotated[
        str, FieldMetadata(alias="isBehavioralBilling"), pydantic.Field(alias="isBehavioralBilling")
    ]
    diagnosis_code_id9: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId9"), pydantic.Field(alias="diagnosisCodeId9")
    ]
    diagnosis_code_library_id9: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId9"), pydantic.Field(alias="diagnosisCodeLibraryId9")
    ]
    diagnosis_code_id10: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId10"), pydantic.Field(alias="diagnosisCodeId10")
    ]
    diagnosis_code_library_id10: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId10"), pydantic.Field(alias="diagnosisCodeLibraryId10")
    ]
    diagnosis_code_id11: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId11"), pydantic.Field(alias="diagnosisCodeId11")
    ]
    diagnosis_code_library_id11: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId11"), pydantic.Field(alias="diagnosisCodeLibraryId11")
    ]
    diagnosis_code_id12: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId12"), pydantic.Field(alias="diagnosisCodeId12")
    ]
    diagnosis_code_library_id12: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId12"), pydantic.Field(alias="diagnosisCodeLibraryId12")
    ]
    snomed_concept_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="snomedConceptId"), pydantic.Field(alias="snomedConceptId")
    ]
    snomed_concept_id2: typing_extensions.Annotated[
        str, FieldMetadata(alias="snomedConceptId2"), pydantic.Field(alias="snomedConceptId2")
    ]
    snomed_concept_id3: typing_extensions.Annotated[
        str, FieldMetadata(alias="snomedConceptId3"), pydantic.Field(alias="snomedConceptId3")
    ]
    snomed_concept_id4: typing_extensions.Annotated[
        str, FieldMetadata(alias="snomedConceptId4"), pydantic.Field(alias="snomedConceptId4")
    ]
    is_dental: typing_extensions.Annotated[str, FieldMetadata(alias="isDental"), pydantic.Field(alias="isDental")]
    is_supernumerary: typing_extensions.Annotated[
        str, FieldMetadata(alias="isSupernumerary"), pydantic.Field(alias="isSupernumerary")
    ]
    surface_descriptor: typing_extensions.Annotated[
        str, FieldMetadata(alias="surfaceDescriptor"), pydantic.Field(alias="surfaceDescriptor")
    ]
    is_defective: typing_extensions.Annotated[
        str, FieldMetadata(alias="isDefective"), pydantic.Field(alias="isDefective")
    ]
    not_applicable_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="notApplicableDate"), pydantic.Field(alias="notApplicableDate")
    ]
    approval_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="approvalDate"), pydantic.Field(alias="approvalDate")
    ]
    medical_director_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="medicalDirectorId"), pydantic.Field(alias="medicalDirectorId")
    ]
    asa_crosswalk_library_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="asaCrosswalkLibraryId"), pydantic.Field(alias="asaCrosswalkLibraryId")
    ]
    surgical_procedure_code_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="surgicalProcedureCodeId"), pydantic.Field(alias="surgicalProcedureCodeId")
    ]
    surgical_procedure_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="surgicalProcedureDescription"), pydantic.Field(alias="surgicalProcedureDescription")
    ]
    basis_of_measure: typing_extensions.Annotated[
        str, FieldMetadata(alias="basisOfMeasure"), pydantic.Field(alias="basisOfMeasure")
    ]
    national_drug_units: typing_extensions.Annotated[
        str, FieldMetadata(alias="nationalDrugUnits"), pydantic.Field(alias="nationalDrugUnits")
    ]
    teeth: str
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
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
