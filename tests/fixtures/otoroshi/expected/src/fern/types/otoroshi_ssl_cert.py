

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_ssl_cert_ca_ref import OtoroshiSslCertCaRef
from .otoroshi_ssl_cert_cert_type import OtoroshiSslCertCertType
from .otoroshi_ssl_cert_password import OtoroshiSslCertPassword


class OtoroshiSslCert(UniversalBaseModel):
    """
    The otoroshi model for X509 certificates
    """

    cert_type: typing_extensions.Annotated[
        typing.Optional[OtoroshiSslCertCertType],
        FieldMetadata(alias="certType"),
        pydantic.Field(alias="certType", description="the kind of certificate"),
    ] = None
    """
    the kind of certificate
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity name
    """

    revoked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Certificate is revoked
    """

    subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    Certificate subject
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity description
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity tags
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Certificate domain
    """

    ca: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is cert a CA ?
    """

    keypair: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is cert used for its keypair only ?
    """

    lets_encrypt: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="letsEncrypt"),
        pydantic.Field(alias="letsEncrypt", description="Let's encrypt (ACME) generated"),
    ] = None
    """
    Let's encrypt (ACME) generated
    """

    auto_renew: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoRenew"),
        pydantic.Field(alias="autoRenew", description="Auto renew cert"),
    ] = None
    """
    Auto renew cert
    """

    ca_ref: typing_extensions.Annotated[
        typing.Optional[OtoroshiSslCertCaRef],
        FieldMetadata(alias="caRef"),
        pydantic.Field(alias="caRef", description="Reference to the CA (if any)"),
    ] = None
    """
    Reference to the CA (if any)
    """

    to: typing.Optional[float] = pydantic.Field(default=None)
    """
    Stop date
    """

    exposed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the cert exposed (public key exposed in jwks.json)
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity id
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    sans: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Certificate SANs
    """

    client: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is cert a client cert ?
    """

    from_: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="from"), pydantic.Field(alias="from", description="Start date")
    ] = None
    """
    Start date
    """

    valid: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is cert valid
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Entity metadata
    """

    private_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="privateKey"),
        pydantic.Field(alias="privateKey", description="Certificate private key (PEM encoded)"),
    ] = None
    """
    Certificate private key (PEM encoded)
    """

    self_signed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="selfSigned"),
        pydantic.Field(alias="selfSigned", description="Is cert self signed"),
    ] = None
    """
    Is cert self signed
    """

    chain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Certicates chain (PEM encoded)
    """

    password: typing.Optional[OtoroshiSslCertPassword] = pydantic.Field(default=None)
    """
    Certificate password
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
