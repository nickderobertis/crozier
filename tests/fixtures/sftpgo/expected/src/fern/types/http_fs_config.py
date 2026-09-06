

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret import Secret


class HttpFsConfig(UniversalBaseModel):
    endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTP/S endpoint URL. SFTPGo will use this URL as base, for example for the `stat` API, SFTPGo will add `/stat/{name}`
    """

    username: typing.Optional[str] = None
    password: typing.Optional[Secret] = None
    api_key: typing.Optional[Secret] = None
    skip_tls_verify: typing.Optional[bool] = None
    equality_check_mode: typing.Optional[int] = pydantic.Field(default=None)
    """
    Defines how to check if this config points to the same server as another config. If different configs point to the same server the renaming between the fs configs is allowed:
     * `0` username and endpoint must match. This is the default
     * `1` only the endpoint must match
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
