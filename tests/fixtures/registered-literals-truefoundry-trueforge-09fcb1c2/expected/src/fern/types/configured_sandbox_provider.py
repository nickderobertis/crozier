

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_build_status import SandboxBuildStatus
from .sandbox_provider_manifest import SandboxProviderManifest


class ConfiguredSandboxProvider(UniversalBaseModel):
    manifest: SandboxProviderManifest
    status: SandboxBuildStatus
    status_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable detail for the current status; null when ready.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
