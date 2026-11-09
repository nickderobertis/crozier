

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .numbers_bacs import NumbersBacs


class NumbersBacsNullable(NumbersBacs):
    """
    Identifying information for transferring money to or from a UK bank account via BACS.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
