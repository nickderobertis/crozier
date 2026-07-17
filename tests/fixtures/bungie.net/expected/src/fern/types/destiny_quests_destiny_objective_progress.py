

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyQuestsDestinyObjectiveProgress(UniversalBaseModel):
    """
    Returns data about a character's status with a given Objective. Combine with DestinyObjectiveDefinition static data for display purposes.
    """

    activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityHash"),
        pydantic.Field(
            alias="activityHash",
            description="If the Objective has an Activity associated with it, this is the unique identifier of the Activity being referred to. Use to look up the DestinyActivityDefinition in static data. This will give localized data about *what* you should be playing for the objective to be achieved.",
        ),
    ] = None
    """
    If the Objective has an Activity associated with it, this is the unique identifier of the Activity being referred to. Use to look up the DestinyActivityDefinition in static data. This will give localized data about *what* you should be playing for the objective to be achieved.
    """

    complete: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the Objective is completed.
    """

    completion_value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="completionValue"),
        pydantic.Field(
            alias="completionValue",
            description='As of Forsaken, objectives\' completion value is determined dynamically at runtime.\r\nThis value represents the threshold of progress you need to surpass in order for this objective to be considered "complete".\r\nIf you were using objective data, switch from using the DestinyObjectiveDefinition\'s "completionValue" to this value.',
        ),
    ] = None
    """
    As of Forsaken, objectives' completion value is determined dynamically at runtime.
    This value represents the threshold of progress you need to surpass in order for this objective to be considered "complete".
    If you were using objective data, switch from using the DestinyObjectiveDefinition's "completionValue" to this value.
    """

    destination_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="destinationHash"),
        pydantic.Field(
            alias="destinationHash",
            description="If the Objective has a Destination associated with it, this is the unique identifier of the Destination being referred to. Use to look up the DestinyDestinationDefinition in static data. This will give localized data about *where* in the universe the objective should be achieved.",
        ),
    ] = None
    """
    If the Objective has a Destination associated with it, this is the unique identifier of the Destination being referred to. Use to look up the DestinyDestinationDefinition in static data. This will give localized data about *where* in the universe the objective should be achieved.
    """

    objective_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="objectiveHash"),
        pydantic.Field(
            alias="objectiveHash",
            description="The unique identifier of the Objective being referred to. Use to look up the DestinyObjectiveDefinition in static data.",
        ),
    ] = None
    """
    The unique identifier of the Objective being referred to. Use to look up the DestinyObjectiveDefinition in static data.
    """

    progress: typing.Optional[int] = pydantic.Field(default=None)
    """
    If progress has been made, and the progress can be measured numerically, this will be the value of that progress. You can compare it to the DestinyObjectiveDefinition.completionValue property for current vs. upper bounds, and use DestinyObjectiveDefinition.inProgressValueStyle or completedValueStyle to determine how this should be rendered. Note that progress, in Destiny 2, need not be a literal numeric progression. It could be one of a number of possible values, even a Timestamp. Always examine DestinyObjectiveDefinition.inProgressValueStyle or completedValueStyle before rendering progress.
    """

    visible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, the objective is visible in-game. Otherwise, it's not yet visible to the player. Up to you if you want to honor this property.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
