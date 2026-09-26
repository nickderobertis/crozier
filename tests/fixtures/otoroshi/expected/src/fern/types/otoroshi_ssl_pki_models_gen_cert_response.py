

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_ssl_pki_models_gen_cert_response_csr_query import OtoroshiSslPkiModelsGenCertResponseCsrQuery


class OtoroshiSslPkiModelsGenCertResponse(UniversalBaseModel):
    """
    Response for a certificate generation operation
    """

    ca: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ca cert (PEM encoded)
    """

    ca_chain: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="caChain"),
        pydantic.Field(alias="caChain", description="Ca chain (PEM encoded)"),
    ] = None
    """
    Ca chain (PEM encoded)
    """

    csr_query: typing_extensions.Annotated[
        typing.Optional[OtoroshiSslPkiModelsGenCertResponseCsrQuery],
        FieldMetadata(alias="csrQuery"),
        pydantic.Field(alias="csrQuery", description="JSON generation query"),
    ] = None
    """
    JSON generation query
    """

    cert: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cert (PEM encoded)
    """

    serial: typing.Optional[int] = pydantic.Field(default=None)
    """
    Certificate serial number
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Private key (PEM encoded)
    """

    csr: typing.Optional[str] = pydantic.Field(default=None)
    """
    CSR (PEM encoded)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
