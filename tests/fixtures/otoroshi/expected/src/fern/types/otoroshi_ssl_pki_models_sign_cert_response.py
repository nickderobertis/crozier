

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_ssl_pki_models_sign_cert_response_ca import OtoroshiSslPkiModelsSignCertResponseCa


class OtoroshiSslPkiModelsSignCertResponse(UniversalBaseModel):
    """
    Response for a certificate signing operation
    """

    cert: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cert (PEM encoded)
    """

    csr: typing.Optional[str] = pydantic.Field(default=None)
    """
    CSR (PEM encoded)
    """

    ca: typing.Optional[OtoroshiSslPkiModelsSignCertResponseCa] = pydantic.Field(default=None)
    """
    Ca cert (PEM encoded)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
