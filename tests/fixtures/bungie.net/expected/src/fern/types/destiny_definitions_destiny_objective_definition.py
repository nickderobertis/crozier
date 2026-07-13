

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_objective_perk_entry_definition import (
    DestinyDefinitionsDestinyObjectivePerkEntryDefinition,
)
from .destiny_definitions_destiny_objective_stat_entry_definition import (
    DestinyDefinitionsDestinyObjectiveStatEntryDefinition,
)


class DestinyDefinitionsDestinyObjectiveDefinition(UniversalBaseModel):
    """
    Defines an "Objective".
    An objective is a specific task you should accomplish in the game. These are referred to by:
    - Quest Steps (which are DestinyInventoryItemDefinition entities with Objectives)
    - Challenges (which are Objectives defined on an DestinyActivityDefintion)
    - Milestones (which refer to Objectives that are defined on both Quest Steps and Activities)
    - Anything else that the designers decide to do later.
    Objectives have progress, a notion of having been Completed, human readable data describing the task to be accomplished, and a lot of optional tack-on data that can enhance the information provided about the task.
    """

    allow_negative_value: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowNegativeValue")
    ] = pydantic.Field(default=None)
    """
    If true, the value is allowed to go negative.
    """

    allow_overcompletion: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowOvercompletion")
    ] = pydantic.Field(default=None)
    """
    If True, the progress will continue even beyond the point where the objective met its minimum completion requirements. Your UI will have to accommodate it.
    """

    allow_value_change_when_completed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowValueChangeWhenCompleted")
    ] = pydantic.Field(default=None)
    """
    If true, you can effectively "un-complete" this objective if you lose progress after crossing the completion threshold. 
    If False, once you complete the task it will remain completed forever by locking the value.
    """

    completed_value_style: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="completedValueStyle")
    ] = pydantic.Field(default=None)
    """
    The style to use when the objective is completed.
    """

    completion_value: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="completionValue")] = (
        pydantic.Field(default=None)
    )
    """
    The value that the unlock value defined in unlockValueHash must reach in order for the objective to be considered Completed. Used in calculating progress and completion status.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = pydantic.Field(default=None)
    """
    Ideally, this should tell you what your task is. I'm not going to lie to you though. Sometimes this doesn't have useful information at all. Which sucks, but there's nothing either of us can do about it.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    in_progress_value_style: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="inProgressValueStyle")
    ] = pydantic.Field(default=None)
    """
    The style to use when the objective is still in progress.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    is_counting_downward: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isCountingDownward")
    ] = pydantic.Field(default=None)
    """
    If true, completion means having an unlock value less than or equal to the completionValue.
    If False, completion means having an unlock value greater than or equal to the completionValue.
    """

    location_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="locationHash")] = (
        pydantic.Field(default=None)
    )
    """
    OPTIONAL: a hash identifier for the location at which this objective must be accomplished, if there is a location defined. Look up the DestinyLocationDefinition for this hash for that additional location info.
    """

    minimum_visibility_threshold: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minimumVisibilityThreshold")
    ] = pydantic.Field(default=None)
    """
    If nonzero, this is the minimum value at which the objective's progression should be shown. Otherwise, don't show it yet.
    """

    perks: typing.Optional[DestinyDefinitionsDestinyObjectivePerkEntryDefinition] = pydantic.Field(default=None)
    """
    If this objective enables Perks intrinsically, the conditions for that enabling are defined here.
    """

    progress_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="progressDescription")
    ] = pydantic.Field(default=None)
    """
    Text to describe the progress bar.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    scope: typing.Optional[int] = pydantic.Field(default=None)
    """
    A shortcut for determining the most restrictive gating that this Objective is set to use. This includes both the dynamic determination of progress and of completion values. See the DestinyGatingScope enum's documentation for more details.
    """

    show_value_on_complete: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showValueOnComplete")
    ] = pydantic.Field(default=None)
    """
    If True, you should continue showing the progression value in the UI after it's complete. I mean, we already do that in BNet anyways, but if you want to be better behaved than us you could honor this flag.
    """

    stats: typing.Optional[DestinyDefinitionsDestinyObjectiveStatEntryDefinition] = pydantic.Field(default=None)
    """
    If this objective enables modifications on a player's stats intrinsically, the conditions are defined here.
    """

    ui_label: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uiLabel")] = pydantic.Field(
        default=None
    )
    """
    Objectives can have arbitrary UI-defined identifiers that define the style applied to objectives. For convenience, known UI labels will be defined in the uiStyle enum value.
    """

    ui_style: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="uiStyle")] = pydantic.Field(
        default=None
    )
    """
    If the objective has a known UI label value, this property will represent it.
    """

    value_style: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="valueStyle")] = pydantic.Field(
        default=None
    )
    """
    The UI style applied to the objective. It's an enum, take a look at DestinyUnlockValueUIStyle for details of the possible styles. Use this info as you wish to customize your UI.
    DEPRECATED: This is no longer populated by Destiny 2 game content. Please use inProgressValueStyle and completedValueStyle instead.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
