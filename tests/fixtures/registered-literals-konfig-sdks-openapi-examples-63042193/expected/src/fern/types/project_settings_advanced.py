

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProjectSettingsAdvanced(UniversalBaseModel):
    autocancel_builds: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Except for the default branch, cancel running pipelines on a branch when a new pipeline starts on that branch.
    """

    build_fork_prs: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Run builds for pull requests from forks.
    """

    build_prs_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Once enabled, we will only build branches that have associated pull requests open.
    """

    disable_ssh: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When set to true, job re-runs with SSH debugging access will be disabled for the project.
    """

    forks_receive_secret_env_vars: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Run builds for forked pull requests with this project's configuration, environment variables, and secrets.
    """

    oss: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Free and Open Source. Enabling this grants additional credits, and lets others see your builds, both through the web UI and the API.
    """

    set_github_status: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Report the status of every pushed commit to GitHub's status API. Updates reported per job.
    """

    setup_workflows: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enabling allows you to conditionally trigger configurations outside of the primary `.circleci` parent directory.
    """

    write_settings_requires_admin: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether updating these settings requires a user to be an organization administrator. When disabled, updating settings can be done by any member.
    """

    pr_only_branch_overrides: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    This field is used in conjunction with the `build_prs_only`, it allows you to specify a list of branches that will always triger a build. The value passed will overwrite the existing value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
