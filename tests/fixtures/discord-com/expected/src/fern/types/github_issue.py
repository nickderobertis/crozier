

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .github_user import GithubUser


class GithubIssue(UniversalBaseModel):
    id: int
    number: int
    html_url: str
    user: GithubUser
    title: str
    body: typing.Optional[str] = None
    pull_request: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
