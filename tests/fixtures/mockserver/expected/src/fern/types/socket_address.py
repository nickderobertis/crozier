

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .socket_address_scheme import SocketAddressScheme


class SocketAddress(UniversalBaseModel):
    """
    remote address to send request to, only used for request overrides
    """

    host: typing.Optional[str] = None
    port: typing.Optional[int] = None
    scheme: typing.Optional[SocketAddressScheme] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
