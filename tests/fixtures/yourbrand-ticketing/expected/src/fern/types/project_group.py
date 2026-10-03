

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project import Project


class ProjectGroup(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    project: typing.Optional[Project] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
