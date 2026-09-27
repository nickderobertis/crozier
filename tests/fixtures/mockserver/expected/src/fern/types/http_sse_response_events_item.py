

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delay import Delay


class HttpSseResponseEventsItem(UniversalBaseModel):
    event: typing.Optional[str] = None
    data: typing.Optional[str] = None
    id: typing.Optional[str] = None
    retry: typing.Optional[int] = None
    delay: typing.Optional[Delay] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
