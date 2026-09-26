

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item_setup_files_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetupFilesItem,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetup(UniversalBaseModel):
    env: typing.Dict[str, str]
    files: typing.List[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetupFilesItem]
    launch_args: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="launchArgs"), pydantic.Field(alias="launchArgs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
