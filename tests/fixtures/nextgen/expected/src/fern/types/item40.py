

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item40(UniversalBaseModel):
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="sequenceNumber"), pydantic.Field(alias="sequenceNumber")
    ]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    maximum_tobacco_free_duration: typing_extensions.Annotated[
        str, FieldMetadata(alias="maximumTobaccoFreeDuration"), pydantic.Field(alias="maximumTobaccoFreeDuration")
    ]
    pack_years: typing_extensions.Annotated[str, FieldMetadata(alias="packYears"), pydantic.Field(alias="packYears")]
    passive_exposure: typing_extensions.Annotated[
        str, FieldMetadata(alias="passiveExposure"), pydantic.Field(alias="passiveExposure")
    ]
    relapse_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="relapseReason"), pydantic.Field(alias="relapseReason")
    ]
    tobacco_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoType"), pydantic.Field(alias="tobaccoType")
    ]
    social_history_tobacco_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="socialHistoryTobaccoType"), pydantic.Field(alias="socialHistoryTobaccoType")
    ]
    tobacco_use_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoUseStatus"), pydantic.Field(alias="tobaccoUseStatus")
    ]
    total_pack_years: typing_extensions.Annotated[
        str, FieldMetadata(alias="totalPackYears"), pydantic.Field(alias="totalPackYears")
    ]
    tried_to_quit: typing_extensions.Annotated[
        str, FieldMetadata(alias="triedToQuit"), pydantic.Field(alias="triedToQuit")
    ]
    units_per_day: typing_extensions.Annotated[
        str, FieldMetadata(alias="unitsPerDay"), pydantic.Field(alias="unitsPerDay")
    ]
    year_quit: typing_extensions.Annotated[str, FieldMetadata(alias="yearQuit"), pydantic.Field(alias="yearQuit")]
    years_used: typing_extensions.Annotated[str, FieldMetadata(alias="yearsUsed"), pydantic.Field(alias="yearsUsed")]
    age_started: typing_extensions.Annotated[str, FieldMetadata(alias="ageStarted"), pydantic.Field(alias="ageStarted")]
    age_stopped: typing_extensions.Annotated[str, FieldMetadata(alias="ageStopped"), pydantic.Field(alias="ageStopped")]
    date_started: typing_extensions.Annotated[
        str, FieldMetadata(alias="dateStarted"), pydantic.Field(alias="dateStarted")
    ]
    date_stopped: typing_extensions.Annotated[
        str, FieldMetadata(alias="dateStopped"), pydantic.Field(alias="dateStopped")
    ]
    smoking_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="smokingStatus"), pydantic.Field(alias="smokingStatus")
    ]
    tobacco_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoStatus"), pydantic.Field(alias="tobaccoStatus")
    ]
    usage_per_day: typing_extensions.Annotated[
        str, FieldMetadata(alias="usagePerDay"), pydantic.Field(alias="usagePerDay")
    ]
    social_history_create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="socialHistoryCreateTimestamp"), pydantic.Field(alias="socialHistoryCreateTimestamp")
    ]
    tobacco_user_profile_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoUserProfileCode"), pydantic.Field(alias="tobaccoUserProfileCode")
    ]
    tobacco_user_profile: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoUserProfile"), pydantic.Field(alias="tobaccoUserProfile")
    ]
    use_daily_cigarette: typing_extensions.Annotated[
        str, FieldMetadata(alias="useDailyCigarette"), pydantic.Field(alias="useDailyCigarette")
    ]
    age_started_cigarette: typing_extensions.Annotated[
        str, FieldMetadata(alias="ageStartedCigarette"), pydantic.Field(alias="ageStartedCigarette")
    ]
    age_stopped_cigarette: typing_extensions.Annotated[
        str, FieldMetadata(alias="ageStoppedCigarette"), pydantic.Field(alias="ageStoppedCigarette")
    ]
    usage_per_day_cigarette: typing_extensions.Annotated[
        str, FieldMetadata(alias="usagePerDayCigarette"), pydantic.Field(alias="usagePerDayCigarette")
    ]
    use_daily_cigarillo: typing_extensions.Annotated[
        str, FieldMetadata(alias="useDailyCigarillo"), pydantic.Field(alias="useDailyCigarillo")
    ]
    age_started_cigarillo: typing_extensions.Annotated[
        str, FieldMetadata(alias="ageStartedCigarillo"), pydantic.Field(alias="ageStartedCigarillo")
    ]
    age_stopped_cigarillo: typing_extensions.Annotated[
        str, FieldMetadata(alias="ageStoppedCigarillo"), pydantic.Field(alias="ageStoppedCigarillo")
    ]
    usage_per_day_cigarillo: typing_extensions.Annotated[
        str, FieldMetadata(alias="usagePerDayCigarillo"), pydantic.Field(alias="usagePerDayCigarillo")
    ]
    use_daily_cigar: typing_extensions.Annotated[
        str, FieldMetadata(alias="useDailyCigar"), pydantic.Field(alias="useDailyCigar")
    ]
    age_started_cigar: typing_extensions.Annotated[
        str, FieldMetadata(alias="ageStartedCigar"), pydantic.Field(alias="ageStartedCigar")
    ]
    age_stopped_cigar: typing_extensions.Annotated[
        str, FieldMetadata(alias="ageStoppedCigar"), pydantic.Field(alias="ageStoppedCigar")
    ]
    usage_per_day_cigar: typing_extensions.Annotated[
        str, FieldMetadata(alias="usagePerDayCigar"), pydantic.Field(alias="usagePerDayCigar")
    ]
    use_daily_pipe: typing_extensions.Annotated[
        str, FieldMetadata(alias="useDailyPipe"), pydantic.Field(alias="useDailyPipe")
    ]
    age_started_pipe: typing_extensions.Annotated[
        str, FieldMetadata(alias="ageStartedPipe"), pydantic.Field(alias="ageStartedPipe")
    ]
    age_stopped_pipe: typing_extensions.Annotated[
        str, FieldMetadata(alias="ageStoppedPipe"), pydantic.Field(alias="ageStoppedPipe")
    ]
    usage_per_day_pipe: typing_extensions.Annotated[
        str, FieldMetadata(alias="usagePerDayPipe"), pydantic.Field(alias="usagePerDayPipe")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
