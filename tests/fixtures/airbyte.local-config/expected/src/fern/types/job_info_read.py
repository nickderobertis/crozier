

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attempt_info_read import AttemptInfoRead
from .job_read import JobRead


class JobInfoRead(UniversalBaseModel):
    attempts: typing.List[AttemptInfoRead]
    job: JobRead

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
