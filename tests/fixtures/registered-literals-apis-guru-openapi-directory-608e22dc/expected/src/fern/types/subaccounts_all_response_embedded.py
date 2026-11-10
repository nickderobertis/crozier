

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .subaccount_response import SubaccountResponse


class SubaccountsAllResponseEmbedded(UniversalBaseModel):
    primary_account: typing.Optional[SubaccountResponse] = None
    subaccounts: typing.Optional[typing.List[SubaccountResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
