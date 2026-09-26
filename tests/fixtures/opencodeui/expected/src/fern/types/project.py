

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_commands import ProjectCommands
from .project_icon import ProjectIcon
from .project_time import ProjectTime
from .project_vcs import ProjectVcs


class Project(UniversalBaseModel):
    id: str
    worktree: str
    vcs: typing.Optional[ProjectVcs] = None
    name: typing.Optional[str] = None
    icon: typing.Optional[ProjectIcon] = None
    commands: typing.Optional[ProjectCommands] = None
    time: ProjectTime
    sandboxes: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
