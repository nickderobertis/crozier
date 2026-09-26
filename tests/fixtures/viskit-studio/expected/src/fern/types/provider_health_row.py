

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_health_row_status import ProviderHealthRowStatus


class ProviderHealthRow(UniversalBaseModel):
    base_url: typing.Optional[str] = None
    endpoint_id: str
    last_check: typing.Optional[str] = None
    latency_ms: typing.Optional[int] = None
    role: str
    status: typing.Optional[ProviderHealthRowStatus] = None
    unbound: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
