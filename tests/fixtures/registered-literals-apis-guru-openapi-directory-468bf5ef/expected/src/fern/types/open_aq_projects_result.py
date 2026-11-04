

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .meta import Meta
from .projects_row import ProjectsRow


class OpenAqProjectsResult(UniversalBaseModel):
    meta: typing.Optional[Meta] = None
    results: typing.List[ProjectsRow]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
