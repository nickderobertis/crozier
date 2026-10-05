

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vcs_provider import VcsProvider


class RepoOwnersResponse(UniversalBaseModel):
    """
    Response model for repository OWNERS file data.

    Attention: usernames are provider-specific (e.g., GitHub usernames).
    """

    approvers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of usernames who can approve changes
    """

    provider: VcsProvider = pydantic.Field()
    """
    VCS provider type
    """

    reviewers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of usernames who can review changes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
