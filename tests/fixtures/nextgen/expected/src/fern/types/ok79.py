

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok79(UniversalBaseModel):
    id: str
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    middle_name: typing_extensions.Annotated[str, FieldMetadata(alias="middleName"), pydantic.Field(alias="middleName")]
    prefix: str
    prefix_id: typing_extensions.Annotated[str, FieldMetadata(alias="prefixId"), pydantic.Field(alias="prefixId")]
    suffix: str
    suffix_id: typing_extensions.Annotated[str, FieldMetadata(alias="suffixId"), pydantic.Field(alias="suffixId")]
    address_line1: typing_extensions.Annotated[
        str, FieldMetadata(alias="addressLine1"), pydantic.Field(alias="addressLine1")
    ]
    address_line2: typing_extensions.Annotated[
        str, FieldMetadata(alias="addressLine2"), pydantic.Field(alias="addressLine2")
    ]
    city: str
    state: str
    zip: str
    country_id: typing_extensions.Annotated[str, FieldMetadata(alias="countryId"), pydantic.Field(alias="countryId")]
    country: str
    county_id: typing_extensions.Annotated[str, FieldMetadata(alias="countyId"), pydantic.Field(alias="countyId")]
    county: str
    secondary_address_line1: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryAddressLine1"), pydantic.Field(alias="secondaryAddressLine1")
    ]
    secondary_address_line2: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryAddressLine2"), pydantic.Field(alias="secondaryAddressLine2")
    ]
    secondary_city: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryCity"), pydantic.Field(alias="secondaryCity")
    ]
    secondary_state: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryState"), pydantic.Field(alias="secondaryState")
    ]
    secondary_zip: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryZip"), pydantic.Field(alias="secondaryZip")
    ]
    secondary_country_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryCountryId"), pydantic.Field(alias="secondaryCountryId")
    ]
    secondary_country: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryCountry"), pydantic.Field(alias="secondaryCountry")
    ]
    secondary_county_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryCountyId"), pydantic.Field(alias="secondaryCountyId")
    ]
    secondary_county: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryCounty"), pydantic.Field(alias="secondaryCounty")
    ]
    home_phone: typing_extensions.Annotated[str, FieldMetadata(alias="homePhone"), pydantic.Field(alias="homePhone")]
    home_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="homePhoneComment"), pydantic.Field(alias="homePhoneComment")
    ]
    secondary_home_phone: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryHomePhone"), pydantic.Field(alias="secondaryHomePhone")
    ]
    secondary_home_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryHomePhoneComment"), pydantic.Field(alias="secondaryHomePhoneComment")
    ]
    day_phone: typing_extensions.Annotated[str, FieldMetadata(alias="dayPhone"), pydantic.Field(alias="dayPhone")]
    day_phone_extension: typing_extensions.Annotated[
        str, FieldMetadata(alias="dayPhoneExtension"), pydantic.Field(alias="dayPhoneExtension")
    ]
    day_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="dayPhoneComment"), pydantic.Field(alias="dayPhoneComment")
    ]
    alternate_phone: typing_extensions.Annotated[
        str, FieldMetadata(alias="alternatePhone"), pydantic.Field(alias="alternatePhone")
    ]
    alternate_phone_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="alternatePhoneDescription"), pydantic.Field(alias="alternatePhoneDescription")
    ]
    alternate_phone_extension: typing_extensions.Annotated[
        str, FieldMetadata(alias="alternatePhoneExtension"), pydantic.Field(alias="alternatePhoneExtension")
    ]
    alternate_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="alternatePhoneComment"), pydantic.Field(alias="alternatePhoneComment")
    ]
    international_home_phone: typing_extensions.Annotated[
        str, FieldMetadata(alias="internationalHomePhone"), pydantic.Field(alias="internationalHomePhone")
    ]
    international_work_phone: typing_extensions.Annotated[
        str, FieldMetadata(alias="internationalWorkPhone"), pydantic.Field(alias="internationalWorkPhone")
    ]
    international_zip: typing_extensions.Annotated[
        str, FieldMetadata(alias="internationalZip"), pydantic.Field(alias="internationalZip")
    ]
    cell_phone: typing_extensions.Annotated[str, FieldMetadata(alias="cellPhone"), pydantic.Field(alias="cellPhone")]
    cell_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="cellPhoneComment"), pydantic.Field(alias="cellPhoneComment")
    ]
    email: str
    email_address_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="emailAddressComment"), pydantic.Field(alias="emailAddressComment")
    ]
    contact_sequence: typing_extensions.Annotated[
        str, FieldMetadata(alias="contactSequence"), pydantic.Field(alias="contactSequence")
    ]
    sex: str
    date_of_birth: typing_extensions.Annotated[
        str, FieldMetadata(alias="dateOfBirth"), pydantic.Field(alias="dateOfBirth")
    ]
    age: str
    social_security_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="socialSecurityNumber"), pydantic.Field(alias="socialSecurityNumber")
    ]
    contact_preference_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="contactPreferenceId"), pydantic.Field(alias="contactPreferenceId")
    ]
    contact_preference_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="contactPreferenceDescription"), pydantic.Field(alias="contactPreferenceDescription")
    ]
    primary_care_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="primaryCareProviderId"), pydantic.Field(alias="primaryCareProviderId")
    ]
    primary_care_provider_full_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="primaryCareProviderFullName"), pydantic.Field(alias="primaryCareProviderFullName")
    ]
    primary_care_provider_first_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="primaryCareProviderFirstName"), pydantic.Field(alias="primaryCareProviderFirstName")
    ]
    primary_care_provider_last_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="primaryCareProviderLastName"), pydantic.Field(alias="primaryCareProviderLastName")
    ]
    primary_care_provider_middle_initial: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="primaryCareProviderMiddleInitial"),
        pydantic.Field(alias="primaryCareProviderMiddleInitial"),
    ]
    marital_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="maritalStatus"), pydantic.Field(alias="maritalStatus")
    ]
    student_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="studentStatus"), pydantic.Field(alias="studentStatus")
    ]
    is_expired: typing_extensions.Annotated[str, FieldMetadata(alias="isExpired"), pydantic.Field(alias="isExpired")]
    is_smoker: typing_extensions.Annotated[str, FieldMetadata(alias="isSmoker"), pydantic.Field(alias="isSmoker")]
    is_veteran: typing_extensions.Annotated[str, FieldMetadata(alias="isVeteran"), pydantic.Field(alias="isVeteran")]
    notification_preference_selected: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="notificationPreferenceSelected"),
        pydantic.Field(alias="notificationPreferenceSelected"),
    ]
    preferred_language_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="preferredLanguageId"), pydantic.Field(alias="preferredLanguageId")
    ]
    preferred_language: typing_extensions.Annotated[
        str, FieldMetadata(alias="preferredLanguage"), pydantic.Field(alias="preferredLanguage")
    ]
    religion_id: typing_extensions.Annotated[str, FieldMetadata(alias="religionId"), pydantic.Field(alias="religionId")]
    church_id: typing_extensions.Annotated[str, FieldMetadata(alias="churchId"), pydantic.Field(alias="churchId")]
    uds_homeless_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsHomelessStatusId"), pydantic.Field(alias="udsHomelessStatusId")
    ]
    uds_migrant_worker_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsMigrantWorkerStatusId"), pydantic.Field(alias="udsMigrantWorkerStatusId")
    ]
    uds_language_barrier_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsLanguageBarrierId"), pydantic.Field(alias="udsLanguageBarrierId")
    ]
    uds_primary_medical_coverage_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsPrimaryMedicalCoverageId"), pydantic.Field(alias="udsPrimaryMedicalCoverageId")
    ]
    uds_public_housing_primary_care_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsPublicHousingPrimaryCareId"), pydantic.Field(alias="udsPublicHousingPrimaryCareId")
    ]
    uds_school_based_health_center_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsSchoolBasedHealthCenterId"), pydantic.Field(alias="udsSchoolBasedHealthCenterId")
    ]
    uds_tribal_affiliation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsTribalAffiliationId"), pydantic.Field(alias="udsTribalAffiliationId")
    ]
    uds_blood_quantum_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsBloodQuantumId"), pydantic.Field(alias="udsBloodQuantumId")
    ]
    uds_veteran_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsVeteranStatus"), pydantic.Field(alias="udsVeteranStatus")
    ]
    is_self_payer: typing_extensions.Annotated[
        str, FieldMetadata(alias="isSelfPayer"), pydantic.Field(alias="isSelfPayer")
    ]
    uds_has_consent_to_treat: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsHasConsentToTreat"), pydantic.Field(alias="udsHasConsentToTreat")
    ]
    uds_consent_to_treat_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsConsentToTreatDate"), pydantic.Field(alias="udsConsentToTreatDate")
    ]
    uds_ihs_eligibility_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsIhsEligibilityStatusId"), pydantic.Field(alias="udsIhsEligibilityStatusId")
    ]
    uds_tribal_class_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsTribalClassId"), pydantic.Field(alias="udsTribalClassId")
    ]
    uds_decendancy_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="udsDecendancyId"), pydantic.Field(alias="udsDecendancyId")
    ]
    community_code_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="communityCodeId"), pydantic.Field(alias="communityCodeId")
    ]
    current_gender: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentGender"), pydantic.Field(alias="currentGender")
    ]
    previous_first_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="previousFirstName"), pydantic.Field(alias="previousFirstName")
    ]
    sexual_orientation: typing_extensions.Annotated[
        str, FieldMetadata(alias="sexualOrientation"), pydantic.Field(alias="sexualOrientation")
    ]
    preferred_pronoun: typing_extensions.Annotated[
        str, FieldMetadata(alias="preferredPronoun"), pydantic.Field(alias="preferredPronoun")
    ]
    patient_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientStatusId"), pydantic.Field(alias="patientStatusId")
    ]
    patient_status_change_reason_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientStatusChangeReasonId"), pydantic.Field(alias="patientStatusChangeReasonId")
    ]
    user_defined_demographic1id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic1Id"), pydantic.Field(alias="userDefinedDemographic1Id")
    ]
    user_defined_demographic2id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic2Id"), pydantic.Field(alias="userDefinedDemographic2Id")
    ]
    user_defined_demographic3id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic3Id"), pydantic.Field(alias="userDefinedDemographic3Id")
    ]
    user_defined_demographic4id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic4Id"), pydantic.Field(alias="userDefinedDemographic4Id")
    ]
    user_defined_demographic5id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic5Id"), pydantic.Field(alias="userDefinedDemographic5Id")
    ]
    user_defined_demographic6id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic6Id"), pydantic.Field(alias="userDefinedDemographic6Id")
    ]
    user_defined_demographic7id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic7Id"), pydantic.Field(alias="userDefinedDemographic7Id")
    ]
    user_defined_demographic8id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic8Id"), pydantic.Field(alias="userDefinedDemographic8Id")
    ]
    user_defined_demographic9id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic9Id"), pydantic.Field(alias="userDefinedDemographic9Id")
    ]
    user_defined_demographic10id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic10Id"), pydantic.Field(alias="userDefinedDemographic10Id")
    ]
    user_defined_demographic11id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic11Id"), pydantic.Field(alias="userDefinedDemographic11Id")
    ]
    user_defined_demographic12id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic12Id"), pydantic.Field(alias="userDefinedDemographic12Id")
    ]
    user_defined_demographic13id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic13Id"), pydantic.Field(alias="userDefinedDemographic13Id")
    ]
    user_defined_demographic14id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDefinedDemographic14Id"), pydantic.Field(alias="userDefinedDemographic14Id")
    ]
    is_current_gender_protected: typing_extensions.Annotated[
        str, FieldMetadata(alias="isCurrentGenderProtected"), pydantic.Field(alias="isCurrentGenderProtected")
    ]
    is_gender_identity_protected: typing_extensions.Annotated[
        str, FieldMetadata(alias="isGenderIdentityProtected"), pydantic.Field(alias="isGenderIdentityProtected")
    ]
    is_preferred_pronoun_protected: typing_extensions.Annotated[
        str, FieldMetadata(alias="isPreferredPronounProtected"), pydantic.Field(alias="isPreferredPronounProtected")
    ]
    is_sexual_orientation_protected: typing_extensions.Annotated[
        str, FieldMetadata(alias="isSexualOrientationProtected"), pydantic.Field(alias="isSexualOrientationProtected")
    ]
    other_id_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="otherIdNumber"), pydantic.Field(alias="otherIdNumber")
    ]
    prior_last_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="priorLastName"), pydantic.Field(alias="priorLastName")
    ]
    external_id: typing_extensions.Annotated[str, FieldMetadata(alias="externalId"), pydantic.Field(alias="externalId")]
    primary_dental_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="primaryDentalProviderId"), pydantic.Field(alias="primaryDentalProviderId")
    ]
    primary_dental_provider_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="primaryDentalProviderName"), pydantic.Field(alias="primaryDentalProviderName")
    ]
    nickname: str
    show_contact_info_on_alert: typing_extensions.Annotated[
        str, FieldMetadata(alias="showContactInfoOnAlert"), pydantic.Field(alias="showContactInfoOnAlert")
    ]
    mothers_maiden_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="mothersMaidenName"), pydantic.Field(alias="mothersMaidenName")
    ]
    has_email: typing_extensions.Annotated[str, FieldMetadata(alias="hasEmail"), pydantic.Field(alias="hasEmail")]
    has_phone_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasPhoneNumber"), pydantic.Field(alias="hasPhoneNumber")
    ]
    uses_portal: typing_extensions.Annotated[str, FieldMetadata(alias="usesPortal"), pydantic.Field(alias="usesPortal")]
    uses_sms: typing_extensions.Annotated[str, FieldMetadata(alias="usesSms"), pydantic.Field(alias="usesSms")]
    has_voice: typing_extensions.Annotated[str, FieldMetadata(alias="hasVoice"), pydantic.Field(alias="hasVoice")]
    is_opt_out: typing_extensions.Annotated[str, FieldMetadata(alias="isOptOut"), pydantic.Field(alias="isOptOut")]
    is_home_phone_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="isHomePhoneNotApplicable"), pydantic.Field(alias="isHomePhoneNotApplicable")
    ]
    is_cell_phone_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="isCellPhoneNotApplicable"), pydantic.Field(alias="isCellPhoneNotApplicable")
    ]
    is_alternate_phone_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="isAlternatePhoneNotApplicable"), pydantic.Field(alias="isAlternatePhoneNotApplicable")
    ]
    is_day_phone_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="isDayPhoneNotApplicable"), pydantic.Field(alias="isDayPhoneNotApplicable")
    ]
    is_secondary_home_phone_not_applicable: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="isSecondaryHomePhoneNotApplicable"),
        pydantic.Field(alias="isSecondaryHomePhoneNotApplicable"),
    ]
    is_international_phone_not_applicable: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="isInternationalPhoneNotApplicable"),
        pydantic.Field(alias="isInternationalPhoneNotApplicable"),
    ]
    is_email_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="isEmailNotApplicable"), pydantic.Field(alias="isEmailNotApplicable")
    ]
    expired_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="expiredDate"), pydantic.Field(alias="expiredDate")
    ]
    expired_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="expiredTime"), pydantic.Field(alias="expiredTime")
    ]
    expired_time_tz: typing_extensions.Annotated[
        str, FieldMetadata(alias="expiredTimeTz"), pydantic.Field(alias="expiredTimeTz")
    ]
    birth_mothers_last_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="birthMothersLastName"), pydantic.Field(alias="birthMothersLastName")
    ]
    birth_mothers_first_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="birthMothersFirstName"), pydantic.Field(alias="birthMothersFirstName")
    ]
    birth_mothers_middle_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="birthMothersMiddleName"), pydantic.Field(alias="birthMothersMiddleName")
    ]
    exempt_from_person_merge: typing_extensions.Annotated[
        str, FieldMetadata(alias="exemptFromPersonMerge"), pydantic.Field(alias="exemptFromPersonMerge")
    ]
    address_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="addressTypeId"), pydantic.Field(alias="addressTypeId")
    ]
    secondary_address_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryAddressTypeId"), pydantic.Field(alias="secondaryAddressTypeId")
    ]
    is_enterprise_chart: typing_extensions.Annotated[
        str, FieldMetadata(alias="isEnterpriseChart"), pydantic.Field(alias="isEnterpriseChart")
    ]
    other_reason_sexual_orientation: typing_extensions.Annotated[
        str, FieldMetadata(alias="otherReasonSexualOrientation"), pydantic.Field(alias="otherReasonSexualOrientation")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
