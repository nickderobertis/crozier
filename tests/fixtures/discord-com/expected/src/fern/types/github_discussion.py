

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .github_user import GithubUser


class GithubDiscussion(UniversalBaseModel):
    title: str
    number: int
    html_url: str
    answer_html_url: typing.Optional[str] = None
    body: typing.Optional[str] = None
    user: GithubUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
