

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyVendorAcceptedItemDefinition(UniversalBaseModel):
    """
    If you ever wondered how the Vault works, here it is.
    The Vault is merely a set of inventory buckets that exist on your Profile/Account level. When you transfer items in the Vault, the game is using the Vault Vendor's DestinyVendorAcceptedItemDefinitions to see where the appropriate destination bucket is for the source bucket from whence your item is moving. If it finds such an entry, it transfers the item to the other bucket.
    The mechanics for Postmaster works similarly, which is also a vendor. All driven by Accepted Items.
    """

    accepted_inventory_bucket_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="acceptedInventoryBucketHash")
    ] = pydantic.Field(default=None)
    """
    The "source" bucket for a transfer. When a user wants to transfer an item, the appropriate DestinyVendorDefinition's acceptedItems property is evaluated, looking for an entry where acceptedInventoryBucketHash matches the bucket that the item being transferred is currently located. If it exists, the item will be transferred into whatever bucket is defined by destinationInventoryBucketHash.
    """

    destination_inventory_bucket_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="destinationInventoryBucketHash")
    ] = pydantic.Field(default=None)
    """
    This is the bucket where the item being transferred will be put, given that it was being transferred *from* the bucket defined in acceptedInventoryBucketHash.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
