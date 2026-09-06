

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tls_versions import TlsVersions


class WebDavBinding(UniversalBaseModel):
    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    TCP address the server listen on
    """

    port: typing.Optional[int] = pydantic.Field(default=None)
    """
    the port used for serving requests
    """

    enable_https: typing.Optional[bool] = None
    min_tls_version: typing.Optional[TlsVersions] = None
    client_auth_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    1 means that client certificate authentication is required in addition to HTTP basic authentication
    """

    tls_cipher_suites: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of supported cipher suites for TLS version 1.2. If empty  a default list of secure cipher suites is used, with a preference order based on hardware performance
    """

    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Prefix for WebDAV resources, if empty WebDAV resources will be available at the `/` URI
    """

    proxy_allowed: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of IP addresses and IP ranges allowed to set proxy headers
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
