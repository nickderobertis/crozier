

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SshBinding(UniversalBaseModel):
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
