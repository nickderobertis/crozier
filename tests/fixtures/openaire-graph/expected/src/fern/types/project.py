

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_pid import ProjectPid


class Project(UniversalBaseModel):
    id: typing.Optional[str] = None
    code: typing.Optional[str] = None
    acronym: typing.Optional[str] = None
    title: typing.Optional[str] = None
    funder: typing.Optional[str] = None
    pids: typing.Optional[typing.List[ProjectPid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
