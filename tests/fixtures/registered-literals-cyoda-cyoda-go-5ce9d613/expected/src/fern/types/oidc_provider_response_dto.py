

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OidcProviderResponseDto(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    ID for this OIDC provider entity
    """

    well_known_config_uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="wellKnownConfigUri"),
        pydantic.Field(
            alias="wellKnownConfigUri", description="URI to the OIDC provider's well-known configuration endpoint"
        ),
    ]
    """
    URI to the OIDC provider's well-known configuration endpoint
    """

    active: bool = pydantic.Field()
    """
    Whether this OIDC provider is currently active and used for JWT validation
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When this OIDC provider was registered"),
    ]
    """
    When this OIDC provider was registered
    """

    issuers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of allowed issuer URIs from this OIDC provider. When present and non-empty, JWT validation requires the 'iss' claim to match one of these values. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
