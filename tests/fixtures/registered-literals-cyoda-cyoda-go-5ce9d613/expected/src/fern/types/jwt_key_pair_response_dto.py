

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .jwt_key_pair_response_dto_algorithm import JwtKeyPairResponseDtoAlgorithm


class JwtKeyPairResponseDto(UniversalBaseModel):
    key_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="keyId"),
        pydantic.Field(
            alias="keyId",
            description="Unique identifier for this key-pair (UUID). Included in JWT header as 'kid' claim.",
        ),
    ]
    """
    Unique identifier for this key-pair (UUID). Included in JWT header as 'kid' claim.
    """

    algorithm: JwtKeyPairResponseDtoAlgorithm
    public_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="publicKey"),
        pydantic.Field(
            alias="publicKey", description="Base64-encoded public key in X.509 SubjectPublicKeyInfo format."
        ),
    ]
    """
    Base64-encoded public key in X.509 SubjectPublicKeyInfo format.
    """

    valid_from: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="validFrom"),
        pydantic.Field(alias="validFrom", description="When this key-pair becomes valid"),
    ]
    """
    When this key-pair becomes valid
    """

    valid_to: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="validTo"),
        pydantic.Field(alias="validTo", description="When this key-pair expires"),
    ] = None
    """
    When this key-pair expires
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
