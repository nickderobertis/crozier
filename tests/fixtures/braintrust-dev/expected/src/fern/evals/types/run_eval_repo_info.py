

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunEvalRepoInfo(UniversalBaseModel):
    """
    Optionally explicitly specify the git metadata for this experiment. This takes precedence over `gitMetadataSettings` if specified.
    """

    commit: typing.Optional[str] = pydantic.Field(default=None)
    """
    SHA of most recent commit
    """

    branch: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the branch the most recent commit belongs to
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the tag on the most recent commit
    """

    dirty: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the repo had uncommitted changes when snapshotted
    """

    author_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the author of the most recent commit
    """

    author_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email of the author of the most recent commit
    """

    commit_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Most recent commit message
    """

    commit_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    Time of the most recent commit
    """

    git_diff: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the repo was dirty when run, this includes the diff between the current state of the repo and the most recent commit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
