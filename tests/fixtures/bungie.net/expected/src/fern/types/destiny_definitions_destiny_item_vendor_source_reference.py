

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemVendorSourceReference(UniversalBaseModel):
    """
    Represents that a vendor could sell this item, and provides a quick link to that vendor and sale item.
     Note that we do not and cannot make a guarantee that the vendor will ever *actually* sell this item, only that the Vendor has a definition that indicates it *could* be sold.
     Note also that a vendor may sell the same item in multiple "ways", which means there may be multiple vendorItemIndexes for a single Vendor hash.
    """

    vendor_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vendorHash")] = pydantic.Field(
        default=None
    )
    """
    The identifier for the vendor that may sell this item.
    """

    vendor_item_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="vendorItemIndexes")
    ] = pydantic.Field(default=None)
    """
    The Vendor sale item indexes that represent the sale information for this item. The same vendor may sell an item in multiple "ways", hence why this is a list. (for instance, a weapon may be "sold" as a reward in a quest, for Glimmer, and for Masterwork Cores: each of those ways would be represented by a different vendor sale item with a different index)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
