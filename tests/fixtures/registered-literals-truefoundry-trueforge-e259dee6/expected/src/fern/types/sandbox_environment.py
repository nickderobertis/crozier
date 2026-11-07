

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_by_subject import CreatedBySubject
from .resource_name import ResourceName
from .sandbox_environment_lifecycle_stage import SandboxEnvironmentLifecycleStage
from .sandbox_environment_manifest import SandboxEnvironmentManifest
from .sandbox_environment_version_status import SandboxEnvironmentVersionStatus


class SandboxEnvironment(UniversalBaseModel):
    created_at: dt.datetime = pydantic.Field()
    """
    ISO-8601 create time.
    """

    created_by_subject: CreatedBySubject
    description: str = pydantic.Field()
    """
    Human-readable description; empty when unset.
    """

    id: str = pydantic.Field()
    """
    Immutable server-generated environment identifier.
    """

    lifecycle_stage: SandboxEnvironmentLifecycleStage
    manifest: SandboxEnvironmentManifest
    name: ResourceName
    status: SandboxEnvironmentVersionStatus
    status_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Failure detail when status is failed; null otherwise.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    ISO-8601 last update time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
