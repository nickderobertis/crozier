

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_processes_item_stop_signal import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemStopSignal,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemStop(UniversalBaseModel):
    signal: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemStopSignal
    timeout_ms: typing_extensions.Annotated[int, FieldMetadata(alias="timeoutMs"), pydantic.Field(alias="timeoutMs")]
    grace_period_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="gracePeriodMs"), pydantic.Field(alias="gracePeriodMs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
