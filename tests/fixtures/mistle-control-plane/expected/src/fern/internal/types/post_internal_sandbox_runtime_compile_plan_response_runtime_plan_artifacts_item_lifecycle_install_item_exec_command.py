

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemExecCommand(
    UniversalBaseModel
):
    args: typing.List[str]
    env: typing.Optional[typing.Dict[str, str]] = None
    cwd: typing.Optional[str] = None
    timeout_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="timeoutMs"), pydantic.Field(alias="timeoutMs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
