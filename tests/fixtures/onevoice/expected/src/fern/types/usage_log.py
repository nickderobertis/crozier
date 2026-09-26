

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsageLog(UniversalBaseModel):
    id: typing.Optional[str] = None
    business_id: str
    user_id: str
    conversation_id: typing.Optional[str] = None
    request_id: typing.Optional[str] = None
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    cache_read_tokens: typing.Optional[int] = None
    cache_creation_tokens: typing.Optional[int] = None
    provider_cost_usd: float
    commission_usd: float
    user_cost_usd: float
    user_tier: str
    created_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
