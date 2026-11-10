

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .numbers_eft import NumbersEft


class NumbersEftNullable(NumbersEft):
    """
    Identifying information for transferring money to or from a Canadian bank account via EFT.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
