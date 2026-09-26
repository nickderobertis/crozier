

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_artifacts_item_lifecycle_install_item_github_release_install_asset_zero_format import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetZeroFormat,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_artifacts_item_lifecycle_install_item_github_release_install_asset_zero_kind import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetZeroKind,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetZero(
    UniversalBaseModel
):
    kind: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetZeroKind
    file_name: typing_extensions.Annotated[str, FieldMetadata(alias="fileName"), pydantic.Field(alias="fileName")]
    format: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetZeroFormat
    sha256: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
