

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class CreditRelayCreateResponse(UniversalBaseModel):
    """
    CreditRelayCreateResponse defines the response schema for `/credit/relay/create`
    """

    relay_token: str = pydantic.Field()
    """
    A token that can be shared with a third party to allow them to access the Asset Report. This token should be stored securely.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
