

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_setup_files_item_write_mode import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetupFilesItemWriteMode,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetupFilesItem(UniversalBaseModel):
    file_id: typing_extensions.Annotated[str, FieldMetadata(alias="fileId"), pydantic.Field(alias="fileId")]
    path: str
    mode: int
    content: str
    write_mode: typing_extensions.Annotated[
        typing.Optional[
            PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetupFilesItemWriteMode
        ],
        FieldMetadata(alias="writeMode"),
        pydantic.Field(alias="writeMode"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
