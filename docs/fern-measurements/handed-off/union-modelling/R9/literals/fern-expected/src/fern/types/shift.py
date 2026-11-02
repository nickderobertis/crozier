

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .shift_assignment import ShiftAssignment
from .shift_backup import ShiftBackup


class Shift(UniversalBaseModel):
    id: str
    assignment: typing.Optional[ShiftAssignment] = None
    backup: typing.Optional[ShiftBackup] = pydantic.Field(default=None)
    """
    Who stands in if the assignment falls through.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
