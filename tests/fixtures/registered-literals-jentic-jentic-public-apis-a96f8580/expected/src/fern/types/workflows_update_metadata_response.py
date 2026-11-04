

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_update_metadata_response_approvals import WorkflowsUpdateMetadataResponseApprovals
from .workflows_update_metadata_response_attributes import WorkflowsUpdateMetadataResponseAttributes
from .workflows_update_metadata_response_creator import WorkflowsUpdateMetadataResponseCreator
from .workflows_update_metadata_response_roles_item import WorkflowsUpdateMetadataResponseRolesItem
from .workflows_update_metadata_response_schema import WorkflowsUpdateMetadataResponseSchema
from .workflows_update_metadata_response_signatures import WorkflowsUpdateMetadataResponseSignatures


class WorkflowsUpdateMetadataResponse(UniversalBaseModel):
    title: typing.Optional[str] = None
    id: typing.Optional[str] = None
    ironclad_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ironcladId"), pydantic.Field(alias="ironcladId")
    ] = None
    template: typing.Optional[str] = None
    step: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[WorkflowsUpdateMetadataResponseSchema],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema"),
    ] = None
    attributes: typing.Optional[WorkflowsUpdateMetadataResponseAttributes] = None
    is_cancelled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isCancelled"), pydantic.Field(alias="isCancelled")
    ] = None
    is_complete: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isComplete"), pydantic.Field(alias="isComplete")
    ] = None
    status: typing.Optional[str] = None
    creator: typing.Optional[WorkflowsUpdateMetadataResponseCreator] = None
    created: typing.Optional[str] = None
    last_updated: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ] = None
    roles: typing.Optional[typing.List[WorkflowsUpdateMetadataResponseRolesItem]] = None
    approvals: typing.Optional[WorkflowsUpdateMetadataResponseApprovals] = None
    signatures: typing.Optional[WorkflowsUpdateMetadataResponseSignatures] = None
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
