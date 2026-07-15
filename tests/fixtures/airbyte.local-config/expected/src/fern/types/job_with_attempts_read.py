

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attempt_read import AttemptRead
from .job_read import JobRead


class JobWithAttemptsRead(UniversalBaseModel):
    attempts: typing.Optional[typing.List[AttemptRead]] = None
    job: typing.Optional[JobRead] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
