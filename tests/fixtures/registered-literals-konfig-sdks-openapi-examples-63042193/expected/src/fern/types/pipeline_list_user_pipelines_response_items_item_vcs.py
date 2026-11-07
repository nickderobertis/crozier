

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_list_user_pipelines_response_items_item_vcs_commit import (
    PipelineListUserPipelinesResponseItemsItemVcsCommit,
)


class PipelineListUserPipelinesResponseItemsItemVcs(UniversalBaseModel):
    """
    VCS information for the pipeline.
    """

    provider_name: str = pydantic.Field()
    """
    Name of the VCS provider (e.g. GitHub, Bitbucket).
    """

    target_repository_url: str = pydantic.Field()
    """
    URL for the repository the trigger targets (i.e. the repository where the PR will be merged). For fork-PR pipelines, this is the URL to the parent repo. For other pipelines, the `origin_` and `target_repository_url`s will be the same.
    """

    branch: typing.Optional[str] = pydantic.Field(default=None)
    """
    The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only).
    """

    review_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The code review id.
    """

    review_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The code review URL.
    """

    revision: str = pydantic.Field()
    """
    The code revision the pipeline ran.
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive.
    """

    commit: typing.Optional[PipelineListUserPipelinesResponseItemsItemVcsCommit] = pydantic.Field(default=None)
    """
    The latest commit in the pipeline.
    """

    origin_repository_url: str = pydantic.Field()
    """
    URL for the repository where the trigger originated. For fork-PR pipelines, this is the URL to the fork. For other pipelines the `origin_` and `target_repository_url`s will be the same.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
