

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class DepositSwitchTokenCreateResponse(UniversalBaseModel):
    """
    DepositSwitchTokenCreateResponse defines the response schema for `/deposit_switch/token/create`
    """

    deposit_switch_token: str = pydantic.Field()
    """
    Deposit switch token, used to initialize Link for the Deposit Switch product
    """

    deposit_switch_token_expiration_time: str = pydantic.Field()
    """
    Expiration time of the token, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
