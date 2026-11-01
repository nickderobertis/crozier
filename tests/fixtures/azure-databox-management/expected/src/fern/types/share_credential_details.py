

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .share_credential_details_share_type import ShareCredentialDetailsShareType
from .share_credential_details_supported_access_protocols_item import ShareCredentialDetailsSupportedAccessProtocolsItem


class ShareCredentialDetails(UniversalBaseModel):
    """
    Credential details of the shares in account.
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Password for the share.
    """

    share_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shareName"),
        pydantic.Field(alias="shareName", description="Name of the share."),
    ] = None
    """
    Name of the share.
    """

    share_type: typing_extensions.Annotated[
        typing.Optional[ShareCredentialDetailsShareType],
        FieldMetadata(alias="shareType"),
        pydantic.Field(alias="shareType", description="Type of the share."),
    ] = None
    """
    Type of the share.
    """

    supported_access_protocols: typing_extensions.Annotated[
        typing.Optional[typing.List[ShareCredentialDetailsSupportedAccessProtocolsItem]],
        FieldMetadata(alias="supportedAccessProtocols"),
        pydantic.Field(alias="supportedAccessProtocols", description="Access protocols supported on the device."),
    ] = None
    """
    Access protocols supported on the device.
    """

    user_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userName"),
        pydantic.Field(alias="userName", description="User name for the share."),
    ] = None
    """
    User name for the share.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
