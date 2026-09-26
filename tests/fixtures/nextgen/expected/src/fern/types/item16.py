

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item16(UniversalBaseModel):
    exercise_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseType"), pydantic.Field(alias="exerciseType")
    ]
    exercise_type2: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseType2"), pydantic.Field(alias="exerciseType2")
    ]
    exercise_type3: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseType3"), pydantic.Field(alias="exerciseType3")
    ]
    exercise_frequency: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseFrequency"), pydantic.Field(alias="exerciseFrequency")
    ]
    exercise_hours_work: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseHoursWork"), pydantic.Field(alias="exerciseHoursWork")
    ]
    alcohol_usage: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholUsage"), pydantic.Field(alias="alcoholUsage")
    ]
    alcohol_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholType"), pydantic.Field(alias="alcoholType")
    ]
    alcohol_frequency: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholFrequency"), pydantic.Field(alias="alcoholFrequency")
    ]
    amount_per_day: typing_extensions.Annotated[
        str, FieldMetadata(alias="amountPerDay"), pydantic.Field(alias="amountPerDay")
    ]
    last_alcoholic_beverage: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastAlcoholicBeverage"), pydantic.Field(alias="lastAlcoholicBeverage")
    ]
    drugs: str
    drug_age: typing_extensions.Annotated[str, FieldMetadata(alias="drugAge"), pydantic.Field(alias="drugAge")]
    drug_type1: typing_extensions.Annotated[str, FieldMetadata(alias="drugType1"), pydantic.Field(alias="drugType1")]
    drug_frequency1: typing_extensions.Annotated[
        str, FieldMetadata(alias="drugFrequency1"), pydantic.Field(alias="drugFrequency1")
    ]
    drug_route: typing_extensions.Annotated[str, FieldMetadata(alias="drugRoute"), pydantic.Field(alias="drugRoute")]
    drug_type2: typing_extensions.Annotated[str, FieldMetadata(alias="drugType2"), pydantic.Field(alias="drugType2")]
    drug_frequency2: typing_extensions.Annotated[
        str, FieldMetadata(alias="drugFrequency2"), pydantic.Field(alias="drugFrequency2")
    ]
    drug_route2: typing_extensions.Annotated[str, FieldMetadata(alias="drugRoute2"), pydantic.Field(alias="drugRoute2")]
    drug_type3: typing_extensions.Annotated[str, FieldMetadata(alias="drugType3"), pydantic.Field(alias="drugType3")]
    drug_frequency3: typing_extensions.Annotated[
        str, FieldMetadata(alias="drugFrequency3"), pydantic.Field(alias="drugFrequency3")
    ]
    drug_route3: typing_extensions.Annotated[str, FieldMetadata(alias="drugRoute3"), pydantic.Field(alias="drugRoute3")]
    drug_treatment: typing_extensions.Annotated[
        str, FieldMetadata(alias="drugTreatment"), pydantic.Field(alias="drugTreatment")
    ]
    drug_treatment_count: typing_extensions.Annotated[
        str, FieldMetadata(alias="drugTreatmentCount"), pydantic.Field(alias="drugTreatmentCount")
    ]
    drug_medical_attention: typing_extensions.Annotated[
        str, FieldMetadata(alias="drugMedicalAttention"), pydantic.Field(alias="drugMedicalAttention")
    ]
    drug_medical_attention_count: typing_extensions.Annotated[
        str, FieldMetadata(alias="drugMedicalAttentionCount"), pydantic.Field(alias="drugMedicalAttentionCount")
    ]
    education_level: typing_extensions.Annotated[
        str, FieldMetadata(alias="educationLevel"), pydantic.Field(alias="educationLevel")
    ]
    degree: str
    passive_smoker: typing_extensions.Annotated[
        str, FieldMetadata(alias="passiveSmoker"), pydantic.Field(alias="passiveSmoker")
    ]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    tobacco_user_profile: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoUserProfile"), pydantic.Field(alias="tobaccoUserProfile")
    ]
    passive_tobacco_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="passiveTobaccoType"), pydantic.Field(alias="passiveTobaccoType")
    ]
    passive_length_exposure: typing_extensions.Annotated[
        str, FieldMetadata(alias="passiveLengthExposure"), pydantic.Field(alias="passiveLengthExposure")
    ]
    passive_level_exposure: typing_extensions.Annotated[
        str, FieldMetadata(alias="passiveLevelExposure"), pydantic.Field(alias="passiveLevelExposure")
    ]
    employment_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="employmentName"), pydantic.Field(alias="employmentName")
    ]
    employment_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="employmentStatus"), pydantic.Field(alias="employmentStatus")
    ]
    employment_restrictions: typing_extensions.Annotated[
        str, FieldMetadata(alias="employmentRestrictions"), pydantic.Field(alias="employmentRestrictions")
    ]
    occupation: str
    employment_retire_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="employmentRetireDate"), pydantic.Field(alias="employmentRetireDate")
    ]
    employment_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="employmentId"), pydantic.Field(alias="employmentId")
    ]
    tobacco_use_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoUseHealthConcern"), pydantic.Field(alias="tobaccoUseHealthConcern")
    ]
    tobacco_use_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoUseCategory"), pydantic.Field(alias="tobaccoUseCategory")
    ]
    exercise_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseHealthConcern"), pydantic.Field(alias="exerciseHealthConcern")
    ]
    exercise_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseCategory"), pydantic.Field(alias="exerciseCategory")
    ]
    alcohol_intake_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholIntakeHealthConcern"), pydantic.Field(alias="alcoholIntakeHealthConcern")
    ]
    alcohol_intake_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholIntakeCategory"), pydantic.Field(alias="alcoholIntakeCategory")
    ]
    employment_detail_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="employmentDetailHealthConcern"), pydantic.Field(alias="employmentDetailHealthConcern")
    ]
    employment_detail_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="employmentDetailCategory"), pydantic.Field(alias="employmentDetailCategory")
    ]
    drug_misuse_behavior_health_concern: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="drugMisuseBehaviorHealthConcern"),
        pydantic.Field(alias="drugMisuseBehaviorHealthConcern"),
    ]
    drug_misuse_behavior_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="drugMisuseBehaviorCategory"), pydantic.Field(alias="drugMisuseBehaviorCategory")
    ]
    educational_achievement_health_concern: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="educationalAchievementHealthConcern"),
        pydantic.Field(alias="educationalAchievementHealthConcern"),
    ]
    educational_achievement_category: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="educationalAchievementCategory"),
        pydantic.Field(alias="educationalAchievementCategory"),
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
