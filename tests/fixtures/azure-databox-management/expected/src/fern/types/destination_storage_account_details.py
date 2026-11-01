

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .destination_account_details import DestinationAccountDetails


class DestinationStorageAccountDetails(DestinationAccountDetails):
    """
    Details for the destination storage account.
    """

    storage_account_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="storageAccountId"),
        pydantic.Field(alias="storageAccountId", description="Destination Storage Account Arm Id."),
    ]
    """
    Destination Storage Account Arm Id.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
