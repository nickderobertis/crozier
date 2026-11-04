

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_list_all_workflow_schemas_response_list_item import WorkflowsListAllWorkflowSchemasResponseListItem


class WorkflowsListAllWorkflowSchemasResponse(UniversalBaseModel):
    list_: typing_extensions.Annotated[
        typing.Optional[typing.List[WorkflowsListAllWorkflowSchemasResponseListItem]],
        FieldMetadata(alias="list"),
        pydantic.Field(alias="list"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
