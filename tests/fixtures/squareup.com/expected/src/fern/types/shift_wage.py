

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class ShiftWage(UniversalBaseModel):
    """
    The hourly wage rate used to compensate an employee for this shift.
    """

    hourly_rate: typing.Optional[Money] = None
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the job performed during this shift. Square
    labor-reporting UIs might group shifts together by title.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
