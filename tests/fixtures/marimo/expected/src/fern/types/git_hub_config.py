

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GitHubConfig(UniversalBaseModel):
    """
    Configuration options for GitHub.

        **Keys.**

        - `api_key`: the GitHub API token
        - `base_url`: the base URL for the API
        - `copilot_settings`: configuration settings for GitHub Copilot LSP.
            Supports settings like `http` (proxy configuration), `telemetry`,
            and `github-enterprise` (enterprise URI).
    """

    api_key: typing.Optional[str] = None
    base_url: typing.Optional[str] = None
    copilot_settings: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
