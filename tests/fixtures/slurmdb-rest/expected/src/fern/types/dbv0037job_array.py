

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_array_limits import Dbv0037JobArrayLimits


class Dbv0037JobArray(UniversalBaseModel):
    """
    Array properties (optional)
    """

    job_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Job id of array
    """

    limits: typing.Optional[Dbv0037JobArrayLimits] = None
    task: typing.Optional[str] = pydantic.Field(default=None)
    """
    Array task
    """

    task_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Array task id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
