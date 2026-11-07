

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_get_by_slug_response_vcs_info import ProjectGetBySlugResponseVcsInfo


class ProjectGetBySlugResponse(UniversalBaseModel):
    """
    NOTE: The definition of Project is subject to change.
    """

    slug: str = pydantic.Field()
    """
    Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    """

    name: str = pydantic.Field()
    """
    The name of the project
    """

    id: str
    organization_name: str = pydantic.Field()
    """
    The name of the organization the project belongs to
    """

    organization_slug: str = pydantic.Field()
    """
    The slug of the organization the project belongs to
    """

    organization_id: str = pydantic.Field()
    """
    The id of the organization the project belongs to
    """

    vcs_info: ProjectGetBySlugResponseVcsInfo = pydantic.Field()
    """
    Information about the VCS that hosts the project source code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
