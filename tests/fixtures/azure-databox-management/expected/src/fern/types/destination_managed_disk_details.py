

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .destination_account_details import DestinationAccountDetails


class DestinationManagedDiskDetails(DestinationAccountDetails):
    """
    Details for the destination compute disks.
    """

    resource_group_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="resourceGroupId"),
        pydantic.Field(
            alias="resourceGroupId",
            description="Destination Resource Group Id where the Compute disks should be created.",
        ),
    ]
    """
    Destination Resource Group Id where the Compute disks should be created.
    """

    staging_storage_account_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="stagingStorageAccountId"),
        pydantic.Field(
            alias="stagingStorageAccountId",
            description="Arm Id of the storage account that can be used to copy the vhd for staging.",
        ),
    ]
    """
    Arm Id of the storage account that can be used to copy the vhd for staging.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
