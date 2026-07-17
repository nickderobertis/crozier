

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_entities_items_destiny_item_component import DestinyEntitiesItemsDestinyItemComponent
from .destiny_responses_destiny_item_response import DestinyResponsesDestinyItemResponse


class DestinyResponsesDestinyItemChangeResponse(UniversalBaseModel):
    added_inventory_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyEntitiesItemsDestinyItemComponent]],
        FieldMetadata(alias="addedInventoryItems"),
        pydantic.Field(
            alias="addedInventoryItems",
            description="Items that appeared in the inventory possibly as a result of an action.",
        ),
    ] = None
    """
    Items that appeared in the inventory possibly as a result of an action.
    """

    item: typing.Optional[DestinyResponsesDestinyItemResponse] = None
    removed_inventory_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyEntitiesItemsDestinyItemComponent]],
        FieldMetadata(alias="removedInventoryItems"),
        pydantic.Field(
            alias="removedInventoryItems",
            description="Items that disappeared from the inventory possibly as a result of an action.",
        ),
    ] = None
    """
    Items that disappeared from the inventory possibly as a result of an action.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
