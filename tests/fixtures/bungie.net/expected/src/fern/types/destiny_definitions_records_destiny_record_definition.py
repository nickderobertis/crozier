

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_presentation_destiny_presentation_child_block import (
    DestinyDefinitionsPresentationDestinyPresentationChildBlock,
)
from .destiny_definitions_presentation_destiny_presentation_node_requirements_block import (
    DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock,
)
from .destiny_definitions_records_destiny_record_completion_block import (
    DestinyDefinitionsRecordsDestinyRecordCompletionBlock,
)
from .destiny_definitions_records_destiny_record_expiration_block import (
    DestinyDefinitionsRecordsDestinyRecordExpirationBlock,
)
from .destiny_definitions_records_destiny_record_interval_block import (
    DestinyDefinitionsRecordsDestinyRecordIntervalBlock,
)
from .destiny_definitions_records_destiny_record_title_block import DestinyDefinitionsRecordsDestinyRecordTitleBlock
from .destiny_definitions_records_schema_record_state_block import DestinyDefinitionsRecordsSchemaRecordStateBlock
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyDefinitionsRecordsDestinyRecordDefinition(UniversalBaseModel):
    completion_info: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsRecordsDestinyRecordCompletionBlock], FieldMetadata(alias="completionInfo")
    ] = None
    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = None
    expiration_info: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsRecordsDestinyRecordExpirationBlock], FieldMetadata(alias="expirationInfo")
    ] = None
    for_title_gilding: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="forTitleGilding")] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    interval_info: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsRecordsDestinyRecordIntervalBlock], FieldMetadata(alias="intervalInfo")
    ] = pydantic.Field(default=None)
    """
    Some records have multiple 'interval' objectives, and the record may be claimed at each completed interval
    """

    lore_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="loreHash")] = None
    objective_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="objectiveHashes")
    ] = None
    parent_node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="parentNodeHashes")
    ] = pydantic.Field(default=None)
    """
    A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
    """

    presentation_info: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsPresentationDestinyPresentationChildBlock],
        FieldMetadata(alias="presentationInfo"),
    ] = None
    presentation_node_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="presentationNodeType")
    ] = None
    record_value_style: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="recordValueStyle")] = (
        None
    )
    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    requirements: typing.Optional[DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock] = None
    reward_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyItemQuantity]], FieldMetadata(alias="rewardItems")
    ] = pydantic.Field(default=None)
    """
    If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.
     However, note that some records intentionally have "hidden" rewards. These will not be returned in this list.
    """

    scope: typing.Optional[int] = pydantic.Field(default=None)
    """
    Indicates whether this Record's state is determined on a per-character or on an account-wide basis.
    """

    should_show_large_icons: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="shouldShowLargeIcons")
    ] = pydantic.Field(default=None)
    """
    A hint to show a large icon for a reward
    """

    state_info: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsRecordsSchemaRecordStateBlock], FieldMetadata(alias="stateInfo")
    ] = None
    title_info: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsRecordsDestinyRecordTitleBlock], FieldMetadata(alias="titleInfo")
    ] = None
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
