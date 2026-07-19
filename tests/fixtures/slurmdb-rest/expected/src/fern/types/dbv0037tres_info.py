

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037error import Dbv0037Error
from .dbv0037tres_list import Dbv0037TresList


class Dbv0037TresInfo(UniversalBaseModel):
    errors: typing.Optional[typing.List[Dbv0037Error]] = pydantic.Field(default=None)
    """
    Slurm errors
    """

    tres: typing.Optional[typing.List[Dbv0037TresList]] = pydantic.Field(default=None)
    """
    Array of tres
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
