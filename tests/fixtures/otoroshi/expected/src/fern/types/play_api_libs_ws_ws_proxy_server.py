

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PlayApiLibsWsWsProxyServer(UniversalBaseModel):
    """
    Proxy server
    """

    host: typing.Optional[str] = pydantic.Field(default=None)
    """
    The hostname of the proxy server.
    """

    port: typing.Optional[str] = pydantic.Field(default=None)
    """
    The port of the proxy server.
    """

    protocol: typing.Optional[str] = pydantic.Field(default=None)
    """
    The protocol of the proxy server.  Use "http" or "https".  Defaults to "http" if not specified.
    """

    principal: typing.Optional[str] = pydantic.Field(default=None)
    """
    The principal (aka username) of the credentials for the proxy server.
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    The password for the credentials for the proxy server.
    """

    ntlm_domain: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ntlmDomain"),
        pydantic.Field(alias="ntlmDomain", description="The ntlm domain for the proxy server."),
    ] = None
    """
    The ntlm domain for the proxy server.
    """

    encoding: typing.Optional[str] = pydantic.Field(default=None)
    """
    The realm's charset.
    """

    non_proxy_hosts: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nonProxyHosts"),
        pydantic.Field(alias="nonProxyHosts", description="The non proxied hosts"),
    ] = None
    """
    The non proxied hosts
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
