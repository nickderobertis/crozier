

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class ProcessorStripeBankAccountTokenCreateResponse(UniversalBaseModel):
    """
    ProcessorStripeBankAccountTokenCreateResponse defines the response schema for `/processor/stripe/bank_account/create`
    """

    request_id: RequestId
    stripe_bank_account_token: str = pydantic.Field()
    """
    A token that can be sent to Stripe for use in making API calls to Plaid
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
