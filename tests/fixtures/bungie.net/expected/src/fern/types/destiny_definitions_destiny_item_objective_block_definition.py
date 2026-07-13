

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_objective_display_properties import (
    DestinyDefinitionsDestinyObjectiveDisplayProperties,
)


class DestinyDefinitionsDestinyItemObjectiveBlockDefinition(UniversalBaseModel):
    """
    An item can have objectives on it. In practice, these are the exclusive purview of "Quest Step" items: DestinyInventoryItemDefinitions that represent a specific step in a Quest.
    Quest steps have 1:M objectives that we end up processing and returning in live data as DestinyQuestStatus data, and other useful information.
    """

    display_activity_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="displayActivityHashes")
    ] = pydantic.Field(default=None)
    """
    For every entry in objectiveHashes, there is a corresponding entry in this array at the same index. If the objective is meant to be associated with a specific DestinyActivityDefinition, there will be a valid hash at that index. Otherwise, it will be invalid (0).
    Rendered somewhat obsolete by perObjectiveDisplayProperties, which currently has much the same information but may end up with more info in the future.
    """

    display_as_stat_tracker: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="displayAsStatTracker")
    ] = None
    narrative: typing.Optional[str] = pydantic.Field(default=None)
    """
    The localized string for narrative text related to this quest step, if any.
    """

    objective_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="objectiveHashes")
    ] = pydantic.Field(default=None)
    """
    The hashes to Objectives (DestinyObjectiveDefinition) that are part of this Quest Step, in the order that they should be rendered.
    """

    objective_verb_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="objectiveVerbName")] = (
        pydantic.Field(default=None)
    )
    """
    The localized string describing an action to be performed associated with the objectives, if any.
    """

    per_objective_display_properties: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyObjectiveDisplayProperties]],
        FieldMetadata(alias="perObjectiveDisplayProperties"),
    ] = pydantic.Field(default=None)
    """
    One entry per Objective on the item, it will have related display information.
    """

    quest_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="questTypeHash")] = (
        pydantic.Field(default=None)
    )
    """
    A hashed value for the questTypeIdentifier, because apparently I like to be redundant.
    """

    quest_type_identifier: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="questTypeIdentifier")
    ] = pydantic.Field(default=None)
    """
    The identifier for the type of quest being performed, if any. Not associated with any fixed definition, yet.
    """

    questline_item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="questlineItemHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash for the DestinyInventoryItemDefinition representing the Quest to which this Quest Step belongs.
    """

    require_full_objective_completion: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requireFullObjectiveCompletion")
    ] = pydantic.Field(default=None)
    """
    If True, all objectives must be completed for the step to be completed. If False, any one objective can be completed for the step to be completed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
