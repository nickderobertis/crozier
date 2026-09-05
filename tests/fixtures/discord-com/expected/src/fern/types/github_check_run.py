

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .github_check_pull_request import GithubCheckPullRequest
from .github_check_run_output import GithubCheckRunOutput
from .github_check_suite import GithubCheckSuite


class GithubCheckRun(UniversalBaseModel):
    conclusion: typing.Optional[str] = None
    name: str
    html_url: str
    check_suite: GithubCheckSuite
    details_url: typing.Optional[str] = None
    output: typing.Optional[GithubCheckRunOutput] = None
    pull_requests: typing.Optional[typing.List[GithubCheckPullRequest]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
