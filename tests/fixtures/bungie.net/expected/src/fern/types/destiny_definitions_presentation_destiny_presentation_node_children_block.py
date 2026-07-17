

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_presentation_destiny_presentation_node_child_entry import (
    DestinyDefinitionsPresentationDestinyPresentationNodeChildEntry,
)
from .destiny_definitions_presentation_destiny_presentation_node_collectible_child_entry import (
    DestinyDefinitionsPresentationDestinyPresentationNodeCollectibleChildEntry,
)
from .destiny_definitions_presentation_destiny_presentation_node_craftable_child_entry import (
    DestinyDefinitionsPresentationDestinyPresentationNodeCraftableChildEntry,
)
from .destiny_definitions_presentation_destiny_presentation_node_metric_child_entry import (
    DestinyDefinitionsPresentationDestinyPresentationNodeMetricChildEntry,
)
from .destiny_definitions_presentation_destiny_presentation_node_record_child_entry import (
    DestinyDefinitionsPresentationDestinyPresentationNodeRecordChildEntry,
)


class DestinyDefinitionsPresentationDestinyPresentationNodeChildrenBlock(UniversalBaseModel):
    """
    As/if presentation nodes begin to host more entities as children, these lists will be added to. One list property exists per type of entity that can be treated as a child of this presentation node, and each holds the identifier of the entity and any associated information needed to display the UI for that entity (if anything)
    """

    collectibles: typing.Optional[
        typing.List[DestinyDefinitionsPresentationDestinyPresentationNodeCollectibleChildEntry]
    ] = None
    craftables: typing.Optional[
        typing.List[DestinyDefinitionsPresentationDestinyPresentationNodeCraftableChildEntry]
    ] = None
    metrics: typing.Optional[typing.List[DestinyDefinitionsPresentationDestinyPresentationNodeMetricChildEntry]] = None
    presentation_nodes: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsPresentationDestinyPresentationNodeChildEntry]],
        FieldMetadata(alias="presentationNodes"),
        pydantic.Field(alias="presentationNodes"),
    ] = None
    records: typing.Optional[typing.List[DestinyDefinitionsPresentationDestinyPresentationNodeRecordChildEntry]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
