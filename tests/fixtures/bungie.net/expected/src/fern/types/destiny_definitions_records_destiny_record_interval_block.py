

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_records_destiny_record_interval_objective import (
    DestinyDefinitionsRecordsDestinyRecordIntervalObjective,
)
from .destiny_definitions_records_destiny_record_interval_rewards import (
    DestinyDefinitionsRecordsDestinyRecordIntervalRewards,
)


class DestinyDefinitionsRecordsDestinyRecordIntervalBlock(UniversalBaseModel):
    interval_objectives: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsRecordsDestinyRecordIntervalObjective]],
        FieldMetadata(alias="intervalObjectives"),
        pydantic.Field(alias="intervalObjectives"),
    ] = None
    interval_rewards: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsRecordsDestinyRecordIntervalRewards]],
        FieldMetadata(alias="intervalRewards"),
        pydantic.Field(alias="intervalRewards"),
    ] = None
    original_objective_array_insertion_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="originalObjectiveArrayInsertionIndex"),
        pydantic.Field(alias="originalObjectiveArrayInsertionIndex"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
