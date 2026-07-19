

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037error import Dbv0037Error
from .dbv0037job import Dbv0037Job


class Dbv0037JobInfo(UniversalBaseModel):
    errors: typing.Optional[typing.List[Dbv0037Error]] = pydantic.Field(default=None)
    """
    Slurm errors
    """

    jobs: typing.Optional[typing.List[Dbv0037Job]] = pydantic.Field(default=None)
    """
    Array of jobs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
