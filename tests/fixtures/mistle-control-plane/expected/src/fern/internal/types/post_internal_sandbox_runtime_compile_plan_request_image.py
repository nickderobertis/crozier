

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_request_image_kind import (
    PostInternalSandboxRuntimeCompilePlanRequestImageKind,
)


class PostInternalSandboxRuntimeCompilePlanRequestImage(UniversalBaseModel):
    image_id: typing_extensions.Annotated[str, FieldMetadata(alias="imageId"), pydantic.Field(alias="imageId")]
    kind: PostInternalSandboxRuntimeCompilePlanRequestImageKind

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
