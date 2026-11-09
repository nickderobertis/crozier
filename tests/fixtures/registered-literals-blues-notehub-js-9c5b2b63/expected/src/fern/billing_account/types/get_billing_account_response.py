

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_billing_account_response_plan import GetBillingAccountResponsePlan


class GetBillingAccountResponse(UniversalBaseModel):
    contact_uid: typing.Optional[str] = None
    email: typing.Optional[str] = None
    name: typing.Optional[str] = None
    owner: typing.Optional[str] = None
    plan: typing.Optional[GetBillingAccountResponsePlan] = None
    suspended: typing.Optional[bool] = None
    uid: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
