

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .named import Named


class Gauge(Named):
    unit: typing.Optional[str] = None
    precision: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
