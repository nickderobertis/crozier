

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemActionRequiredItemDefinition(UniversalBaseModel):
    """
    The definition of an item and quantity required in a character's inventory in order to perform an action.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The minimum quantity of the item you have to have.
    """

    delete_on_action: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="deleteOnAction")] = (
        pydantic.Field(default=None)
    )
    """
    If true, the item/quantity will be deleted from your inventory when the action is performed. Otherwise, you'll retain these required items after the action is complete.
    """

    item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemHash")] = pydantic.Field(
        default=None
    )
    """
    The hash identifier of the item you need to have. Use it to look up the DestinyInventoryItemDefinition for more info.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
