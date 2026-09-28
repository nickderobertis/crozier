

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_ssl_pki_models_gen_csr_query_existing_serial_number import (
    OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
)
from .otoroshi_ssl_pki_models_gen_csr_query_subject import OtoroshiSslPkiModelsGenCsrQuerySubject
from .otoroshi_ssl_pki_models_gen_key_pair_query import OtoroshiSslPkiModelsGenKeyPairQuery


class OtoroshiSslPkiModelsGenCsrQuery(UniversalBaseModel):
    """
    Settings for generating a certificate
    """

    client: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is cert client ?
    """

    hosts: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Certificate SANs
    """

    key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = pydantic.Field(default=None)
    """
    Keypair specs
    """

    include_aia: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="includeAIA"),
        pydantic.Field(alias="includeAIA", description="Include AIA extension (if generated from otoroshi CA)"),
    ] = None
    """
    Include AIA extension (if generated from otoroshi CA)
    """

    signature_alg: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signatureAlg"),
        pydantic.Field(alias="signatureAlg", description="Signature algorithm"),
    ] = None
    """
    Signature algorithm
    """

    existing_serial_number: typing_extensions.Annotated[
        typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber],
        FieldMetadata(alias="existingSerialNumber"),
        pydantic.Field(alias="existingSerialNumber", description=""),
    ] = None
    """
    
    """

    duration: typing.Optional[float] = pydantic.Field(default=None)
    """
    Certificate lifespan
    """

    digest_alg: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="digestAlg"),
        pydantic.Field(alias="digestAlg", description="Digest algo"),
    ] = None
    """
    Digest algo
    """

    ca: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is cert ca ?
    """

    name: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Certificate name
    """

    subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = pydantic.Field(default=None)
    """
    Certificate subject
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
