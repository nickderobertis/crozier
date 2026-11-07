

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .trusted_key_response_dto_audience import TrustedKeyResponseDtoAudience


class TrustedKeyResponseDto(UniversalBaseModel):
    key_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="keyId"), pydantic.Field(alias="keyId", description="Unique key identifier")
    ]
    """
    Unique key identifier
    """

    jwk: typing.Dict[str, typing.Dict[str, typing.Any]] = pydantic.Field()
    """
    The registered public key in JWK format (RFC 7517). Contains only public key components. 
    """

    audience: TrustedKeyResponseDtoAudience
    valid_from: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="validFrom"),
        pydantic.Field(alias="validFrom", description="When this key became valid"),
    ]
    """
    When this key became valid
    """

    legal_entity_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="legalEntityId"),
        pydantic.Field(alias="legalEntityId", description="The tenant this key is bound to"),
    ]
    """
    The tenant this key is bound to
    """

    issuers: typing.Optional[typing.List[str]] = None
    valid_to: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="validTo"),
        pydantic.Field(alias="validTo", description="When this key expires"),
    ] = None
    """
    When this key expires
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
