

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employee import Employee
from .hris_job import HrisJob


class HrisJobs(UniversalBaseModel):
    employee: typing.Optional[Employee] = None
    jobs: typing.Optional[typing.List[HrisJob]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
