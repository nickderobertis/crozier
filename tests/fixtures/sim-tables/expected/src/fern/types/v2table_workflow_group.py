

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_workflow_group_dependencies import V2TableWorkflowGroupDependencies
from .v2table_workflow_group_deployment_mode import V2TableWorkflowGroupDeploymentMode
from .v2table_workflow_group_input_mappings_item import V2TableWorkflowGroupInputMappingsItem
from .v2table_workflow_group_outputs_item import V2TableWorkflowGroupOutputsItem
from .v2table_workflow_group_type import V2TableWorkflowGroupType


class V2TableWorkflowGroup(UniversalBaseModel):
    """
    A workflow or enrichment producer and the columns it populates.
    """

    id: str = pydantic.Field()
    """
    Unique workflow-group identifier.
    """

    workflow_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflowId"),
        pydantic.Field(alias="workflowId", description="Backing workflow identifier for a manual group."),
    ]
    """
    Backing workflow identifier for a manual group.
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

    type: typing.Optional[V2TableWorkflowGroupType] = pydantic.Field(default=None)
    """
    Producer type.
    """

    dependencies: typing.Optional[V2TableWorkflowGroupDependencies] = pydantic.Field(default=None)
    """
    Input column dependencies.
    """

    outputs: typing.List[V2TableWorkflowGroupOutputsItem] = pydantic.Field()
    """
    Workflow outputs mapped to table columns.
    """

    input_mappings: typing_extensions.Annotated[
        typing.Optional[typing.List[V2TableWorkflowGroupInputMappingsItem]],
        FieldMetadata(alias="inputMappings"),
        pydantic.Field(alias="inputMappings", description="Workflow inputs mapped from table columns."),
    ] = None
    """
    Workflow inputs mapped from table columns.
    """

    deployment_mode: typing_extensions.Annotated[
        typing.Optional[V2TableWorkflowGroupDeploymentMode],
        FieldMetadata(alias="deploymentMode"),
        pydantic.Field(alias="deploymentMode", description="Workflow execution mode."),
    ] = None
    """
    Workflow execution mode.
    """

    auto_run: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoRun"),
        pydantic.Field(alias="autoRun", description="Whether the group automatically runs for new rows."),
    ] = None
    """
    Whether the group automatically runs for new rows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
