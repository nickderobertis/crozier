

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KvdbCompactStatusGetResponse(UniversalBaseModel):
    samp_lwm_pct: typing.Optional[int] = None
    samp_hwm_pct: typing.Optional[int] = None
    samp_curr_pct: typing.Optional[int] = None
    active: typing.Optional[bool] = None
    canceled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
