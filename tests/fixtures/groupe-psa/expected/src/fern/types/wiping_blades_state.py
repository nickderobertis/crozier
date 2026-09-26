

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .created_at_field import CreatedAtField
from .wiping_blades_state_base import WipingBladesStateBase


class WipingBladesState(CreatedAtField, WipingBladesStateBase):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
