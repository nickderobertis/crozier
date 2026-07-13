

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_presentation_destiny_presentation_node_children_block import (
    DestinyDefinitionsPresentationDestinyPresentationNodeChildrenBlock,
)
from .destiny_definitions_presentation_destiny_presentation_node_requirements_block import (
    DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock,
)


class DestinyDefinitionsPresentationDestinyPresentationNodeDefinition(UniversalBaseModel):
    """
    A PresentationNode is an entity that represents a logical grouping of other entities visually/organizationally.
    For now, Presentation Nodes may contain the following... but it may be used for more in the future:
    - Collectibles - Records (Or, as the public will call them, "Triumphs." Don't ask me why we're overloading the term "Triumph", it still hurts me to think about it) - Metrics (aka Stat Trackers) - Other Presentation Nodes, allowing a tree of Presentation Nodes to be created
    Part of me wants to break these into conceptual definitions per entity being collected, but the possibility of these different types being mixed in the same UI and the possibility that it could actually be more useful to return the "bare metal" presentation node concept has resulted in me deciding against that for the time being.
    We'll see if I come to regret this as well.
    """

    children: typing.Optional[DestinyDefinitionsPresentationDestinyPresentationNodeChildrenBlock] = pydantic.Field(
        default=None
    )
    """
    The child entities contained by this presentation node.
    """

    completion_record_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="completionRecordHash")
    ] = pydantic.Field(default=None)
    """
    If this presentation node has an associated "Record" that you can accomplish for completing its children, this is the identifier of that Record.
    """

    disable_child_subscreen_navigation: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="disableChildSubscreenNavigation")
    ] = pydantic.Field(default=None)
    """
    If this presentation node has children, but the game doesn't let you inspect the details of those children, that is indicated here.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = None
    display_style: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="displayStyle")] = (
        pydantic.Field(default=None)
    )
    """
    A hint for how to display this presentation node when it's shown in a list.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    max_category_record_score: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxCategoryRecordScore")
    ] = None
    node_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="nodeType")] = None
    objective_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="objectiveHash")] = (
        pydantic.Field(default=None)
    )
    """
    If this presentation node shows a related objective (for instance, if it tracks the progress of its children), the objective being tracked is indicated here.
    """

    original_icon: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="originalIcon")] = (
        pydantic.Field(default=None)
    )
    """
    The original icon for this presentation node, before we futzed with it.
    """

    parent_node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="parentNodeHashes")
    ] = pydantic.Field(default=None)
    """
    A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
    """

    presentation_node_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="presentationNodeType")
    ] = None
    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    requirements: typing.Optional[DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock] = (
        pydantic.Field(default=None)
    )
    """
    The requirements for being able to interact with this presentation node and its children.
    """

    root_view_icon: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="rootViewIcon")] = (
        pydantic.Field(default=None)
    )
    """
    Some presentation nodes are meant to be explicitly shown on the "root" or "entry" screens for the feature to which they are related. You should use this icon when showing them on such a view, if you have a similar "entry point" view in your UI. If you don't have a UI, then I guess it doesn't matter either way does it?
    """

    scope: typing.Optional[int] = pydantic.Field(default=None)
    """
    Indicates whether this presentation node's state is determined on a per-character or on an account-wide basis.
    """

    screen_style: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="screenStyle")] = (
        pydantic.Field(default=None)
    )
    """
    A hint for how to display this presentation node when it's shown in its own detail screen.
    """

    trait_hashes: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="traitHashes")] = (
        None
    )
    trait_ids: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="traitIds")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
