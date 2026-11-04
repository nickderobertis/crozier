

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_all_workflow_schemas_response_list_item_schema import ListAllWorkflowSchemasResponseListItemSchema


class ListAllWorkflowSchemasResponseListItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[ListAllWorkflowSchemasResponseListItemSchema],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema"),
    ] = None
    permissions: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
