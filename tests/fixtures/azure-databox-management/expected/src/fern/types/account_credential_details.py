

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_credential_details_data_destination_type import AccountCredentialDetailsDataDestinationType
from .share_credential_details import ShareCredentialDetails


class AccountCredentialDetails(UniversalBaseModel):
    """
    Credential details of the account.
    """

    account_connection_string: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountConnectionString"),
        pydantic.Field(
            alias="accountConnectionString",
            description="Connection string of the account endpoint to use the account as a storage endpoint on the device.",
        ),
    ] = None
    """
    Connection string of the account endpoint to use the account as a storage endpoint on the device.
    """

    account_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountName"),
        pydantic.Field(alias="accountName", description="Name of the account."),
    ] = None
    """
    Name of the account.
    """

    data_destination_type: typing_extensions.Annotated[
        typing.Optional[AccountCredentialDetailsDataDestinationType],
        FieldMetadata(alias="dataDestinationType"),
        pydantic.Field(alias="dataDestinationType", description="Data Destination Type."),
    ] = None
    """
    Data Destination Type.
    """

    share_credential_details: typing_extensions.Annotated[
        typing.Optional[typing.List[ShareCredentialDetails]],
        FieldMetadata(alias="shareCredentialDetails"),
        pydantic.Field(alias="shareCredentialDetails", description="Per share level unencrypted access credentials."),
    ] = None
    """
    Per share level unencrypted access credentials.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
