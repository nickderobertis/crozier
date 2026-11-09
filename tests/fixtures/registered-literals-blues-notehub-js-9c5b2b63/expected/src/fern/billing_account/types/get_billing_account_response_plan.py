

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_billing_account_response_plan_type import GetBillingAccountResponsePlanType


class GetBillingAccountResponsePlan(UniversalBaseModel):
    current_balance: typing.Optional[int] = None
    end_date: typing.Optional[dt.datetime] = None
    event_capacity: typing.Optional[int] = None
    start_date: typing.Optional[dt.datetime] = None
    type: typing.Optional[GetBillingAccountResponsePlanType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
