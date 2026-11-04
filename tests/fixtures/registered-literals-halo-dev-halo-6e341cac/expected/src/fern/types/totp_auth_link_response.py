

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TotpAuthLinkResponse(UniversalBaseModel):
    """
    TOTP provisioning data for configuring an authenticator app.
    """

    auth_link: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="authLink"),
        pydantic.Field(alias="authLink", description="otpauth URI that can be encoded as a QR code."),
    ]
    """
    otpauth URI that can be encoded as a QR code.
    """

    raw_secret: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="rawSecret"),
        pydantic.Field(alias="rawSecret", description="Raw TOTP secret for manual authenticator setup."),
    ]
    """
    Raw TOTP secret for manual authenticator setup.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
