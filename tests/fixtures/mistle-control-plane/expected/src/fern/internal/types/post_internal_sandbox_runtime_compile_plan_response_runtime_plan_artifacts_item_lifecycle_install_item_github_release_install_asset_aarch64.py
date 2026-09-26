

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_artifacts_item_lifecycle_install_item_github_release_install_asset_aarch64aarch64 import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetAarch64Aarch64,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_artifacts_item_lifecycle_install_item_github_release_install_asset_aarch64kind import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetAarch64Kind,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_artifacts_item_lifecycle_install_item_github_release_install_asset_aarch64x8664 import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetAarch64X8664,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetAarch64(
    UniversalBaseModel
):
    kind: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetAarch64Kind
    x8664: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetAarch64X8664,
        FieldMetadata(alias="x86_64"),
        pydantic.Field(alias="x86_64"),
    ]
    aarch64: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetAarch64Aarch64

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
