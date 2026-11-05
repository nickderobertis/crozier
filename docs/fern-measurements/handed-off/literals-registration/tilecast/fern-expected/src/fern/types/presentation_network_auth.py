

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PresentationNetworkAuth(UniversalBaseModel):
    identity: typing.Optional[str] = None
    anonymous_identity: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="anonymousIdentity"), pydantic.Field(alias="anonymousIdentity")
    ] = None
    ca_certificate_pem: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caCertificatePem"),
        pydantic.Field(
            alias="caCertificatePem", description="Public CA certificate chain for Enterprise server validation."
        ),
    ] = None
    """
    Public CA certificate chain for Enterprise server validation.
    """

    domain_suffix_match: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="domainSuffixMatch"),
        pydantic.Field(
            alias="domainSuffixMatch", description="Expected RADIUS server domain; requires caCertificatePem."
        ),
    ] = None
    """
    Expected RADIUS server domain; requires caCertificatePem.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
