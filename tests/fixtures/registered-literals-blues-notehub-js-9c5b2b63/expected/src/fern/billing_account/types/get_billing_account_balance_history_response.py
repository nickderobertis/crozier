

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_billing_account_balance_history_response_data_item import GetBillingAccountBalanceHistoryResponseDataItem


class GetBillingAccountBalanceHistoryResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetBillingAccountBalanceHistoryResponseDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
