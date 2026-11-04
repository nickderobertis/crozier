

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BuildSecrets(UniversalBaseModel):
    """
    Secrets used to sign/verify launcher builds.
    """

    private_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="privateKey"),
        pydantic.Field(alias="privateKey", description="Base64-encoded private key."),
    ]
    """
    Base64-encoded private key.
    """

    public_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="Base64-encoded public key."),
    ]
    """
    Base64-encoded public key.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
