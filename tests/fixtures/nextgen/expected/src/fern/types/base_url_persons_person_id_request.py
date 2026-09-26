

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdRequest(UniversalBaseModel):
    other_id_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="OtherIdNumber"), pydantic.Field(alias="OtherIdNumber")
    ]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="LastName"), pydantic.Field(alias="LastName")]
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="FirstName"), pydantic.Field(alias="FirstName")]
    middle_name: typing_extensions.Annotated[str, FieldMetadata(alias="MiddleName"), pydantic.Field(alias="MiddleName")]
    prior_last_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="PriorLastName"), pydantic.Field(alias="PriorLastName")
    ]
    address_line1: typing_extensions.Annotated[
        str, FieldMetadata(alias="AddressLine1"), pydantic.Field(alias="AddressLine1")
    ]
    address_line2: typing_extensions.Annotated[
        str, FieldMetadata(alias="AddressLine2"), pydantic.Field(alias="AddressLine2")
    ]
    city: typing_extensions.Annotated[str, FieldMetadata(alias="City"), pydantic.Field(alias="City")]
    state: typing_extensions.Annotated[str, FieldMetadata(alias="State"), pydantic.Field(alias="State")]
    zip: typing_extensions.Annotated[str, FieldMetadata(alias="Zip"), pydantic.Field(alias="Zip")]
    country_id: typing_extensions.Annotated[str, FieldMetadata(alias="CountryId"), pydantic.Field(alias="CountryId")]
    county_id: typing_extensions.Annotated[str, FieldMetadata(alias="CountyId"), pydantic.Field(alias="CountyId")]
    home_phone: typing_extensions.Annotated[str, FieldMetadata(alias="HomePhone"), pydantic.Field(alias="HomePhone")]
    home_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="HomePhoneComment"), pydantic.Field(alias="HomePhoneComment")
    ]
    is_home_phone_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsHomePhoneNotApplicable"), pydantic.Field(alias="IsHomePhoneNotApplicable")
    ]
    alternate_phone: typing_extensions.Annotated[
        str, FieldMetadata(alias="AlternatePhone"), pydantic.Field(alias="AlternatePhone")
    ]
    alternate_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="AlternatePhoneComment"), pydantic.Field(alias="AlternatePhoneComment")
    ]
    alternate_phone_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="AlternatePhoneDescription"), pydantic.Field(alias="AlternatePhoneDescription")
    ]
    alternate_phone_extension: typing_extensions.Annotated[
        str, FieldMetadata(alias="AlternatePhoneExtension"), pydantic.Field(alias="AlternatePhoneExtension")
    ]
    is_alternate_phone_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsAlternatePhoneNotApplicable"), pydantic.Field(alias="IsAlternatePhoneNotApplicable")
    ]
    secondary_home_phone: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryHomePhone"), pydantic.Field(alias="SecondaryHomePhone")
    ]
    secondary_home_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryHomePhoneComment"), pydantic.Field(alias="SecondaryHomePhoneComment")
    ]
    is_secondary_home_phone_not_applicable: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="IsSecondaryHomePhoneNotApplicable"),
        pydantic.Field(alias="IsSecondaryHomePhoneNotApplicable"),
    ]
    email_address: typing_extensions.Annotated[
        str, FieldMetadata(alias="EmailAddress"), pydantic.Field(alias="EmailAddress")
    ]
    email_address_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="EmailAddressComment"), pydantic.Field(alias="EmailAddressComment")
    ]
    is_email_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsEmailNotApplicable"), pydantic.Field(alias="IsEmailNotApplicable")
    ]
    cell_phone: typing_extensions.Annotated[str, FieldMetadata(alias="CellPhone"), pydantic.Field(alias="CellPhone")]
    cell_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="CellPhoneComment"), pydantic.Field(alias="CellPhoneComment")
    ]
    is_cell_phone_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsCellPhoneNotApplicable"), pydantic.Field(alias="IsCellPhoneNotApplicable")
    ]
    day_phone: typing_extensions.Annotated[str, FieldMetadata(alias="DayPhone"), pydantic.Field(alias="DayPhone")]
    day_phone_ext: typing_extensions.Annotated[
        str, FieldMetadata(alias="DayPhoneExt"), pydantic.Field(alias="DayPhoneExt")
    ]
    day_phone_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="DayPhoneComment"), pydantic.Field(alias="DayPhoneComment")
    ]
    is_day_phone_not_applicable: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsDayPhoneNotApplicable"), pydantic.Field(alias="IsDayPhoneNotApplicable")
    ]
    international_home_phone: typing_extensions.Annotated[
        str, FieldMetadata(alias="InternationalHomePhone"), pydantic.Field(alias="InternationalHomePhone")
    ]
    is_international_phone_not_applicable: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="IsInternationalPhoneNotApplicable"),
        pydantic.Field(alias="IsInternationalPhoneNotApplicable"),
    ]
    international_work_phone: typing_extensions.Annotated[
        str, FieldMetadata(alias="InternationalWorkPhone"), pydantic.Field(alias="InternationalWorkPhone")
    ]
    international_zip: typing_extensions.Annotated[
        str, FieldMetadata(alias="InternationalZip"), pydantic.Field(alias="InternationalZip")
    ]
    secondary_address_line1: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryAddressLine1"), pydantic.Field(alias="SecondaryAddressLine1")
    ]
    secondary_address_line2: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryAddressLine2"), pydantic.Field(alias="SecondaryAddressLine2")
    ]
    secondary_city: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryCity"), pydantic.Field(alias="SecondaryCity")
    ]
    secondary_state: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryState"), pydantic.Field(alias="SecondaryState")
    ]
    secondary_zip: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryZip"), pydantic.Field(alias="SecondaryZip")
    ]
    secondary_country_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryCountryId"), pydantic.Field(alias="SecondaryCountryId")
    ]
    secondary_county_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryCountyId"), pydantic.Field(alias="SecondaryCountyId")
    ]
    date_of_birth: typing_extensions.Annotated[
        str, FieldMetadata(alias="DateOfBirth"), pydantic.Field(alias="DateOfBirth")
    ]
    sex: typing_extensions.Annotated[str, FieldMetadata(alias="Sex"), pydantic.Field(alias="Sex")]
    social_security_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="SocialSecurityNumber"), pydantic.Field(alias="SocialSecurityNumber")
    ]
    marital_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="MaritalStatus"), pydantic.Field(alias="MaritalStatus")
    ]
    is_expired: typing_extensions.Annotated[str, FieldMetadata(alias="IsExpired"), pydantic.Field(alias="IsExpired")]
    expired_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="ExpiredDate"), pydantic.Field(alias="ExpiredDate")
    ]
    expired_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="ExpiredTime"), pydantic.Field(alias="ExpiredTime")
    ]
    expired_time_tz: typing_extensions.Annotated[
        str, FieldMetadata(alias="ExpiredTimeTz"), pydantic.Field(alias="ExpiredTimeTz")
    ]
    is_smoker: typing_extensions.Annotated[str, FieldMetadata(alias="IsSmoker"), pydantic.Field(alias="IsSmoker")]
    is_veteran: typing_extensions.Annotated[str, FieldMetadata(alias="IsVeteran"), pydantic.Field(alias="IsVeteran")]
    race_id: typing_extensions.Annotated[str, FieldMetadata(alias="RaceId"), pydantic.Field(alias="RaceId")]
    language_id: typing_extensions.Annotated[str, FieldMetadata(alias="LanguageId"), pydantic.Field(alias="LanguageId")]
    religion_id: typing_extensions.Annotated[str, FieldMetadata(alias="ReligionId"), pydantic.Field(alias="ReligionId")]
    church_id: typing_extensions.Annotated[str, FieldMetadata(alias="ChurchId"), pydantic.Field(alias="ChurchId")]
    student_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="StudentStatus"), pydantic.Field(alias="StudentStatus")
    ]
    primary_care_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="PrimaryCareProviderId"), pydantic.Field(alias="PrimaryCareProviderId")
    ]
    external_id: typing_extensions.Annotated[str, FieldMetadata(alias="ExternalId"), pydantic.Field(alias="ExternalId")]
    nickname: typing_extensions.Annotated[str, FieldMetadata(alias="Nickname"), pydantic.Field(alias="Nickname")]
    uds_homeless_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsHomelessStatusId"), pydantic.Field(alias="UdsHomelessStatusId")
    ]
    uds_migrant_worker_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsMigrantWorkerStatusId"), pydantic.Field(alias="UdsMigrantWorkerStatusId")
    ]
    uds_language_barrier_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsLanguageBarrierId"), pydantic.Field(alias="UdsLanguageBarrierId")
    ]
    uds_primary_medical_coverage_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsPrimaryMedicalCoverageId"), pydantic.Field(alias="UdsPrimaryMedicalCoverageId")
    ]
    contact_sequence: typing_extensions.Annotated[
        str, FieldMetadata(alias="ContactSequence"), pydantic.Field(alias="ContactSequence")
    ]
    contact_preference_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="ContactPreferenceId"), pydantic.Field(alias="ContactPreferenceId")
    ]
    show_contact_info_on_alert: typing_extensions.Annotated[
        str, FieldMetadata(alias="ShowContactInfoOnAlert"), pydantic.Field(alias="ShowContactInfoOnAlert")
    ]
    is_enterprise_chart: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsEnterpriseChart"), pydantic.Field(alias="IsEnterpriseChart")
    ]
    uds_public_housing_primary_care_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsPublicHousingPrimaryCareId"), pydantic.Field(alias="UdsPublicHousingPrimaryCareId")
    ]
    uds_school_based_health_center_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsSchoolBasedHealthCenterId"), pydantic.Field(alias="UdsSchoolBasedHealthCenterId")
    ]
    is_self_payer: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsSelfPayer"), pydantic.Field(alias="IsSelfPayer")
    ]
    uds_tribal_affiliation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsTribalAffiliationId"), pydantic.Field(alias="UdsTribalAffiliationId")
    ]
    uds_blood_quantum_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsBloodQuantumId"), pydantic.Field(alias="UdsBloodQuantumId")
    ]
    uds_veteran_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsVeteranStatus"), pydantic.Field(alias="UdsVeteranStatus")
    ]
    uds_has_consent_to_treat: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsHasConsentToTreat"), pydantic.Field(alias="UdsHasConsentToTreat")
    ]
    mothers_maiden_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="MothersMaidenName"), pydantic.Field(alias="MothersMaidenName")
    ]
    uds_ihs_eligibility_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsIhsEligibilityStatusId"), pydantic.Field(alias="UdsIhsEligibilityStatusId")
    ]
    uds_tribal_class_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsTribalClassId"), pydantic.Field(alias="UdsTribalClassId")
    ]
    uds_decendancy_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsDecendancyId"), pydantic.Field(alias="UdsDecendancyId")
    ]
    uds_consent_to_treat_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="UdsConsentToTreatDate"), pydantic.Field(alias="UdsConsentToTreatDate")
    ]
    community_code_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="CommunityCodeId"), pydantic.Field(alias="CommunityCodeId")
    ]
    ethnicity_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="EthnicityId"), pydantic.Field(alias="EthnicityId")
    ]
    primary_dental_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="PrimaryDentalProviderId"), pydantic.Field(alias="PrimaryDentalProviderId")
    ]
    address_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="AddressTypeId"), pydantic.Field(alias="AddressTypeId")
    ]
    secondary_address_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="SecondaryAddressTypeId"), pydantic.Field(alias="SecondaryAddressTypeId")
    ]
    prefix_id: typing_extensions.Annotated[str, FieldMetadata(alias="PrefixId"), pydantic.Field(alias="PrefixId")]
    suffix_id: typing_extensions.Annotated[str, FieldMetadata(alias="SuffixId"), pydantic.Field(alias="SuffixId")]
    birth_mothers_last_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="BirthMothersLastName"), pydantic.Field(alias="BirthMothersLastName")
    ]
    birth_mothers_first_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="BirthMothersFirstName"), pydantic.Field(alias="BirthMothersFirstName")
    ]
    birth_mothers_middle_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="BirthMothersMiddleName"), pydantic.Field(alias="BirthMothersMiddleName")
    ]
    has_email: typing_extensions.Annotated[str, FieldMetadata(alias="HasEmail"), pydantic.Field(alias="HasEmail")]
    has_phone_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="HasPhoneNumber"), pydantic.Field(alias="HasPhoneNumber")
    ]
    uses_portal: typing_extensions.Annotated[str, FieldMetadata(alias="UsesPortal"), pydantic.Field(alias="UsesPortal")]
    uses_sms: typing_extensions.Annotated[str, FieldMetadata(alias="UsesSms"), pydantic.Field(alias="UsesSms")]
    has_voice: typing_extensions.Annotated[str, FieldMetadata(alias="HasVoice"), pydantic.Field(alias="HasVoice")]
    is_opt_out: typing_extensions.Annotated[str, FieldMetadata(alias="IsOptOut"), pydantic.Field(alias="IsOptOut")]
    exempt_from_person_merge: typing_extensions.Annotated[
        str, FieldMetadata(alias="ExemptFromPersonMerge"), pydantic.Field(alias="ExemptFromPersonMerge")
    ]
    sexual_orientation: typing_extensions.Annotated[
        str, FieldMetadata(alias="SexualOrientation"), pydantic.Field(alias="SexualOrientation")
    ]
    preferred_pronoun: typing_extensions.Annotated[
        str, FieldMetadata(alias="PreferredPronoun"), pydantic.Field(alias="PreferredPronoun")
    ]
    gender_identity_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="GenderIdentityCode"), pydantic.Field(alias="GenderIdentityCode")
    ]
    current_gender: typing_extensions.Annotated[
        str, FieldMetadata(alias="CurrentGender"), pydantic.Field(alias="CurrentGender")
    ]
    previous_first_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="PreviousFirstName"), pydantic.Field(alias="PreviousFirstName")
    ]
    other_reason_sexual_orientation: typing_extensions.Annotated[
        str, FieldMetadata(alias="OtherReasonSexualOrientation"), pydantic.Field(alias="OtherReasonSexualOrientation")
    ]
    other_reason_gender_identity: typing_extensions.Annotated[
        str, FieldMetadata(alias="OtherReasonGenderIdentity"), pydantic.Field(alias="OtherReasonGenderIdentity")
    ]
    patient_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="PatientStatusId"), pydantic.Field(alias="PatientStatusId")
    ]
    patient_status_change_reason_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="PatientStatusChangeReasonId"), pydantic.Field(alias="PatientStatusChangeReasonId")
    ]
    user_defined_demographic1id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic1Id"), pydantic.Field(alias="UserDefinedDemographic1Id")
    ]
    user_defined_demographic2id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic2Id"), pydantic.Field(alias="UserDefinedDemographic2Id")
    ]
    user_defined_demographic3id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic3Id"), pydantic.Field(alias="UserDefinedDemographic3Id")
    ]
    user_defined_demographic4id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic4Id"), pydantic.Field(alias="UserDefinedDemographic4Id")
    ]
    user_defined_demographic5id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic5Id"), pydantic.Field(alias="UserDefinedDemographic5Id")
    ]
    user_defined_demographic6id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic6Id"), pydantic.Field(alias="UserDefinedDemographic6Id")
    ]
    user_defined_demographic7id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic7Id"), pydantic.Field(alias="UserDefinedDemographic7Id")
    ]
    user_defined_demographic8id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic8Id"), pydantic.Field(alias="UserDefinedDemographic8Id")
    ]
    user_defined_demographic9id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic9Id"), pydantic.Field(alias="UserDefinedDemographic9Id")
    ]
    user_defined_demographic10id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic10Id"), pydantic.Field(alias="UserDefinedDemographic10Id")
    ]
    user_defined_demographic11id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic11Id"), pydantic.Field(alias="UserDefinedDemographic11Id")
    ]
    user_defined_demographic12id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic12Id"), pydantic.Field(alias="UserDefinedDemographic12Id")
    ]
    user_defined_demographic13id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic13Id"), pydantic.Field(alias="UserDefinedDemographic13Id")
    ]
    user_defined_demographic14id: typing_extensions.Annotated[
        str, FieldMetadata(alias="UserDefinedDemographic14Id"), pydantic.Field(alias="UserDefinedDemographic14Id")
    ]
    ignore_duplicate_persons: typing_extensions.Annotated[
        str, FieldMetadata(alias="IgnoreDuplicatePersons"), pydantic.Field(alias="IgnoreDuplicatePersons")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
