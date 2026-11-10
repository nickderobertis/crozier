

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .numbers_ach import NumbersAch


class NumbersAchNullable(NumbersAch):
    """
    Identifying information for transferring money to or from a US account via ACH or wire transfer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
