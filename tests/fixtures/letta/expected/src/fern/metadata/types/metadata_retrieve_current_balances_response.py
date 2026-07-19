

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataRetrieveCurrentBalancesResponse(UniversalBaseModel):
    total_balance: float
    monthly_credit_balance: float
    purchased_credit_balance: float
    billing_tier: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
