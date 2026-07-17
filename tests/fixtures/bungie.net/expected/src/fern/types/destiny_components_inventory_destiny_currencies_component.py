

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyComponentsInventoryDestinyCurrenciesComponent(UniversalBaseModel):
    """
    This component provides a quick lookup of every item the requested character has and how much of that item they have.
    Requesting this component will allow you to circumvent manually putting together the list of which currencies you have for the purpose of testing currency requirements on an item being purchased, or operations that have costs.
    You *could* figure this out yourself by doing a GetCharacter or GetProfile request and forming your own lookup table, but that is inconvenient enough that this feels like a worthwhile (and optional) redundency. Don't bother requesting it if you have already created your own lookup from prior GetCharacter/GetProfile calls.
    """

    item_quantities: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="itemQuantities"),
        pydantic.Field(
            alias="itemQuantities",
            description="A dictionary - keyed by the item's hash identifier (DestinyInventoryItemDefinition), and whose value is the amount of that item you have across all available inventory buckets for purchasing.\r\nThis allows you to see whether the requesting character can afford any given purchase/action without having to re-create this list itself.",
        ),
    ] = None
    """
    A dictionary - keyed by the item's hash identifier (DestinyInventoryItemDefinition), and whose value is the amount of that item you have across all available inventory buckets for purchasing.
    This allows you to see whether the requesting character can afford any given purchase/action without having to re-create this list itself.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
