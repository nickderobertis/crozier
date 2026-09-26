

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_agent_runtimes_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItem,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_artifacts_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItem,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_associated_resource_event_routing import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAssociatedResourceEventRouting,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_egress_routes_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItem,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_image import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanImage,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_runtime_clients_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItem,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_skills import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanSkills,
)
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_workspace_sources_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItem,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlan(UniversalBaseModel):
    sandbox_profile_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sandboxProfileId"), pydantic.Field(alias="sandboxProfileId")
    ]
    version: int
    image: PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanImage
    setup_script: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="setupScript"), pydantic.Field(alias="setupScript")
    ] = None
    egress_routes: typing_extensions.Annotated[
        typing.List[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItem],
        FieldMetadata(alias="egressRoutes"),
        pydantic.Field(alias="egressRoutes"),
    ]
    artifacts: typing.List[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItem]
    workspace_sources: typing_extensions.Annotated[
        typing.List[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItem],
        FieldMetadata(alias="workspaceSources"),
        pydantic.Field(alias="workspaceSources"),
    ]
    skills: typing.Optional[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanSkills] = None
    runtime_clients: typing_extensions.Annotated[
        typing.List[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItem],
        FieldMetadata(alias="runtimeClients"),
        pydantic.Field(alias="runtimeClients"),
    ]
    agent_runtimes: typing_extensions.Annotated[
        typing.List[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItem],
        FieldMetadata(alias="agentRuntimes"),
        pydantic.Field(alias="agentRuntimes"),
    ]
    associated_resource_event_routing: typing_extensions.Annotated[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAssociatedResourceEventRouting,
        FieldMetadata(alias="associatedResourceEventRouting"),
        pydantic.Field(alias="associatedResourceEventRouting"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
