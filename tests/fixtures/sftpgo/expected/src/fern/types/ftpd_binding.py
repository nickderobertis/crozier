

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .passive_ip_override import PassiveIpOverride
from .tls_versions import TlsVersions


class FtpdBinding(UniversalBaseModel):
    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    TCP address the server listen on
    """

    port: typing.Optional[int] = pydantic.Field(default=None)
    """
    the port used for serving requests
    """

    apply_proxy_config: typing.Optional[bool] = pydantic.Field(default=None)
    """
    apply the proxy configuration, if any
    """

    tls_mode: typing.Optional[int] = pydantic.Field(default=None)
    """
    TLS mode:
      * `0` - clear or explicit TLS
      * `1` - explicit TLS required
      * `2` - implicit TLS
    """

    min_tls_version: typing.Optional[TlsVersions] = None
    force_passive_ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    External IP address for passive connections
    """

    passive_ip_overrides: typing.Optional[typing.List[PassiveIpOverride]] = None
    client_auth_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    1 means that client certificate authentication is required in addition to FTP authentication
    """

    tls_cipher_suites: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of supported cipher suites for TLS version 1.2. If empty  a default list of secure cipher suites is used, with a preference order based on hardware performance
    """

    passive_connections_security: typing.Optional[int] = pydantic.Field(default=None)
    """
    Active connections security:
      * `0` - require matching peer IP addresses of control and data connection
      * `1` - disable any checks
    """

    active_connections_security: typing.Optional[int] = pydantic.Field(default=None)
    """
    Active connections security:
      * `0` - require matching peer IP addresses of control and data connection
      * `1` - disable any checks
    """

    ignore_ascii_transfer_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    Ignore client requests to perform ASCII translations:
      * `0` - ASCII translations are enabled
      * `1` - ASCII translations are silently ignored
    """

    debug: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If enabled any FTP command will be logged
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
