

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WebAuthnCredentialResponse(UniversalBaseModel):
    client_data_json: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientDataJSON"), pydantic.Field(alias="clientDataJSON", description="base64url")
    ]
    """
    base64url
    """

    attestation_object: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="attestationObject"),
        pydantic.Field(alias="attestationObject", description="base64url"),
    ]
    """
    base64url
    """

    transports: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
