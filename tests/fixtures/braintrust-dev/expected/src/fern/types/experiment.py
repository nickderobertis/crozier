

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .repo_info import RepoInfo


class Experiment(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the experiment
    """

    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the experiment belongs under
    """

    name: str = pydantic.Field()
    """
    Name of the experiment. Within a project, experiment names are unique
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the experiment
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of experiment creation
    """

    repo_info: typing.Optional[RepoInfo] = None
    commit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Commit, taken directly from `repo_info.commit`
    """

    base_exp_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id of default base experiment to compare against when viewing this experiment
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of experiment deletion, or null if the experiment is still active
    """

    dataset_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier of the linked dataset, or null if the experiment is not linked to a dataset
    """

    dataset_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version number of the linked dataset the experiment was run against. This can be used to reproduce the experiment after the dataset has been modified.
    """

    parameters_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier of the linked saved parameters object, or null if the experiment is not linked to saved parameters
    """

    parameters_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version number of the linked saved parameters object the experiment was run against.
    """

    public: bool = pydantic.Field()
    """
    Whether or not the experiment is public. Public experiments can be viewed by anybody inside or outside the organization
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the user who created the experiment
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    User-controlled metadata about the experiment
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of tags for the experiment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
