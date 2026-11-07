

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gateway_error_error import GatewayErrorError


class GatewayError(UniversalBaseModel):
    """
    OpenAI-style error envelope returned by /v1/* gateway routes.
    """

    error: GatewayErrorError

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
