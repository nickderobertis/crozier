

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delay import Delay
from .http_forward_scheme import HttpForwardScheme


class HttpForward(UniversalBaseModel):
    """
    host and port to forward to
    """

    delay: typing.Optional[Delay] = None
    host: typing.Optional[str] = None
    port: typing.Optional[int] = None
    scheme: typing.Optional[HttpForwardScheme] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
