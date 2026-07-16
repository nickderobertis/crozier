

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_node_activation_requirement import DestinyDefinitionsDestinyNodeActivationRequirement
from .destiny_definitions_destiny_node_step_definition import DestinyDefinitionsDestinyNodeStepDefinition


class DestinyDefinitionsDestinyTalentNodeDefinition(UniversalBaseModel):
    """
    Talent Grids on items have Nodes. These nodes have positions in the talent grid's UI, and contain "Steps" (DestinyTalentNodeStepDefinition), one of whom will be the "Current" step.
    The Current Step determines the visual properties of the node, as well as what the node grants when it is activated.
    See DestinyTalentGridDefinition for a more complete overview of how Talent Grids work, and how they are used in Destiny 2 (and how they were used in Destiny 1).
    """

    auto_unlocks: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoUnlocks"),
        pydantic.Field(
            alias="autoUnlocks",
            description="If true, this node will automatically unlock when the Talent Grid's level reaches the required level of the current step of this node.",
        ),
    ] = None
    """
    If true, this node will automatically unlock when the Talent Grid's level reaches the required level of the current step of this node.
    """

    binary_pair_node_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="binaryPairNodeIndex"),
        pydantic.Field(
            alias="binaryPairNodeIndex",
            description='At one point, Talent Nodes supported the idea of "Binary Pairs": nodes that overlapped each other visually, and where activating one deactivated the other. They ended up not being used, mostly because Exclusive Sets are *almost* a superset of this concept, but the potential for it to be used still exists in theory.\r\nIf this is ever used, this will be the index into the DestinyTalentGridDefinition.nodes property for the node that is the binary pair match to this node. Activating one deactivates the other.',
        ),
    ] = None
    """
    At one point, Talent Nodes supported the idea of "Binary Pairs": nodes that overlapped each other visually, and where activating one deactivated the other. They ended up not being used, mostly because Exclusive Sets are *almost* a superset of this concept, but the potential for it to be used still exists in theory.
    If this is ever used, this will be the index into the DestinyTalentGridDefinition.nodes property for the node that is the binary pair match to this node. Activating one deactivates the other.
    """

    column: typing.Optional[int] = pydantic.Field(default=None)
    """
    The visual "column" where the node should be shown in the UI. If negative, the node is hidden.
    """

    exclusive_with_node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="exclusiveWithNodeHashes"),
        pydantic.Field(
            alias="exclusiveWithNodeHashes",
            description="The nodeHash values for nodes that are in an Exclusive Set with this node.\r\nSee DestinyTalentGridDefinition.exclusiveSets for more info about exclusive sets.\r\nAgain, note that these are nodeHashes and *not* nodeIndexes.",
        ),
    ] = None
    """
    The nodeHash values for nodes that are in an Exclusive Set with this node.
    See DestinyTalentGridDefinition.exclusiveSets for more info about exclusive sets.
    Again, note that these are nodeHashes and *not* nodeIndexes.
    """

    group_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="groupHash"),
        pydantic.Field(
            alias="groupHash",
            description='As of Destiny 2, nodes can exist as part of "Exclusive Groups". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause "opposing" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.\r\nSee DestinyTalentExclusiveGroup for more information on the details. This is an identifier for this node\'s group, if it is part of one.',
        ),
    ] = None
    """
    As of Destiny 2, nodes can exist as part of "Exclusive Groups". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause "opposing" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.
    See DestinyTalentExclusiveGroup for more information on the details. This is an identifier for this node's group, if it is part of one.
    """

    ignore_for_completion: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="ignoreForCompletion"),
        pydantic.Field(
            alias="ignoreForCompletion",
            description="Comes from the talent grid node style: if true, then this node should be ignored for determining whether the grid is complete.",
        ),
    ] = None
    """
    Comes from the talent grid node style: if true, then this node should be ignored for determining whether the grid is complete.
    """

    is_random: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isRandom"),
        pydantic.Field(
            alias="isRandom",
            description="If this is true, the node's step is determined randomly rather than the first step being chosen.",
        ),
    ] = None
    """
    If this is true, the node's step is determined randomly rather than the first step being chosen.
    """

    is_random_repurchasable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isRandomRepurchasable"),
        pydantic.Field(
            alias="isRandomRepurchasable",
            description='If this is true, the node can be "re-rolled" to acquire a different random current step. This is not used, but still exists for a theoretical future of talent grids.',
        ),
    ] = None
    """
    If this is true, the node can be "re-rolled" to acquire a different random current step. This is not used, but still exists for a theoretical future of talent grids.
    """

    last_step_repeats: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="lastStepRepeats"),
        pydantic.Field(
            alias="lastStepRepeats",
            description="At one point, Nodes were going to be able to be activated multiple times, changing the current step and potentially piling on multiple effects from the previously activated steps. This property would indicate if the last step could be activated multiple times. \r\nThis is not currently used, but it isn't out of the question that this could end up being used again in a theoretical future.",
        ),
    ] = None
    """
    At one point, Nodes were going to be able to be activated multiple times, changing the current step and potentially piling on multiple effects from the previously activated steps. This property would indicate if the last step could be activated multiple times. 
    This is not currently used, but it isn't out of the question that this could end up being used again in a theoretical future.
    """

    layout_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="layoutIdentifier"),
        pydantic.Field(
            alias="layoutIdentifier",
            description="A string identifier for a custom visual layout to apply to this talent node. Unfortunately, we do not have any data for rendering these custom layouts. It will be up to you to interpret these strings and change your UI if you want to have custom UI matching these layouts.",
        ),
    ] = None
    """
    A string identifier for a custom visual layout to apply to this talent node. Unfortunately, we do not have any data for rendering these custom layouts. It will be up to you to interpret these strings and change your UI if you want to have custom UI matching these layouts.
    """

    lore_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="loreHash"),
        pydantic.Field(
            alias="loreHash",
            description="Talent nodes can be associated with a piece of Lore, generally rendered in a tooltip. This is the hash identifier of the lore element to show, if there is one to be show.",
        ),
    ] = None
    """
    Talent nodes can be associated with a piece of Lore, generally rendered in a tooltip. This is the hash identifier of the lore element to show, if there is one to be show.
    """

    node_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nodeHash"),
        pydantic.Field(
            alias="nodeHash",
            description="The hash identifier for the node, which unfortunately is also content version dependent but can be (and ideally, should be) used instead of the nodeIndex to uniquely identify the node.\r\nThe two exist side-by-side for backcompat reasons due to the Great Talent Node Restructuring of Destiny 1, and I ran out of time to remove one of them and standardize on the other. Sorry!",
        ),
    ] = None
    """
    The hash identifier for the node, which unfortunately is also content version dependent but can be (and ideally, should be) used instead of the nodeIndex to uniquely identify the node.
    The two exist side-by-side for backcompat reasons due to the Great Talent Node Restructuring of Destiny 1, and I ran out of time to remove one of them and standardize on the other. Sorry!
    """

    node_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nodeIndex"),
        pydantic.Field(
            alias="nodeIndex",
            description='The index into the DestinyTalentGridDefinition\'s "nodes" property where this node is located. Used to uniquely identify the node within the Talent Grid. Note that this is content version dependent: make sure you have the latest version of content before trying to use these properties.',
        ),
    ] = None
    """
    The index into the DestinyTalentGridDefinition's "nodes" property where this node is located. Used to uniquely identify the node within the Talent Grid. Note that this is content version dependent: make sure you have the latest version of content before trying to use these properties.
    """

    node_style_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nodeStyleIdentifier"),
        pydantic.Field(
            alias="nodeStyleIdentifier",
            description="Comes from the talent grid node style: this identifier should be used to determine how to render the node in the UI.",
        ),
    ] = None
    """
    Comes from the talent grid node style: this identifier should be used to determine how to render the node in the UI.
    """

    prerequisite_node_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="prerequisiteNodeIndexes"),
        pydantic.Field(
            alias="prerequisiteNodeIndexes",
            description="Indexes into the DestinyTalentGridDefinition.nodes property for any nodes that must be activated before this one is allowed to be activated.\r\nI would have liked to change this to hashes for Destiny 2, but we have run out of time.",
        ),
    ] = None
    """
    Indexes into the DestinyTalentGridDefinition.nodes property for any nodes that must be activated before this one is allowed to be activated.
    I would have liked to change this to hashes for Destiny 2, but we have run out of time.
    """

    random_activation_requirement: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyNodeActivationRequirement],
        FieldMetadata(alias="randomActivationRequirement"),
        pydantic.Field(
            alias="randomActivationRequirement",
            description='At one point, you were going to be able to repurchase talent nodes that had random steps, to "re-roll" the current step of the node (and thus change the properties of your item). This was to be the activation requirement for performing that re-roll.\r\nThe system still exists to do this, as far as I know, so it may yet come back around!',
        ),
    ] = None
    """
    At one point, you were going to be able to repurchase talent nodes that had random steps, to "re-roll" the current step of the node (and thus change the properties of your item). This was to be the activation requirement for performing that re-roll.
    The system still exists to do this, as far as I know, so it may yet come back around!
    """

    random_start_progression_bar_at_progression: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="randomStartProgressionBarAtProgression"),
        pydantic.Field(
            alias="randomStartProgressionBarAtProgression",
            description="If the node's step is randomly selected, this is the amount of the Talent Grid's progression experience at which the progression bar for the node should be shown.",
        ),
    ] = None
    """
    If the node's step is randomly selected, this is the amount of the Talent Grid's progression experience at which the progression bar for the node should be shown.
    """

    row: typing.Optional[int] = pydantic.Field(default=None)
    """
    The visual "row" where the node should be shown in the UI. If negative, then the node is hidden.
    """

    steps: typing.Optional[typing.List[DestinyDefinitionsDestinyNodeStepDefinition]] = pydantic.Field(default=None)
    """
    At this point, "steps" have been obfuscated into conceptual entities, aggregating the underlying notions of "properties" and "true steps".
    If you need to know a step as it truly exists - such as when recreating Node logic when processing Vendor data - you'll have to use the "realSteps" property below.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
