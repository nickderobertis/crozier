

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .program import Program


class PreconditioningProgram(Program):
    slot: typing.Optional[int] = pydantic.Field(default=None)
    """
    This program number. Can only be used ONE time in the same preconditioning list.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines whether this program is enabled or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
