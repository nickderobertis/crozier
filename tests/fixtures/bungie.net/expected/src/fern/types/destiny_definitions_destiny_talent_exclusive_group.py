

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyTalentExclusiveGroup(UniversalBaseModel):
    """
    As of Destiny 2, nodes can exist as part of "Exclusive Groups". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause "opposing" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.
    """

    group_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="groupHash"),
        pydantic.Field(
            alias="groupHash",
            description="The identifier for this exclusive group. Only guaranteed unique within the talent grid, not globally.",
        ),
    ] = None
    """
    The identifier for this exclusive group. Only guaranteed unique within the talent grid, not globally.
    """

    lore_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="loreHash"),
        pydantic.Field(
            alias="loreHash",
            description="If this group has an associated piece of lore to show next to it, this will be the identifier for that DestinyLoreDefinition.",
        ),
    ] = None
    """
    If this group has an associated piece of lore to show next to it, this will be the identifier for that DestinyLoreDefinition.
    """

    node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="nodeHashes"),
        pydantic.Field(
            alias="nodeHashes",
            description="A quick reference of the talent nodes that are part of this group, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)",
        ),
    ] = None
    """
    A quick reference of the talent nodes that are part of this group, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)
    """

    opposing_group_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="opposingGroupHashes"),
        pydantic.Field(
            alias="opposingGroupHashes",
            description="A quick reference of Groups whose nodes will be deactivated if any node in this group is activated.",
        ),
    ] = None
    """
    A quick reference of Groups whose nodes will be deactivated if any node in this group is activated.
    """

    opposing_node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="opposingNodeHashes"),
        pydantic.Field(
            alias="opposingNodeHashes",
            description="A quick reference of Nodes that will be deactivated if any node in this group is activated, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)",
        ),
    ] = None
    """
    A quick reference of Nodes that will be deactivated if any node in this group is activated, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
