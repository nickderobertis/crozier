

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflow_response_model_attributes import WorkflowResponseModelAttributes
from .workflow_response_model_creator import WorkflowResponseModelCreator
from .workflow_response_model_roles_item import WorkflowResponseModelRolesItem
from .workflow_response_model_schema import WorkflowResponseModelSchema
from .workflow_response_model_status import WorkflowResponseModelStatus
from .workflow_state_model import WorkflowStateModel


class WorkflowResponseModel(UniversalBaseModel):
    """
    The response from a successful workflow retrieval.
    """

    id: str
    ironclad_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ironcladId"), pydantic.Field(alias="ironcladId")
    ] = None
    title: str
    template: str
    step: str
    schema_: typing_extensions.Annotated[
        WorkflowResponseModelSchema, FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ]
    attributes: WorkflowResponseModelAttributes
    is_cancelled: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isCancelled"), pydantic.Field(alias="isCancelled")
    ]
    is_complete: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isComplete"), pydantic.Field(alias="isComplete")
    ]
    status: WorkflowResponseModelStatus
    creator: typing.Optional[WorkflowResponseModelCreator] = None
    created: str
    last_updated: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    roles: typing.List[WorkflowResponseModelRolesItem]
    approvals: WorkflowStateModel
    signatures: WorkflowStateModel
    record_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="recordIds"), pydantic.Field(alias="recordIds")
    ] = None
    is_revertible_to_review: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isRevertibleToReview"), pydantic.Field(alias="isRevertibleToReview")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
