

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_projects_response_projects_item import GetProjectsResponseProjectsItem


class GetProjectsResponse(UniversalBaseModel):
    projects: typing.Optional[typing.List[GetProjectsResponseProjectsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
