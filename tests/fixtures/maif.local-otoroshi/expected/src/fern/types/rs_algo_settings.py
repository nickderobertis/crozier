

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RsAlgoSettings(UniversalBaseModel):
    """
    Settings for an HMAC + SHA signing algorithm
    """

    private_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="privateKey"),
        pydantic.Field(alias="privateKey", description="The private key for the RSA function"),
    ] = None
    """
    The private key for the RSA function
    """

    public_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="The public key for the RSA function"),
    ]
    """
    The public key for the RSA function
    """

    size: int = pydantic.Field()
    """
    Size for SHA function. can be 256, 384 or 512
    """

    type: str = pydantic.Field()
    """
    String with value RSAlgoSettings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
