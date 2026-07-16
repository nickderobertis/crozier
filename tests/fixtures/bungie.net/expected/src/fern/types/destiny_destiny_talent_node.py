

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_material_requirement import DestinyDefinitionsDestinyMaterialRequirement
from .destiny_destiny_talent_node_stat_block import DestinyDestinyTalentNodeStatBlock


class DestinyDestinyTalentNode(UniversalBaseModel):
    """
    I see you've come to find out more about Talent Nodes. I'm so sorry. Talent Nodes are the conceptual, visual nodes that appear on Talent Grids. Talent Grids, in Destiny 1, were found on almost every instanced item: they had Nodes that could be activated to change the properties of the item. In Destiny 2, Talent Grids only exist for Builds/Subclasses, and while the basic concept is the same (Nodes can be activated once you've gained sufficient Experience on the Item, and provide effects), there are some new concepts from Destiny 1. Examine DestinyTalentGridDefinition and its subordinates for more information. This is the "Live" information for the current status of a Talent Node on a specific item. Talent Nodes have many Steps, but only one can be active at any one time: and it is the Step that determines both the visual and the game state-changing properties that the Node provides. Examine this and DestinyTalentNodeStepDefinition carefully. *IMPORTANT NOTE* Talent Nodes are, unfortunately, Content Version DEPENDENT. Though they refer to hashes for Nodes and Steps, those hashes are not guaranteed to be immutable across content versions. This is a source of great exasperation for me, but as a result anyone using Talent Grid data must ensure that the content version of their static content matches that of the server responses before showing or making decisions based on talent grid data.
    """

    activation_grid_level: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activationGridLevel"),
        pydantic.Field(
            alias="activationGridLevel",
            description="The progression level required on the Talent Grid in order to be able to activate this talent node. Talent Grids have their own Progression - similar to Character Level, but in this case it is experience related to the item itself.",
        ),
    ] = None
    """
    The progression level required on the Talent Grid in order to be able to activate this talent node. Talent Grids have their own Progression - similar to Character Level, but in this case it is experience related to the item itself.
    """

    hidden: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the talent node is actually visible in the game's UI. Whether you want to show it in your own UI is up to you! I'm not gonna tell you who to sock it to.
    """

    is_activated: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isActivated"),
        pydantic.Field(
            alias="isActivated",
            description="If true, the node is activated: it's current step then provides its benefits.",
        ),
    ] = None
    """
    If true, the node is activated: it's current step then provides its benefits.
    """

    materials_to_upgrade: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyMaterialRequirement]],
        FieldMetadata(alias="materialsToUpgrade"),
        pydantic.Field(
            alias="materialsToUpgrade",
            description="If the node has material requirements to be activated, this is the list of those requirements.",
        ),
    ] = None
    """
    If the node has material requirements to be activated, this is the list of those requirements.
    """

    node_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nodeHash"),
        pydantic.Field(
            alias="nodeHash",
            description="The hash of the Talent Node being referred to (in DestinyTalentGridDefinition.nodes). Deceptively CONTENT VERSION DEPENDENT. We have no guarantee of the hash's immutability between content versions.",
        ),
    ] = None
    """
    The hash of the Talent Node being referred to (in DestinyTalentGridDefinition.nodes). Deceptively CONTENT VERSION DEPENDENT. We have no guarantee of the hash's immutability between content versions.
    """

    node_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nodeIndex"),
        pydantic.Field(
            alias="nodeIndex",
            description="The index of the Talent Node being referred to (an index into DestinyTalentGridDefinition.nodes[]). CONTENT VERSION DEPENDENT.",
        ),
    ] = None
    """
    The index of the Talent Node being referred to (an index into DestinyTalentGridDefinition.nodes[]). CONTENT VERSION DEPENDENT.
    """

    node_stats_block: typing_extensions.Annotated[
        typing.Optional[DestinyDestinyTalentNodeStatBlock],
        FieldMetadata(alias="nodeStatsBlock"),
        pydantic.Field(
            alias="nodeStatsBlock",
            description="This property has some history. A talent grid can provide stats on both the item it's related to and the character equipping the item. This returns data about those stat bonuses.",
        ),
    ] = None
    """
    This property has some history. A talent grid can provide stats on both the item it's related to and the character equipping the item. This returns data about those stat bonuses.
    """

    progress_percent: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="progressPercent"),
        pydantic.Field(
            alias="progressPercent",
            description="If you want to show a progress bar or circle for how close this talent node is to being activate-able, this is the percentage to show. It follows the node's underlying rules about when the progress bar should first show up, and when it should be filled.",
        ),
    ] = None
    """
    If you want to show a progress bar or circle for how close this talent node is to being activate-able, this is the percentage to show. It follows the node's underlying rules about when the progress bar should first show up, and when it should be filled.
    """

    state: typing.Optional[int] = pydantic.Field(default=None)
    """
    An DestinyTalentNodeState enum value indicating the node's state: whether it can be activated or swapped, and why not if neither can be performed.
    """

    step_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="stepIndex"),
        pydantic.Field(
            alias="stepIndex",
            description="The currently relevant Step for the node. It is this step that has rendering data for the node and the benefits that are provided if the node is activated. (the actual rules for benefits provided are extremely complicated in theory, but with how Talent Grids are being used in Destiny 2 you don't have to worry about a lot of those old Destiny 1 rules.) This is an index into: DestinyTalentGridDefinition.nodes[nodeIndex].steps[stepIndex]",
        ),
    ] = None
    """
    The currently relevant Step for the node. It is this step that has rendering data for the node and the benefits that are provided if the node is activated. (the actual rules for benefits provided are extremely complicated in theory, but with how Talent Grids are being used in Destiny 2 you don't have to worry about a lot of those old Destiny 1 rules.) This is an index into: DestinyTalentGridDefinition.nodes[nodeIndex].steps[stepIndex]
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
