

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class SandboxProcessorTokenCreateResponse(UniversalBaseModel):
    """
    SandboxProcessorTokenCreateResponse defines the response schema for `/sandbox/processor_token/create`
    """

    processor_token: str = pydantic.Field()
    """
    A processor token that can be used to call the `/processor/` endpoints.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
