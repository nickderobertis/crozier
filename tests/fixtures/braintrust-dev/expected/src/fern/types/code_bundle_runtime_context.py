

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .code_bundle_runtime_context_runtime import CodeBundleRuntimeContextRuntime


class CodeBundleRuntimeContext(UniversalBaseModel):
    runtime: CodeBundleRuntimeContextRuntime
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
