

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item39(UniversalBaseModel):
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    modify_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimezone"), pydantic.Field(alias="modifyTimestampTimezone")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    home_language: typing_extensions.Annotated[
        str, FieldMetadata(alias="homeLanguage"), pydantic.Field(alias="homeLanguage")
    ]
    birth_country: typing_extensions.Annotated[
        str, FieldMetadata(alias="birthCountry"), pydantic.Field(alias="birthCountry")
    ]
    hand_dominance: typing_extensions.Annotated[
        str, FieldMetadata(alias="handDominance"), pydantic.Field(alias="handDominance")
    ]
    education_level: typing_extensions.Annotated[
        str, FieldMetadata(alias="educationLevel"), pydantic.Field(alias="educationLevel")
    ]
    education_degree: typing_extensions.Annotated[
        str, FieldMetadata(alias="educationDegree"), pydantic.Field(alias="educationDegree")
    ]
    education_degree_country: typing_extensions.Annotated[
        str, FieldMetadata(alias="educationDegreeCountry"), pydantic.Field(alias="educationDegreeCountry")
    ]
    occupational_hazard1: typing_extensions.Annotated[
        str, FieldMetadata(alias="occupationalHazard1"), pydantic.Field(alias="occupationalHazard1")
    ]
    occupational_hazard2: typing_extensions.Annotated[
        str, FieldMetadata(alias="occupationalHazard2"), pydantic.Field(alias="occupationalHazard2")
    ]
    has_military_experience: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasMilitaryExperience"), pydantic.Field(alias="hasMilitaryExperience")
    ]
    military_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="militaryType"), pydantic.Field(alias="militaryType")
    ]
    military_branch: typing_extensions.Annotated[
        str, FieldMetadata(alias="militaryBranch"), pydantic.Field(alias="militaryBranch")
    ]
    military_years_served: typing_extensions.Annotated[
        str, FieldMetadata(alias="militaryYearsServed"), pydantic.Field(alias="militaryYearsServed")
    ]
    military_discharge_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="militaryDischargeType"), pydantic.Field(alias="militaryDischargeType")
    ]
    military_stationed_overseas: typing_extensions.Annotated[
        str, FieldMetadata(alias="militaryStationedOverseas"), pydantic.Field(alias="militaryStationedOverseas")
    ]
    military_stationed_overseas_location: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="militaryStationedOverseasLocation"),
        pydantic.Field(alias="militaryStationedOverseasLocation"),
    ]
    military_noise_exposure: typing_extensions.Annotated[
        str, FieldMetadata(alias="militaryNoiseExposure"), pydantic.Field(alias="militaryNoiseExposure")
    ]
    military_biohazard_exposure: typing_extensions.Annotated[
        str, FieldMetadata(alias="militaryBiohazardExposure"), pydantic.Field(alias="militaryBiohazardExposure")
    ]
    previous_widowed: typing_extensions.Annotated[
        str, FieldMetadata(alias="previousWidowed"), pydantic.Field(alias="previousWidowed")
    ]
    previous_widowed_times: typing_extensions.Annotated[
        str, FieldMetadata(alias="previousWidowedTimes"), pydantic.Field(alias="previousWidowedTimes")
    ]
    previous_divorce: typing_extensions.Annotated[
        str, FieldMetadata(alias="previousDivorce"), pydantic.Field(alias="previousDivorce")
    ]
    previous_divorce_times: typing_extensions.Annotated[
        str, FieldMetadata(alias="previousDivorceTimes"), pydantic.Field(alias="previousDivorceTimes")
    ]
    has_children: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasChildren"), pydantic.Field(alias="hasChildren")
    ]
    sons_count: typing_extensions.Annotated[str, FieldMetadata(alias="sonsCount"), pydantic.Field(alias="sonsCount")]
    daughters_count: typing_extensions.Annotated[
        str, FieldMetadata(alias="daughtersCount"), pydantic.Field(alias="daughtersCount")
    ]
    support_network_comments: typing_extensions.Annotated[
        str, FieldMetadata(alias="supportNetworkComments"), pydantic.Field(alias="supportNetworkComments")
    ]
    support_network: typing_extensions.Annotated[
        str, FieldMetadata(alias="supportNetwork"), pydantic.Field(alias="supportNetwork")
    ]
    primary_residence_comments: typing_extensions.Annotated[
        str, FieldMetadata(alias="primaryResidenceComments"), pydantic.Field(alias="primaryResidenceComments")
    ]
    tobacco_usage: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoUsage"), pydantic.Field(alias="tobaccoUsage")
    ]
    tobacco_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoType"), pydantic.Field(alias="tobaccoType")
    ]
    tobacco_units_per_day: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoUnitsPerDay"), pydantic.Field(alias="tobaccoUnitsPerDay")
    ]
    tobacco_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoUnit"), pydantic.Field(alias="tobaccoUnit")
    ]
    tobacco_years_smoked: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoYearsSmoked"), pydantic.Field(alias="tobaccoYearsSmoked")
    ]
    tobacco_pack_years: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoPackYears"), pydantic.Field(alias="tobaccoPackYears")
    ]
    tobacco_current_or_past: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoCurrentOrPast"), pydantic.Field(alias="tobaccoCurrentOrPast")
    ]
    tobacco_previous_cessation_attempt: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tobaccoPreviousCessationAttempt"),
        pydantic.Field(alias="tobaccoPreviousCessationAttempt"),
    ]
    tobacco_year_quit: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoYearQuit"), pydantic.Field(alias="tobaccoYearQuit")
    ]
    tobacco_longest_free_period: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoLongestFreePeriod"), pydantic.Field(alias="tobaccoLongestFreePeriod")
    ]
    tobacco_relapse_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoRelapseReason"), pydantic.Field(alias="tobaccoRelapseReason")
    ]
    passive_smoke_exposure: typing_extensions.Annotated[
        str, FieldMetadata(alias="passiveSmokeExposure"), pydantic.Field(alias="passiveSmokeExposure")
    ]
    tobacco_cessation_methods: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoCessationMethods"), pydantic.Field(alias="tobaccoCessationMethods")
    ]
    alcohol_usage: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholUsage"), pydantic.Field(alias="alcoholUsage")
    ]
    caffeine_usage: typing_extensions.Annotated[
        str, FieldMetadata(alias="caffeineUsage"), pydantic.Field(alias="caffeineUsage")
    ]
    caffeine_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="caffeineType"), pydantic.Field(alias="caffeineType")
    ]
    caffeine_type2: typing_extensions.Annotated[
        str, FieldMetadata(alias="caffeineType2"), pydantic.Field(alias="caffeineType2")
    ]
    caffeine_per_day: typing_extensions.Annotated[
        str, FieldMetadata(alias="caffeinePerDay"), pydantic.Field(alias="caffeinePerDay")
    ]
    activity_level: typing_extensions.Annotated[
        str, FieldMetadata(alias="activityLevel"), pydantic.Field(alias="activityLevel")
    ]
    health_club_member: typing_extensions.Annotated[
        str, FieldMetadata(alias="healthClubMember"), pydantic.Field(alias="healthClubMember")
    ]
    exercise_frequency: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseFrequency"), pydantic.Field(alias="exerciseFrequency")
    ]
    exercise_hours_week: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseHoursWeek"), pydantic.Field(alias="exerciseHoursWeek")
    ]
    exercise_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="exerciseType"), pydantic.Field(alias="exerciseType")
    ]
    exercisetype2: str
    exercisetype3: str
    hobby1: str
    hobby2: str
    hobby3: str
    diet_history1: typing_extensions.Annotated[
        str, FieldMetadata(alias="dietHistory1"), pydantic.Field(alias="dietHistory1")
    ]
    diet_history2: typing_extensions.Annotated[
        str, FieldMetadata(alias="dietHistory2"), pydantic.Field(alias="dietHistory2")
    ]
    diet_history3: typing_extensions.Annotated[
        str, FieldMetadata(alias="dietHistory3"), pydantic.Field(alias="dietHistory3")
    ]
    diet_history4: typing_extensions.Annotated[
        str, FieldMetadata(alias="dietHistory4"), pydantic.Field(alias="dietHistory4")
    ]
    diet_history5: typing_extensions.Annotated[
        str, FieldMetadata(alias="dietHistory5"), pydantic.Field(alias="dietHistory5")
    ]
    pet_animals: typing_extensions.Annotated[str, FieldMetadata(alias="petAnimals"), pydantic.Field(alias="petAnimals")]
    pet_birds: typing_extensions.Annotated[str, FieldMetadata(alias="petBirds"), pydantic.Field(alias="petBirds")]
    pet_dogs: typing_extensions.Annotated[str, FieldMetadata(alias="petDogs"), pydantic.Field(alias="petDogs")]
    pet_rodents: typing_extensions.Annotated[str, FieldMetadata(alias="petRodents"), pydantic.Field(alias="petRodents")]
    pet_reptiles: typing_extensions.Annotated[
        str, FieldMetadata(alias="petReptiles"), pydantic.Field(alias="petReptiles")
    ]
    pet_other: typing_extensions.Annotated[str, FieldMetadata(alias="petOther"), pydantic.Field(alias="petOther")]
    pets: str
    cleans_animals: typing_extensions.Annotated[
        str, FieldMetadata(alias="cleansAnimals"), pydantic.Field(alias="cleansAnimals")
    ]
    changes_in_sleep_patterns: typing_extensions.Annotated[
        str, FieldMetadata(alias="changesInSleepPatterns"), pydantic.Field(alias="changesInSleepPatterns")
    ]
    religious_affiliation: typing_extensions.Annotated[
        str, FieldMetadata(alias="religiousAffiliation"), pydantic.Field(alias="religiousAffiliation")
    ]
    practice_religion: typing_extensions.Annotated[
        str, FieldMetadata(alias="practiceReligion"), pydantic.Field(alias="practiceReligion")
    ]
    spiritual_beliefs: typing_extensions.Annotated[
        str, FieldMetadata(alias="spiritualBeliefs"), pydantic.Field(alias="spiritualBeliefs")
    ]
    importance_of_religion_spirituality: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="importanceOfReligionSpirituality"),
        pydantic.Field(alias="importanceOfReligionSpirituality"),
    ]
    smoke_detectors_in_home: typing_extensions.Annotated[
        str, FieldMetadata(alias="smokeDetectorsInHome"), pydantic.Field(alias="smokeDetectorsInHome")
    ]
    carbon_monoxide_detectors_in_home: typing_extensions.Annotated[
        str, FieldMetadata(alias="carbonMonoxideDetectorsInHome"), pydantic.Field(alias="carbonMonoxideDetectorsInHome")
    ]
    radon_in_home: typing_extensions.Annotated[
        str, FieldMetadata(alias="radonInHome"), pydantic.Field(alias="radonInHome")
    ]
    home_heating: typing_extensions.Annotated[
        str, FieldMetadata(alias="homeHeating"), pydantic.Field(alias="homeHeating")
    ]
    seat_belt_usage: typing_extensions.Annotated[
        str, FieldMetadata(alias="seatBeltUsage"), pydantic.Field(alias="seatBeltUsage")
    ]
    fire_arms_at_home: typing_extensions.Annotated[
        str, FieldMetadata(alias="fireArmsAtHome"), pydantic.Field(alias="fireArmsAtHome")
    ]
    agrees_to_transfusion: typing_extensions.Annotated[
        str, FieldMetadata(alias="agreesToTransfusion"), pydantic.Field(alias="agreesToTransfusion")
    ]
    travel_out_of_state: typing_extensions.Annotated[
        str, FieldMetadata(alias="travelOutOfState"), pydantic.Field(alias="travelOutOfState")
    ]
    travel_out_of_state_location: typing_extensions.Annotated[
        str, FieldMetadata(alias="travelOutOfStateLocation"), pydantic.Field(alias="travelOutOfStateLocation")
    ]
    travel_out_of_country: typing_extensions.Annotated[
        str, FieldMetadata(alias="travelOutOfCountry"), pydantic.Field(alias="travelOutOfCountry")
    ]
    travel_out_of_counrty_location: typing_extensions.Annotated[
        str, FieldMetadata(alias="travelOutOfCounrtyLocation"), pydantic.Field(alias="travelOutOfCounrtyLocation")
    ]
    travel_out_of_country_region: typing_extensions.Annotated[
        str, FieldMetadata(alias="travelOutOfCountryRegion"), pydantic.Field(alias="travelOutOfCountryRegion")
    ]
    travel_exposure: typing_extensions.Annotated[
        str, FieldMetadata(alias="travelExposure"), pydantic.Field(alias="travelExposure")
    ]
    travel_exposure_detail: typing_extensions.Annotated[
        str, FieldMetadata(alias="travelExposureDetail"), pydantic.Field(alias="travelExposureDetail")
    ]
    advance_directives_review_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="advanceDirectivesReviewDate"), pydantic.Field(alias="advanceDirectivesReviewDate")
    ]
    advance_directives_none: typing_extensions.Annotated[
        str, FieldMetadata(alias="advanceDirectivesNone"), pydantic.Field(alias="advanceDirectivesNone")
    ]
    advance_directives_refused: typing_extensions.Annotated[
        str, FieldMetadata(alias="advanceDirectivesRefused"), pydantic.Field(alias="advanceDirectivesRefused")
    ]
    advance_directives_dnr: typing_extensions.Annotated[
        str, FieldMetadata(alias="advanceDirectivesDnr"), pydantic.Field(alias="advanceDirectivesDnr")
    ]
    advance_directives_living_will: typing_extensions.Annotated[
        str, FieldMetadata(alias="advanceDirectivesLivingWill"), pydantic.Field(alias="advanceDirectivesLivingWill")
    ]
    advance_directives_do_not_place_on_life_support: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="advanceDirectivesDoNotPlaceOnLifeSupport"),
        pydantic.Field(alias="advanceDirectivesDoNotPlaceOnLifeSupport"),
    ]
    advance_directives_durable_power_of_attorney: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="advanceDirectivesDurablePowerOfAttorney"),
        pydantic.Field(alias="advanceDirectivesDurablePowerOfAttorney"),
    ]
    advance_directives_hc_proxy: typing_extensions.Annotated[
        str, FieldMetadata(alias="advanceDirectivesHcProxy"), pydantic.Field(alias="advanceDirectivesHcProxy")
    ]
    advance_directives_hc_proxy_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="advanceDirectivesHcProxyName"), pydantic.Field(alias="advanceDirectivesHcProxyName")
    ]
    advance_directives_incremented: typing_extensions.Annotated[
        str, FieldMetadata(alias="advanceDirectivesIncremented"), pydantic.Field(alias="advanceDirectivesIncremented")
    ]
    advance_directives_discussions_count: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="advanceDirectivesDiscussionsCount"),
        pydantic.Field(alias="advanceDirectivesDiscussionsCount"),
    ]
    comments: str
    alcohol_year_quit: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholYearQuit"), pydantic.Field(alias="alcoholYearQuit")
    ]
    alcohol_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholType"), pydantic.Field(alias="alcoholType")
    ]
    alcohol_frequency: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholFrequency"), pydantic.Field(alias="alcoholFrequency")
    ]
    alcohol_last_drink: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholLastDrink"), pydantic.Field(alias="alcoholLastDrink")
    ]
    alcohol_amount: typing_extensions.Annotated[
        str, FieldMetadata(alias="alcoholAmount"), pydantic.Field(alias="alcoholAmount")
    ]
    smoking_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="smokingStatus"), pydantic.Field(alias="smokingStatus")
    ]
    smoking_status_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="smokingStatusCode"), pydantic.Field(alias="smokingStatusCode")
    ]
    marital_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="maritalStatus"), pydantic.Field(alias="maritalStatus")
    ]
    religion: str
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
