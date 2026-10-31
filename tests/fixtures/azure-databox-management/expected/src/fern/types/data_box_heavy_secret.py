

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_credential_details import AccountCredentialDetails
from .appliance_network_configuration import ApplianceNetworkConfiguration


class DataBoxHeavySecret(UniversalBaseModel):
    """
    The secrets related to a databox heavy.
    """

    account_credential_details: typing_extensions.Annotated[
        typing.Optional[typing.List[AccountCredentialDetails]],
        FieldMetadata(alias="accountCredentialDetails"),
        pydantic.Field(alias="accountCredentialDetails", description="Per account level access credentials."),
    ] = None
    """
    Per account level access credentials.
    """

    device_password: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="devicePassword"),
        pydantic.Field(alias="devicePassword", description="Password for out of the box experience on device."),
    ] = None
    """
    Password for out of the box experience on device.
    """

    device_serial_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deviceSerialNumber"),
        pydantic.Field(alias="deviceSerialNumber", description="Serial number of the assigned device."),
    ] = None
    """
    Serial number of the assigned device.
    """

    encoded_validation_cert_pub_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="encodedValidationCertPubKey"),
        pydantic.Field(
            alias="encodedValidationCertPubKey",
            description="The base 64 encoded public key to authenticate with the device",
        ),
    ] = None
    """
    The base 64 encoded public key to authenticate with the device
    """

    network_configurations: typing_extensions.Annotated[
        typing.Optional[typing.List[ApplianceNetworkConfiguration]],
        FieldMetadata(alias="networkConfigurations"),
        pydantic.Field(alias="networkConfigurations", description="Network configuration of the appliance."),
    ] = None
    """
    Network configuration of the appliance.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
