

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlan,
)


class PostInternalSandboxRuntimeCompilePlanResponse(UniversalBaseModel):
    runtime_plan: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlan,
        FieldMetadata(alias="runtimePlan"),
        pydantic.Field(alias="runtimePlan"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
