

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .created_at_field import CreatedAtField
from .maintenance_base import MaintenanceBase
from .updated_at_field import UpdatedAtField


class MaintenanceObj(CreatedAtField, UpdatedAtField, MaintenanceBase):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
