

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_item_set_block_entry_definition import (
    DestinyDefinitionsDestinyItemSetBlockEntryDefinition,
)


class DestinyDefinitionsDestinyItemSetBlockDefinition(UniversalBaseModel):
    """
    Primarily for Quests, this is the definition of properties related to the item if it is a quest and its various quest steps.
    """

    item_list: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemSetBlockEntryDefinition]],
        FieldMetadata(alias="itemList"),
    ] = pydantic.Field(default=None)
    """
    A collection of hashes of set items, for items such as Quest Metadata items that possess this data.
    """

    quest_line_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="questLineDescription")
    ] = pydantic.Field(default=None)
    """
    The description of the quest line that this quest step is a part of.
    """

    quest_line_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="questLineName")] = (
        pydantic.Field(default=None)
    )
    """
    The name of the quest line that this quest step is a part of.
    """

    quest_step_summary: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="questStepSummary")] = (
        pydantic.Field(default=None)
    )
    """
    An additional summary of this step in the quest line.
    """

    require_ordered_set_item_add: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requireOrderedSetItemAdd")
    ] = pydantic.Field(default=None)
    """
    If true, items in the set can only be added in increasing order, and adding an item will remove any previous item. For Quests, this is by necessity true. Only one quest step is present at a time, and previous steps are removed as you advance in the quest.
    """

    set_is_featured: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="setIsFeatured")] = (
        pydantic.Field(default=None)
    )
    """
    If true, the UI should treat this quest as "featured"
    """

    set_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="setType")] = pydantic.Field(
        default=None
    )
    """
    A string identifier we can use to attempt to identify the category of the Quest.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
