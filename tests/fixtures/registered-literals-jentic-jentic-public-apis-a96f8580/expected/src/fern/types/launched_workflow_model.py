

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attributes_model import AttributesModel
from .launched_workflow_model_approvals import LaunchedWorkflowModelApprovals
from .launched_workflow_model_creator import LaunchedWorkflowModelCreator
from .launched_workflow_model_signatures import LaunchedWorkflowModelSignatures
from .launched_workflow_model_status import LaunchedWorkflowModelStatus
from .launched_workflow_model_step import LaunchedWorkflowModelStep
from .workflow_role_model import WorkflowRoleModel
from .workflow_template_id_model import WorkflowTemplateIdModel


class LaunchedWorkflowModel(UniversalBaseModel):
    """
    The response from a successful workflow launch.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name used for the launched workflow.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the launched workflow.
    """

    ironclad_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ironcladId"),
        pydantic.Field(alias="ironcladId", description="The Ironclad ID of the launched workflow."),
    ] = None
    """
    The Ironclad ID of the launched workflow.
    """

    template: WorkflowTemplateIdModel
    step: typing.Optional[LaunchedWorkflowModelStep] = pydantic.Field(default=None)
    """
    The step the workflow is currently on.
    """

    schema_: typing_extensions.Annotated[AttributesModel, FieldMetadata(alias="schema"), pydantic.Field(alias="schema")]
    is_cancelled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCancelled"),
        pydantic.Field(alias="isCancelled", description="Displays if the launched workflow has been cancelled."),
    ] = None
    """
    Displays if the launched workflow has been cancelled.
    """

    is_complete: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isComplete"),
        pydantic.Field(alias="isComplete", description="Displays if the launched workflow has been completed."),
    ] = None
    """
    Displays if the launched workflow has been completed.
    """

    status: typing.Optional[LaunchedWorkflowModelStatus] = pydantic.Field(default=None)
    """
    The current status of the launched workflow.
    """

    creator: typing.Optional[LaunchedWorkflowModelCreator] = pydantic.Field(default=None)
    """
    
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date (ISO8601 format) the workflow was launched
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date (ISO8601 format) the workflow was last updated"),
    ] = None
    """
    The date (ISO8601 format) the workflow was last updated
    """

    roles: typing.Optional[typing.List[WorkflowRoleModel]] = None
    approvals: LaunchedWorkflowModelApprovals
    signatures: LaunchedWorkflowModelSignatures
    record_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="recordIds"), pydantic.Field(alias="recordIds")
    ] = None
    is_revertible_to_review: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isRevertibleToReview"),
        pydantic.Field(
            alias="isRevertibleToReview",
            description="Displays if the launched workflow can be reverted back to the review step.",
        ),
    ] = None
    """
    Displays if the launched workflow can be reverted back to the review step.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
