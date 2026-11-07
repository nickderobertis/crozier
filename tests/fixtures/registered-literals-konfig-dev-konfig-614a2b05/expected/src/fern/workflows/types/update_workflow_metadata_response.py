

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_workflow_metadata_response_approvals import UpdateWorkflowMetadataResponseApprovals
from .update_workflow_metadata_response_attributes import UpdateWorkflowMetadataResponseAttributes
from .update_workflow_metadata_response_creator import UpdateWorkflowMetadataResponseCreator
from .update_workflow_metadata_response_roles_item import UpdateWorkflowMetadataResponseRolesItem
from .update_workflow_metadata_response_schema import UpdateWorkflowMetadataResponseSchema
from .update_workflow_metadata_response_signatures import UpdateWorkflowMetadataResponseSignatures


class UpdateWorkflowMetadataResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    ironclad_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ironcladId"), pydantic.Field(alias="ironcladId")
    ] = None
    title: typing.Optional[str] = None
    template: typing.Optional[str] = None
    step: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[UpdateWorkflowMetadataResponseSchema],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema"),
    ] = None
    attributes: typing.Optional[UpdateWorkflowMetadataResponseAttributes] = None
    is_cancelled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isCancelled"), pydantic.Field(alias="isCancelled")
    ] = None
    is_complete: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isComplete"), pydantic.Field(alias="isComplete")
    ] = None
    status: typing.Optional[str] = None
    creator: typing.Optional[UpdateWorkflowMetadataResponseCreator] = None
    created: typing.Optional[str] = None
    last_updated: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ] = None
    roles: typing.Optional[typing.List[UpdateWorkflowMetadataResponseRolesItem]] = None
    approvals: typing.Optional[UpdateWorkflowMetadataResponseApprovals] = None
    signatures: typing.Optional[UpdateWorkflowMetadataResponseSignatures] = None
    record_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="recordIds"), pydantic.Field(alias="recordIds")
    ] = None
    is_revertible_to_review: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isRevertibleToReview"), pydantic.Field(alias="isRevertibleToReview")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
