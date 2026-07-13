

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_node_activation_requirement import DestinyDefinitionsDestinyNodeActivationRequirement
from .destiny_definitions_destiny_node_socket_replace_response import DestinyDefinitionsDestinyNodeSocketReplaceResponse
from .destiny_definitions_destiny_talent_node_step_groups import DestinyDefinitionsDestinyTalentNodeStepGroups


class DestinyDefinitionsDestinyNodeStepDefinition(UniversalBaseModel):
    """
    This defines the properties of a "Talent Node Step". When you see a talent node in game, the actual visible properties that you see (its icon, description, the perks and stats it provides) are not provided by the Node itself, but rather by the currently active Step on the node.
    When a Talent Node is activated, the currently active step's benefits are conferred upon the item and character.
    The currently active step on talent nodes are determined when an item is first instantiated. Sometimes it is random, sometimes it is more deterministic (particularly when a node has only a single step).
    Note that, when dealing with Talent Node Steps, you must ensure that you have the latest version of content. stepIndex and nodeStepHash - two ways of identifying the step within a node - are both content version dependent, and thus are subject to change between content updates.
    """

    activation_requirement: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyNodeActivationRequirement],
        FieldMetadata(alias="activationRequirement"),
    ] = pydantic.Field(default=None)
    """
    If the step has requirements for activation (they almost always do, if nothing else than for the Talent Grid's Progression to have reached a certain level), they will be defined here.
    """

    affects_level: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="affectsLevel")] = (
        pydantic.Field(default=None)
    )
    """
    If true, this step can affect the level of the item. See DestinyInventoryItemDefintion for more information about item levels and their effect on stats.
    """

    affects_quality: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="affectsQuality")] = (
        pydantic.Field(default=None)
    )
    """
    If this is true, the step affects the item's Quality in some way. See DestinyInventoryItemDefinition for more information about the meaning of Quality. I already made a joke about Zen and the Art of Motorcycle Maintenance elsewhere in the documentation, so I will avoid doing it again. Oops too late
    """

    can_activate_next_step: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="canActivateNextStep")
    ] = pydantic.Field(default=None)
    """
    There was a time when talent nodes could be activated multiple times, and the effects of subsequent Steps would be compounded on each other, essentially "upgrading" the node. We have moved away from this, but theoretically the capability still exists.
    I continue to return this in case it is used in the future: if true and this step is the current step in the node, you are allowed to activate the node a second time to receive the benefits of the next step in the node, which will then become the active step.
    """

    damage_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="damageType")] = pydantic.Field(
        default=None
    )
    """
    An enum representing a damage type granted by activating this step, if any.
    """

    damage_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="damageTypeHash")] = (
        pydantic.Field(default=None)
    )
    """
    If the step provides a damage type, this will be the hash identifier used to look up the damage type's DestinyDamageTypeDefinition.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = pydantic.Field(default=None)
    """
    These are the display properties actually used to render the Talent Node. The currently active step's displayProperties are shown.
    """

    interaction_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="interactionDescription")
    ] = pydantic.Field(default=None)
    """
    If you can interact with this node in some way, this is the localized description of that interaction.
    """

    is_next_step_random: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isNextStepRandom")] = (
        pydantic.Field(default=None)
    )
    """
    If true, the next step to be chosen is random, and if you're allowed to activate the next step. (if canActivateNextStep = true)
    """

    next_step_index: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="nextStepIndex")] = (
        pydantic.Field(default=None)
    )
    """
    The stepIndex of the next step in the talent node, or -1 if this is the last step or if the next step to be chosen is random.
    This doesn't really matter anymore unless canActivateNextStep begins to be used again.
    """

    node_step_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="nodeStepHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash of this node step. Unfortunately, while it can be used to uniquely identify the step within a node, it is also content version dependent and should not be relied on without ensuring you have the latest vesion of content.
    """

    perk_hashes: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="perkHashes")] = (
        pydantic.Field(default=None)
    )
    """
    The list of hash identifiers for Perks (DestinySandboxPerkDefinition) that are applied when this step is active. Perks provide a variety of benefits and modifications - examine DestinySandboxPerkDefinition to learn more.
    """

    socket_replacements: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyNodeSocketReplaceResponse]],
        FieldMetadata(alias="socketReplacements"),
    ] = pydantic.Field(default=None)
    """
    If this step is activated, this will be a list of information used to replace socket items with new Plugs. See DestinyInventoryItemDefinition for more information about sockets and plugs.
    """

    start_progression_bar_at_progress: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="startProgressionBarAtProgress")
    ] = pydantic.Field(default=None)
    """
    When the Talent Grid's progression reaches this value, the circular "progress bar" that surrounds the talent node should be shown.
    This also indicates the lower bound of said progress bar, with the upper bound being the progress required to reach activationRequirement.gridLevel. (at some point I should precalculate the upper bound and put it in the definition to save people time)
    """

    stat_hashes: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="statHashes")] = (
        pydantic.Field(default=None)
    )
    """
    When the step provides stat benefits on the item or character, this is the list of hash identifiers for stats (DestinyStatDefinition) that are provided.
    """

    step_groups: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyTalentNodeStepGroups], FieldMetadata(alias="stepGroups")
    ] = pydantic.Field(default=None)
    """
    In Destiny 1, the Armory's Perk Filtering was driven by a concept of TalentNodeStepGroups: categorizations of talent nodes based on their functionality. While the Armory isn't a BNet-facing thing for now, and the new Armory will need to account for Sockets rather than Talent Nodes, this categorization capability feels useful enough to still keep around.
    """

    step_index: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="stepIndex")] = pydantic.Field(
        default=None
    )
    """
    The index of this step in the list of Steps on the Talent Node.
    Unfortunately, this is the closest thing we have to an identifier for the Step: steps are not provided a content version agnostic identifier. This means that, when you are dealing with talent nodes, you will need to first ensure that you have the latest version of content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
