

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037error import Dbv0037Error
from .dbv0037wckey import Dbv0037Wckey


class Dbv0037WckeyInfo(UniversalBaseModel):
    errors: typing.Optional[typing.List[Dbv0037Error]] = pydantic.Field(default=None)
    """
    Slurm errors
    """

    wckeys: typing.Optional[typing.List[Dbv0037Wckey]] = pydantic.Field(default=None)
    """
    List of wckeys
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
