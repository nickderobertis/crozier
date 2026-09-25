

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_data_index_view_view_of import ProjectDataIndexViewViewOf


class ProjectDataIndexView(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    view_of: ProjectDataIndexViewViewOf

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
