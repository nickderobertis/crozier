

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .github_check_app import GithubCheckApp
from .github_check_pull_request import GithubCheckPullRequest


class GithubCheckSuite(UniversalBaseModel):
    conclusion: typing.Optional[str] = None
    head_branch: typing.Optional[str] = None
    head_sha: str
    pull_requests: typing.Optional[typing.List[GithubCheckPullRequest]] = None
    app: GithubCheckApp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
