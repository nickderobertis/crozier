

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_artifacts_destiny_artifact_character_scoped import DestinyArtifactsDestinyArtifactCharacterScoped
from .destiny_destiny_progression import DestinyDestinyProgression
from .destiny_entities_items_destiny_item_perks_component import DestinyEntitiesItemsDestinyItemPerksComponent
from .destiny_milestones_destiny_milestone import DestinyMilestonesDestinyMilestone
from .destiny_progression_destiny_faction_progression import DestinyProgressionDestinyFactionProgression
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress
from .destiny_quests_destiny_quest_status import DestinyQuestsDestinyQuestStatus


class DestinyEntitiesCharactersDestinyCharacterProgressionComponent(UniversalBaseModel):
    """
    This component returns anything that could be considered "Progression" on a user: data where the user is gaining levels, reputation, completions, rewards, etc...
    """

    checklists: typing.Optional[typing.Dict[str, typing.Dict[str, bool]]] = pydantic.Field(default=None)
    """
    The set of checklists that can be examined for this specific character, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition)
    For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.
    """

    factions: typing.Optional[typing.Dict[str, DestinyProgressionDestinyFactionProgression]] = pydantic.Field(
        default=None
    )
    """
    A dictionary of all known Factions, keyed by the Faction's hash. It contains data about this character's status with the faction.
    """

    milestones: typing.Optional[typing.Dict[str, DestinyMilestonesDestinyMilestone]] = pydantic.Field(default=None)
    """
    Milestones are related to the simple progressions shown in the game, but return additional and hopefully helpful information for users about the specifics of the Milestone's status.
    """

    progressions: typing.Optional[typing.Dict[str, DestinyDestinyProgression]] = pydantic.Field(default=None)
    """
    A Dictionary of all known progressions for the Character, keyed by the Progression's hash.
    Not all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition.
    """

    quests: typing.Optional[typing.List[DestinyQuestsDestinyQuestStatus]] = pydantic.Field(default=None)
    """
    If the user has any active quests, the quests' statuses will be returned here.
     Note that quests have been largely supplanted by Milestones, but that doesn't mean that they won't make a comeback independent of milestones at some point.
     (Fun fact: quests came back as I feared they would, but we never looped back to populate this... I'm going to put that in the backlog.)
    """

    seasonal_artifact: typing_extensions.Annotated[
        typing.Optional[DestinyArtifactsDestinyArtifactCharacterScoped],
        FieldMetadata(alias="seasonalArtifact"),
        pydantic.Field(
            alias="seasonalArtifact",
            description="Data related to your progress on the current season's artifact that can vary per character.",
        ),
    ] = None
    """
    Data related to your progress on the current season's artifact that can vary per character.
    """

    uninstanced_item_objectives: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.List[DestinyQuestsDestinyObjectiveProgress]]],
        FieldMetadata(alias="uninstancedItemObjectives"),
        pydantic.Field(
            alias="uninstancedItemObjectives",
            description="Sometimes, you have items in your inventory that don't have instances, but still have Objective information. This provides you that objective information for uninstanced items. \r\nThis dictionary is keyed by the item's hash: which you can use to look up the name and description for the overall task(s) implied by the objective. The value is the list of objectives for this item, and their statuses.",
        ),
    ] = None
    """
    Sometimes, you have items in your inventory that don't have instances, but still have Objective information. This provides you that objective information for uninstanced items. 
    This dictionary is keyed by the item's hash: which you can use to look up the name and description for the overall task(s) implied by the objective. The value is the list of objectives for this item, and their statuses.
    """

    uninstanced_item_perks: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyEntitiesItemsDestinyItemPerksComponent]],
        FieldMetadata(alias="uninstancedItemPerks"),
        pydantic.Field(
            alias="uninstancedItemPerks",
            description="Sometimes, you have items in your inventory that don't have instances, but still have perks (for example: Trials passage cards). This gives you the perk information for uninstanced items.\r\nThis dictionary is keyed by item hash, which you can use to look up the corresponding item definition. The value is the list of perks states for the item.",
        ),
    ] = None
    """
    Sometimes, you have items in your inventory that don't have instances, but still have perks (for example: Trials passage cards). This gives you the perk information for uninstanced items.
    This dictionary is keyed by item hash, which you can use to look up the corresponding item definition. The value is the list of perks states for the item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
