

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gateway_error_error import GatewayErrorError


class GatewayError(UniversalBaseModel):
    """
    Returned by gateway infrastructure errors before an RPC handler runs, such as origin, routing, method, authentication, or quota checks.
    """

    error: GatewayErrorError = pydantic.Field()
    """
    Gateway error reason or structured gateway failure details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
