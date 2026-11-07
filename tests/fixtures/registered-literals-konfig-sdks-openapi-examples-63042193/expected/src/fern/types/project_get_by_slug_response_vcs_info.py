

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_get_by_slug_response_vcs_info_provider import ProjectGetBySlugResponseVcsInfoProvider


class ProjectGetBySlugResponseVcsInfo(UniversalBaseModel):
    """
    Information about the VCS that hosts the project source code.
    """

    vcs_url: str = pydantic.Field()
    """
    URL to the repository hosting the project's code
    """

    provider: ProjectGetBySlugResponseVcsInfoProvider = pydantic.Field()
    """
    The VCS provider
    """

    default_branch: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
