

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .add_table_workflow_group_request_group_dependencies import AddTableWorkflowGroupRequestGroupDependencies
from .add_table_workflow_group_request_group_deployment_mode import AddTableWorkflowGroupRequestGroupDeploymentMode
from .add_table_workflow_group_request_group_input_mappings_item import (
    AddTableWorkflowGroupRequestGroupInputMappingsItem,
)
from .add_table_workflow_group_request_group_outputs_item import AddTableWorkflowGroupRequestGroupOutputsItem
from .add_table_workflow_group_request_group_type import AddTableWorkflowGroupRequestGroupType


class AddTableWorkflowGroupRequestGroup(UniversalBaseModel):
    """
    Workflow or enrichment producer definition.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional client-provided workflow-group identifier.
    """

    workflow_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workflowId"),
        pydantic.Field(
            alias="workflowId",
            description="Backing workflow identifier. Required when `type` is `manual` (which is also the default when `type` is omitted); omit it for an `enrichment` group.",
        ),
    ] = None
    """
    Backing workflow identifier. Required when `type` is `manual` (which is also the default when `type` is omitted); omit it for an `enrichment` group.
    """

    enrichment_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="enrichmentId"),
        pydantic.Field(alias="enrichmentId", description="Registry enrichment identifier."),
    ] = None
    """
    Registry enrichment identifier.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Workflow-group display name.
    """

    type: typing.Optional[AddTableWorkflowGroupRequestGroupType] = pydantic.Field(default=None)
    """
    Workflow-group producer type.
    """

    dependencies: typing.Optional[AddTableWorkflowGroupRequestGroupDependencies] = pydantic.Field(default=None)
    """
    Producer input dependencies.
    """

    outputs: typing.List[AddTableWorkflowGroupRequestGroupOutputsItem] = pydantic.Field()
    """
    Producer outputs mapped to columns.
    """

    input_mappings: typing_extensions.Annotated[
        typing.Optional[typing.List[AddTableWorkflowGroupRequestGroupInputMappingsItem]],
        FieldMetadata(alias="inputMappings"),
        pydantic.Field(alias="inputMappings", description="Workflow inputs mapped from table columns."),
    ] = None
    """
    Workflow inputs mapped from table columns.
    """

    deployment_mode: typing_extensions.Annotated[
        typing.Optional[AddTableWorkflowGroupRequestGroupDeploymentMode],
        FieldMetadata(alias="deploymentMode"),
        pydantic.Field(alias="deploymentMode", description="Workflow state used for cell runs."),
    ] = None
    """
    Workflow state used for cell runs.
    """

    auto_run: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoRun"),
        pydantic.Field(alias="autoRun", description="Whether this group automatically runs for new rows."),
    ] = None
    """
    Whether this group automatically runs for new rows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
