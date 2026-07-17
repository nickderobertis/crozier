

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyDefinitionsDestinyItemValueBlockDefinition(UniversalBaseModel):
    """
    This defines an item's "Value". Unfortunately, this appears to be used in different ways depending on the way that the item itself is used.
    For items being sold at a Vendor, this is the default "sale price" of the item. These days, the vendor itself almost always sets the price, but it still possible for the price to fall back to this value. For quests, it is a preview of rewards you can gain by completing the quest. For dummy items, if the itemValue refers to an Emblem, it is the emblem that should be shown as the reward. (jeez louise)
    It will likely be used in a number of other ways in the future, it appears to be a bucket where they put arbitrary items and quantities into the item.
    """

    item_value: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyItemQuantity]],
        FieldMetadata(alias="itemValue"),
        pydantic.Field(
            alias="itemValue",
            description='References to the items that make up this item\'s "value", and the quantity.',
        ),
    ] = None
    """
    References to the items that make up this item's "value", and the quantity.
    """

    value_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="valueDescription"),
        pydantic.Field(
            alias="valueDescription",
            description="If there's a localized text description of the value provided, this will be said description.",
        ),
    ] = None
    """
    If there's a localized text description of the value provided, this will be said description.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
