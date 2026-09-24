

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .air_base import AirBase
from .created_at_field import CreatedAtField


class Air(CreatedAtField, AirBase):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
