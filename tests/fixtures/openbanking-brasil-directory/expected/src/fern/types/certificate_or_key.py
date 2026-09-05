

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .organisation_id import OrganisationId
from .software_statement_id import SoftwareStatementId


class CertificateOrKey(UniversalBaseModel):
    client_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ClientName"), pydantic.Field(alias="ClientName")
    ] = None
    expiry_date_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ExpiryDateTime"), pydantic.Field(alias="ExpiryDateTime")
    ] = None
    jwk_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="JwkPath"),
        pydantic.Field(alias="JwkPath", description="Used to display path to JWKS containing this certificate"),
    ] = None
    """
    Used to display path to JWKS containing this certificate
    """

    org_jwk_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrgJwkPath"),
        pydantic.Field(alias="OrgJwkPath", description="Used to display path to Org JWKS containing org certificates"),
    ] = None
    """
    Used to display path to Org JWKS containing org certificates
    """

    organisation_id: typing_extensions.Annotated[
        typing.Optional[OrganisationId], FieldMetadata(alias="OrganisationId"), pydantic.Field(alias="OrganisationId")
    ] = None
    signed_cert_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SignedCertPath"),
        pydantic.Field(
            alias="SignedCertPath", description="Used to display location of the signed certificate in PEM format"
        ),
    ] = None
    """
    Used to display location of the signed certificate in PEM format
    """

    software_statement_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[SoftwareStatementId]],
        FieldMetadata(alias="SoftwareStatementIds"),
        pydantic.Field(alias="SoftwareStatementIds"),
    ] = None
    status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None
    valid_from_date_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ValidFromDateTime"), pydantic.Field(alias="ValidFromDateTime")
    ] = None
    e: typing.Optional[str] = None
    key_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="keyType"), pydantic.Field(alias="keyType")
    ] = None
    kid: typing.Optional[str] = None
    kty: typing.Optional[str] = None
    n: typing.Optional[str] = None
    use: typing.Optional[str] = None
    x5c: typing.Optional[typing.List[str]] = None
    x5t: typing.Optional[str] = None
    x5thash_s256: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="x5thashS256"), pydantic.Field(alias="x5thashS256")
    ] = None
    x5u: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
