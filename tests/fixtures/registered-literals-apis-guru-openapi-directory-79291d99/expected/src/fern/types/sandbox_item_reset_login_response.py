

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class SandboxItemResetLoginResponse(UniversalBaseModel):
    """
    SandboxItemResetLoginResponse defines the response schema for `/sandbox/item/reset_login`
    """

    request_id: RequestId
    reset_login: bool = pydantic.Field()
    """
    `true` if the call succeeded
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
