

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobGetDetailsResponseProject(UniversalBaseModel):
    """
    Information about a project.
    """

    id: str
    slug: str = pydantic.Field()
    """
    Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    """

    name: str = pydantic.Field()
    """
    The name of the project
    """

    external_url: str = pydantic.Field()
    """
    URL to the repository hosting the project's code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
