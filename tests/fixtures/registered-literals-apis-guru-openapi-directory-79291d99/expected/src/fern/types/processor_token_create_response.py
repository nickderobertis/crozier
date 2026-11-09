

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class ProcessorTokenCreateResponse(UniversalBaseModel):
    """
    ProcessorTokenCreateResponse defines the response schema for `/processor/token/create` and `/processor/apex/processor_token/create`
    """

    processor_token: str = pydantic.Field()
    """
    The `processor_token` that can then be used by the Plaid partner to make API requests
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
