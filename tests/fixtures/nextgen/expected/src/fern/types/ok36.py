

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok36(UniversalBaseModel):
    group_name: typing_extensions.Annotated[str, FieldMetadata(alias="groupName"), pydantic.Field(alias="groupName")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    is_status_processed_successfully: typing_extensions.Annotated[
        str, FieldMetadata(alias="isStatusProcessedSuccessfully"), pydantic.Field(alias="isStatusProcessedSuccessfully")
    ]
    is_rule_found: typing_extensions.Annotated[
        str, FieldMetadata(alias="isRuleFound"), pydantic.Field(alias="isRuleFound")
    ]
    reference_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="referenceDate"), pydantic.Field(alias="referenceDate")
    ]
    person_date_of_birth: typing_extensions.Annotated[
        str, FieldMetadata(alias="personDateOfBirth"), pydantic.Field(alias="personDateOfBirth")
    ]
    cdc_start_month: typing_extensions.Annotated[
        str, FieldMetadata(alias="cdcStartMonth"), pydantic.Field(alias="cdcStartMonth")
    ]
    cdc_end_month: typing_extensions.Annotated[
        str, FieldMetadata(alias="cdcEndMonth"), pydantic.Field(alias="cdcEndMonth")
    ]
    next_due_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="nextDueDate"), pydantic.Field(alias="nextDueDate")
    ]
    status: str
    status_calculation_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="statusCalculationCode"), pydantic.Field(alias="statusCalculationCode")
    ]
    dose_sequence_status_calulated_for: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="doseSequenceStatusCalulatedFor"),
        pydantic.Field(alias="doseSequenceStatusCalulatedFor"),
    ]
    group_minimum_age_in_days: typing_extensions.Annotated[
        str, FieldMetadata(alias="groupMinimumAgeInDays"), pydantic.Field(alias="groupMinimumAgeInDays")
    ]
    group_maximum_age_in_days: typing_extensions.Annotated[
        str, FieldMetadata(alias="groupMaximumAgeInDays"), pydantic.Field(alias="groupMaximumAgeInDays")
    ]
    dose_minimum_age_in_days: typing_extensions.Annotated[
        str, FieldMetadata(alias="doseMinimumAgeInDays"), pydantic.Field(alias="doseMinimumAgeInDays")
    ]
    dose_maximum_age_in_days: typing_extensions.Annotated[
        str, FieldMetadata(alias="doseMaximumAgeInDays"), pydantic.Field(alias="doseMaximumAgeInDays")
    ]
    cvx_to_administer: typing_extensions.Annotated[
        str, FieldMetadata(alias="cvxToAdminister"), pydantic.Field(alias="cvxToAdminister")
    ]
    vaccine_to_administer: typing_extensions.Annotated[
        str, FieldMetadata(alias="vaccineToAdminister"), pydantic.Field(alias="vaccineToAdminister")
    ]
    total_doses: typing_extensions.Annotated[str, FieldMetadata(alias="totalDoses"), pydantic.Field(alias="totalDoses")]
    status_calculation_message: typing_extensions.Annotated[
        str, FieldMetadata(alias="statusCalculationMessage"), pydantic.Field(alias="statusCalculationMessage")
    ]
    next_due_date_calculation_message: typing_extensions.Annotated[
        str, FieldMetadata(alias="nextDueDateCalculationMessage"), pydantic.Field(alias="nextDueDateCalculationMessage")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
