

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_tcp_tcp_target import OtoroshiTcpTcpTarget


class OtoroshiTcpTcpRule(UniversalBaseModel):
    """
    Associate targets for a domain (SNI)
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    match on SNI domain
    """

    targets: typing.Optional[typing.List[OtoroshiTcpTcpTarget]] = pydantic.Field(default=None)
    """
    TCP targets
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
