

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Certificate(UniversalBaseModel):
    """
    A SSL/TLS X509 certificate
    """

    auto_renew: typing_extensions.Annotated[str, FieldMetadata(alias="autoRenew")] = pydantic.Field()
    """
    Allow Otoroshi to renew the certificate (if self signed)
    """

    ca: str = pydantic.Field()
    """
    Certificate is a CA (read only)
    """

    ca_ref: typing_extensions.Annotated[str, FieldMetadata(alias="caRef")] = pydantic.Field()
    """
    Reference for a CA certificate in otoroshi
    """

    chain: str = pydantic.Field()
    """
    Certificate chain of trust in PEM format
    """

    domain: str = pydantic.Field()
    """
    Domain of the certificate (read only)
    """

    from_: typing_extensions.Annotated[str, FieldMetadata(alias="from")] = pydantic.Field()
    """
    Start date of validity
    """

    id: str = pydantic.Field()
    """
    Id of the certificate
    """

    private_key: typing_extensions.Annotated[str, FieldMetadata(alias="privateKey")] = pydantic.Field()
    """
    PKCS8 private key in PEM format
    """

    self_signed: typing_extensions.Annotated[str, FieldMetadata(alias="selfSigned")] = pydantic.Field()
    """
    Certificate is self signed  read only)
    """

    subject: str = pydantic.Field()
    """
    Subject of the certificate (read only)
    """

    to: str = pydantic.Field()
    """
    End date of validity
    """

    valid: str = pydantic.Field()
    """
    Certificate is valid (read only)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
