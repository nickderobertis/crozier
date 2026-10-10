

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_sandbox_provider_type import CatalogSandboxProviderType


class CatalogSandboxProvider(UniversalBaseModel):
    auto_archive_interval_in_minutes: int = pydantic.Field()
    """
    Minutes before Daytona auto-archives the sandbox (0 disables).
    """

    auto_delete_interval_in_minutes: int = pydantic.Field()
    """
    Minutes before Daytona auto-deletes the sandbox (0 disables).
    """

    auto_stop_interval_in_minutes: int = pydantic.Field()
    """
    Minutes of idle time before Daytona auto-stops the sandbox (0 disables).
    """

    exec_timeout_ms: int = pydantic.Field()
    """
    Default sandbox command exec timeout in milliseconds.
    """

    type: CatalogSandboxProviderType = pydantic.Field()
    """
    Daytona sandbox provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
